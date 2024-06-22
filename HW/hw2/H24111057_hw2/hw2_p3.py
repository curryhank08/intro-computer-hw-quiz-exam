"""
author: H24111057 姚博瀚
"""

# 輸入年份和月份
year = int((input("Please input Year：")))
month = int((input("Please iunput Month：")))


# 定義calendar；由兩個變數所決定
def calendar(year, month):
    # 判斷是否閏年
    def is_leap_year(y):
        return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

    # 計算每個月的天數；並定義為days_in_month
    def days_in_month(m):
        if m in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif m == 2:
            return 29 if is_leap_year(year) else 28
        else:
            return 30

    # Zeller's congruence 算法計算星期幾
    def day_of_week(y, m, d):
        if m < 3:
            y -= 1
            m += 12
        k = y % 100
        j = y // 100
        f = k + k//4 + j//4 - 2*j + 13*(m+1)//5 + d - 1
        return f % 7
    # 印出一個空行；默認的print() 等於 print(end="\n")；如打 print("\n") 會等於 print("\n", end="\n") 變成換兩行
    print()
    # 印出日歷標題
    print(f'       AD {year} Month {month} ')
    # 印出星期標題
    print('Sun Mon Tue Wed Thu Fri Sat')

    # 計算當月1號星期幾
    first_day = day_of_week(year, month, 1)
    # 根據1號是星期幾印出第一周的空格；一天四個空格
    print("    " * (first_day), end="")

    # 印出每一天，每周換行
    # + 1 是因為range()的結束位置不包含在結果序列，沒 + 1 會少掉每月的最後一天
    for day in range(1, days_in_month(month) + 1):
        # 1~9號前面增加2格空格對齊
        if day < 10:
            print("  ", end="")
        # 10~號前面增加1格空格對齊
        elif day >= 10:
            print(" ", end="")
        # 印出日期
        print(day, end=" ")
        # 判斷是否需要換行
        if (first_day + day) % 7 == 0:
            print()
        # 處理最後一天之後的空白位置
        elif day == days_in_month(month):
            print("    " * day_of_week(year, month, days_in_month(month)), end="")
            # print(" " * (5 - (first_day + day) % 7) * 4, end="")


# 執行所定義的calender函數；year, month是使用者所輸入的值
calendar(year, month)
