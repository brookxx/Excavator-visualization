from parameters import Params
from parameters_cal import Params_c
import math

"""输入：逆解计算出的关节空间的角度"""
"""基于关节的运动范围限制，判断逆解是否可行"""

def exam_reach(results, params_c):

	flag = 1
	flag_p = 1
	flag_n = 1
	if len(results) == 1:
		if results[0][0] < params_c.phi_1_min or results[0][0] > params_c.phi_1_max or \
			results[0][1] < params_c.phi_2_min or results[0][1] > params_c.phi_2_max or \
			results[0][2] < params_c.phi_3_min or results[0][2] > params_c.phi_3_max:
				flag = 0
				flag_p = 0
				flag_n = 0
	elif len(results) == 2:
		if(results[0][0] < params_c.phi_1_min or results[0][0] > params_c.phi_1_max or \
			results[0][1] < params_c.phi_2_min or results[0][1] > params_c.phi_2_max or \
			results[0][2] < params_c.phi_3_min or results[0][2] > params_c.phi_3_max):
				flag_p = 0 
		if(results[1][0] < params_c.phi_1_min or results[1][0] > params_c.phi_1_max or \
			results[1][1] < params_c.phi_2_min or results[1][1] > params_c.phi_2_max or \
			results[1][2] < params_c.phi_3_min or results[1][2] > params_c.phi_3_max):
				flag_n = 0
		if flag_p==0 and flag_n==0:
			flag = 0

	else:
	    return('不止有两个解');
	return flag, flag_p, flag_n
	
