import numpy as np
import pandas as pd
import gymnasium as gym
from gymnasium import spaces
import random

class MoiTruongGiaoDichDaMa(gym.Env):
    def __init__(self, danh_sach_df, so_du_ban_dau=10_000_000, ty_le_phi=0.0025):
        super(MoiTruongGiaoDichDaMa, self).__init__()

        self.danh_sach_df = danh_sach_df
        self.so_du_ban_dau = so_du_ban_dau
        self.ty_le_phi = ty_le_phi

        self.df = random.choice(self.danh_sach_df).reset_index(drop=True)
        self.action_space = spaces.Discrete(3)
        self.cot_dac_trung = ['Close', 'RSI', 'MACD', 'OBV', 'ATR', 'Macro_IR', 'Foreign_Flow', 'News_Sentiment']
        self.observation_space = spaces.Box(low=-np.inf, high=np.inf, shape=(len(self.cot_dac_trung) + 2,), dtype=np.float32)

        self.buoc_hien_tai = 0
        self.so_du = self.so_du_ban_dau
        self.so_luong_co_phieu = 0
        self.tong_tai_san = self.so_du_ban_dau

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.df = random.choice(self.danh_sach_df).reset_index(drop=True)
        self.buoc_hien_tai = 0
        self.so_du = self.so_du_ban_dau
        self.so_luong_co_phieu = 0
        self.tong_tai_san = self.so_du_ban_dau
        return self._lay_quan_sat(), {}

    def _lay_quan_sat(self):
        obs = [self.so_du, self.so_luong_co_phieu]
        dac_trung = self.df.loc[self.buoc_hien_tai, self.cot_dac_trung].values.tolist()
        obs.extend(dac_trung)
        return np.array(obs, dtype=np.float32)

    def step(self, hanh_dong):
        gia_hien_tai = self.df.loc[self.buoc_hien_tai, 'Close']
        tai_san_truoc = self.tong_tai_san

        if hanh_dong == 1:
            ngan_sach = self.so_du * 0.5
            so_co_phieu_mua = int(ngan_sach / gia_hien_tai) if gia_hien_tai > 0 else 0
            if so_co_phieu_mua > 0:
                chi_phi = so_co_phieu_mua * gia_hien_tai
                phi = chi_phi * self.ty_le_phi
                self.so_du -= (chi_phi + phi)
                self.so_luong_co_phieu += so_co_phieu_mua

        elif hanh_dong == 2:
            if self.so_luong_co_phieu > 0:
                doanh_thu = self.so_luong_co_phieu * gia_hien_tai
                phi = doanh_thu * self.ty_le_phi
                self.so_du += (doanh_thu - phi)
                self.so_luong_co_phieu = 0

        self.tong_tai_san = self.so_du + (self.so_luong_co_phieu * gia_hien_tai)
        phan_thuong = self.tong_tai_san - tai_san_truoc

        if self.tong_tai_san < self.so_du_ban_dau * 0.8:
            phan_thuong -= 2_000_000

        self.buoc_hien_tai += 1
        hoan_thanh = self.buoc_hien_tai >= len(self.df) - 1

        obs = self._lay_quan_sat()
        info = {'net_worth': self.tong_tai_san}

        return obs, float(phan_thuong), hoan_thanh, False, info

MultiStockEnv = MoiTruongGiaoDichDaMa
