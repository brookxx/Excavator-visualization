from parameters import Params
from parameters_cal import Params_c
import ik
import exam_reach as er
import math
import tkinter as tk

params = Params()
params_c = Params_c()

dhparams = [(0,0,0,0),(params_c.l_CF/1000,0,0,0),(params_c.l_FQ/1000,0,0,0),(params_c.l_QV/1000,0,0,0)]

def visual_ik(x, y, phi):
	results, flag, result_num = ik.ik(dhparams, x, y, phi, params)
	if flag == 0:
		print("该坐标无解")
	else:
		flag, flag_p, flag_n = er.exam_reach(results, params_c)
		if flag == 0:
			print("该坐标超出工作范围")
		else:
			if flag_p == 1:
				return results[0]
			elif flag_p == 0 and flag_n == 1:
				return results[1]


