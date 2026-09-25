import torch
import torch.nn as nn
import numpy as np

class MangBayesDanhGiaRuiRo(nn.Module):
    def __init__(self, so_chieu_dau_vao, chieu_an=128):
        super(MangBayesDanhGiaRuiRo, self).__init__()
        self.fc1 = nn.Linear(so_chieu_dau_vao, chieu_an)
        self.dropout1 = nn.Dropout(p=0.3)
        self.fc2 = nn.Linear(chieu_an, chieu_an // 2)
        self.dropout2 = nn.Dropout(p=0.3)
        self.out = nn.Linear(chieu_an // 2, 3)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.dropout1(x)
        x = torch.relu(self.fc2(x))
        x = self.dropout2(x)
        return self.out(x)

    def du_doan_do_bat_dinh(self, x, so_lan_lay_mau=100):
        self.train()
        ket_qua = []
        with torch.no_grad():
            for _ in range(so_lan_lay_mau):
                preds = self.forward(x)
                ket_qua.append(preds.numpy())

        ket_qua = np.array(ket_qua)
        gia_tri_trung_binh = np.mean(ket_qua, axis=0)
        phuong_sai = np.var(ket_qua, axis=0)

        return gia_tri_trung_binh, phuong_sai

BayesianTradingNetwork = MangBayesDanhGiaRuiRo
