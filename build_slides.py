import os
import subprocess
import time

base_dir = "/Users/wufamily/Documents/ssu ying justfont resume"
html_dir = os.path.join(base_dir, "slides_html")
img_dir = os.path.join(base_dir, "slides")
os.makedirs(html_dir, exist_ok=True)
os.makedirs(img_dir, exist_ok=True)

# Shared CSS Header for slides
def get_head(theme):
    is_dark = (theme == 'dark')
    bg_body = "#07090e" if is_dark else "#f8fafc"
    text_body = "#e2e8f0" if is_dark else "#1e293b"
    
    return f"""<!DOCTYPE html>
<html lang="zh-TW" class="{'dark' if is_dark else ''}">
<head>
    <meta charset="UTF-8">
    <title>Slide</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@600;700&family=Quicksand:wght@500;600;700&display=swap" rel="stylesheet">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            darkMode: 'class',
            theme: {{
                extend: {{
                    colors: {{
                        rainbow: {{
                            red: '#FF0055',
                            redDark: '#E11D48',
                            orange: '#FF6B00',
                            orangeDark: '#EA580C',
                            yellow: '#FFD100',
                            yellowDark: '#D97706',
                            green: '#00F5D4',
                            greenDark: '#0D9488',
                            blue: '#0088FF',
                            blueDark: '#2563EB',
                        }}
                    }},
                    fontFamily: {{
                        heading: ['Comfortaa', 'OpenHuninn', 'GenSenRounded', 'sans-serif'],
                        body: ['Quicksand', 'OpenHuninn', 'GenSenRounded', 'sans-serif'],
                    }}
                }}
            }}
        }}
    </script>
    <style>
        @font-face {{
            font-family: 'OpenHuninn';
            src: url('../fonts/jf-openhuninn-2.1.ttf') format('truetype');
            font-weight: 400 700;
        }}
        @font-face {{
            font-family: 'GenSenRounded';
            src: url('../fonts/gensen/GenSenRounded2TW-R.otf') format('opentype');
            font-weight: 400;
        }}
        @font-face {{
            font-family: 'GenSenRounded';
            src: url('../fonts/gensen/GenSenRounded2TW-M.otf') format('opentype');
            font-weight: 500;
        }}
        @font-face {{
            font-family: 'GenSenRounded';
            src: url('../fonts/gensen/GenSenRounded2TW-B.otf') format('opentype');
            font-weight: 700;
        }}
        @font-face {{
            font-family: 'GenSenRounded';
            src: url('../fonts/gensen/GenSenRounded2TW-H.otf') format('opentype');
            font-weight: 800 900;
        }}
        body {{
            margin: 0;
            padding: 0;
            width: 1920px;
            height: 1080px;
            overflow: hidden;
            background-color: {bg_body};
            color: {text_body};
            font-family: 'Quicksand', 'OpenHuninn', 'GenSenRounded', sans-serif;
            -webkit-font-smoothing: antialiased;
        }}
        .slide-container {{
            width: 1920px;
            height: 1080px;
            box-sizing: border-box;
            padding: 48px 64px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}
        p.indent {{
            text-indent: 2em;
        }}
        .solid-dot-blue {{ background-color: {'#0088FF' if is_dark else '#2563EB'}; border: none !important; }}
        .solid-dot-green {{ background-color: {'#00F5D4' if is_dark else '#0D9488'}; border: none !important; }}
        .solid-dot-yellow {{ background-color: {'#FFD100' if is_dark else '#D97706'}; border: none !important; }}
        .solid-dot-red {{ background-color: {'#FF0055' if is_dark else '#E11D48'}; border: none !important; }}
    </style>
</head>
<body class="{'dark' if is_dark else ''}">
"""

def get_footer(theme, page_num, total_pages=6):
    is_dark = (theme == 'dark')
    border_color = "border-slate-800" if is_dark else "border-slate-200"
    text_color = "text-slate-400" if is_dark else "text-slate-600"
    return f"""
    <!-- Slide Footer -->
    <div class="pt-4 border-t {border_color} flex items-center justify-between {text_color} text-sm font-medium">
        <div class="flex items-center gap-6">
            <span>吳思穎 Alice Wu ｜ 應徵 justfont 行政營運專員</span>
            <span><i class="fas fa-phone mr-1"></i> 0958-321-139</span>
            <span><i class="fas fa-envelope mr-1"></i> ichbinalicewu35@gmail.com</span>
        </div>
        <div class="flex items-center gap-4">
            <span>字體：justfont 粉圓體 ＆ 源泉圓體</span>
            <span class="font-bold font-mono px-2.5 py-0.5 rounded {'bg-slate-800 text-white' if is_dark else 'bg-slate-200 text-slate-800'}">{page_num} / {total_pages}</span>
        </div>
    </div>
</div>
</body>
</html>
"""

# Slide 1: 自我介紹
def slide_01_intro(theme):
    is_dark = (theme == 'dark')
    card_bg = "bg-[#0d121c] border-slate-800" if is_dark else "bg-white border-slate-200 shadow-sm"
    h_color = "text-rose-500" if is_dark else "text-rose-600"
    badge_bg = "bg-rose-950/60 text-rose-300 border-rose-900/60" if is_dark else "bg-rose-50 text-rose-700 border-rose-200"
    text_main = "text-slate-200" if is_dark else "text-slate-700"
    
    return get_head(theme) + f"""
<div class="slide-container">
    <!-- Header -->
    <div class="flex items-center justify-between pb-3 border-b {'border-slate-800' if is_dark else 'border-slate-200'}">
        <div class="flex items-center gap-4">
            <div class="w-12 h-12 rounded-full border-2 {'border-rose-500 text-rose-500' if is_dark else 'border-rose-600 text-rose-600'} flex items-center justify-center font-heading font-black text-xl">
                吳
            </div>
            <div>
                <h1 class="font-heading text-3xl font-black {'text-white' if is_dark else 'text-slate-900'}">吳思穎 <span class="{h_color} text-2xl font-bold">Alice Wu</span></h1>
                <p class="text-xs {'text-slate-400' if is_dark else 'text-slate-500'}">專案行政與活動營運 ｜ 建立清楚重複的流程 ｜ 法規轉譯與實務自動化</p>
            </div>
        </div>
        <div class="flex items-center gap-3 text-sm">
            <span class="px-3 py-1 rounded-full text-xs font-bold border {badge_bg}">應徵職缺｜justfont 行政營運專員</span>
            <span class="px-3 py-1 rounded-full text-xs font-bold {'bg-emerald-950/60 text-emerald-300 border border-emerald-900/60' if is_dark else 'bg-emerald-50 text-emerald-700 border border-emerald-200'}">待業中（錄取後一週可上班）</span>
        </div>
    </div>

    <!-- Main Content: 自我介紹信件容器 -->
    <div class="my-auto rounded-2xl border {card_bg} p-8 space-y-5">
        <div class="flex items-center justify-between border-b {'border-slate-800' if is_dark else 'border-slate-100'} pb-3">
            <div class="flex items-center gap-2.5 {h_color} font-heading text-2xl font-bold">
                <i class="fas fa-paper-plane text-xl"></i>
                <span>自我介紹</span>
            </div>
            <span class="font-mono text-xs font-semibold px-3 py-1 rounded {'bg-slate-800 text-slate-300' if is_dark else 'bg-slate-100 text-slate-700'}">
                [行政營運專員] 吳思穎
            </span>
        </div>

        <div class="grid grid-cols-2 gap-8 text-[15px] {text_main} leading-relaxed">
            <div class="space-y-4">
                <p class="font-bold {'text-white' if is_dark else 'text-slate-900'} text-base">justfont 您好：</p>
                <p class="indent">我是吳思穎 Alice，有約6年專案行政與活動營運經驗。看到 justfont 徵求行政營運專員，想誠摯地投遞應徵。</p>
                <p class="indent">我對 justfont 的認識，是從使用粉圓體開始的。Google 文件能用粉圓時，我非常開心；後來也追蹤了Instagram，蘭陽黑體的「信任遊戲」短片讓我印象深刻。我喜歡在穩定架構下又帶有個人風格的字體，也相信不同情境適合用不同字體表達情緒，所以選擇越多越好。小時候的硬筆字比賽多半以標楷體為標準，我的美感也是很晚才開始累積，所以特別珍惜 justfont 讓更多人接觸到多元字體的努力。</p>
            </div>
            <div class="space-y-4">
                <p class="indent">在過去的工作中，我習慣把重複、容易出錯的事情整理成清楚的流程。例如我設計了說明會核銷的試算表範本，讓年底整理時間從約一個工作天縮短到半天內，後來被會計推薦給其他專案參考；也設計過前後測成效統計表，讓每場結束就能看見結果並調整課程。參與專案 AI 客服導入時，我也學到什麼工作適合交給 AI、什麼工作不必，曾建議某個名單篩選流程用調整邏輯與程式自動化處理即可，確保名單的正確性可控，不必全部交給 LLM，意見後來獲得甲方採納。</p>
                <p class="indent">我的客服經驗以電話與面對面為主，文字客服、收款與開立發票、合約審閱的實務經驗較少，這幾項我很願意學習，也習慣在遇到沒做過的事時先查資料，再整理成可重複使用的做法。</p>
                <div class="pt-2 flex items-center justify-between border-t {'border-slate-800' if is_dark else 'border-slate-100'}">
                    <p class="indent text-sm">隨信附上履歷，期待有機會與您現場面談。</p>
                    <div class="text-right">
                        <span class="text-xs {'text-slate-400' if is_dark else 'text-slate-500'}">祝 徵才順利</span>
                        <span class="font-heading font-bold text-base {'text-white' if is_dark else 'text-slate-900'} ml-3">吳思穎 Alice</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
""" + get_footer(theme, 1)

# Slide 2: 行政工作實績（一）帳務核銷 ＆ 試算表與資料管理
def slide_02_admin1(theme):
    is_dark = (theme == 'dark')
    card_bg = "bg-[#0d121c] border-slate-800" if is_dark else "bg-white border-slate-200 shadow-sm"
    h_color = "text-rainbow-yellow" if is_dark else "text-amber-600"
    text_main = "text-slate-300" if is_dark else "text-slate-700"
    
    return get_head(theme) + f"""
<div class="slide-container">
    <!-- Header -->
    <div class="flex items-center justify-between pb-3 border-b {'border-slate-800' if is_dark else 'border-slate-200'}">
        <div class="flex items-center gap-3">
            <h2 class="font-heading text-3xl font-black {h_color}">行政工作實績</h2>
            <span class="text-lg font-bold {'text-white' if is_dark else 'text-slate-900'}">（一）帳務核銷 ＆ 試算表與資料管理</span>
        </div>
        <span class="text-xs font-semibold px-3 py-1 rounded-full {'bg-amber-950/60 text-amber-300 border border-amber-900/60' if is_dark else 'bg-amber-50 text-amber-700 border border-amber-200'}">
            環資國際 ｜ 專案執行（約 6 年）實務產出
        </span>
    </div>

    <!-- Content: 左右兩欄 -->
    <div class="grid grid-cols-12 gap-6 my-auto items-stretch">
        <!-- 左欄: 帳務與核銷 -->
        <div class="col-span-5 rounded-2xl border {card_bg} p-6 flex flex-col justify-between">
            <div class="space-y-3">
                <div class="flex items-center gap-2.5 font-heading text-xl font-bold {'text-white' if is_dark else 'text-slate-900'}">
                    <div class="w-8 h-8 rounded-lg {'bg-orange-950/60 text-rainbow-orange' if is_dark else 'bg-orange-100 text-orange-600'} flex items-center justify-center text-sm">
                        <i class="fas fa-file-invoice-dollar"></i>
                    </div>
                    <span>帳務與核銷</span>
                </div>
                <div class="text-[14px] {text_main} leading-relaxed space-y-2">
                    <p class="indent">負責年度說明會（10～15 場）經費的預算編列、預支、請款與核銷，涵蓋場地、餐盒、交通、住宿、郵寄等項目，年度總額約 10 萬元、核銷細項約 100 筆。</p>
                    <p class="indent">自行設計雲端試算表記帳範本並附填寫說明，由經手同事於活動期間逐筆登錄金額與憑證轉手人員；年底核銷整理時間由約一個工作天縮短至半天內，憑證遺失時可追溯。範本經會計推薦給其他專案參考。</p>
                </div>
            </div>
            <div class="mt-3 rounded-xl overflow-hidden border {'border-slate-800' if is_dark else 'border-slate-200'}">
                <img src="../images/image1.jpeg" class="w-full h-44 object-cover object-top">
                <div class="p-2 bg-slate-100 dark:bg-[#111622] text-[11px] {'text-slate-400' if is_dark else 'text-slate-500'} flex justify-between">
                    <span><i class="fas fa-table mr-1 text-orange-500"></i> 雲端試算表記帳範本</span>
                    <span>隨時掌握預算剩餘金額</span>
                </div>
            </div>
        </div>

        <!-- 右欄: 試算表與資料管理 -->
        <div class="col-span-7 rounded-2xl border {card_bg} p-6 flex flex-col justify-between">
            <div class="space-y-3">
                <div class="flex items-center gap-2.5 font-heading text-xl font-bold {'text-white' if is_dark else 'text-slate-900'}">
                    <div class="w-8 h-8 rounded-lg {'bg-amber-950/60 text-rainbow-yellow' if is_dark else 'bg-amber-100 text-amber-700'} flex items-center justify-center text-sm">
                        <i class="fas fa-file-excel"></i>
                    </div>
                    <span>試算表與資料管理</span>
                </div>
                <div class="text-[13px] {text_main} leading-relaxed space-y-1.5">
                    <p class="indent"><strong class="{'text-white' if is_dark else 'text-slate-900'}">excel資料庫與 Word 合併列印：</strong>具備 Excel 樞紐分析、IF、COUNTIF、XLOOKUP使用經驗；Excel資料庫搭配 Word 合併列印功能，批次產出活動場地包裹標籤、獎品寄送與行前通知，整合原本分散重複資料，利用程式自動化抓取資料，減少批次處理人為錯誤。</p>
                    <p class="indent"><strong class="{'text-white' if is_dark else 'text-slate-900'}">說明會學習成效統計表（四層試算表）：</strong>以自編抽獎流水號串接前後測資料，建立「貼入原始資料即自動計算」試算表，訂定資料比對規則；成效結果由年底統整提前至每場結束即可得出，依答錯率調整下一場重點並完成交接。</p>
                </div>
            </div>
            
            <div class="grid grid-cols-5 gap-2.5 mt-3">
                <div class="col-span-2 rounded-lg overflow-hidden border {'border-slate-800' if is_dark else 'border-slate-200'}">
                    <img src="../images/image2.jpeg" class="w-full h-32 object-cover">
                    <div class="p-1 bg-slate-100 dark:bg-[#111622] text-[10px] text-center {'text-slate-400' if is_dark else 'text-slate-600'}">Word 合併列印行前通知</div>
                </div>
                <div class="col-span-3 grid grid-cols-4 gap-1.5">
                    <div class="rounded overflow-hidden border {'border-slate-800' if is_dark else 'border-slate-200'}">
                        <img src="../images/image3.jpeg" class="w-full h-24 object-cover">
                        <div class="p-0.5 text-center text-[9px] bg-slate-100 dark:bg-[#111622]">圖一 問卷原始</div>
                    </div>
                    <div class="rounded overflow-hidden border {'border-slate-800' if is_dark else 'border-slate-200'}">
                        <img src="../images/image4.jpeg" class="w-full h-24 object-cover">
                        <div class="p-0.5 text-center text-[9px] bg-slate-100 dark:bg-[#111622]">圖二 會後資料</div>
                    </div>
                    <div class="rounded overflow-hidden border {'border-slate-800' if is_dark else 'border-slate-200'}">
                        <img src="../images/image5.jpeg" class="w-full h-24 object-cover">
                        <div class="p-0.5 text-center text-[9px] bg-slate-100 dark:bg-[#111622]">圖三 Kahoot判定</div>
                    </div>
                    <div class="rounded overflow-hidden border {'border-slate-800' if is_dark else 'border-slate-200'}">
                        <img src="../images/image6.jpeg" class="w-full h-24 object-cover">
                        <div class="p-0.5 text-center text-[9px] bg-slate-100 dark:bg-[#111622]">圖四 XLOOKUP</div>
                    </div>
                    <div class="col-span-4 text-center text-[11px] {'text-slate-400' if is_dark else 'text-slate-500'} pt-0.5">
                        <i class="fas fa-layer-group text-amber-500 mr-1"></i> 四層試算表架構：問卷 ➔ 會後資料 ➔ Kahoot對錯 ➔ 前後測自動串接計算
                    </div>
                </div>
            </div>
        </div>
    </div>
""" + get_footer(theme, 2)

# Slide 3: 行政工作實績（二）AI 與自動化
def slide_03_admin2(theme):
    is_dark = (theme == 'dark')
    card_bg = "bg-[#0d121c] border-slate-800" if is_dark else "bg-white border-slate-200 shadow-sm"
    h_color = "text-rainbow-yellow" if is_dark else "text-amber-600"
    text_main = "text-slate-300" if is_dark else "text-slate-700"
    
    return get_head(theme) + f"""
<div class="slide-container">
    <!-- Header -->
    <div class="flex items-center justify-between pb-3 border-b {'border-slate-800' if is_dark else 'border-slate-200'}">
        <div class="flex items-center gap-3">
            <h2 class="font-heading text-3xl font-black {h_color}">行政工作實績</h2>
            <span class="text-lg font-bold {'text-white' if is_dark else 'text-slate-900'}">（二）AI 客服導入實作與流程自動化評估</span>
        </div>
        <span class="text-xs font-semibold px-3 py-1 rounded-full {'bg-teal-950/60 text-teal-300 border border-teal-900/60' if is_dark else 'bg-teal-50 text-teal-700 border border-teal-200'}">
            AI 與自動化實績
        </span>
    </div>

    <!-- Content: 文字說明 + 6張簡報投影片 -->
    <div class="my-auto space-y-5">
        <div class="rounded-2xl border {card_bg} p-6">
            <div class="flex items-center gap-2.5 font-heading text-xl font-bold {'text-white' if is_dark else 'text-slate-900'} mb-3">
                <div class="w-8 h-8 rounded-lg {'bg-teal-950/60 text-rainbow-green' if is_dark else 'bg-teal-100 text-teal-700'} flex items-center justify-center text-sm">
                    <i class="fas fa-robot"></i>
                </div>
                <span>AI 客服導入與測試工作（2026年 1 月上線）</span>
            </div>
            
            <div class="grid grid-cols-12 gap-6 text-[14px] {text_main} leading-relaxed">
                <div class="col-span-8 space-y-2">
                    <p class="indent">參與專案 AI 客服導入（2026年 1 月上線）：比較多種 LLM 與 embedding／RAG 方案並建立測試紀錄；針對電話紀錄與常見問答兩種資料測試三種組合，採「電話紀錄之提問＋常見問答之回答」，以涵蓋多樣真實問法並降低誤答；擬定資料庫整理 SOP 與清洗流程，資料品質不佳時改向第一線客服徵集常見問答；由 20～30 位同仁參與、累計至少 3,000 筆測試，依題型統計準確率（單一題型達約 90%），並依結果調整資料。</p>
                </div>
                <div class="col-span-4 space-y-2 border-l {'border-slate-800' if is_dark else 'border-slate-200'} pl-4 text-[13px]">
                    <p class="indent"><strong class="{'text-white' if is_dark else 'text-slate-900'}">Dify 工作流建置：</strong>使用 Dify 自建 AI 工作流，便於追蹤與除錯；撰寫 AI 技術科普與導入評估報告，協助承辦單位決策。</p>
                    <p class="indent"><strong class="{'text-white' if is_dark else 'text-slate-900'}">名單自動化評估：</strong>研究過往作法後，建議調整判斷順序並搭配程式自動化，無須全面交由 LLM 處理，獲甲方採納。</p>
                </div>
            </div>
        </div>

        <!-- 6 張投影片展示 -->
        <div class="rounded-2xl border {card_bg} p-5 space-y-2">
            <div class="flex justify-between items-center text-xs {'text-slate-400' if is_dark else 'text-slate-600'} font-semibold">
                <span><i class="fas fa-file-powerpoint text-teal-500 mr-1.5"></i> 大語言模型 (LLM) 測試工作分享簡報成果（共 6 張投影片）</span>
                <span>跨組分享 ＆ 內部技術教育訓練</span>
            </div>
            <div class="grid grid-cols-6 gap-3">
                <div class="rounded-lg overflow-hidden border {'border-slate-800' if is_dark else 'border-slate-200'}">
                    <img src="../images/image7.jpeg" class="w-full h-28 object-cover">
                    <div class="p-1 text-center text-[11px] font-medium bg-slate-100 dark:bg-[#111622]">1. 簡報封面</div>
                </div>
                <div class="rounded-lg overflow-hidden border {'border-slate-800' if is_dark else 'border-slate-200'}">
                    <img src="../images/image8.jpeg" class="w-full h-28 object-cover">
                    <div class="p-1 text-center text-[11px] font-medium bg-slate-100 dark:bg-[#111622]">2. 備料與烹調</div>
                </div>
                <div class="rounded-lg overflow-hidden border {'border-slate-800' if is_dark else 'border-slate-200'}">
                    <img src="../images/image9.jpeg" class="w-full h-28 object-cover">
                    <div class="p-1 text-center text-[11px] font-medium bg-slate-100 dark:bg-[#111622]">3. RAG架構圖</div>
                </div>
                <div class="rounded-lg overflow-hidden border {'border-slate-800' if is_dark else 'border-slate-200'}">
                    <img src="../images/image10.jpeg" class="w-full h-28 object-cover">
                    <div class="p-1 text-center text-[11px] font-medium bg-slate-100 dark:bg-[#111622]">4. 3x3方案測試</div>
                </div>
                <div class="rounded-lg overflow-hidden border {'border-slate-800' if is_dark else 'border-slate-200'}">
                    <img src="../images/image11.jpeg" class="w-full h-28 object-cover">
                    <div class="p-1 text-center text-[11px] font-medium bg-slate-100 dark:bg-[#111622]">5. 測試紀錄表</div>
                </div>
                <div class="rounded-lg overflow-hidden border {'border-slate-800' if is_dark else 'border-slate-200'}">
                    <img src="../images/image12.jpeg" class="w-full h-28 object-cover">
                    <div class="p-1 text-center text-[11px] font-medium bg-slate-100 dark:bg-[#111622]">6. 品質評估統計</div>
                </div>
            </div>
        </div>
    </div>
""" + get_footer(theme, 3)

# Slide 4: 行政工作實績（三）流程文件檔案 ＆ 活動營運與溝通
def slide_04_admin3(theme):
    is_dark = (theme == 'dark')
    card_bg = "bg-[#0d121c] border-slate-800" if is_dark else "bg-white border-slate-200 shadow-sm"
    h_color = "text-rainbow-yellow" if is_dark else "text-amber-600"
    text_main = "text-slate-300" if is_dark else "text-slate-700"
    
    return get_head(theme) + f"""
<div class="slide-container">
    <!-- Header -->
    <div class="flex items-center justify-between pb-3 border-b {'border-slate-800' if is_dark else 'border-slate-200'}">
        <div class="flex items-center gap-3">
            <h2 class="font-heading text-3xl font-black {h_color}">行政工作實績</h2>
            <span class="text-lg font-bold {'text-white' if is_dark else 'text-slate-900'}">（三）流程文件、公文合約、活動營運與溝通</span>
        </div>
        <span class="text-xs font-semibold px-3 py-1 rounded-full {'bg-blue-950/60 text-blue-300 border border-blue-900/60' if is_dark else 'bg-blue-50 text-blue-700 border border-blue-200'}">
            行政庶務與跨團隊協作
        </span>
    </div>

    <!-- Content: 左右兩欄 -->
    <div class="grid grid-cols-12 gap-6 my-auto items-stretch">
        <!-- 左欄: 流程、文件與檔案 -->
        <div class="col-span-5 rounded-2xl border {card_bg} p-6 flex flex-col justify-between">
            <div class="space-y-4">
                <div class="flex items-center gap-2.5 font-heading text-xl font-bold {'text-white' if is_dark else 'text-slate-900'}">
                    <div class="w-8 h-8 rounded-lg {'bg-blue-950/60 text-rainbow-blue' if is_dark else 'bg-blue-100 text-blue-600'} flex items-center justify-center text-sm">
                        <i class="fas fa-folder-tree"></i>
                    </div>
                    <span>流程、文件與檔案</span>
                </div>
                
                <div class="space-y-4 text-[14px] {text_main} leading-relaxed">
                    <div class="p-4 rounded-xl {'bg-[#111622] border border-slate-800' if is_dark else 'bg-slate-50 border border-slate-200'} space-y-1.5">
                        <h4 class="font-bold {'text-white' if is_dark else 'text-slate-900'} text-[15px] flex items-center gap-2">
                            <i class="fas fa-sitemap text-blue-500 text-xs"></i> 檔案分層與版本命名規則
                        </h4>
                        <p class="indent">自訂檔案分層與版本規則（<code class="text-xs font-mono px-2 py-0.5 rounded {'bg-slate-800 text-blue-300' if is_dark else 'bg-slate-200 text-blue-700'}">年度＼工項＼文件標題＼編輯日期＼版本</code>），為所做工作撰寫備忘與交接說明，離職前以文件與存檔路徑完成交接。</p>
                    </div>

                    <div class="p-4 rounded-xl {'bg-[#111622] border border-slate-800' if is_dark else 'bg-slate-50 border border-slate-200'} space-y-1.5">
                        <h4 class="font-bold {'text-white' if is_dark else 'text-slate-900'} text-[15px] flex items-center gap-2">
                            <i class="fas fa-file-signature text-blue-500 text-xs"></i> 公文撰擬與場地租借合約
                        </h4>
                        <p class="indent">負責專案進度報告與請款之公文撰擬與提送（參照既有範本；遇無前例類型時自行查閱規範），並協辦年度說明會場地租借合約。</p>
                    </div>
                </div>
            </div>
            
            <div class="p-3 rounded-lg text-xs {'bg-slate-900 text-slate-400' if is_dark else 'bg-slate-100 text-slate-600'}">
                <i class="fas fa-shield-halved text-blue-500 mr-1.5"></i> 嚴謹的文件生命週期控管與交接 SOP，降低人員更迭之溝通成本。
            </div>
        </div>

        <!-- 右欄: 活動營運與溝通 -->
        <div class="col-span-7 rounded-2xl border {card_bg} p-6 flex flex-col justify-between">
            <div class="space-y-3">
                <div class="flex items-center gap-2.5 font-heading text-xl font-bold {'text-white' if is_dark else 'text-slate-900'}">
                    <div class="w-8 h-8 rounded-lg {'bg-rose-950/60 text-rainbow-red' if is_dark else 'bg-rose-100 text-rose-600'} flex items-center justify-center text-sm">
                        <i class="fas fa-users-gear"></i>
                    </div>
                    <span>活動營運與溝通</span>
                </div>

                <div class="grid grid-cols-2 gap-3.5 text-[13px] {text_main} leading-relaxed">
                    <div class="p-3.5 rounded-xl {'bg-[#111622] border border-slate-800' if is_dark else 'bg-slate-50 border border-slate-200'} space-y-1">
                        <h5 class="font-bold {'text-white' if is_dark else 'text-slate-900'} text-[14px] flex items-center gap-1.5">
                            <span class="w-1.5 h-1.5 rounded-full bg-rose-500"></span> 說明會報名前置統籌
                        </h5>
                        <p class="indent">統籌年度說明會報名前置作業：整理場次、時程與報名須知供官網上架，自系統後台彙整報名人數估算講義數量，並製作簽到表、工作人員行前通知與場地動線／站位示意圖。</p>
                    </div>

                    <div class="p-3.5 rounded-xl {'bg-[#111622] border border-slate-800' if is_dark else 'bg-slate-50 border border-slate-200'} space-y-1">
                        <h5 class="font-bold {'text-white' if is_dark else 'text-slate-900'} text-[14px] flex items-center gap-1.5">
                            <span class="w-1.5 h-1.5 rounded-full bg-rose-500"></span> 第一線客服與實體講師
                        </h5>
                        <p class="indent">擔任專案電話客服代班（每日約 10～20 通），並每年兩度、各連續約一個月每日至少 20 通外撥電話向業者說明新政策，執行 5～6 年；每年至少擔任 3 場說明會講師，回答法規申報問題。</p>
                    </div>

                    <div class="p-3.5 rounded-xl {'bg-[#111622] border border-slate-800' if is_dark else 'bg-slate-50 border border-slate-200'} space-y-1">
                        <h5 class="font-bold {'text-white' if is_dark else 'text-slate-900'} text-[14px] flex items-center gap-1.5">
                            <span class="w-1.5 h-1.5 rounded-full bg-rose-500"></span> 個資與資料最小揭露原則
                        </h5>
                        <p class="indent">處理報名與客服資料時採最小揭露原則：簽到單僅列公司名稱、統編與人數；建立 AI 客服資料庫時過濾含聯絡人姓氏、營運狀況與密碼的內容。</p>
                    </div>

                    <div class="p-3.5 rounded-xl {'bg-[#111622] border border-slate-800' if is_dark else 'bg-slate-50 border border-slate-200'} space-y-1">
                        <h5 class="font-bold {'text-white' if is_dark else 'text-slate-900'} text-[14px] flex items-center gap-1.5">
                            <span class="w-1.5 h-1.5 rounded-full bg-rose-500"></span> 跨組分享與流程諮詢
                        </h5>
                        <p class="indent">受主管邀請於公司內分享 AI 客服測試心得與線上說明會控場流程；整理之場地名單於組內流通，主管並轉介他組同仁來諮詢。</p>
                    </div>
                </div>
            </div>

            <div class="p-3 rounded-lg text-xs {'bg-slate-900 text-slate-400' if is_dark else 'bg-slate-100 text-slate-600'} flex items-center justify-between">
                <span><i class="fas fa-handshake text-rose-500 mr-1.5"></i> 兼具法規精確轉譯與現場面對面親和力，具備完整跨領域溝通能耐。</span>
            </div>
        </div>
    </div>
""" + get_footer(theme, 4)

# Slide 5: 學經歷時間軸
def slide_05_timeline(theme):
    is_dark = (theme == 'dark')
    card_bg = "bg-[#0d121c] border-slate-800" if is_dark else "bg-white border-slate-200 shadow-sm"
    h_color = "text-rainbow-green" if is_dark else "text-teal-600"
    text_main = "text-slate-300" if is_dark else "text-slate-700"
    
    return get_head(theme) + f"""
<div class="slide-container">
    <!-- Header -->
    <div class="flex items-center justify-between pb-3 border-b {'border-slate-800' if is_dark else 'border-slate-200'}">
        <div class="flex items-center gap-3">
            <h2 class="font-heading text-3xl font-black {h_color}">學經歷時間軸</h2>
            <span class="text-lg font-bold {'text-white' if is_dark else 'text-slate-900'}">總年資 6~7 年工作經歷 ｜ 104 履歷精準呈現</span>
        </div>
        <span class="text-xs font-semibold px-3 py-1 rounded-full {'bg-teal-950/60 text-teal-300 border border-teal-900/60' if is_dark else 'bg-teal-50 text-teal-700 border border-teal-200'}">
            完整學經歷
        </span>
    </div>

    <!-- 橫向4大階段時間軸卡片 -->
    <div class="grid grid-cols-4 gap-5 my-auto items-stretch">
        
        <!-- 階段 1: IMO (藍色實心點) -->
        <div class="rounded-2xl border {card_bg} p-5 flex flex-col justify-between border-t-4 {'border-t-blue-500' if is_dark else 'border-t-blue-600'}">
            <div class="space-y-3">
                <div class="flex items-center gap-2">
                    <span class="w-3.5 h-3.5 rounded-full solid-dot-blue"></span>
                    <span class="text-xs font-mono font-bold px-2 py-0.5 rounded {'bg-blue-950/60 text-blue-300' if is_dark else 'bg-blue-50 text-blue-700'}">
                        2026/5 ～ 2026/7（3個月）
                    </span>
                </div>
                <div>
                    <h3 class="font-heading text-base font-bold {'text-white' if is_dark else 'text-slate-900'} leading-snug">
                        埃恩歐設計顧問 (IMO)
                    </h3>
                    <p class="{'text-blue-400' if is_dark else 'text-blue-600'} font-bold text-xs mt-0.5">行政秘書</p>
                </div>
                <div class="text-[12px] {text_main} space-y-1.5 leading-relaxed">
                    <p><strong>行政庶務：</strong>電話接聽與轉接、信件收發與郵寄。</p>
                    <p><strong>設施管理：</strong>環境維護、用品訂購、租賃管理。</p>
                    <p><strong>人資財務：</strong>出缺勤、零用金、二代健保補充保費申報。</p>
                    <p><strong>數位管理：</strong>公司網站文章更新與維護。</p>
                </div>
            </div>
            <div class="mt-2 text-[11px] p-2 rounded {'bg-slate-900 text-slate-400' if is_dark else 'bg-slate-50 text-slate-600 border border-slate-200'}">
                <i class="fas fa-globe text-blue-500 mr-1"></i> 西籍主管、美籍同事，日常英文為主、中文為輔，具雙語溝通經驗。
            </div>
        </div>

        <!-- 階段 2: 環資國際 (綠色實心點) -->
        <div class="rounded-2xl border {card_bg} p-5 flex flex-col justify-between border-t-4 {'border-t-teal-400' if is_dark else 'border-t-teal-600'}">
            <div class="space-y-3">
                <div class="flex items-center gap-2">
                    <span class="w-3.5 h-3.5 rounded-full solid-dot-green"></span>
                    <span class="text-xs font-mono font-bold px-2 py-0.5 rounded {'bg-teal-950/60 text-teal-300' if is_dark else 'bg-teal-50 text-teal-700'}">
                        2020/8 ～ 2026/3（5年8個月）
                    </span>
                </div>
                <div>
                    <h3 class="font-heading text-base font-bold {'text-white' if is_dark else 'text-slate-900'} leading-snug">
                        環資國際有限公司
                    </h3>
                    <p class="{'text-teal-400' if is_dark else 'text-teal-600'} font-bold text-xs mt-0.5">環境工程師 / 專案執行</p>
                </div>
                <div class="text-[12px] {text_main} space-y-1.5 leading-relaxed">
                    <p><strong>年度活動統籌：</strong>巡迴說明會 10-15 場、Google Meet 350 人線上會議、Kahoot!/問卷即時分析、擔任講師與主持。</p>
                    <p><strong>教材與視覺化：</strong>環保法規新舊差異分析，PPT 結構化排版、社群圖卡 5W1H 原則。</p>
                    <p><strong>AI 客服轉型：</strong>LINE@ 分流、Dify 知識庫架構與 AI 工作流建置、業務需求與技術端轉譯窗口。</p>
                </div>
            </div>
            <div class="mt-2 text-[11px] p-2 rounded {'bg-slate-900 text-slate-400' if is_dark else 'bg-slate-50 text-slate-600 border border-slate-200'}">
                <i class="fas fa-star text-teal-500 mr-1"></i> 歷練最深厚之 5 年 8 個月顧問專案經驗。
            </div>
        </div>

        <!-- 階段 3: 德利威電子 (黃色實心點) -->
        <div class="rounded-2xl border {card_bg} p-5 flex flex-col justify-between border-t-4 {'border-t-amber-400' if is_dark else 'border-t-amber-500'}">
            <div class="space-y-3">
                <div class="flex items-center gap-2">
                    <span class="w-3.5 h-3.5 rounded-full solid-dot-yellow"></span>
                    <span class="text-xs font-mono font-bold px-2 py-0.5 rounded {'bg-amber-950/60 text-amber-300' if is_dark else 'bg-amber-50 text-amber-700'}">
                        2019/7 ～ 2020/2（8個月）
                    </span>
                </div>
                <div>
                    <h3 class="font-heading text-base font-bold {'text-white' if is_dark else 'text-slate-900'} leading-snug">
                        德利威電子股份有限公司
                    </h3>
                    <p class="{'text-amber-400' if is_dark else 'text-amber-600'} font-bold text-xs mt-0.5">行政櫃台／文管（約聘）</p>
                </div>
                <div class="text-[12px] {text_main} space-y-1.5 leading-relaxed">
                    <p><strong>行政庶務：</strong>電話接聽過濾、費用請款、零用金管理、機器叫修、用品採購、郵局寄件、訪客接待與訂餐。</p>
                    <p><strong>文管作業：</strong>一般文書處理歸檔、收發會簽追蹤（ECR/ECN）、產品圖面發行更新、客戶承認書彙整建檔。</p>
                </div>
            </div>
            <div class="mt-2 text-[11px] p-2 rounded {'bg-slate-900 text-slate-400' if is_dark else 'bg-slate-50 text-slate-600 border border-slate-200'}">
                <i class="fas fa-check text-amber-500 mr-1"></i> 扎實的文管制度與製造業行政底子。
            </div>
        </div>

        <!-- 階段 4: 輔仁大學 (紅色實心點) -->
        <div class="rounded-2xl border {card_bg} p-5 flex flex-col justify-between border-t-4 {'border-t-rose-500' if is_dark else 'border-t-rose-600'}">
            <div class="space-y-3">
                <div class="flex items-center gap-2">
                    <span class="w-3.5 h-3.5 rounded-full solid-dot-red"></span>
                    <span class="text-xs font-mono font-bold px-2 py-0.5 rounded {'bg-rose-950/60 text-rose-300' if is_dark else 'bg-rose-50 text-rose-700'}">
                        2014/9 ～ 2019/6
                    </span>
                </div>
                <div>
                    <h3 class="font-heading text-base font-bold {'text-white' if is_dark else 'text-slate-900'} leading-snug">
                        私立輔仁大學
                    </h3>
                    <p class="{'text-rose-400' if is_dark else 'text-rose-600'} font-bold text-xs mt-0.5">中文系 ＆ 德文系（雙學士）</p>
                </div>
                <div class="text-[12px] {text_main} space-y-2 leading-relaxed">
                    <p class="indent"><strong class="{'text-white' if is_dark else 'text-slate-900'}">中國文學系：</strong>具備敏銳文字校對能力、敘事結構與文案撰寫底蘊。</p>
                    <p class="indent"><strong class="{'text-white' if is_dark else 'text-slate-900'}">德語語文學系：</strong>養成嚴謹邏輯思考、跨文化國際溝通與外語理解能力。</p>
                </div>
            </div>
            <div class="mt-2 text-[11px] p-2 rounded {'bg-slate-900 text-slate-400' if is_dark else 'bg-slate-50 text-slate-600 border border-slate-200'}">
                <i class="fas fa-graduation-cap text-rose-500 mr-1"></i> 雙學士文理思維兼備之深厚基礎。
            </div>
        </div>

    </div>
""" + get_footer(theme, 5)

# Slide 6: 證照與技能
def slide_06_skills(theme):
    is_dark = (theme == 'dark')
    card_bg = "bg-[#0d121c] border-slate-800" if is_dark else "bg-white border-slate-200 shadow-sm"
    h_color = "text-rainbow-blue" if is_dark else "text-blue-600"
    text_main = "text-slate-300" if is_dark else "text-slate-700"
    
    return get_head(theme) + f"""
<div class="slide-container">
    <!-- Header -->
    <div class="flex items-center justify-between pb-3 border-b {'border-slate-800' if is_dark else 'border-slate-200'}">
        <div class="flex items-center gap-3">
            <h2 class="font-heading text-3xl font-black {h_color}">證照與技能</h2>
            <span class="text-lg font-bold {'text-white' if is_dark else 'text-slate-900'}">專業檢定證照、語言能力與擅長工具應用</span>
        </div>
        <span class="text-xs font-semibold px-3 py-1 rounded-full {'bg-blue-950/60 text-blue-300 border border-blue-900/60' if is_dark else 'bg-blue-50 text-blue-700 border border-blue-200'}">
            專業資格認證
        </span>
    </div>

    <!-- 3 大欄位 -->
    <div class="grid grid-cols-3 gap-6 my-auto items-stretch">

        <!-- 欄位 1: 資格認證 -->
        <div class="rounded-2xl border {card_bg} p-6 flex flex-col justify-between">
            <div class="space-y-4">
                <div class="flex items-center gap-2.5 font-heading text-xl font-bold {'text-white' if is_dark else 'text-slate-900'}">
                    <div class="w-8 h-8 rounded-lg {'bg-amber-950/60 text-rainbow-yellow' if is_dark else 'bg-amber-100 text-amber-700'} flex items-center justify-center text-sm">
                        <i class="fas fa-award"></i>
                    </div>
                    <span>專業資格認證</span>
                </div>
                
                <ul class="text-[13px] {text_main} space-y-3">
                    <li class="p-2.5 rounded-lg {'bg-[#111622] border border-slate-800' if is_dark else 'bg-slate-50 border border-slate-200'}">
                        <strong class="{'text-white' if is_dark else 'text-slate-900'} block text-[14px]">普通小型車駕照</strong>
                        <span class="text-xs {'text-slate-400' if is_dark else 'text-slate-500'}">中華民國交通部公路總局 4011510151103<br>（有效期限 2026/10 ～ 2065/12）</span>
                    </li>
                    <li class="p-2.5 rounded-lg {'bg-[#111622] border border-slate-800' if is_dark else 'bg-slate-50 border border-slate-200'}">
                        <strong class="{'text-white' if is_dark else 'text-slate-900'} block text-[14px]">TOEIC 多益測驗 860 分</strong>
                        <span class="text-xs {'text-slate-400' if is_dark else 'text-slate-500'}">聽力 465 / 閱讀 395（2019）</span>
                    </li>
                    <li class="p-2.5 rounded-lg {'bg-[#111622] border border-slate-800' if is_dark else 'bg-slate-50 border border-slate-200'}">
                        <strong class="{'text-white' if is_dark else 'text-slate-900'} block text-[14px]">FLPT 德語檢定</strong>
                        <span class="text-xs {'text-slate-400' if is_dark else 'text-slate-500'}">筆試 237分 (B2) / 口試 S2 (B1)（2019）</span>
                    </li>
                    <li class="p-2.5 rounded-lg {'bg-[#111622] border border-slate-800' if is_dark else 'bg-slate-50 border border-slate-200'}">
                        <strong class="{'text-white' if is_dark else 'text-slate-900'} block text-[14px]">全方位基礎人力資源管理師認證</strong>
                        <span class="text-xs {'text-slate-400' if is_dark else 'text-slate-500'}">社團法人中華人力資源管理協會</span>
                    </li>
                </ul>
            </div>
        </div>

        <!-- 欄位 2: 擅長工具 -->
        <div class="rounded-2xl border {card_bg} p-6 flex flex-col justify-between">
            <div class="space-y-4">
                <div class="flex items-center gap-2.5 font-heading text-xl font-bold {'text-white' if is_dark else 'text-slate-900'}">
                    <div class="w-8 h-8 rounded-lg {'bg-teal-950/60 text-rainbow-green' if is_dark else 'bg-teal-100 text-teal-700'} flex items-center justify-center text-sm">
                        <i class="fas fa-laptop-code"></i>
                    </div>
                    <span>擅長工具與應用</span>
                </div>

                <div class="space-y-4 text-[13px] {text_main}">
                    <div class="space-y-2">
                        <strong class="{'text-white' if is_dark else 'text-slate-900'} block text-[14px]">辦公室應用：</strong>
                        <div class="flex flex-wrap gap-2">
                            <span class="px-2.5 py-1 rounded {'bg-slate-800 text-white' if is_dark else 'bg-slate-100 text-slate-800 border border-slate-200'} font-semibold">Excel (樞紐/IF/COUNTIF/XLOOKUP)</span>
                            <span class="px-2.5 py-1 rounded {'bg-slate-800 text-white' if is_dark else 'bg-slate-100 text-slate-800 border border-slate-200'} font-semibold">Word (合併列印批次作業)</span>
                            <span class="px-2.5 py-1 rounded {'bg-slate-800 text-white' if is_dark else 'bg-slate-100 text-slate-800 border border-slate-200'}">PowerPoint (簡報視覺化)</span>
                            <span class="px-2.5 py-1 rounded {'bg-slate-800 text-white' if is_dark else 'bg-slate-100 text-slate-800 border border-slate-200'}">Outlook</span>
                        </div>
                    </div>

                    <div class="space-y-2">
                        <strong class="{'text-white' if is_dark else 'text-slate-900'} block text-[14px]">數位與協作平台：</strong>
                        <div class="flex flex-wrap gap-2">
                            <span class="px-2.5 py-1 rounded {'bg-slate-800 text-teal-300' if is_dark else 'bg-teal-50 text-teal-800 border border-teal-200'} font-semibold">Dify (AI 工作流與知識庫)</span>
                            <span class="px-2.5 py-1 rounded {'bg-slate-800 text-white' if is_dark else 'bg-slate-100 text-slate-800 border border-slate-200'}">Google Meet (百人視訊)</span>
                            <span class="px-2.5 py-1 rounded {'bg-slate-800 text-white' if is_dark else 'bg-slate-100 text-slate-800 border border-slate-200'}">LINE@ 官方帳號</span>
                            <span class="px-2.5 py-1 rounded {'bg-slate-800 text-white' if is_dark else 'bg-slate-100 text-slate-800 border border-slate-200'}">Kahoot! 互動機制</span>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="p-3 rounded-lg text-xs {'bg-slate-900 text-slate-400' if is_dark else 'bg-slate-100 text-slate-600'}">
                <i class="fas fa-keyboard text-teal-500 mr-1.5"></i> 熟練 Office 自動化串接與雲端協同作業工具。
            </div>
        </div>

        <!-- 欄位 3: 語言能力與求職條件 -->
        <div class="rounded-2xl border {card_bg} p-6 flex flex-col justify-between">
            <div class="space-y-4">
                <div class="flex items-center gap-2.5 font-heading text-xl font-bold {'text-white' if is_dark else 'text-slate-900'}">
                    <div class="w-8 h-8 rounded-lg {'bg-rose-950/60 text-rainbow-red' if is_dark else 'bg-rose-100 text-rose-600'} flex items-center justify-center text-sm">
                        <i class="fas fa-language"></i>
                    </div>
                    <span>語言能力 ＆ 求職條件</span>
                </div>

                <div class="space-y-4 text-[13px] {text_main}">
                    <div class="p-3 rounded-xl {'bg-[#111622] border border-slate-800' if is_dark else 'bg-slate-50 border border-slate-200'} space-y-1.5">
                        <strong class="{'text-white' if is_dark else 'text-slate-900'} block text-[14px]">語言能力：</strong>
                        <ul class="space-y-1">
                            <li>・<strong>英文：</strong>聽/中等 說/中等 讀/中等 寫/中等（日常英語工作溝通）</li>
                            <li>・<strong>德文：</strong>聽/中等 說/中等 讀/中等 寫/中等（雙學士）</li>
                            <li>・<strong>台語：</strong>略懂</li>
                        </ul>
                    </div>

                    <div class="p-3 rounded-xl {'bg-[#111622] border border-slate-800' if is_dark else 'bg-slate-50 border border-slate-200'} space-y-1.5">
                        <strong class="{'text-white' if is_dark else 'text-slate-900'} block text-[14px]">求職狀態：</strong>
                        <ul class="space-y-1 text-xs">
                            <li>・<strong>應徵職稱：</strong>行政營運專員 ｜ 專案執行人員</li>
                            <li>・<strong>就業狀態：</strong>待業中（錄取後一週可上班）</li>
                            <li>・<strong>希望地點：</strong>台北市、新北市（對遠端工作有意願）</li>
                        </ul>
                    </div>
                </div>
            </div>

            <div class="p-3 rounded-lg text-xs {'bg-slate-900 text-slate-400' if is_dark else 'bg-slate-100 text-slate-600'} flex justify-between items-center">
                <span><i class="fas fa-envelope text-rose-500 mr-1.5"></i> ichbinalicewu35@gmail.com</span>
                <span>0958-321-139</span>
            </div>
        </div>

    </div>
""" + get_footer(theme, 6)

# Write all HTML slides
slide_funcs = [
    ("01_intro", slide_01_intro),
    ("02_admin1", slide_02_admin1),
    ("03_admin2", slide_03_admin2),
    ("04_admin3", slide_04_admin3),
    ("05_timeline", slide_05_timeline),
    ("06_skills", slide_06_skills),
]

for theme in ["dark", "light"]:
    for name, func in slide_funcs:
        filename = f"{theme}_{name}.html"
        path = os.path.join(html_dir, filename)
        content = func(theme)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated: {filename}")

print("All HTML slide files generated successfully.")
