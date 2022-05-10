#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################
####          Copyright 2020 GuYueHome (www.guyuehome.com).          ###
########################################################################

# 该例程将发布joint_states话题，消息类型sensor_msgs::JointState

import rospy
from sensor_msgs.msg import JointState
import visual_ik as vi
import tkinter as tk
#from multiprocessing import Process
from threading import *


new_tag = 0
huizhuantai,dongbi,dougan,chandou = 0, 0.5, -2, -1.5
step1,step2,step3,step4 = 0, 0, 0, 0
def joint_state_publisher():
	global new_tag,huizhuantai,dongbi,dougan,chandou,step1,step2,step3,step4
	# ROS节点初始化
	rospy.init_node('joint_state_publisher', anonymous=True,disable_signals=True)

	# 创建一个Publisher，发布名为/joint_states的topic，消息类型为sensor_msgs::JointState，队列长度10
	joint_state_pub = rospy.Publisher('/joint_states', JointState, queue_size=1000)
	#设置循环的频率
	rate = rospy.Rate(100)
	# 初始化sensor_msgs::JointState类型的消息
	while not rospy.is_shutdown():
		if new_tag == 0:
			joint_state_msg = JointState()
			joint_state_msg.header.stamp = rospy.get_rostime()
			joint_state_msg.name = ['joint1','joint2','joint3','joint4']
			joint_state_msg.position = [huizhuantai,dongbi,dougan,chandou]
			joint_state_msg.velocity = [1, 1, 1, 1]
			# 发布消息
			joint_state_pub.publish(joint_state_msg)
    		##rospy.loginfo("Publsh joint  velocity command[%0.2f m/s, %0.2f rad/s]",
				##vel_msg.linear.x, vel_msg.angular.z)
			# 按照循环频率延时
			rate.sleep()
		elif new_tag == 1:
			i = 0
			while i < 100:
				huizhuantai += step1
				dongbi += step2
				dougan += step3
				chandou += step4
				i += 1
				joint_state_msg = JointState()
				joint_state_msg.header.stamp = rospy.get_rostime()
				joint_state_msg.name = ['joint1','joint2','joint3','joint4']
				joint_state_msg.position = [huizhuantai,dongbi,dougan,chandou]
				joint_state_msg.velocity = [1, 1, 1, 1]
				joint_state_pub.publish(joint_state_msg)
				rate.sleep()
			new_tag =0

def joint_state_input():
	global new_tag,huizhuantai,dongbi,dougan,chandou,step1,step2,step3,step4
	window = tk.Tk()
	window.title('my window')
	window.geometry('200x400')
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
		global new_tag,huizhuantai,dongbi,dougan,chandou,step1,step2,step3,step4
		x = e1.get()
		y = e2.get()
		phi = e3.get()
		huizhuantai2 = e4.get()
		x = float(x)
		y = float(y)
		phi = float(phi)
		huizhuantai2  = float(huizhuantai2)
		dongbi2,dougan2,chandou2 = vi.visual_ik(x, y, phi)
		step1 = (huizhuantai2-huizhuantai)/100
		step2 = (dongbi2-dongbi)/100
		step3 = (dougan2-dougan)/100
		step4 = (chandou2-chandou)/100
		new_tag = 1

	def chushihua():
		global new_tag,huizhuantai,dongbi,dougan,chandou,step1,step2,step3,step4
		huizhuantai2,dongbi2,dougan2,chandou2 = 0, 0.5, -2, -1.5
		step1 = (huizhuantai2-huizhuantai)/100
		step2 = (dongbi2-dongbi)/100
		step3 = (dougan2-dougan)/100
		step4 = (chandou2-chandou)/100
		new_tag = 1

	b1 = tk.Button(window,text='可视化',width=15,height=1,command=keshihua)
	b1.pack()
	b2 = tk.Button(window,text='初始化',width=15,height=1,command=chushihua)
	b2.pack()
	window.mainloop()

if __name__ == '__main__':
	try:
		#Process(target = joint_state_input).start()
		#Process(target = joint_state_publisher).start()
		t1 = Thread(target = joint_state_input)
		t2 = Thread(target = joint_state_publisher)
		t1.start()
		t2.start()
	except rospy.ROSInterruptException:
		pass
