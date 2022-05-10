import numpy as np
import math

class Params:
	
	def __init__(self):

		"""工作装置尺寸"""
		"""基准，动臂根铰点C为原点"""
		self.A_x = 497.00
		self.A_y = -644.50
		self.C_x = -100.000
		self.C_y = -800.00
		self.y = -1902.00
		
		"""动臂"""
		self.BC = 2508.00
		self.CF = 5700.00
		self.CD = 3379.60
		self.DF = 2807.70
		self.BF = 3601.20
		
		"""斗杆"""
		self.EF = 850.00
		self.FG = 619.70
		self.EG = 1173.90
		self.GQ = 2656.00
		self.FQ = 2925.00
		self.GN = 2249.60
		self.NQ = 410.00
		
		"""铲斗"""
		self.KQ = 458.20
		self.QV = 1469.80
		self.KV = 1605.10
		self.zeta = np.deg2rad([45]) 
		"""铲斗角度"""
		
		"""连杆"""
		self.MN = 640.00
		self.MK = 600.00
		
		"""液压缸尺寸"""
		self.AB_home = 2667.00
		self.DE_home = 2402.00
		self.GM_home = 1786.00
		self.AB_min = 1869.00
		self.AB_max = 3154.00
		self.DE_min = 2130.00
		self.DE_max = 3620.00
		self.GM_min = 1713.00
		self.GM_max = 2825.00
		
