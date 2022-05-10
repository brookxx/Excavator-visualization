from parameters import Params
from parameters_cal import Params_c
import ik
import exam_reach as er
import math
import visual_ik as vi
params = Params()
params_c = Params_c()
dhparams = [(0,0,0,0),(params_c.l_CF/1000,0,0,0),(params_c.l_FQ/1000,0,0,0),(params_c.l_QV/1000,0,0,0)]
while True:
	print("Tool坐标系的坐标和角度")
	x = input("x=")
	y = input("y=")
	phi = input("phi=")
	huizhuantai2 = input("请输入回转台转动角度")
	x = float(x)
	y = float(y)
	phi = float(phi)
	huizhuantai2  = float(huizhuantai2)
	#results2, flag2, result_num2 = ik.ik(dhparams, x, y, phi,params)
	#flag2, flag2_p, flag2_n = er.exam_reach(results2, params_c)
	dongbi2,dougan2,chandou2 = vi.visual_ik(x, y, phi)
	print(huizhuantai2,dongbi2,dougan2,chandou2)
