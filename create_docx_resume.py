import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def create_resume_docx_5pages(output_path, img_dir):
    doc = Document()
    
    # Page setup: A4, 0.7 inch margins for optimal 5-page fit
    for section in doc.sections:
        section.top_margin = Inches(0.7)
        section.bottom_margin = Inches(0.7)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)
        section.page_width = Inches(8.27)
        section.page_height = Inches(11.69)
        
    def set_run_font(run, font_name="微軟正黑體", size_pt=10, bold=False, color=RGBColor(30, 41, 59)):
        run.font.name = font_name
        run.font.size = Pt(size_pt)
        run.bold = bold
        run.font.color.rgb = color
        rPr = run._r.get_or_add_rPr()
        rFonts = parse_xml(f'<w:rFonts {nsdecls("w")} w:ascii="{font_name}" w:hAnsi="{font_name}" w:eastAsia="{font_name}"/>')
        rPr.append(rFonts)

    def add_section_header(title, space_before=10):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(space_before)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(title)
        set_run_font(run, font_name="微軟正黑體", size_pt=13, bold=True, color=RGBColor(15, 23, 42))
        pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="8" w:space="3" w:color="CBD5E1"/></w:pBdr>')
        p._p.get_or_add_pPr().append(pBdr)

    def add_body_p(text, indent=True, space_after=3.5, size_pt=9.5):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = 1.25
        prefix = "\u3000\u3000" if indent else ""
        run = p.add_run(prefix + text)
        set_run_font(run, font_name="微軟正黑體", size_pt=size_pt, color=RGBColor(51, 65, 85))
        return p

    def add_image_with_caption(img_path, caption_text, width=Inches(5.8), space_after=6):
        if os.path.exists(img_path):
            p_img = doc.add_paragraph()
            p_img.paragraph_format.space_before = Pt(4)
            p_img.paragraph_format.space_after = Pt(1)
            p_img.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.keep_with_next = True
            run_img = p_img.add_run()
            run_img.add_picture(img_path, width=width)
            
            p_cap = doc.add_paragraph()
            p_cap.paragraph_format.space_after = Pt(space_after)
            p_cap.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run_cap = p_cap.add_run(caption_text)
            set_run_font(run_cap, font_name="微軟正黑體", size_pt=8, color=RGBColor(100, 116, 139))

    # ==================== 第 1 頁：個人資料 ＆ 自我介紹 ====================
    p_top = doc.add_paragraph()
    p_top.paragraph_format.space_after = Pt(1)
    run_name = p_top.add_run("吳思穎  Alice Wu")
    set_run_font(run_name, size_pt=18, bold=True, color=RGBColor(15, 23, 42))
    
    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_after = Pt(6)
    run_target = p_sub.add_run("應徵職缺：justfont 行政營運專員 ｜ 專案執行人員")
    set_run_font(run_target, size_pt=10.5, bold=True, color=RGBColor(225, 29, 72))

    # Info Table
    info_table = doc.add_table(rows=3, cols=2)
    info_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    info_table.autofit = False
    
    col_widths = [Inches(3.3), Inches(3.3)]
    for row in info_table.rows:
        for idx, width in enumerate(col_widths):
            row.cells[idx].width = width

    info_data = [
        [("個人資料：", "女、30歲 ｜ 總年資：6~7年工作經歷"), ("就業狀態：", "待業中（錄取後一週可上班）")],
        [("聯絡手機：", "0958-321-139"), ("電子信箱：", "ichbinalicewu35@gmail.com")],
        [("通訊地址：", "新北市土城區學士路"), ("最高學歷：", "私立輔仁大學 中文系 ＆ 德文系 雙學士")]
    ]

    for r_idx, row in enumerate(info_data):
        for c_idx, (label, val) in enumerate(row):
            cell = info_table.cell(r_idx, c_idx)
            cell_p = cell.paragraphs[0]
            cell_p.paragraph_format.space_after = Pt(1.5)
            run_l = cell_p.add_run(label)
            set_run_font(run_l, size_pt=9, bold=True, color=RGBColor(71, 85, 105))
            run_v = cell_p.add_run(" " + val)
            set_run_font(run_v, size_pt=9, color=RGBColor(30, 41, 59))

    # 自我介紹
    add_section_header("自我介紹", space_before=14)
    
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(3)
    p_title.paragraph_format.space_after = Pt(4)
    run_t = p_title.add_run("[行政營運專員] 吳思穎")
    set_run_font(run_t, size_pt=10, bold=True, color=RGBColor(15, 23, 42))

    add_body_p("您好，", indent=False, space_after=3, size_pt=10)
    add_body_p("我是吳思穎 Alice，有約6年專案行政與活動營運經驗。看到 justfont 徵求行政營運專員，想誠摯地投遞應徵。", size_pt=10)
    add_body_p("我對 justfont 的認識，是從使用粉圓體開始的。Google 文件能用粉圓時，我非常開心；後來也追蹤了Instagram，蘭陽黑體的「信任遊戲」短片讓我印象深刻。我喜歡在穩定架構下又帶有個人風格的字體，也相信不同情境適合用不同字體表達情緒，所以選擇越多越好。小時候的硬筆字比賽多半以標楷體為標準，我的美感也是很晚才開始累積，所以特別珍惜 justfont 讓更多人接觸到多元字體的努力。", size_pt=10)
    add_body_p("在過去的工作中，我習慣把重複、容易出錯的事情整理成清楚的流程。例如我設計了說明會核銷的試算表範本，讓年底整理時間從約一個工作天縮短到半天內，後來被會計推薦給其他專案參考；也設計過前後測成效統計表，讓每場結束就能看見結果並調整課程。參與專案 AI 客服導入時，我也學到什麼工作適合交給 AI、什麼工作不必，曾建議某個名單篩選流程用調整邏輯與程式自動化處理即可，確保名單的正確性可控，不必全部交給 LLM，意見後來獲得甲方採納。", size_pt=10)
    add_body_p("我的客服經驗以電話與面對面為主，文字客服、收款與開立發票、合約審閱的實務經驗較少，這幾項我很願意學習，也習慣在遇到沒做過的事時先查資料，再整理成可重複使用的做法。", size_pt=10)
    add_body_p("隨信附上履歷，期待有機會與您現場面談。", size_pt=10)
    
    p_sign = doc.add_paragraph()
    p_sign.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_sign.paragraph_format.space_after = Pt(4)
    run_wish = p_sign.add_run("祝  徵才順利\n")
    set_run_font(run_wish, size_pt=9.5, color=RGBColor(100, 116, 139))
    run_author = p_sign.add_run("吳思穎 Alice")
    set_run_font(run_author, size_pt=10.5, bold=True, color=RGBColor(15, 23, 42))

    # >>> 換頁到第 2 頁 <<<
    doc.add_page_break()

    # ==================== 第 2 頁：行政工作實績（一）帳務核銷 ＆ 試算表與資料管理 ====================
    add_section_header("行政工作實績（一）帳務核銷 ＆ 試算表與資料管理", space_before=4)

    # 01. 帳務與核銷
    p_sub1 = doc.add_paragraph()
    p_sub1.paragraph_format.space_before = Pt(6)
    p_sub1.paragraph_format.space_after = Pt(2)
    run_sub1 = p_sub1.add_run("01. 帳務與核銷")
    set_run_font(run_sub1, size_pt=11, bold=True, color=RGBColor(217, 119, 6))

    add_body_p("負責年度說明會（10～15 場）經費的預算編列、預支、請款與核銷，涵蓋場地、餐盒、交通、住宿、郵寄等項目，年度總額約 10 萬元、核銷細項約 100 筆。")
    add_body_p("自行設計雲端試算表記帳範本並附填寫說明，由經手同事於活動期間逐筆登錄金額與憑證轉手人員；年底核銷整理時間由約一個工作天縮短至半天內，憑證遺失時可追溯。範本經會計推薦給其他專案參考。")
    add_image_with_caption(os.path.join(img_dir, "image1.jpeg"), "【圖示】自行設計之雲端試算表記帳範本（隨時掌握預算剩餘金額、核銷進度與憑證流向）", width=Inches(6.0), space_after=8)

    # 02. 試算表與資料管理 (A)
    p_sub2 = doc.add_paragraph()
    p_sub2.paragraph_format.space_before = Pt(6)
    p_sub2.paragraph_format.space_after = Pt(2)
    run_sub2 = p_sub2.add_run("02. 試算表與資料管理")
    set_run_font(run_sub2, size_pt=11, bold=True, color=RGBColor(217, 119, 6))

    p_sub2_1 = doc.add_paragraph()
    p_sub2_1.paragraph_format.space_after = Pt(2)
    run_s21 = p_sub2_1.add_run("● excel資料庫與 Word 合併列印批次作業：")
    set_run_font(run_s21, size_pt=10, bold=True, color=RGBColor(15, 23, 42))
    add_body_p("具備 Excel 樞紐分析、IF、COUNTIF、XLOOKUP使用經驗；Excel資料庫搭配 Word 合併列印功能，批次產出活動場地包裹標籤、獎品寄送與行前通知，整合原本分散於各資料夾的重複資料，利用程式自動化抓取資料，減少批次處理的人為錯誤。")
    add_image_with_caption(os.path.join(img_dir, "image2.jpeg"), "【圖示】郵寄主清單搭配 Word 合併列印產出行前通知與包裹標籤", width=Inches(5.8), space_after=6)

    p_note = doc.add_paragraph()
    p_note.paragraph_format.space_before = Pt(2)
    p_note.paragraph_format.space_after = Pt(2)
    run_n = p_note.add_run("※ 說明會學習成效統計表（四層試算表架構：圖一至圖四）詳見次頁。")
    set_run_font(run_n, size_pt=9, color=RGBColor(100, 116, 139))

    # >>> 換頁到第 3 頁 <<<
    doc.add_page_break()

    # ==================== 第 3 頁：行政工作實績（二）說明會成效四層試算表 ＆ 流程文件檔案 ====================
    add_section_header("行政工作實績（二）成效統計四層試算表 ＆ 流程文件檔案", space_before=4)

    p_sub2_2 = doc.add_paragraph()
    p_sub2_2.paragraph_format.space_before = Pt(4)
    p_sub2_2.paragraph_format.space_after = Pt(2)
    run_s22 = p_sub2_2.add_run("● 說明會學習成效統計表（四層試算表架構）：")
    set_run_font(run_s22, size_pt=10.5, bold=True, color=RGBColor(15, 23, 42))
    add_body_p("設計說明會學習成效統計表（年約 1,000 份問卷）：以自編抽獎流水號串接前後測資料，建立「貼入原始資料即自動計算」的四層試算表，訂定資料比對規則（無法對應者人工檢視後剔除）；成效結果由年底統整提前至每場結束即可得出，並依各題答錯率調整下一場講課重點；完成操作說明並交接。")

    # 2x2 表格排版 4 張試算表
    tbl_4 = doc.add_table(rows=2, cols=2)
    tbl_4.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_4.autofit = False
    
    t_widths = [Inches(3.2), Inches(3.2)]
    for r in tbl_4.rows:
        for idx, w in enumerate(t_widths):
            r.cells[idx].width = w

    imgs_4 = [
        (os.path.join(img_dir, "image3.jpeg"), "【圖一】Google 問卷原始資料（抽獎流水號）"),
        (os.path.join(img_dir, "image4.jpeg"), "【圖二】會後原始資料彙整"),
        (os.path.join(img_dir, "image5.jpeg"), "【圖三】Kahoot! 資料對錯自動判定"),
        (os.path.join(img_dir, "image6.jpeg"), "【圖四】前後測結果一覽表（XLOOKUP串接）"),
    ]

    for i, (path, cap) in enumerate(imgs_4):
        row = i // 2
        col = i % 2
        c = tbl_4.cell(row, col)
        cp = c.paragraphs[0]
        cp.paragraph_format.space_after = Pt(1)
        cp.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        cpr = cp.add_run()
        if os.path.exists(path):
            cpr.add_picture(path, width=Inches(3.0))
        cp_cap = c.add_paragraph()
        cp_cap.paragraph_format.space_after = Pt(4)
        cp_cap.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_c = cp_cap.add_run(cap)
        set_run_font(r_c, size_pt=7.5, color=RGBColor(100, 116, 139))

    # 03. 流程、文件與檔案
    p_sub3 = doc.add_paragraph()
    p_sub3.paragraph_format.space_before = Pt(10)
    p_sub3.paragraph_format.space_after = Pt(2)
    run_sub3 = p_sub3.add_run("03. 流程、文件與檔案")
    set_run_font(run_sub3, size_pt=11, bold=True, color=RGBColor(37, 99, 235))

    add_body_p("● 檔案分層與版本命名規則：自訂檔案分層與版本規則（年度＼工項＼文件標題＼編輯日期＼版本），為所做工作撰寫備忘與交接說明，離職前以文件與存檔路徑完成交接。")
    add_body_p("● 公文撰擬與場地租借合約：負責專案進度報告與請款之公文撰擬與提送（參照既有範本；遇無前例類型時自行查閱規範），並協辦年度說明會場地租借合約。")

    # >>> 換頁到第 4 頁 <<<
    doc.add_page_break()

    # ==================== 第 4 頁：行政工作實績（三）AI 客服與自動化 ＆ 活動營運溝通 ====================
    add_section_header("行政工作實績（三）AI 客服與自動化 ＆ 活動營運溝通", space_before=4)

    # 04. AI 與自動化
    p_sub4 = doc.add_paragraph()
    p_sub4.paragraph_format.space_before = Pt(4)
    p_sub4.paragraph_format.space_after = Pt(2)
    run_sub4 = p_sub4.add_run("04. AI 與自動化")
    set_run_font(run_sub4, size_pt=11, bold=True, color=RGBColor(13, 148, 136))

    add_body_p("參與專案 AI 客服導入（2026年 1 月上線）：比較多種 LLM 與 embedding／RAG 方案並建立測試紀錄；針對電話紀錄與常見問答兩種資料測試三種組合，採「電話紀錄之提問＋常見問答之回答」，以涵蓋多樣真實問法並降低誤答；擬定資料庫整理 SOP 與清洗流程，資料品質不佳時改向第一線客服徵集常見問答；由 20～30 位同仁參與、累計至少 3,000 筆測試，依題型統計準確率（單一題型達約 90%），並依結果調整資料。")
    add_body_p("使用 Dify 自建 AI 工作流，便於追蹤與除錯；撰寫 AI 技術科普與導入評估報告，協助承辦單位決策。協助評估名單篩選流程自動化：研究過往作法後，建議調整判斷順序並搭配程式自動化，無須全面交由 LLM 處理，經報告後獲採納。")

    # 6 张投影片 (2x3 表格)
    p_ppt_title = doc.add_paragraph()
    p_ppt_title.paragraph_format.space_before = Pt(4)
    p_ppt_title.paragraph_format.space_after = Pt(2)
    run_ppt = p_ppt_title.add_run("● 大語言模型 (LLM) 測試工作分享簡報（共 6 張投影片）：")
    set_run_font(run_ppt, size_pt=9.5, bold=True, color=RGBColor(15, 23, 42))

    tbl_6 = doc.add_table(rows=2, cols=3)
    tbl_6.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_6.autofit = False
    
    t6_widths = [Inches(2.13), Inches(2.13), Inches(2.13)]
    for r in tbl_6.rows:
        for idx, w in enumerate(t6_widths):
            r.cells[idx].width = w

    imgs_6 = [
        (os.path.join(img_dir, "image7.jpeg"), "1. 簡報封面"),
        (os.path.join(img_dir, "image8.jpeg"), "2. 備料與烹調"),
        (os.path.join(img_dir, "image9.jpeg"), "3. RAG架構圖"),
        (os.path.join(img_dir, "image10.jpeg"), "4. 3x3方案測試"),
        (os.path.join(img_dir, "image11.jpeg"), "5. 測試紀錄表"),
        (os.path.join(img_dir, "image12.jpeg"), "6. 品質評估統計"),
    ]

    for i, (path, cap) in enumerate(imgs_6):
        row = i // 3
        col = i % 3
        c = tbl_6.cell(row, col)
        cp = c.paragraphs[0]
        cp.paragraph_format.space_after = Pt(1)
        cp.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        cpr = cp.add_run()
        if os.path.exists(path):
            cpr.add_picture(path, width=Inches(2.0))
        cp_cap = c.add_paragraph()
        cp_cap.paragraph_format.space_after = Pt(3)
        cp_cap.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_c = cp_cap.add_run(cap)
        set_run_font(r_c, size_pt=7, color=RGBColor(100, 116, 139))

    # 05. 活動營運與溝通
    p_sub5 = doc.add_paragraph()
    p_sub5.paragraph_format.space_before = Pt(8)
    p_sub5.paragraph_format.space_after = Pt(2)
    run_sub5 = p_sub5.add_run("05. 活動營運與溝通")
    set_run_font(run_sub5, size_pt=11, bold=True, color=RGBColor(225, 29, 72))

    add_body_p("● 說明會報名前置統籌：整理場次、時程與報名須知供官網上架，自系統後台彙整報名人數估算講義數量，並製作簽到表、工作人員行前通知與場地動線／站位示意圖。")
    add_body_p("● 第一線客服與實體講師：擔任專案電話客服代班（每日約 10～20 通），並每年兩度、各連續約一個月每日至少 20 通外撥電話向業者說明新政策，執行 5～6 年；每年至少擔任 3 場說明會講師，課後面對面回答 5～20 位業者的法規與申報問題。")
    add_body_p("● 個資與敏感資料最小揭露原則：簽到單僅列公司名稱、統編與人數；建立 AI 客服資料庫時過濾含聯絡人姓氏、營運狀況與密碼的內容。")
    add_body_p("● 跨組經驗分享與流程諮詢：受主管邀請於公司內分享 AI 客服測試心得與線上說明會控場流程；整理之場地名單於組內流通，主管並轉介他組同仁來諮詢。")

    # >>> 換頁到第 5 頁 <<<
    doc.add_page_break()

    # ==================== 第 5 頁：學經歷時間軸 ＆ 證照與技能 ====================
    add_section_header("學經歷時間軸", space_before=4)

    # 4.1 IMO
    p_e1 = doc.add_paragraph()
    p_e1.paragraph_format.space_before = Pt(4)
    p_e1.paragraph_format.space_after = Pt(1)
    run_e1 = p_e1.add_run("埃恩歐設計顧問有限公司 (IMO Architecture + Design Ltd.) ｜ 行政秘書")
    set_run_font(run_e1, size_pt=10.5, bold=True, color=RGBColor(15, 23, 42))
    
    p_e1_sub = doc.add_paragraph()
    p_e1_sub.paragraph_format.space_after = Pt(2)
    run_e1_s = p_e1_sub.add_run("2026/5 ～ 2026/7（3個月） ｜ 台北市大安區 ｜ 建築設計業 1~30人 ｜ 主管西班牙籍、同事美籍，雙語溝通經驗")
    set_run_font(run_e1_s, size_pt=8.5, color=RGBColor(100, 116, 139))
    add_body_p("行政庶務（電話、信件郵寄）、辦公室設施管理維護、人事財務（出缺勤、零用金、二代健保補充保費申報）、網站文章維護。", indent=False, space_after=5)

    # 4.2 環資國際
    p_e2 = doc.add_paragraph()
    p_e2.paragraph_format.space_before = Pt(4)
    p_e2.paragraph_format.space_after = Pt(1)
    run_e2 = p_e2.add_run("環資國際有限公司 ｜ 環境工程師 / 專案執行")
    set_run_font(run_e2, size_pt=10.5, bold=True, color=RGBColor(15, 23, 42))
    
    p_e2_sub = doc.add_paragraph()
    p_e2_sub.paragraph_format.space_after = Pt(2)
    run_e2_s = p_e2_sub.add_run("2020/8 ～ 2026/3（5年8個月） ｜ 台北市萬華區 ｜ 工商顧問服務業 100~500人")
    set_run_font(run_e2_s, size_pt=8.5, color=RGBColor(100, 116, 139))
    add_body_p("年度活動統籌（巡迴說明會 10-15 場約千人、Google Meet 350 人線上會議、Kahoot!/問卷即時分析、講師主持）；教材文宣規劃（法規轉譯、PPT視覺化、社群圖卡）；客服系統轉型（LINE@ 分流、Dify 知識庫架構與工作流建置、跨團隊窗口）。", indent=False, space_after=5)

    # 4.3 德利威電子
    p_e3 = doc.add_paragraph()
    p_e3.paragraph_format.space_before = Pt(4)
    p_e3.paragraph_format.space_after = Pt(1)
    run_e3 = p_e3.add_run("德利威電子股份有限公司 ｜ 行政櫃台／文管（約聘）")
    set_run_font(run_e3, size_pt=10.5, bold=True, color=RGBColor(15, 23, 42))
    
    p_e3_sub = doc.add_paragraph()
    p_e3_sub.paragraph_format.space_after = Pt(2)
    run_e3_s = p_e3_sub.add_run("2019/7 ～ 2020/2（8個月） ｜ 新北市中和區 ｜ 其他金屬相關製造業 500人以上")
    set_run_font(run_e3_s, size_pt=8.5, color=RGBColor(100, 116, 139))
    add_body_p("行政請款、零用金、用品叫修採購、接待訂餐；文管歸檔、會簽追蹤（ECR/ECN）、產品圖面更新、客戶承認書彙整建檔。", indent=False, space_after=5)

    # 4.4 輔仁大學
    p_edu = doc.add_paragraph()
    p_edu.paragraph_format.space_before = Pt(4)
    p_edu.paragraph_format.space_after = Pt(1)
    run_edu = p_edu.add_run("私立輔仁大學 ｜ 雙學士")
    set_run_font(run_edu, size_pt=10.5, bold=True, color=RGBColor(15, 23, 42))
    add_body_p("中國文學系 大學畢業（2014/9 ～ 2018/6） ＆ 德語語文學系 大學畢業（2015/9 ～ 2019/6，雙學士）", indent=False, space_after=10)

    # 證照與技能
    add_section_header("證照與技能", space_before=6)

    add_body_p("【專業資格認證】", indent=False, space_after=2, size_pt=9.5)
    add_body_p("・陸上運輸相關證照：普通小型車駕照（中華民國交通部公路總局 4011510151103，2026/10 ～ 2065/12）", indent=False, space_after=2)
    add_body_p("・英語相關證照：TOEIC (多益測驗) 860 分（聽力 465 / 閱讀 395，2019）", indent=False, space_after=2)
    add_body_p("・其他語言證照：FLPT (德語檢定) 筆試 237分 (B2) / 口試 S2 (B1)（2019）", indent=False, space_after=2)
    add_body_p("・人力資源相關證照：全方位基礎人力資源管理師認證（社團法人中華人力資源管理協會）", indent=False, space_after=5)

    add_body_p("【擅長工具與語言】", indent=False, space_after=2, size_pt=9.5)
    add_body_p("・辦公室應用類：PowerPoint、Word（合併列印）、Excel（樞紐分析、IF、COUNTIF、XLOOKUP）、Outlook", indent=False, space_after=2)
    add_body_p("・數位與協作平台：Dify (AI 工作流與知識庫)、Google Meet、LINE@ 官方帳號、Kahoot!", indent=False, space_after=2)
    add_body_p("・語言能力：英文（中等，英語工作環境溝通）、德文（中等，雙學士）、台語（略懂）", indent=False, space_after=6)

    doc.save(output_path)
    print(f"5-page Docx saved to: {output_path} ({os.path.getsize(output_path)} bytes)")

if __name__ == "__main__":
    out = "/Users/wufamily/Documents/ssu ying justfont resume/吳思穎_justfont應徵履歷_附實績圖文.docx"
    imgs = "/Users/wufamily/Documents/ssu ying justfont resume/images"
    create_resume_docx_5pages(out, imgs)
