題目一
請實作一個提供匯率轉換的 API,轉換金額請四捨五入到小數點第二位,且轉換後的金額顯
示格式請增加逗點分隔做為千分位表示,如 123,456.78 ,不限程式語言。(請附上 github /
gitlab / bitbucket 連結)
實作要求:
- 請附上如何執行的說明文件如 README
- 請針對您的 API 撰寫單元測試
- Method 請用 GET
- 輸入範例:
?source=USD&target=JPY&amount=$1,525
- 輸出範例:
{
"msg": "success"
"amount": "$170496.53"