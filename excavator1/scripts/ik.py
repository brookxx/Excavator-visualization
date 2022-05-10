
from parameters import Params
from parameters_cal import Params_c
import math
params = Params()

def ik(dhparams, x, y, phi,params):

	"""输入：[x, y, phi]-Tool坐标系的坐标和角度"""
	"""给定Tool位置及方向，计算逆解"""

	"""转化为腕部坐标系坐标和角度"""
	x = x-dhparams[3][0]*math.cos(phi);
	y = y-dhparams[3][0]*math.sin(phi);
	phi = phi;
	
	"""设定参数"""
	flag = 1;
	result_num = 0;
	l1 = dhparams[1][0];
	l2 = dhparams[2][0];
	
	c2 = (x**2 + y**2 - l1**2 - l2**2)/(2 * l1 * l2);
	if abs(c2)>1:
	    flag = 0;
	    results = [];
	else:
	    s2 = math.sqrt(1 - c2**2);
	    theta2 = math.atan2(s2, c2);
	    theta2_n = -math.atan2(s2, c2);
	    
	    if x == 0 and y == 0:
	        theta1 = inf
	        theta3 = inf
	    else:
	        k1 = l1 + l2 * c2
	        k2 = l2 * s2
	        theta1 = math.atan2(y,x) - math.atan2(k2,k1)
	        theta3 = phi - theta1 - theta2
	    
	    if c2**2 == 1:
	        result_num = 1
	        results = [theta1, theta2, theta3]
	    else:
	        result_num = 2
	        theta1_n = math.atan2(y,x) - math.atan2(-k2,k1)
	        theta2_n = math.atan2(-s2, c2)
	        theta3_n = phi - theta1_n - theta2_n
	        results = [[],[]]
	        results[0] = [theta1, theta2, theta3]
	        results[1] = [theta1_n, theta2_n, theta3_n]

	    
	    """放缩至-math.pi到math.pi"""
	    """results = wrapTomath.pi(results);"""
   
	for i in range(len(results)):
		for j in range(3):
			while results[i][j] > 2*math.pi:
				results[i][j] = results[i][j]-2*math.pi  
			while results[i][j]<0:
				results[i][j] = results[i][j]+2*math.pi

			if results[i][j]>math.pi:
				results[i][j] = results[i][j] - 2*math.pi

	return results, flag, result_num


