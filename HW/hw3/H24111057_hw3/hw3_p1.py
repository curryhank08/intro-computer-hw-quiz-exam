""" 
author: H24111057 統計系 姚博瀚
"""

n = int(input("Input the total number of students (n>0) : "))

# 生成所有n個學生的ID，並加入叫做All_ID的list
All_ID = []
for i in range(1, n+1):
    All_ID.append(i)
# All_ID = list(range(1, n+1))

# 把要離開的學生的index初始化成0
remove_index = 0

while len(All_ID) > 1:
    # 計算喊出3要離開的學生的index ; 每次刪除一名學生後，len(All_ID)會少1，位於刪除學生後面的學生的index會往前一格，所以+2就夠
    remove_index = (remove_index + 2) % len(All_ID)

    # 根據remove_index從All_ID list移除喊出3的學生
    All_ID.pop(remove_index)

# 只剩一名學生時，印出該學生ID
if len(All_ID) == 1:
    print("The last ID is : ", All_ID[0])
