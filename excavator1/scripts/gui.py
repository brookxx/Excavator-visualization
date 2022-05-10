import tkinter as tk
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
	#print("Tool坐标系的坐标和角度")
	#x = input("x=")
	#y = input("y=")
	#phi = input("phi=")
	#huizhuantai2 = input("请输入回转台角度")

	#results2, flag2, result_num2 = ik.ik(dhparams, x, y, phi,params)
	#flag2, flag2_p, flag2_n = er.exam_reach(results2, params_c)
	#dongbi2,dougan2,chandou2 = vi.visual_ik(x, y, phi)
	#print(huizhuantai2,dongbi2,dougan2,chandou2)
	
	window = tk.Tk()
	window.title('my window')
	window.geometry('200x300')
	xl = tk.Label(window,text='请输入Tool坐标系x=',width=20,height=2)
	xl.pack()
	e1 = tk.Entry(window,show=None)
	e1.pack()
	yl = tk.Label(window,text='请输入Tool坐标系y=',width=20,height=2)
	yl.pack()
	e2 = tk.Entry(window,show=None)
	e2.pack()
	phil = tk.Label(window,text='请输入Tool坐标系phi=',width=20,height=2)
	phil.pack()
	e3 = tk.Entry(window,show=None)
	e3.pack()
	huizuantail = tk.Label(window,text='请输入回转台角度=',width=20,height=2)
	huizuantail.pack()
	e4 = tk.Entry(window,show=None)
	e4.pack()
	
	def keshihua():
		x = e1.get()
		y = e2.get()
		phi = e3.get()
		huizhuantai = e4.get()
		
		x = float(x)
		y = float(y)
		phi = float(phi)
		huizhuantai  = float(huizhuantai)
		dongbi2,dougan2,chandou2 = vi.visual_ik(x, y, phi)
		print(huizhuantai,dongbi2,dougan2,chandou2)

			
	b1 = tk.Button(window,text='可视化',width=15,height=2,command=keshihua)
	b1.pack()
	
	window.mainloop()
	
