"""
author: H24111057姚博瀚
"""

#令f為輸入的值並轉成浮點數 ; f為兩物體間的萬有引力
f = float(input("Input the force (N): "))
#令m1為輸入的值並轉成浮點數 ; m1為其中一個物體的質量
m1 = float(input("Input the mass of m1 (kg): "))
#令r為輸入的值並轉成浮點數 ; r為兩物體間的距離
r = float(input("Input the distance (m): "))
#令G為重力常數並轉成浮點數
G = float(6.67*(1e-11))
#令c為光速並轉成浮點數
c = float(299792458)

#計算另一物體m2的質量與能量
mm2 = (f * (r**2)) / (m1 * G)
em2 = mm2 * (c**2)
#印出m2的質量與能量
print(f"The mass of m2 = {mm2}\nThe energy of m2 = {em2}")