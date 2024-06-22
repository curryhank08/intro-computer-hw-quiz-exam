"""
author: H24111057 姚博瀚
"""

# 令num為輸入的值
num = input("Input the range number:")
# 把num轉成int
int_num = int(num)
# 創一個放perfect number的list
perfect_numbers = []

# 測試2~int_num ; + 1 是因為range()的結束位置不包含在結果序列，沒 + 1 會少掉int_num
for i in range(2, int_num + 1):
    # 創一個放因數的list
    divisors = []
    """ 
    #測試1~(int_num-1)是否為因數
    for h in range(1, i):
    """
    # 測試1~(int_num)是否為因數
    for h in range(1, i+1):
        # 如相除餘0，則除數h為i的因數，把該除數加進divisors list
        if (i % h) == 0:
            divisors.append(h)
    # print(divisors)
    """
    # divisors已不包含正在測試的i
    # if sum(divisors) == i:
    """
    # divisors 包含正在測試的i
    # 如divisors list內的所有因數總和的一半等於i，i則為perfect number，把i加入perfect_number list
    if sum(divisors)/2 == i:
        perfect_numbers.append(i)
        
# 印出存在perfect_numbers list裡的所有perfect number
for i in range(len(perfect_numbers)):
    print(perfect_numbers[i])
