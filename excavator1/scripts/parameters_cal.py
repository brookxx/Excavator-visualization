from parameters import Params
import math
params = Params()

"""回转机构"""


aa = -params.y + params.C_y
"""转台高度"""
bb = -params.C_y
"""点C在转台坐标系上的纵坐标"""
cc = -params.C_x
"""点C在转台坐标系上的横坐标"""
"""phi_0 = params.phi_0"""
"""转台绕z轴转动的角度"""
l_AC = math.sqrt(params.A_x**2 + params.A_y**2)
D_ACx = abs(math.atan(params.A_y/params.A_x))
"""AC与水平面倾角"""

"""动臂"""
l_BC = params.BC
l_CF = params.CF
l_CD = params.CD
l_DF = params.DF
l_EF = params.EF
D_CBF = math.acos((params.BC**2 + params.BF**2 - params.CF**2)/(2 * params.BC * params.BF))
D_BCF = math.acos((params.BC**2 + params.CF**2 - params.BF**2) / (2 * params.BC * params.CF))
D_CFB = math.pi - D_CBF - D_BCF;
D_CFD = math.acos((params.DF**2 + params.CF**2 - params.CD**2)/ (2 * params.DF * params.CF))
"""动臂上的结构角CFD"""
D_DCF = math.acos((params.CD**2 + params.CF**2 - params.DF**2)/(2 * params.CD * params.CF))

"""斗杆"""
l_EF = params.EF
l_FG = params.FG
l_EG = params.EG
l_GQ = params.GQ
l_FQ = params.FQ
l_GN = params.GN
l_NQ = params.NQ
D_EFQ = math.acos((params.FQ**2 + params.FG**2 - params.GQ**2)/ (2 * params.FQ * params.FG))+math.acos((params.FG**2 + params.EF**2 - params.EG**2)/ (2 * params.FG * params.EF))
D_GFQ = math.acos((params.FQ**2 + params.FG**2 - params.GQ**2)/ (2 * params.FQ * params.FG))
"""经验值"""
D_FQG = math.acos((params.FQ**2 + params.GQ**2 - params.FG**2)/ (2 * params.FQ * params.GQ))
D_NQG = math.acos((params.NQ**2 + params.GQ**2 - params.GN**2)/ (2 * params.NQ * params.GQ))

"""铲斗及连杆"""
l_KQ = params.KQ
l_QV = params.QV
l_KV = params.KV
l_MN = params.MN
l_MK = params.MK
D_KVQ = math.acos((params.KV**2 + params.QV**2 - params.KQ**2)/(2 * params.KV * params.QV))
D_VKQ = math.acos((params.KV**2 + params.KQ**2 - params.QV**2)/(2 * params.KV * params.KQ))
"""l_FN在后面计算"""
D_KQV = math.acos((params.KQ**2 + params.QV**2 - params.KV**2)/(2 * params.KQ * params.QV))

"""液压缸尺寸"""
"""动臂油缸"""
l_AB_min = params.AB_min
l_AB_max = params.AB_max

"""斗杆油缸"""
l_FQ_min = params.DE_min
l_FQ_max = params.DE_max

"""铲斗油缸"""
l_GM_min = params.GM_min
l_GM_max = params.GM_max

"""校核动臂三角形"""
if (l_AC + l_AB_min)>l_BC and abs(l_AC - l_BC)<l_AB_min and abs(l_BC - l_AB_min) < l_AC and (l_AC + l_BC)>l_AB_max and abs(l_AC - l_AB_max)<l_BC and abs(l_BC - l_AB_max)<l_AC:
	print('动臂机构无问题')
else:
    over_all = 100;
    print('动臂机构存在干涉！')


"""动臂摆角"""
phi_1_max = math.acos((l_AC**2 + l_BC**2 - l_AB_max**2)/ (2 * l_AC * l_BC)) - D_ACx - D_BCF
"""动臂最大仰角"""
phi_1_min = math.acos((l_AC**2 + l_BC**2 - l_AB_min**2)/ (2 * l_AC * l_BC)) - D_ACx - D_BCF
"""动臂最大俯角"""

"""校核斗杆三角形"""
if (l_EF + l_FQ_min)>l_DF and abs(l_EF - l_DF)<l_FQ_min and abs(l_DF - l_FQ_min) < l_EF and (l_EF + l_DF)>l_FQ_max and abs(l_EF - l_FQ_max)<l_DF and abs(l_DF - l_FQ_max)<l_EF:
	print('斗杆机构无问题！')
else:
    over_all = 100;
    print('斗杆机构存在干涉！')


"""斗杆摆角"""
phi_2_min = math.pi - D_CFD - D_EFQ - math.acos((l_DF**2 + l_EF**2 - l_FQ_max**2) / (2 * l_DF * l_EF))
phi_2_max = math.pi - D_CFD - D_EFQ - math.acos((l_DF**2 + l_EF**2 - l_FQ_min**2) / (2 * l_DF * l_EF))

"""铲斗摆角"""
"""
% phi_2 = deg2rad(-60); % 斗杆瞬时摆角
% R_3 = [1,      0     ,      0     ;...
%     0,  math.cos(phi_2), -math.sin(phi_2);...
%     0,  math.sin(phi_2),  math.cos(phi_2)]                                        % O_3相对于O_2的转换矩阵
% 
% xyz_E_3 = [0; l_EF * math.cos(D_EFQ); l_EF * math.sin(D_EFQ)]                        % 点E在O_3坐标系下的坐标
% xyz_E_0 = R_1 * (xyz_C_1 + R_2 * (xyz_F_2 + R_3 * xyz_E_3)) + [0; 0; aa]   % 点E在O_0坐标系下的坐标
% 
% xyz_G_3 = [0; l_FG * math.cos(D_GFQ); l_FG * math.sin(D_GFQ)]                        % 点G在O_3坐标系下的坐标
% xyz_G_0 = R_1 * (xyz_C_1 + R_2 * (xyz_F_2 + R_3 * xyz_G_3)) + [0; 0; aa]   % 点G在O_0坐标系下的坐标
"""
z_N_3 = params.NQ * math.sin(D_FQG - D_NQG)           
"""
                          % 点N在O_3坐标系下的z坐标
% xyz_N_3 = [0; l_FQ - math.sqrt(l_NQ**2 - z_N_3**2); z_N_3]                        % 点N在O_3坐标系下的坐标
% xyz_N_0 = R_1 * (xyz_C_1 + R_2 * (xyz_F_2 + R_3 * xyz_N_3)) + [0; 0; aa]   % 点N在O_0坐标系下的坐标
% 
% xyz_Q_3 = [0; l_FQ; 0];                                                     % 点Q在O_3坐标系下的坐标
% xyz_Q_0 = R_1 * (xyz_C_1 + R_2 * (xyz_F_2 + R_3 * xyz_Q_3)) + [0; 0; aa]   % 点Q在O_0坐标系下的坐标
"""
D_MNG_min = math.acos((l_GN**2 + l_MN**2 - l_GM_min**2) / (2 * l_GN * l_MN))
D_MNG_max = math.acos((l_GN**2 + l_MN**2 - l_GM_max**2) / (2 * l_GN * l_MN))

l_FN = math.sqrt((l_FQ - math.sqrt(l_NQ**2 - z_N_3**2))**2 + z_N_3**2);
D_FNG =math.acos((l_FN**2 + l_GN**2 - l_FG**2) / (2 * l_FN * l_GN))
D_FNQ =math.acos((l_FN**2 + l_NQ**2 - l_FQ**2) / (2 * l_FN * l_NQ))
D_FQN =math.acos((l_FQ**2 + l_NQ**2 - l_FN**2) / (2 * l_FQ * l_NQ))
"""
% theta = - D_MNG_min + 2*math.pi - D_FNG - D_FNQ - D_FQN                        %中间变量
% xyz_M_3 = [0; xyz_N_3(2) + l_MN * math.cos(theta); xyz_N_3(3) + l_MN * math.sin(theta)]               % 点M在O_3坐标系下的坐标(对应D_MNG_min）
% xyz_M_0 = R_1 * (xyz_C_1 + R_2 * (xyz_F_2 + R_3 * xyz_M_3)) + [0; 0; aa]                   % 点M在O_0坐标系下的坐标(对应D_MNG_min）
"""
l_MQ_max = math.sqrt(l_NQ**2 + l_MN**2 - 2 * l_NQ * l_MN * math.cos(2*math.pi - D_MNG_min - D_FNG - D_FNQ))
l_MQ_min = math.sqrt(l_NQ**2 + l_MN**2 - 2 * l_NQ * l_MN * math.cos(2*math.pi - D_MNG_max - D_FNG - D_FNQ))
D_NQM_max = math.acos((l_NQ**2 + l_MQ_min**2 - l_MN**2) / (2 * l_NQ * l_MQ_min))
D_NQM_min = math.acos((l_NQ**2 + l_MQ_max**2 - l_MN**2) / (2 * l_NQ * l_MQ_max))
D_MQK_max = math.acos((l_KQ**2 + l_MQ_min**2 - l_MK**2) / (2 * l_KQ * l_MQ_min))
D_MQK_min = math.acos((l_KQ**2 + l_MQ_max**2 - l_MK**2) / (2 * l_KQ * l_MQ_max))
phi_3_max = -(D_FQN + D_NQM_min + D_MQK_min + D_KQV - math.pi)
phi_3_min = -(D_FQN + D_NQM_max + D_MQK_max + D_KQV - math.pi)

class Params_c:
	
	def __init__(self):
		"""输出"""
		self.phi_1_max = phi_1_max
		self.phi_1_min = phi_1_min
		
		self.phi_2_max = phi_2_max
		self.phi_2_min = phi_2_min
		
		self.phi_3_max = phi_3_max
		self.phi_3_min = phi_3_min
		
		self.aa = aa
		self.bb = bb
		self.cc = cc
		
		self.l_AC = l_AC
		self.l_BC = l_BC
		self.D_BCF = D_BCF
		self.D_ACx = D_ACx
		
		self.D_EFQ = D_EFQ
		self.D_CFD = D_CFD
		self.l_DF = l_DF
		self.l_EF = l_EF
		
		self.l_GN = l_GN
		self.l_MN = l_MN
		self.D_FNQ = D_FNQ
		self.D_FNG = D_FNG
		self.l_KQ = l_KQ
		self.l_MK = l_MK
		self.l_NQ = l_NQ
		self.l_MN = l_MN
		self.D_FQN = D_FQN
		self.D_KQV = D_KQV
		self.D_KVQ = D_KVQ
		self.D_VKQ = D_VKQ
		
		self.l_CF = l_CF
		self.l_FQ = l_FQ
		self.l_QV = l_QV
		self.D_ACx = D_ACx
		self.l_AC = l_AC
		self.l_CD = l_CD
		self.D_DCF = D_DCF
		self.l_FG = l_FG
		self.D_GFQ = D_GFQ
		self.A_x = params.A_x
		self.A_y = params.A_y
		self.l_FN = l_FN
		self.D_FQN = D_FQN
		self.zeta = params.zeta
	
