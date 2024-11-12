import pandas as pd
import requests


url = 'https://goodinfo.tw/tw2/StockList.asp?MARKET_CAT=%E7%86%B1%E9%96%80%E6%8E%92%E8%A1%8C&INDUSTRY_CAT=%E5%85%AC%E5%8F%B8%E7%B8%BD%E5%B8%82%E5%80%BC%E6%9C%80%E9%AB%98@@%E5%85%AC%E5%8F%B8%E7%B8%BD%E5%B8%82%E5%80%BC@@%E5%85%AC%E5%8F%B8%E7%B8%BD%E5%B8%82%E5%80%BC%E6%9C%80%E9%AB%98&SHEET=%E5%85%AC%E5%8F%B8%E5%9F%BA%E6%9C%AC%E8%B3%87%E6%96%99'
    
response = requests.get(url)

# 檢查是否成功獲取資料
if response.status_code == 200:
    print("成功抓取資料！")
else:
    print(f"抓取資料失敗，狀態碼：{response.status_code}")
        
         

