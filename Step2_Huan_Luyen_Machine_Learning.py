import sys
import warnings
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report
import lightgbm as lgb
from Step1_Thu_Thap_Va_Tao_Dac_Trung import tai_du_lieu_co_phieu

warnings.filterwarnings('ignore')
sys.stdout.reconfigure(encoding='utf-8')

def huan_luyen_cac_mo_hinh_ml(df, ty_le_train=0.75):
    cac_cot_dac_trung = ['Returns', 'RSI', 'MACD', 'OBV', 'ATR', 'Macro_IR', 'Foreign_Flow', 'News_Sentiment']
    X = df[cac_cot_dac_trung]
    y = df['Target']

    vi_tri_cat = int(len(df) * ty_le_train)
    X_train, X_test = X.iloc[:vi_tri_cat], X.iloc[vi_tri_cat:]
    y_train, y_test = y.iloc[:vi_tri_cat], y.iloc[vi_tri_cat:]

    print(f"Tap Train: {len(X_train)} phien | Tap Test: {len(X_test)} phien")

    mo_hinh_lgb = lgb.LGBMClassifier(n_estimators=100, learning_rate=0.03, max_depth=4, random_state=42, verbose=-1)
    mo_hinh_lgb.fit(X_train, y_train)
    du_doan_lgb = mo_hinh_lgb.predict(X_test)
    chinh_xac_lgb = accuracy_score(y_test, du_doan_lgb)

    mo_hinh_rf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
    mo_hinh_rf.fit(X_train, y_train)
    du_doan_rf = mo_hinh_rf.predict(X_test)
    chinh_xac_rf = accuracy_score(y_test, du_doan_rf)

    mo_hinh_mlp = MLPClassifier(hidden_layer_sizes=(64, 32), activation='relu', max_iter=200, random_state=42)
    mo_hinh_mlp.fit(X_train, y_train)
    du_doan_mlp = mo_hinh_mlp.predict(X_test)
    chinh_xac_mlp = accuracy_score(y_test, du_doan_mlp)

    print("Ket qua do chinh xac tren tap kiem thu Out-of-sample:")
    print(f"  + LightGBM       : {chinh_xac_lgb * 100:.2f}%")
    print(f"  + Random Forest  : {chinh_xac_rf * 100:.2f}%")
    print(f"  + Neural Net MLP : {chinh_xac_mlp * 100:.2f}%")

    cac_mo_hinh = {
        'LightGBM': mo_hinh_lgb,
        'RandomForest': mo_hinh_rf,
        'NeuralNetwork': mo_hinh_mlp
    }
    return cac_mo_hinh, (X_test, y_test)

if __name__ == "__main__":
    df = tai_du_lieu_co_phieu("FPT.VN", ngay_bat_dau="2018-01-01", ngay_ket_thuc="2026-01-01")
    if df is not None:
        mo_hinh, tap_kiem_thu = huan_luyen_cac_mo_hinh_ml(df)
    else:
        print("Khong the lay du lieu FPT.VN de huan luyen")
