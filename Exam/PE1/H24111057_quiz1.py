""" 
author: H24111057 姚博瀚
"""

#一頓TNT、一餐午餐的能量（in joules）
ton_of_TNT = 4.184 * 10**9
nutritious_lunch = 2930200

richter = float(input("Please input a Richter scale value: "))

#把richter scale轉換為joules、a ton of TNT、lunch為單位的數值
energy = 10 ** ((1.5 * richter) + 4.8)
equ_TNT = energy / ton_of_TNT
equ_lunch = energy / nutritious_lunch

#印出結果
print(
    F"Richter scale value: {richter}\nEquivalence in Joules: {energy:.5f}\nEquivalence in tons of TNT: {equ_TNT:.5f}\nEquivalence in the number of nutritious lunches: {equ_lunch:.5f}"
)