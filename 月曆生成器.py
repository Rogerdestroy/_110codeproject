import calendar
while True: #一般如果不賦值，預設是True
  year=int(input('請輸入年份：')) #用變數year代表年份，使用int把輸入資料變成整數型別
  month=int(input('請輸入月份：')) #原理同上
  print(calendar.month(year,month)) #使用 `print` 函式顯示月曆，變數 year和 month 代表年份和月份