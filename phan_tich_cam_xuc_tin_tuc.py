import numpy as np

class BoPhanTichCamXucTinTuc:
    def __init__(self):
        self.danh_sach_ai = ["Gemini_Pro", "GPT_4", "Claude_Opus"]
        self.trong_so_nguon = {
            "tier_1": 0.65,
            "tier_2": 0.35
        }
        self.diem_trung_lap = 0.5

    def _gia_lap_doc_tin(self, ten_ai, noi_dung, la_chinh_thong):
        diem_co_ban = np.random.uniform(0.1, 0.9)
        sai_so = np.random.uniform(-0.1, 0.1)
        return float(np.clip(diem_co_ban + sai_so, 0.0, 1.0))

    def tinh_diem_cam_xuc(self, ma_ck, ngay, du_lieu_tin_tuc):
        if not du_lieu_tin_tuc or (len(du_lieu_tin_tuc.get("tier_1", [])) == 0 and len(du_lieu_tin_tuc.get("tier_2", [])) == 0):
            return self.diem_trung_lap

        tong_hop_diem = []

        for ai in self.danh_sach_ai:
            diem_t1 = self.diem_trung_lap
            diem_t2 = self.diem_trung_lap

            if du_lieu_tin_tuc.get("tier_1"):
                diem_t1 = float(np.mean([self._gia_lap_doc_tin(ai, bai, True) for bai in du_lieu_tin_tuc["tier_1"]]))

            if du_lieu_tin_tuc.get("tier_2"):
                diem_t2 = float(np.mean([self._gia_lap_doc_tin(ai, bai, False) for bai in du_lieu_tin_tuc["tier_2"]]))

            diem_ai = (diem_t1 * self.trong_so_nguon["tier_1"]) + (diem_t2 * self.trong_so_nguon["tier_2"])
            tong_hop_diem.append(diem_ai)

        return float(np.mean(tong_hop_diem))

EnsembleSentimentEngine = BoPhanTichCamXucTinTuc
