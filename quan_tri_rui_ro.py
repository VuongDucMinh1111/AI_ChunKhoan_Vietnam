import numpy as np
import sys

sys.stdout.reconfigure(encoding='utf-8')

class QuanTriRuiRoVaDanhMuc:
    def __init__(self, tong_nav: float, phi_giao_dich=0.0025, muc_tieu_toi_thieu=0.005, cat_lo_toi_da=-0.07):
        self.tong_nav = tong_nav
        self.phi_giao_dich = phi_giao_dich
        self.muc_tieu_toi_thieu = muc_tieu_toi_thieu
        self.cat_lo_toi_da = cat_lo_toi_da

    def lay_ngan_sach_luot_song(self) -> float:
        if self.tong_nav < 2_000_000:
            return 0.0
        return self.tong_nav * 0.20

    def danh_gia_tin_hieu_mua(self, xac_suat_thang: float, loi_nhuan_ky_vong: float, thua_lo_ky_vong: float) -> bool:
        loi_nhuan_rong = loi_nhuan_ky_vong - (self.phi_giao_dich * 2)
        thua_lo_rong = thua_lo_ky_vong - (self.phi_giao_dich * 2)

        if loi_nhuan_rong <= self.muc_tieu_toi_thieu:
            return False

        xac_suat_thua = 1.0 - xac_suat_thang
        ky_vong_toan_hoc = (xac_suat_thang * loi_nhuan_rong) - (xac_suat_thua * abs(thua_lo_rong))

        if ky_vong_toan_hoc <= 0:
            return False

        return True

    def kiem_tra_cat_lo_dong(self, thua_lo_hien_tai: float, xac_suat_hoi_phuc: float, loi_nhuan_tiem_nang: float) -> str:
        if thua_lo_hien_tai <= self.cat_lo_toi_da:
            return "FORCE_SELL"

        rui_ro_giu_tiep = 0.03
        xac_suat_thua = 1.0 - xac_suat_hoi_phuc
        ky_vong_giu = (xac_suat_hoi_phuc * loi_nhuan_tiem_nang) - (xac_suat_thua * rui_ro_giu_tiep)

        if ky_vong_giu > 0:
            return "HOLD"
        else:
            return "SELL"

RiskAndPortfolioManager = QuanTriRuiRoVaDanhMuc
