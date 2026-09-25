import numpy as np

class RobotQLearning:
    def __init__(self, danh_sach_hanh_dong=[0, 1, 2], toc_do_hoc=0.1, he_so_chiet_khau=0.9, epsilon=0.1):
        self.danh_sach_hanh_dong = danh_sach_hanh_dong
        self.toc_do_hoc = toc_do_hoc
        self.gamma = he_so_chiet_khau
        self.epsilon = epsilon
        self.bang_q = {}

    def lay_gia_tri_q(self, trang_thai, hanh_dong):
        return self.bang_q.get((trang_thai, hanh_dong), 0.0)

    def chon_hanh_dong(self, trang_thai, dang_huan_luyen=True):
        if dang_huan_luyen and np.random.uniform(0, 1) < self.epsilon:
            return int(np.random.choice(self.danh_sach_hanh_dong))

        gia_tri_q_tat_ca = [self.lay_gia_tri_q(trang_thai, a) for a in self.danh_sach_hanh_dong]
        max_q = max(gia_tri_q_tat_ca)
        cac_hanh_dong_tot_nhat = [a for a in self.danh_sach_hanh_dong if self.lay_gia_tri_q(trang_thai, a) == max_q]
        return int(np.random.choice(cac_hanh_dong_tot_nhat))

    def cap_nhat(self, trang_thai, hanh_dong, phan_thuong, trang_thai_tiep):
        du_doan = self.lay_gia_tri_q(trang_thai, hanh_dong)
        q_max_tiep = max([self.lay_gia_tri_q(trang_thai_tiep, a) for a in self.danh_sach_hanh_dong])
        muc_tieu = phan_thuong + self.gamma * q_max_tiep
        self.bang_q[(trang_thai, hanh_dong)] = du_doan + self.toc_do_hoc * (muc_tieu - du_doan)

QLearningTradingBot = RobotQLearning
