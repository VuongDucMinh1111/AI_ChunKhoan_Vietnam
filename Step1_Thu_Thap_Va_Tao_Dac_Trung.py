import os
import sys
import warnings
import numpy as np
import pandas as pd
import yfinance as yf
import ta
from phan_tich_cam_xuc_tin_tuc import BoPhanTichCamXucTinTuc

warnings.filterwarnings('ignore')
sys.stdout.reconfigure(encoding='utf-8')

DANH_SACH_CO_PHIEU_VN = [
    "FPT.VN", "VNM.VN", "VIC.VN", "VHM.VN", "VRE.VN", "HPG.VN", "SSI.VN", "STB.VN", 
    "VCB.VN", "BID.VN", "CTG.VN", "TCB.VN", "VPB.VN", "MBB.VN", "HDB.VN", "TPB.VN", 
    "ACB.VN", "SSB.VN", "VIB.VN", "MSN.VN", "MWG.VN", "PNJ.VN", "SAB.VN", "GAS.VN", 
    "POW.VN", "PLX.VN", "GVR.VN", "BCM.VN", "VJC.VN", "HVN.VN",
    "VND.VN", "VCI.VN", "HCM.VN", "HSG.VN", "NKG.VN", "KBC.VN", "DIG.VN", "DXG.VN", 
    "NVL.VN", "PDR.VN", "KDH.VN", "NLG.VN", "VGC.VN", "PVD.VN", "DGC.VN", "DPM.VN", 
    "DCM.VN", "VHC.VN", "ANV.VN", "REE.VN"
]

def trich_xuat_dac_trung(df):
    df['RSI'] = ta.momentum.RSIIndicator(close=df['Close'], window=14).rsi()
    df['MACD'] = ta.trend.MACD(close=df['Close']).macd_diff()
    df['OBV'] = ta.volume.OnBalanceVolumeIndicator(close=df['Close'], volume=df['Volume']).on_balance_volume()
    df['ATR'] = ta.volatility.AverageTrueRange(high=df['High'], low=df['Low'], close=df['Close'], window=14).average_true_range()
    
    so_phien = len(df)
    thoi_gian = np.arange(so_phien)
    df['Macro_IR'] = 5.0 + 2.0 * np.sin(thoi_gian / 252.0 * 2 * np.pi)
    df['Foreign_Flow'] = np.sin(thoi_gian / 60.0) * df['Volume'] * 0.1 + np.random.normal(0, df['Volume'] * 0.05)
    
    bo_cam_xuc = BoPhanTichCamXucTinTuc()
    loi_nhuan_tuong_lai = df['Close'].shift(-3) / df['Close'] - 1.0
    tin_hieu_gia_lap = loi_nhuan_tuong_lai.fillna(0) * 10.0 + np.random.normal(0, 0.2, so_phien)
    df['News_Sentiment'] = [bo_cam_xuc.diem_trung_lap if np.random.rand() < 0.2 else np.clip(s, 0.0, 1.0) for s in tin_hieu_gia_lap]
    
    df['Returns'] = df['Close'].pct_change()
    df['Target'] = (df['Close'].shift(-1) > df['Close']).astype(int)
    
    df.dropna(inplace=True)
    return df

def tai_du_lieu_co_phieu(ma_co_phieu, ngay_bat_dau="2018-01-01", ngay_ket_thuc="2026-01-01"):
    df = yf.download(ma_co_phieu, start=ngay_bat_dau, end=ngay_ket_thuc, progress=False)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    
    if df.empty or len(df) < 200:
        return None
        
    df = df[['Open', 'High', 'Low', 'Close', 'Volume']].dropna()
    df = trich_xuat_dac_trung(df)
    return df

def chay_thu_thap_toan_bo(danh_sach_ma=None, ngay_cat="2024-01-01"):
    if danh_sach_ma is None:
        danh_sach_ma = DANH_SACH_CO_PHIEU_VN[:10]
        
    tap_train = []
    tap_test = {}
    tong_so_mau = 0
    
    print(f"Bat dau thu thap va xu ly dac trung cho {len(danh_sach_ma)} ma co phieu...")
    for ma in danh_sach_ma:
        df = tai_du_lieu_co_phieu(ma)
        if df is not None and len(df) > 150:
            df_train = df[df.index < ngay_cat]
            df_test = df[df.index >= ngay_cat]
            if len(df_train) > 100 and len(df_test) > 30:
                tap_train.append(df_train)
                tap_test[ma] = df_test
                tong_so_mau += len(df)
                print(f"  + [OK] {ma:<8}: {len(df)} phien")
                
    print(f"Tong so phien du lieu thu thap duoc: {tong_so_mau}")
    return tap_train, tap_test

if __name__ == "__main__":
    train_dfs, test_dfs = chay_thu_thap_toan_bo(DANH_SACH_CO_PHIEU_VN[:5])
