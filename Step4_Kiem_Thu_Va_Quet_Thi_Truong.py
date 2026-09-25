import sys
import warnings
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from Step1_Thu_Thap_Va_Tao_Dac_Trung import tai_du_lieu_co_phieu, DANH_SACH_CO_PHIEU_VN
from quan_tri_rui_ro import QuanTriRuiRoVaDanhMuc

warnings.filterwarnings('ignore')
sys.stdout.reconfigure(encoding='utf-8')

def kiem_thu_chien_luoc_co_phieu(df, bo_quan_tri, ty_le_train=0.75):
    cac_cot = ['Returns', 'RSI', 'MACD', 'OBV', 'ATR', 'Macro_IR', 'Foreign_Flow', 'News_Sentiment']
    X = df[cac_cot]
    y = df['Target']

    cat_idx = int(len(df) * ty_le_train)
    X_train, X_test = X.iloc[:cat_idx], X.iloc[cat_idx:]
    y_train, y_test = y.iloc[:cat_idx], y.iloc[cat_idx:]
    df_test = df.iloc[cat_idx:].copy()

    mo_hinh = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
    mo_hinh.fit(X_train, y_train)

    xac_suat_tang = mo_hinh.predict_proba(X_test)[:, 1]
    df_test['Prob_Win'] = xac_suat_tang

    so_du = bo_quan_tri.tong_nav
    so_co_phieu = 0
    gia_von = 0.0
    lich_su_tai_san = []

    for idx, row in df_test.iterrows():
        gia = row['Close']
        p_win = row['Prob_Win']
        loi_nhuan_tiem_nang = row['ATR'] / gia * 1.5
        rui_ro_tiem_nang = row['ATR'] / gia * 1.0

        if so_co_phieu > 0:
            ty_le_lo = (gia - gia_von) / gia_von
            quyet_dinh = bo_quan_tri.kiem_tra_cat_lo_dong(ty_le_lo, p_win, loi_nhuan_tiem_nang)
            if quyet_dinh in ["FORCE_SELL", "SELL"]:
                doanh_thu = so_co_phieu * gia
                phi = doanh_thu * bo_quan_tri.phi_giao_dich
                so_du += (doanh_thu - phi)
                so_co_phieu = 0
                gia_von = 0.0

        if so_co_phieu == 0:
            cho_phep_mua = bo_quan_tri.danh_gia_tin_hieu_mua(p_win, loi_nhuan_tiem_nang, rui_ro_tiem_nang)
            if cho_phep_mua and p_win > 0.53:
                ngan_sach = bo_quan_tri.lay_ngan_sach_luot_song()
                if ngan_sach > 0:
                    so_luong = int(ngan_sach / gia)
                    if so_luong > 0:
                        chi_phi = so_luong * gia
                        phi = chi_phi * bo_quan_tri.phi_giao_dich
                        so_du -= (chi_phi + phi)
                        so_co_phieu = so_luong
                        gia_von = gia

        tong_val = so_du + (so_co_phieu * gia)
        lich_su_tai_san.append(tong_val)

    tai_san_cuoi = lich_su_tai_san[-1] if lich_su_tai_san else bo_quan_tri.tong_nav
    loi_nhuan_pt = ((tai_san_cuoi - bo_quan_tri.tong_nav) / bo_quan_tri.tong_nav) * 100
    return loi_nhuan_pt, len(df_test)

def quet_radar_toan_thi_truong(danh_sach_ma=None):
    if danh_sach_ma is None:
        danh_sach_ma = DANH_SACH_CO_PHIEU_VN[:8]

    bo_quan_tri = QuanTriRuiRoVaDanhMuc(tong_nav=50_000_000)
    ket_qua = []

    print(f"Quet radar tin hieu giao dich tren {len(danh_sach_ma)} ma...")
    for ma in danh_sach_ma:
        df = tai_du_lieu_co_phieu(ma)
        if df is not None and len(df) > 200:
            roi, so_phien = kiem_thu_chien_luoc_co_phieu(df, bo_quan_tri)
            ket_qua.append({'Ma': ma, 'ROI_Backtest': roi, 'So_Phien': so_phien})
            print(f"  + [{ma:<8}] ROI: {roi:>6.2f}%")

    bang_ket_qua = pd.DataFrame(ket_qua)
    if not bang_ket_qua.empty:
        print("\nBang xep hang co phieu tieng nang:")
        print(bang_ket_qua.sort_values(by='ROI_Backtest', ascending=False).to_string(index=False))
    return bang_ket_qua

if __name__ == "__main__":
    quet_radar_toan_thi_truong(DANH_SACH_CO_PHIEU_VN[:5])
