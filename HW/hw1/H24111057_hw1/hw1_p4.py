"""
author: H24111057姚博瀚
"""

#令h1為輸入的值並轉成浮點數
h1 = float(input("Input the height of the 1st ball (m) : "))
#令m1為輸入的值並轉成浮點數
m1 = float(input("Input the mass of the 1st ball (kg) : "))
#令m1為輸入的值並轉成浮點數
m2 = float(input("Input the mass of the 2nd ball (kg) : "))

#令重力加速度g為9.8
g = 9.8 # gravity acceleration (m/s^2)

#依公式計算m1滑下來後的速度，並令為v1i，同時為m1碰撞前的速度
v1i = (2 * g * h1)**0.5
#因m2碰撞前為靜止，故令v2i為m2碰撞前的速度
v2i = 0
#v2'=[(m2-m1)/(m1+m2)]*v2i +[(2*m1)/(m1+m2)]*v1i ;計算m2碰撞後的速度，並令為v2f
v2f = ((m1 - m2)/(m1 + m2)) * v2i + (2 * m1/(m1 + m2)) * v1i

#印出m1滑下後的速度，也就是m1碰撞前的速度
print("The velocity of the 1st ball after slide (m/s) : ", v1i)
#印出m2碰撞後的速度
print("The velocity of the 2nd ball after collision (m/s) : ", v2f)
