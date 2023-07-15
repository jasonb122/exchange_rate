# 匯率換算 API
## 這個專案是基於 Flask 開發的 API，用於計算貨幣匯率換算。

### 安裝：

- Anaconda安裝(推薦)
  - 複製專案：git clone https://github.com/jasonb122/exchange_rate.git
  - 進入專案目錄：cd exchange_rate
  - 確認是否有requirements.txt檔案內的套件，如沒有的話進行安裝：pip install -r requirements.txt
  - 啟動 Flask 應用程式：flask run
- 本地安裝
  - 複製專案：git clone https://github.com/jasonb122/exchange_rate.git
  - 進入專案目錄：cd exchange_rate
  - 建立虛擬環境：python -m venv venv
  - 啟用虛擬環境：
  - 在 Windows 上：venv\Scripts\activate
  - 在 macOS/Linux 上：source venv/bin/activate
  - 安裝所需套件：pip install -r requirements.txt
  - 啟動 Flask 應用程式：flask run

### 使用方式

此 API 提供一個端點用於計算匯率換算，端點為：

````
GET /exchange_rate
````
- 請求參數
需要提供以下查詢參數：

  - source：原始貨幣代碼（例如 "USD"）。
  - target：目標貨幣代碼（例如 "JPY"）。
  - amount：要換算的金額。



- 使用範例
  要計算從 USD 到 JPY 的匯率換算，金額為 100，可發送 GET 請求到以下 URL：

````
http://localhost:5000/exchange_rate?source=USD&target=JPY&amount=100
````

- 回應
    - 如果請求成功，API 會回傳以下格式的 JSON 回應：
    ````
    {"msg": "success", "amount": "11,180.10"}
    ````
    - 如果缺少任何必填參數（原始貨幣、目標貨幣或金額），API 會回傳以下格式的 JSON 回應：
    ````
    {"error": "Missing parameters"}
    ````
    - 如果提供的金額無效（不是有效的浮點數），API 會回傳以下格式的 JSON 回應：
    ````
    {"error": "Invalid amount"}
    `````
- 測試

    - 要執行此專案的單元測試，請執行以下命令：

    ````
     python -m unittest tests.test_app
    ````
  - 單元測試涵蓋以下情境：

    - 有效的匯率換算並驗證預期結果。
    - 請求缺少必填參數。
    - 請求提供無效的金額。