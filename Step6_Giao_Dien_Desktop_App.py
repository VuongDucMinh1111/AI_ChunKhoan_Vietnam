import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time

class UngDungChungKhoanAI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("He Thong Giao Dich Chung Khoan AI")
        self.geometry("900x600")
        self.configure(bg="#f5f5f5")
        
        style = ttk.Style(self)
        style.theme_use('clam')
        
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both", padx=10, pady=10)
        
        self.tab_live = ttk.Frame(self.notebook)
        self.tab_train = ttk.Frame(self.notebook)
        self.tab_history = ttk.Frame(self.notebook)
        
        self.notebook.add(self.tab_live, text="Giam Sat Real-time")
        self.notebook.add(self.tab_train, text="Trung Tam Huan Luyen AI")
        self.notebook.add(self.tab_history, text="Lich Su Giao Dich")
        
        self.cai_dat_tab_live()
        self.cai_dat_tab_train()
        self.cai_dat_tab_history()

    def cai_dat_tab_live(self):
        frame = ttk.LabelFrame(self.tab_live, text="Trang Thai He Thong Giao Dich")
        frame.pack(fill="x", padx=20, pady=20)
        
        ttk.Label(frame, text="Tong Tai San (NAV) : 543,250,000 VND (+5.4%)", font=("Segoe UI", 12, "bold")).pack(anchor="w", padx=20, pady=10)
        ttk.Label(frame, text="Win Rate Hien Tai   : 68.5%", font=("Segoe UI", 11)).pack(anchor="w", padx=20, pady=5)
        ttk.Label(frame, text="Tin Hieu Mang Bayes : CHO PHEP GIAO DICH (Do tu tin: 85%)", font=("Segoe UI", 11)).pack(anchor="w", padx=20, pady=5)
        ttk.Label(frame, text="Diem Tin Tuc LLM    : TICH CUC (Diem: 0.75)", font=("Segoe UI", 11)).pack(anchor="w", padx=20, pady=5)

    def cai_dat_tab_train(self):
        frame = ttk.LabelFrame(self.tab_train, text="Huan Luyen Cap Nhat He Thong (MLOps)")
        frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        ttk.Label(frame, text="Thu thap du lieu giao dich moi nhat va huan luyen lai toan bo bo nao AI.", font=("Segoe UI", 10)).pack(pady=15)
        
        self.btn_train = tk.Button(frame, text="KICH HOAT HUAN LUYEN", bg="#0078D7", fg="white", font=("Segoe UI", 12, "bold"), command=self.bat_dau_huan_luyen)
        self.btn_train.pack(pady=10, ipadx=20, ipady=10)
        
        self.lbl_status = ttk.Label(frame, text="Trang thai: San sang", font=("Segoe UI", 10, "italic"))
        self.lbl_status.pack(pady=10)
        
        self.progress = ttk.Progressbar(frame, orient="horizontal", length=600, mode="determinate")
        self.progress.pack(pady=10)

    def cai_dat_tab_history(self):
        frame = ttk.LabelFrame(self.tab_history, text="Nhat Ky Khop Lenh He Thong")
        frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        cols = ("Thoi gian", "Ma CK", "Hanh dong", "Gia khop", "Ly do he thong")
        tree = ttk.Treeview(frame, columns=cols, show="headings", height=15)
        
        widths = [150, 80, 100, 100, 300]
        for i, col in enumerate(cols):
            tree.heading(col, text=col)
            tree.column(col, width=widths[i])
        
        tree.insert("", "end", values=("2026-08-20 10:15:22", "FPT.VN", "BUY", "135,000", "LLM Sentiment tot + Ho tro ky thuat"))
        tree.insert("", "end", values=("2026-08-19 14:20:01", "VIC.VN", "SELL", "45,200", "Khoi ngoai ban rong lien tuc"))
        tree.insert("", "end", values=("2026-08-18 09:30:15", "HPG.VN", "HOLD", "-", "Do bat dinh cao, can nhac giu"))
        
        tree.pack(expand=True, fill="both", padx=10, pady=10)

    def bat_dau_huan_luyen(self):
        self.btn_train.config(state="disabled", bg="#aaaaaa")
        self.progress["value"] = 0
        threading.Thread(target=self._tien_trinh_huan_luyen, daemon=True).start()

    def _tien_trinh_huan_luyen(self):
        cac_buoc = [
            "Dang thu thap du lieu thi truong...", 
            "Dang phan tich tin tuc bang LLM...", 
            "Dang huan luyen Agent PPO...", 
            "Dang tinh toan do bat dinh Bayes..."
        ]
        for i in range(101):
            time.sleep(0.04)
            self.progress["value"] = i
            if i % 25 == 0 and i < 100:
                self.lbl_status.config(text=f"Trang thai: {cac_buoc[i//25]} ({i}%)")
        
        self.lbl_status.config(text="Trang thai: Hoan tat huan luyen!")
        self.btn_train.config(state="normal", bg="#0078D7")
        messagebox.showinfo("Thong bao", "Mo hinh AI da duoc cap nhat thanh cong!")

if __name__ == "__main__":
    app = UngDungChungKhoanAI()
    app.mainloop()
