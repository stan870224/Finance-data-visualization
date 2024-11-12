import pandas as pd
import re

# 讀取CSV檔案
file_path = 'top_market_cap_by_sector.csv'
df = pd.read_csv(file_path)

# 自訂函數來清理代號欄位，只取出中間的數字部分並轉換為字串
def parse_code(code):
    if isinstance(code, str):
        # 使用正則表達式提取數字部分
        match = re.search(r'(\d+)', code)
        if match:
            return match.group(1)  # 提取並返回數字部分
    return code

# 處理代號欄位，僅保留數字部分
df['代號'] = df['代號'].apply(parse_code)

# 按產業別分組並儲存到不同的list中
industry_lists = {}
for industry, industry_df in df.groupby('產業別'):
    # 將該產業別的公司資料存入list，並加入到industry_lists字典
    industry_lists[industry] = industry_df[['代號', '名稱', '市值(億)']].to_dict('records')

# 輸出結果，確認每個產業別的前三大市值公司
for industry, companies in industry_lists.items():
    print(f"{industry} 的前三大公司:")
    for company in companies:
        print(company)
    print("\n" + "-"*40 + "\n")
