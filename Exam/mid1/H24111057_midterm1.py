""" 
author: H24111057 統計115 姚博瀚
"""

## 設每列為 j x n (j:9~1; n:9, 6, 3)
# 初始化n
n = 9
# 以空白列分為三段，每段為n=9, 6, 3
while n >= 3:
    # 初始化j
    j = 9
    
    while j >= 1:
        result1 = j * n
        result2 = j * (n - 1)
        result3 = j * (n - 2)
        
        # 計算需補的空格，相乘結果為個位數的會少一格所以要再補回去
        space1 = result1 % 2
        space2 = result2 % 2
        space3 = result3 % 2
        
        # 每列要印出的
        row = f"{j} x {n} = {result1}{' '*space1}\t{j} x {n-1} = {result2}{' '*space2}\t{j} x {n-2} = {result3}{' '*space3}"
        # 印出每列
        print(row)
        
        # 減一到下一列
        j -= 1
        
    # 印完最後一段不需再印出空白列
    if n > 3:
        print()
    
    # 減三到下一段
    n -= 3