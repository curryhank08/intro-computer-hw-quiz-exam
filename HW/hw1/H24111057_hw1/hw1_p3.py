"""
author: H24111057姚博瀚
"""

# unit is m/s ; speed of light
c = 299792458

#令v等於輸入的值，並傳成浮點數;v是太空船的速度
v = float(input("Input velocity (m/s) : ")) 

#依公式由v計算出factor
factor = 1/((1-(v/c)**2)**0.5)
#印出太空船速度v的光速百分比
print("Percentage of light speed =", float( (v / c)*100 ), "%") 

#將四個地方與對應的光年數存入名為'data'的字典；key為地方，value為其地方對應的光年數。
data = {
	"Alpha Centauri":4.3,
	"Barnard's Star":6.0,
	"Betelgeuse (in the Milky Way)":309,
	"Andromeda Galaxy (closest galaxy)":2000000
}

#由迴圈迭代所有的地方，並計算出tp與印出tp(至小數點第6位)
for key, value in data.items():
    tp = value / factor
    print(f"Travel time to {key} = {tp:.6f}")
