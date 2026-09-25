import os
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]

DARK_BLUE = RGBColor(16, 44, 87)
LIGHT_BLUE = RGBColor(53, 162, 159)
TEXT_DARK = RGBColor(33, 37, 41)
TEXT_MUTED = RGBColor(108, 117, 125)
BG_LIGHT = RGBColor(248, 249, 250)
BORDER_GRAY = RGBColor(222, 226, 230)
ACCENT_GREEN = RGBColor(40, 167, 69)
ACCENT_RED = RGBColor(220, 53, 69)
WHITE = RGBColor(255, 255, 255)

def add_header(slide, title_text, category_text="HỆ THỐNG GIAO DỊCH CHỨNG KHOÁN AI QUANT"):
    header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.733), Inches(1.0))
    tf = header_box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    p_cat = tf.paragraphs[0]
    p_cat.text = category_text.upper()
    p_cat.font.size = Pt(11)
    p_cat.font.bold = True
    p_cat.font.color.rgb = LIGHT_BLUE
    
    p_title = tf.add_paragraph()
    p_title.text = title_text
    p_title.font.size = Pt(21)
    p_title.font.bold = True
    p_title.font.color.rgb = DARK_BLUE

def add_footer(slide, current_slide, total_slides=12):
    footer_box = slide.shapes.add_textbox(Inches(0.8), Inches(6.9), Inches(11.733), Inches(0.4))
    tf = footer_box.text_frame
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    p.text = f"Dự án Thử nghiệm Nghiên cứu AI Quant | Tác giả: Vương Đức Minh | Trang {current_slide}/{total_slides}"
    p.font.size = Pt(9.5)
    p.font.color.rgb = TEXT_MUTED

def add_card(slide, x, y, w, h, bg_color=WHITE, border_color=BORDER_GRAY):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    card.line.color.rgb = border_color
    card.line.width = Pt(1.2)
    return card

# =============================================================
# SLIDE 1: TRANG BÌA
# =============================================================
s1 = prs.slides.add_slide(blank_layout)
bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
bg1.fill.solid()
bg1.fill.fore_color.rgb = DARK_BLUE
bg1.line.color.rgb = DARK_BLUE

tb1 = s1.shapes.add_textbox(Inches(1.0), Inches(1.5), Inches(11.3), Inches(4.8))
tf1 = tb1.text_frame
tf1.word_wrap = True

p_sub = tf1.paragraphs[0]
p_sub.text = "BÁO CÁO NGHIÊN CỨU & KIỂM ĐỊNH THUẬT TOÁN ĐỊNH LƯỢNG (AI QUANT)"
p_sub.font.size = Pt(13)
p_sub.font.bold = True
p_sub.font.color.rgb = LIGHT_BLUE

p_main = tf1.add_paragraph()
p_main.text = "Hệ Thống Giao Dịch Chứng Khoán\nỨng Dụng Trí Tuệ Nhân Tạo Đa Tầng"
p_main.font.size = Pt(36)
p_main.font.bold = True
p_main.font.color.rgb = WHITE
p_main.space_after = Pt(16)

p_desc = tf1.add_paragraph()
p_desc.text = "Tích hợp Học tăng cường (PPO), Mạng Bayes (BNN), Đọc tin đa LLM và Lõi Quản trị Rủi ro Động"
p_desc.font.size = Pt(16)
p_desc.font.color.rgb = RGBColor(218, 224, 233)
p_desc.space_after = Pt(25)

p_tag = tf1.add_paragraph()
p_tag.text = "⚠️ ĐÂY LÀ DỰ ÁN NGHIÊN CỨU THỬ NGHIỆM (EXPERIMENTAL RESEARCH) • KHÔNG PHẢI LỜI KHUYÊN ĐẦU TƯ TÀI CHÍNH"
p_tag.font.size = Pt(11)
p_tag.font.bold = True
p_tag.font.color.rgb = RGBColor(255, 193, 7)
p_tag.space_after = Pt(15)

p_auth = tf1.add_paragraph()
p_auth.text = "Tác giả: Vương Đức Minh  |  Thị trường kiểm thử: Chứng khoán Việt Nam (VN30 & Midcaps)"
p_auth.font.size = Pt(12)
p_auth.font.color.rgb = RGBColor(173, 181, 189)

# =============================================================
# SLIDE 2: TỔNG QUAN KIẾN TRÚC 3 TẦNG
# =============================================================
s2 = prs.slides.add_slide(blank_layout)
add_header(s2, "Tổng Quan Kiến Trúc Hệ Thống: Mô Hình 3 Tầng Khép Kín")
add_footer(s2, 2)

if os.path.exists("presentation_assets/chart_architecture.png"):
    s2.shapes.add_picture("presentation_assets/chart_architecture.png", Inches(0.8), Inches(1.5), Inches(7.2), Inches(5.1))

add_card(s2, 8.3, 1.5, 4.2, 5.1, bg_color=BG_LIGHT)
tb2 = s2.shapes.add_textbox(Inches(8.5), Inches(1.7), Inches(3.8), Inches(4.7))
tf2 = tb2.text_frame
tf2.word_wrap = True

p = tf2.paragraphs[0]
p.text = "Triết Lý Thiết Kế 3 Tầng:"
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = DARK_BLUE
p.space_after = Pt(12)

bullets_s2 = [
    ("Tầng 1: Data & Feature Engine", "Cào 125,000 dòng dữ liệu từ Yahoo Finance cho 50 mã VN. Tạo 8+ đặc trưng kỹ thuật, chu kỳ lãi suất vĩ mô và phân tích tin tức đa LLM."),
    ("Tầng 2: Não Bộ AI Ra Quyết Định", "PPO Reinforcement Learning học tự động mua/bán trong môi trường Gym. Kết hợp mạng Bayes (BNN) đo phương sai để triệt tiêu bệnh tự tin thái quá."),
    ("Tầng 3: Lõi Quản Trị Rủi Ro & Thực Thi", "Màng lọc Expected Value, trừ phí 2 chiều, cầu dao ngắt mạch cắt lỗ cứng (-7%) và giao diện Web/Desktop phục vụ giám sát.")
]

for title, desc in bullets_s2:
    p_t = tf2.add_paragraph()
    p_t.text = f"• {title}"
    p_t.font.size = Pt(12)
    p_t.font.bold = True
    p_t.font.color.rgb = LIGHT_BLUE
    
    p_d = tf2.add_paragraph()
    p_d.text = desc
    p_d.font.size = Pt(10.5)
    p_d.font.color.rgb = TEXT_DARK
    p_d.space_after = Pt(10)

# =============================================================
# SLIDE 3: BƯỚC 1 - DỮ LIỆU & ĐẶC TRƯNG KỸ THUẬT
# =============================================================
s3 = prs.slides.add_slide(blank_layout)
add_header(s3, "Bước 1: Thu Thập & Kỹ Thuật Đặc Trưng Dữ Liệu (Step 1)")
add_footer(s3, 3)

col_data = [
    ("50 Mã Cổ Phiếu Lớn", "Bao phủ toàn bộ nhóm VN30 (FPT, VNM, VIC, VHM, HPG, SSI, VCB...) và Top Midcaps tiềm năng (DIG, DXG, PDR, VCI...).", DARK_BLUE),
    ("10 Năm Lịch Sử (~125k Mẫu)", "Dữ liệu giao dịch từ 2015 đến 2025. Đảm bảo trải qua đầy đủ chu kỳ: Uptrend, Downtrend, Đi ngang, Khủng hoảng.", LIGHT_BLUE),
    ("Vector 8 Chiều Chuẩn Hóa", "Observation Space = [Tiền mặt, Cổ phiếu] + [Close, RSI, MACD, OBV, ATR, Macro_IR, Foreign_Flow, News_Sentiment].", DARK_BLUE)
]

for idx, (title, desc, col) in enumerate(col_data):
    x = 0.8 + idx * 4.0
    add_card(s3, x, 1.5, 3.7, 2.3, bg_color=BG_LIGHT)
    tb = s3.shapes.add_textbox(Inches(x + 0.2), Inches(1.7), Inches(3.3), Inches(1.9))
    tf = tb.text_frame
    tf.word_wrap = True
    p_t = tf.paragraphs[0]
    p_t.text = title
    p_t.font.size = Pt(13)
    p_t.font.bold = True
    p_t.font.color.rgb = col
    p_t.space_after = Pt(6)
    p_d = tf.add_paragraph()
    p_d.text = desc
    p_d.font.size = Pt(10.5)
    p_d.font.color.rgb = TEXT_DARK

add_card(s3, 0.8, 4.1, 11.733, 2.5, bg_color=WHITE)
tb_sub = s3.shapes.add_textbox(Inches(1.1), Inches(4.3), Inches(11.1), Inches(2.1))
tf_sub = tb_sub.text_frame
tf_sub.word_wrap = True

p_head = tf_sub.paragraphs[0]
p_head.text = "Chi Tiết Thuật Toán Kỹ Thuật Đặc Trưng (Feature Engineering):"
p_head.font.size = Pt(13)
p_head.font.bold = True
p_head.font.color.rgb = DARK_BLUE
p_head.space_after = Pt(6)

details = [
    "Chỉ báo Động lượng & Xu hướng: RSI(14) xác định vùng quá mua/quá bán; MACD Diff bắt điểm đảo chiều; OBV phát hiện dòng tiền gom hàng; ATR(14) đo biên độ co giãn giá thực tế.",
    "Dữ liệu Vĩ mô Giả lập (Macro_IR): Lãi suất điều hành chu kỳ hình sin từ 3% - 7%, mô phỏng sự dịch chuyển dòng tiền giữa kênh gửi tiết kiệm và chứng khoán.",
    "Dòng tiền Khối ngoại (Foreign_Flow): Mô phỏng hoạt động mua/bán ròng của quỹ ngoại, có tính chu kỳ và độ nhiễu thực tế (Gaussian Noise)."
]
for item in details:
    p = tf_sub.add_paragraph()
    p.text = f"• {item}"
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_DARK
    p.space_after = Pt(4)

# =============================================================
# SLIDE 4: BƯỚC 2 - ĐỘNG CƠ CẢM XÚC TIN TỨC LLM ENSEMBLE
# =============================================================
s4 = prs.slides.add_slide(blank_layout)
add_header(s4, "Bước 2: Động Cơ Phân Tích Cảm Xúc Đa Trí Tuệ Nhân Tạo (Step 2)")
add_footer(s4, 4)

add_card(s4, 0.8, 1.5, 5.6, 5.1, bg_color=BG_LIGHT)
tb4_l = s4.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.2), Inches(4.7))
tf4_l = tb4_l.text_frame
tf4_l.word_wrap = True

p = tf4_l.paragraphs[0]
p.text = "Hệ Thống 3 LLMs Đồng Thuận (Ensemble):"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = DARK_BLUE
p.space_after = Pt(10)

llm_items = [
    ("Gemini Pro (Google)", "Thế mạnh đọc hiểu ngữ cảnh tài chính dài, phân tích báo cáo tài chính và sự kiện vĩ mô."),
    ("GPT-4 (OpenAI)", "Khả năng suy luận logic chuyên sâu, bắt bài các luận điểm tinh vi của doanh nghiệp."),
    ("Claude Opus (Anthropic)", "Kiểm duyệt khách quan, triệt tiêu ảo giác (hallucination) và hạn chế cảm xúc quá đà."),
    ("Cơ chế Lấy Trung Bình", "Điểm cuối cùng = Mean(3 LLMs). Khi 1 model bị sai lệch, 2 model còn lại sẽ kéo về cân bằng.")
]
for t, d in llm_items:
    pt = tf4_l.add_paragraph()
    pt.text = f"• {t}:"
    pt.font.size = Pt(11.5)
    pt.font.bold = True
    pt.font.color.rgb = LIGHT_BLUE
    pd = tf4_l.add_paragraph()
    pd.text = d
    pd.font.size = Pt(10)
    pd.font.color.rgb = TEXT_DARK
    pd.space_after = Pt(6)

add_card(s4, 6.7, 1.5, 5.8, 5.1, bg_color=WHITE)
tb4_r = s4.shapes.add_textbox(Inches(6.9), Inches(1.7), Inches(5.4), Inches(4.7))
tf4_r = tb4_r.text_frame
tf4_r.word_wrap = True

p = tf4_r.paragraphs[0]
p.text = "Trọng Số Báo Chí & Xử Lý Ngày Trắng Tin:"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = DARK_BLUE
p.space_after = Pt(10)

rules = [
    ("Báo Chính Thống (Tier 1) - Trọng số 65%", "CafeF, Vietstock, NDH, Bloomberg, Báo cáo UBCK. Đây là nguồn dữ liệu chuẩn mực, ít giật tít, chiếm tỷ trọng quyết định."),
    ("Diễn Đàn & Mạng Xã Hội (Tier 2) - Trọng số 35%", "Nhóm Facebook, Telegram, F247, Twitter. Chứa tâm lý đám đông (Fomo/Fud) nhưng độ nhiễu cực cao, chỉ dùng làm tham chiếu phụ."),
    ("Giải Quyết Ngày Không Có Tin (Zero-News Problem)", "Khi doanh nghiệp không có sự kiện nào trong ngày, hệ thống tự động gán điểm Trung Lập = 0.5. Tuyệt đối không phạt hay thiên vị cổ phiếu!")
]
for t, d in rules:
    pt = tf4_r.add_paragraph()
    pt.text = f"• {t}:"
    pt.font.size = Pt(11.5)
    pt.font.bold = True
    pt.font.color.rgb = DARK_BLUE
    pd = tf4_r.add_paragraph()
    pd.text = d
    pd.font.size = Pt(10)
    pd.font.color.rgb = TEXT_DARK
    pd.space_after = Pt(8)

# =============================================================
# SLIDE 5: BƯỚC 3 - MẠNG BAYES (BNN) ĐO LƯỜNG ĐỘ BẤT ĐỊNH
# =============================================================
s5 = prs.slides.add_slide(blank_layout)
add_header(s5, "Bước 3: Mạng Thần Kinh Bayes (BNN) - Trị Bệnh Tự Tin Thái Quá")
add_footer(s5, 5)

if os.path.exists("presentation_assets/chart_bnn.png"):
    s5.shapes.add_picture("presentation_assets/chart_bnn.png", Inches(0.8), Inches(1.5), Inches(6.8), Inches(5.1))

add_card(s5, 7.9, 1.5, 4.6, 5.1, bg_color=BG_LIGHT)
tb5 = s5.shapes.add_textbox(Inches(8.1), Inches(1.7), Inches(4.2), Inches(4.7))
tf5 = tb5.text_frame
tf5.word_wrap = True

p = tf5.paragraphs[0]
p.text = "Kỹ Thuật Monte Carlo Dropout:"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = DARK_BLUE
p.space_after = Pt(10)

bnn_steps = [
    ("Bật Dropout khi Suy luận (Inference)", "Thay vì tắt dropout như mạng AI thông thường, BNN kích hoạt Dropout (p=0.3) ngay trong lúc test để tạo ngẫu nhiên."),
    ("100 Lần Suy Luận / Bước Nến", "Mỗi bước ra quyết định, dữ liệu chạy qua mạng 100 lần để đo lường phân phối xác suất các phương án."),
    ("Tính Phương Sai (Variance)", "Variance đại diện cho mức độ bối rối của AI. Nếu các lần đoán đồng nhất ➔ Variance thấp ➔ AI chắc chắn."),
    ("Ngưỡng Cắt Rủi Ro (Threshold = 0.5)", "Nếu Variance > 0.5 ➔ AI đang đoán mò! Cầu dao Bayes lập tức ép lệnh về HOLD, bảo vệ an toàn cho tài khoản.")
]
for t, d in bnn_steps:
    pt = tf5.add_paragraph()
    pt.text = f"• {t}:"
    pt.font.size = Pt(11)
    pt.font.bold = True
    pt.font.color.rgb = LIGHT_BLUE
    pd = tf5.add_paragraph()
    pd.text = d
    pd.font.size = Pt(9.8)
    pd.font.color.rgb = TEXT_DARK
    pd.space_after = Pt(6)

# =============================================================
# SLIDE 6: BƯỚC 4 - LÕI QUẢN TRỊ RỦI RO & LÝ THUYẾT TRÒ CHƠI
# =============================================================
s6 = prs.slides.add_slide(blank_layout)
add_header(s6, "Bước 4: Lõi Quản Trị Rủi Ro & Lý Thuyết Trò Chơi (Step 4)")
add_footer(s6, 6)

cards_s6 = [
    ("Luật 2 Triệu & 20% NAV", [
        "Dưới 2.000.000 VNĐ: Ngân sách lướt sóng = 0. Khóa tính năng giao dịch rủi ro, ưu tiên bảo toàn vốn nhỏ.",
        "Trên 2.000.000 VNĐ: Chỉ được trích tối đa 20% tổng tài sản để lướt sóng ngắn hạn.",
        "80% tài sản còn lại giữ tiền mặt hoặc tích sản an toàn."
    ], DARK_BLUE),
    ("Màng Lọc Expected Value (EV)", [
        "Trừ phí 2 chiều: 0.25% x 2 = 0.5% (Phí giao dịch + Thuế TNCN sàn Việt Nam).",
        "Mức bù lạm phát tối thiểu: Lãi ròng sau phí phải > 0.5% mới xem xét.",
        "Kỳ vọng toán học: EV = (P_win x Lãi) - (P_loss x Lỗ). Chỉ giải ngân khi EV > 0."
    ], LIGHT_BLUE),
    ("Cắt Lỗ 2 Tầng Động", [
        "Cầu dao cứng (Hard Stop-loss): Âm -7% (chạm giá sàn HOSE) ➔ Thanh lý ngay lập tức!",
        "Cắt lỗ động (Dynamic Stop-loss): Khi đang âm nhẹ (VD: -3%), tính toán lại EV hồi phục.",
        "Nếu EV hồi phục dương ➔ Tiếp tục GIỮ; nếu EV đảo chiều âm ➔ CẮT LỖ SỚM."
    ], DARK_BLUE)
]

for idx, (title, items, col) in enumerate(cards_s6):
    x = 0.8 + idx * 4.0
    add_card(s6, x, 1.5, 3.7, 5.1, bg_color=BG_LIGHT)
    tb = s6.shapes.add_textbox(Inches(x + 0.2), Inches(1.7), Inches(3.3), Inches(4.7))
    tf = tb.text_frame
    tf.word_wrap = True
    
    pt = tf.paragraphs[0]
    pt.text = title
    pt.font.size = Pt(13)
    pt.font.bold = True
    pt.font.color.rgb = col
    pt.space_after = Pt(10)
    
    for it in items:
        pi = tf.add_paragraph()
        pi.text = f"• {it}"
        pi.font.size = Pt(10)
        pi.font.color.rgb = TEXT_DARK
        pi.space_after = Pt(8)

# =============================================================
# SLIDE 7: BƯỚC 5 - HUẤN LUYỆN HỌC TĂNG CƯỜNG (RL - PPO)
# =============================================================
s7 = prs.slides.add_slide(blank_layout)
add_header(s7, "Bước 5: Huấn Luyện AI Học Tăng Cường (PPO Agent)")
add_footer(s7, 7)

add_card(s7, 0.8, 1.5, 5.6, 5.1, bg_color=BG_LIGHT)
tb7_l = s7.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.2), Inches(4.7))
tf7_l = tb7_l.text_frame
tf7_l.word_wrap = True

p = tf7_l.paragraphs[0]
p.text = "Siêu Tham Số Huấn Luyện PPO:"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = DARK_BLUE
p.space_after = Pt(10)

ppo_params = [
    ("Thuật toán Lõi", "PPO (Proximal Policy Optimization) - Thuật toán RL ổn định nhất hiện nay."),
    ("Kiến trúc Policy", "MlpPolicy (Multi-Layer Perceptron), 2 lớp ẩn kết hợp hàm kích hoạt ReLU."),
    ("Total Timesteps", "50,000 steps trên môi trường tập trung 50 cổ phiếu đa ngành."),
    ("Learning Rate & Batch", "lr = 0.0003, n_steps = 2048, batch_size = 128, ent_coef = 0.01."),
    ("Không Gian Hành Động", "Discrete(3): 0: HOLD (Chờ) | 1: BUY (Mua 50% tiền) | 2: SELL (Chốt toàn bộ).")
]
for t, d in ppo_params:
    pt = tf7_l.add_paragraph()
    pt.text = f"• {t}:"
    pt.font.size = Pt(11.5)
    pt.font.bold = True
    pt.font.color.rgb = LIGHT_BLUE
    pd = tf7_l.add_paragraph()
    pd.text = d
    pd.font.size = Pt(10)
    pd.font.color.rgb = TEXT_DARK
    pd.space_after = Pt(6)

add_card(s7, 6.7, 1.5, 5.8, 5.1, bg_color=WHITE)
tb7_r = s7.shapes.add_textbox(Inches(6.9), Inches(1.7), Inches(5.4), Inches(4.7))
tf7_r = tb7_r.text_frame
tf7_r.word_wrap = True

p = tf7_r.paragraphs[0]
p.text = "Bí Quyết Chống Học Vẹt & Hàm Thưởng:"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = DARK_BLUE
p.space_after = Pt(10)

env_secrets = [
    ("Môi Trường Đa Cổ Phiếu (MultiStockEnv)", "Mỗi lần kết thúc hoặc reset game, Agent bị ném ngẫu nhiên vào một mã cổ phiếu khác trong danh sách 50 mã. Bắt buộc AI phải học bản năng thích nghi thay vì học vẹt đường giá 1 mã cố định!"),
    ("Hàm Thưởng (Reward Function)", "Phần thưởng = Net_Worth(t) - Net_Worth(t-1). AI nhận thưởng khi tài sản tăng và bị phạt khi tài sản giảm."),
    ("Phạt Nặng Đu Đỉnh Phá Sản", "Nếu tổng tài sản tụt dưới 80% vốn ban đầu (< -20%), hệ thống trừ thẳng 2.000.000 điểm phạt. Nhờ đó AI học được phản xạ sợ hãi và tự động chạy trước khi sập hầm!")
]
for t, d in env_secrets:
    pt = tf7_r.add_paragraph()
    pt.text = f"• {t}:"
    pt.font.size = Pt(11.5)
    pt.font.bold = True
    pt.font.color.rgb = DARK_BLUE
    pd = tf7_r.add_paragraph()
    pd.text = d
    pd.font.size = Pt(10)
    pd.font.color.rgb = TEXT_DARK
    pd.space_after = Pt(8)

# =============================================================
# SLIDE 8: BƯỚC 6 - KIỂM THỬ THỰC CHIẾN OUT-OF-SAMPLE
# =============================================================
s8 = prs.slides.add_slide(blank_layout)
add_header(s8, "Bước 6: Kiểm Định Thực Chiến Out-Of-Sample (Proof & Evaluation)")
add_footer(s8, 8)

if os.path.exists("presentation_assets/chart_backtest.png"):
    s8.shapes.add_picture("presentation_assets/chart_backtest.png", Inches(0.8), Inches(1.5), Inches(6.8), Inches(5.1))

add_card(s8, 7.9, 1.5, 4.6, 5.1, bg_color=BG_LIGHT)
tb8 = s8.shapes.add_textbox(Inches(8.1), Inches(1.7), Inches(4.2), Inches(4.7))
tf8 = tb8.text_frame
tf8.word_wrap = True

p = tf8.paragraphs[0]
p.text = "Báo Cáo Kiểm Định Khách Quan:"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = DARK_BLUE
p.space_after = Pt(10)

metrics_s8 = [
    ("Tách Tập Dữ Liệu Nghiêm Ngặt", "Train dữ liệu trước 2024. Đánh giá kiểm thử độc lập từ 2024 - 2026 (Dữ liệu tương lai AI chưa từng thấy)."),
    ("Tỷ Lệ Thắng (Win Rate): 68.5%", "Trong 10 mã cổ phiếu lớn kiểm thử ngẫu nhiên, AI đạt lợi nhuận dương trên 8/10 mã (Tỷ lệ 80%)."),
    ("Bảo Vệ Tài Sản Khi Thị Trường Sập", "Nhờ Cầu dao cắt lỗ (-7%) và BNN Variance, đường cong NAV của AI giữ vững khi thị trường cơ sở rung lắc mạnh."),
    ("Phân Bổ Hành Động Hợp Lý", "Hành vi AI: Chờ đợi (HOLD) chiếm 70% thời gian; chỉ gom mua (BUY) khi đủ điều kiện khắt khe; chốt lời (SELL) dứt khoát.")
]
for t, d in metrics_s8:
    pt = tf8.add_paragraph()
    pt.text = f"• {t}:"
    pt.font.size = Pt(11)
    pt.font.bold = True
    pt.font.color.rgb = LIGHT_BLUE
    pd = tf8.add_paragraph()
    pd.text = d
    pd.font.size = Pt(9.8)
    pd.font.color.rgb = TEXT_DARK
    pd.space_after = Pt(6)

# =============================================================
# SLIDE 9: ỨNG DỤNG THỰC TẾ - WEB DASHBOARD (STREAMLIT)
# =============================================================
s9 = prs.slides.add_slide(blank_layout)
add_header(s9, "Giao Diện Ứng Dụng: Bảng Điều Khiển Web Dashboard (Streamlit)")
add_footer(s9, 9)

if os.path.exists("presentation_assets/web_dashboard_ui.png"):
    s9.shapes.add_picture("presentation_assets/web_dashboard_ui.png", Inches(0.8), Inches(1.5), Inches(7.5), Inches(5.1))

add_card(s9, 8.6, 1.5, 3.9, 5.1, bg_color=BG_LIGHT)
tb9 = s9.shapes.add_textbox(Inches(8.8), Inches(1.7), Inches(3.5), Inches(4.7))
tf9 = tb9.text_frame
tf9.word_wrap = True

p = tf9.paragraphs[0]
p.text = "Tính Năng Web Dashboard:"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = DARK_BLUE
p.space_after = Pt(10)

features_web = [
    ("Tab 1: Giám Sát Real-time", "Hiển thị 4 thẻ KPI trọng tâm: Tổng NAV, Win Rate, Tín hiệu BNN và Điểm cảm xúc tin tức LLM."),
    ("Tab 2: Trạm Huấn Luyện MLOps", "Nút kích hoạt 'Mega Training' chạy ngầm trên luồng riêng, không làm đơ gián đoạn lệnh trên sàn."),
    ("Tab 3: Lịch Sử Khớp Lệnh", "Bảng nhật ký chi tiết: Thời gian, mã CK, hành động, giá khớp và lý do AI giải thích bằng văn bản."),
    ("Khởi Động Nhanh 1-Click", "Chỉ cần click file Chay_Giao_Dien_Web.bat hoặc gõ lệnh streamlit run Step5_Giao_Dien_Web_Dashboard.py.")
]
for t, d in features_web:
    pt = tf9.add_paragraph()
    pt.text = f"• {t}:"
    pt.font.size = Pt(11)
    pt.font.bold = True
    pt.font.color.rgb = LIGHT_BLUE
    pd = tf9.add_paragraph()
    pd.text = d
    pd.font.size = Pt(9.5)
    pd.font.color.rgb = TEXT_DARK
    pd.space_after = Pt(6)

# =============================================================
# SLIDE 10: ỨNG DỤNG THỰC TẾ - DESKTOP APP (TKINTER)
# =============================================================
s10 = prs.slides.add_slide(blank_layout)
add_header(s10, "Giao Diện Ứng Dụng: Phần Mềm Desktop Window (Tkinter)")
add_footer(s10, 10)

if os.path.exists("presentation_assets/desktop_app_ui.png"):
    s10.shapes.add_picture("presentation_assets/desktop_app_ui.png", Inches(0.8), Inches(1.5), Inches(7.5), Inches(5.1))

add_card(s10, 8.6, 1.5, 3.9, 5.1, bg_color=BG_LIGHT)
tb10 = s10.shapes.add_textbox(Inches(8.8), Inches(1.7), Inches(3.5), Inches(4.7))
tf10 = tb10.text_frame
tf10.word_wrap = True

p = tf10.paragraphs[0]
p.text = "Ưu Thế Phiên Bản Desktop:"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = DARK_BLUE
p.space_after = Pt(10)

features_desk = [
    ("Chạy Native Siêu Nhẹ", "Xây dựng trên thư viện Tkinter chuẩn của Python, khởi động trong 1 giây, không cần cài đặt browser hay server web phức tạp."),
    ("Đa Luồng (Multi-Threading)", "Quá trình huấn luyện nặng được đẩy ra Background Thread, thanh Progress Bar chạy mượt mà không treo cửa sổ."),
    ("Trực Quan Cho Nhà Đầu Tư", "Giao diện tab sạch sẽ, thông báo popup khi AI hoàn thành chu kỳ học, phù hợp triển khai trên máy tính cá nhân."),
    ("Khởi Động Nhanh", "Chạy trực tiếp qua file Chay_Giao_Dien_Desktop.bat.")
]
for t, d in features_desk:
    pt = tf10.add_paragraph()
    pt.text = f"• {t}:"
    pt.font.size = Pt(11)
    pt.font.bold = True
    pt.font.color.rgb = LIGHT_BLUE
    pd = tf10.add_paragraph()
    pd.text = d
    pd.font.size = Pt(9.5)
    pd.font.color.rgb = TEXT_DARK
    pd.space_after = Pt(6)

# =============================================================
# SLIDE 11: CÁC HẠN CHẾ CỐT LÕI & THÁCH THỨC THỰC TẾ
# =============================================================
s11 = prs.slides.add_slide(blank_layout)
add_header(s11, "Các Hạn Chế Cốt Lõi & Thách Thức Thị Trường Thực Tế (Limitations)")
add_footer(s11, 11)

limitations = [
    ("1. Rào Cản Chu Kỳ Thanh Toán T+2.5", "Chứng khoán Việt Nam áp dụng chu kỳ T+2.5 (mua xong phải đợi 2.5 ngày mới được bán). Thuật toán RL trong mô phỏng đang giao dịch theo chu kỳ nến ngày, chưa khóa vị thế 2.5 phiên thực tế.", ACCENT_RED),
    ("2. Biên Độ Trần/Sàn (+/- 7%) & Phiên Khớp Lệnh ATO/ATC", "Khi thị trường bán tháo cực đoan ('múa bên trăng' - trắng bên mua), lệnh cắt lỗ của AI có thể không thể khớp được ở giá mong muốn. Phiên ATO/ATC có hiện tượng nhiễu giá khớp lệnh.", ACCENT_RED),
    ("3. Hiện Tượng Trượt Giá (Slippage) & Thanh Khoản", "Giao dịch khối lượng lớn ở các mã Midcaps có thể bị trượt giá đáng kể so với giá đóng cửa trong dữ liệu lịch sử.", DARK_BLUE),
    ("4. Rủi Ro Sự Kiện Bất Thường (Black Swan)", "Các sự kiện địa chính trị, thiên nga đen bất ngờ nằm ngoài phân phối dữ liệu 10 năm qua có thể khiến mô hình AI dự báo sai lệch.", DARK_BLUE),
    ("5. Chi Phí Gọi API LLM Trên Thực Tế", "Việc gọi liên tục 3 LLMs (Gemini, GPT-4, Claude) để cào tin tức hàng ngày của 50 mã sẽ tốn kém chi phí API Token và cần hạ tầng mạng ổn định.", DARK_BLUE)
]

for idx, (title, desc, col) in enumerate(limitations):
    row = idx // 2
    col_idx = idx % 2
    w = 5.7 if idx < 4 else 11.733
    x = 0.8 + col_idx * 6.0 if idx < 4 else 0.8
    y = 1.5 + row * 1.8
    h = 1.6
    
    add_card(s11, x, y, w, h, bg_color=BG_LIGHT)
    tb = s11.shapes.add_textbox(Inches(x + 0.2), Inches(y + 0.15), Inches(w - 0.4), Inches(h - 0.3))
    tf = tb.text_frame
    tf.word_wrap = True
    
    pt = tf.paragraphs[0]
    pt.text = title
    pt.font.size = Pt(12)
    pt.font.bold = True
    pt.font.color.rgb = col
    pt.space_after = Pt(4)
    
    pd = tf.add_paragraph()
    pd.text = desc
    pd.font.size = Pt(10)
    pd.font.color.rgb = TEXT_DARK

# =============================================================
# SLIDE 12: TUYÊN BỐ THỬ NGHIỆM & LỘ TRÌNH PHÁT TRIỂN
# =============================================================
s12 = prs.slides.add_slide(blank_layout)
add_header(s12, "Tuyên Bố Thử Nghiệm & Lộ Trình Phát Triển (Disclaimer & Roadmap)")
add_footer(s12, 12)

card_warn = add_card(s12, 0.8, 1.5, 11.733, 2.2, bg_color=RGBColor(254, 249, 231), border_color=RGBColor(241, 196, 15))
tb_w = s12.shapes.add_textbox(Inches(1.1), Inches(1.7), Inches(11.1), Inches(1.8))
tf_w = tb_w.text_frame
tf_w.word_wrap = True

pw_t = tf_w.paragraphs[0]
pw_t.text = "⚠️ TUYÊN BỐ QUAN TRỌNG: ĐÂY LÀ DỰ ÁN NGHIÊN CỨU & THỬ NGHIỆM HỌC THUẬT"
pw_t.font.size = Pt(13)
pw_t.font.bold = True
pw_t.font.color.rgb = RGBColor(183, 149, 11)
pw_t.space_after = Pt(6)

pw_d = tf_w.add_paragraph()
pw_d.text = "Hệ thống này được phát triển nhằm mục đích thử nghiệm các mô hình học máy định lượng, kiểm định giả thuyết khoa học về Reinforcement Learning và Bayesian Neural Network. Toàn bộ kết quả backtest không bảo đảm lợi nhuận trong tương lai. Tác giả không chịu trách nhiệm pháp lý hoặc tài chính cho bất kỳ quyết định đầu tư tiền thật nào dựa trên mã nguồn này."
pw_d.font.size = Pt(10.5)
pw_d.font.color.rgb = TEXT_DARK

add_card(s12, 0.8, 3.9, 11.733, 2.7, bg_color=WHITE)
tb_rm = s12.shapes.add_textbox(Inches(1.1), Inches(4.1), Inches(11.1), Inches(2.3))
tf_rm = tb_rm.text_frame
tf_rm.word_wrap = True

pr_t = tf_rm.paragraphs[0]
pr_t.text = "Lộ Trình Phát Triển Tiếp Theo (Phase 2 Roadmap):"
pr_t.font.size = Pt(13)
pr_t.font.bold = True
pr_t.font.color.rgb = DARK_BLUE
pr_t.space_after = Pt(8)

roadmap_items = [
    ("Kết Nối API Chứng Khoán Trực Tiếp", "Tích hợp Open API của các công ty chứng khoán Việt Nam (SSI iBoard API, VPS API, DNSE Entrade) để nhận dữ liệu sổ lệnh Real-time (Level 2 Orderbook)."),
    ("Nâng Cấp Mô Hình Time-Series Transformers", "Thử nghiệm các kiến trúc tiên tiến chuyên cho dữ liệu chuỗi thời gian tài chính như PatchTST, Time-LLM hoặc iTransformer."),
    ("Tối Ưu Hóa T+2.5 & Lệnh Điều Kiện", "Bổ sung cơ chế ràng buộc T+2.5 vào môi trường Gymnasium và tích hợp đặt lệnh Trailing Stop / Stop Limit tự động qua Broker.")
]
for t, d in roadmap_items:
    p = tf_rm.add_paragraph()
    p.text = f"• {t}: {d}"
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_DARK
    p.space_after = Pt(6)

output_path = "He_Thong_AI_Chung_Khoan_12_Trang.pptx"
prs.save(output_path)
print(f"PRESENTATION_CREATED_SUCCESSFULLY: {output_path}")
