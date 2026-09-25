import os
import sys
import warnings
import time
import numpy as np
import pandas as pd
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
os.environ["OMP_NUM_THREADS"] = "1"
warnings.filterwarnings('ignore')
sys.stdout.reconfigure(encoding='utf-8')

from moi_truong_giao_dich_rl import MoiTruongGiaoDichDaMa
from Step1_Thu_Thap_Va_Tao_Dac_Trung import chay_thu_thap_toan_bo, DANH_SACH_CO_PHIEU_VN

def huan_luyen_agent_ppo(tap_train, tong_so_buoc=20_000, so_du_khoi_tao=100_000_000):
    env_train = DummyVecEnv([lambda: MoiTruongGiaoDichDaMa(tap_train, so_du_ban_dau=so_du_khoi_tao)])
    model = PPO("MlpPolicy", env_train, learning_rate=0.0003, n_steps=2048, batch_size=128, ent_coef=0.01, verbose=0)
    
    thoi_gian_dau = time.time()
    print(f"Bat dau huan luyen PPO voi {tong_so_buoc} buoc tren {len(tap_train)} ma...")
    model.learn(total_timesteps=tong_so_buoc)
    print(f"Huan luyen hoan tat sau {time.time() - thoi_gian_dau:.1f} giay.")
    return model

def danh_gia_agent_out_of_sample(model, tap_test, so_du_khoi_tao=100_000_000):
    tong_roi = 0.0
    thong_ke_hanh_dong = {0: 0, 1: 0, 2: 0}
    so_ma_thang = 0
    danh_sach_kiem_tra = list(tap_test.items())

    print("\nKet qua danh gia Out-of-Sample tren cac ma chua tung hoc:")
    for ma, df_test in danh_sach_kiem_tra:
        env_test = MoiTruongGiaoDichDaMa([df_test], so_du_ban_dau=so_du_khoi_tao)
        obs, _ = env_test.reset()
        hoan_thanh = False
        dem_rieng = {0: 0, 1: 0, 2: 0}

        while not hoan_thanh:
            action, _ = model.predict(obs, deterministic=True)
            hanh_dong = int(action)
            dem_rieng[hanh_dong] += 1
            thong_ke_hanh_dong[hanh_dong] += 1
            obs, rewards, hoan_thanh, _, _ = env_test.step(hanh_dong)

        lai_lo = env_test.tong_tai_san - so_du_khoi_tao
        roi = (lai_lo / so_du_khoi_tao) * 100
        tong_roi += roi
        if roi > 0:
            so_ma_thang += 1

        print(f"  [{ma:<8}] ROI: {roi:>6.2f}% | Cho:{dem_rieng[0]:>3} | Mua:{dem_rieng[1]:>3} | Ban:{dem_rieng[2]:>3}")

    roi_trung_binh = tong_roi / len(danh_sach_kiem_tra) if danh_sach_kiem_tra else 0.0
    print("\nTong ket danh gia Agent:")
    print(f"  + Ty le ma chien thang : {so_ma_thang}/{len(danh_sach_kiem_tra)}")
    print(f"  + Hanh dong tong hop   : Cho: {thong_ke_hanh_dong[0]} | Mua: {thong_ke_hanh_dong[1]} | Ban: {thong_ke_hanh_dong[2]}")
    print(f"  + ROI trung binh       : {roi_trung_binh:.2f}%")

    return roi_trung_binh

if __name__ == "__main__":
    tap_train, tap_test = chay_thu_thap_toan_bo(DANH_SACH_CO_PHIEU_VN[:6])
    if tap_train and tap_test:
        agent_ppo = huan_luyen_agent_ppo(tap_train, tong_so_buoc=5_000)
        danh_gia_agent_out_of_sample(agent_ppo, tap_test)
