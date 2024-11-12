import pandas as pd
import os
import re

# 指定存放CSV檔案的目錄
data_dir = 'D:' + os.path.sep + 'AI_course' + os.path.sep + 'Finance_data_visualization' + os.path.sep + 'Finance-data-visualization'

# 創建空的DataFrame
all_stocks = pd.DataFrame()

def parse_market_cap(x):
    if isinstance(x, (float, int)):
        return x
    elif isinstance(x, str):
        # 移除千分位符號並提取數值部分
        x = x.replace(',', '')
        match = re.search(r'(\d+(?:\.\d+)?)', x)
        if match:
            return float(match.group(1))
        else:
            return 0.0
    else:
        return 0.0

# 遍歷目錄中的所有CSV檔案
for filename in os.listdir(data_dir):
    if filename.endswith('.csv'):
        file_path = os.path.join(data_dir, filename)
        
        # 讀取每個CSV檔案
        df = pd.read_csv(file_path, header=None, names=['代號', '名稱', '市場', '股價日期', '收盤價', '漲跌價', '漲跌幅', '面值(元)', '股本(億)', '發行量(萬張)', '市值(億)', '成立年數', '掛牌年數', '股票期貨', '選擇權', '權證', '公司債', '私募股', '特別股', '產業別', '董事長', '總經理'])
        
        # 將"產業別"欄位轉換為小寫
        df['產業別'] = df['產業別'].str.lower()
        
        # 使用自定義函數處理市值欄位
        df['市值(億)'] = df['市值(億)'].apply(parse_market_cap)
        
        # 將每個檔案的數據合併到全局DataFrame
        all_stocks = pd.concat([all_stocks, df], ignore_index=True)

# 按產業別和市值排序        
sorted_df = all_stocks.sort_values(['產業別', '市值(億)'], ascending=[True, False])

# 創建一個新的DataFrame儲存結果
result_df = pd.DataFrame(columns=['產業別', '代號', '名稱', '市值(億)'])

# 遍歷每個產業別,將前三大市值公司加入結果
for industry, industry_df in sorted_df.groupby('產業別'):
    top_3 = industry_df.head(3)[['代號', '名稱', '市值(億)']]
    top_3['產業別'] = industry
    result_df = pd.concat([result_df, top_3], ignore_index=True)

# 輸出結果為CSV檔案
result_df.to_csv('top_market_cap_by_sector.csv', index=False)
print("CSV檔案已儲存!")
