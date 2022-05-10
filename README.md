# Excavator-visualization
挖掘机工作装置（无液压杆模型）可视化

scripts文件夹中：

所有python文件，其中

joint_state_publisher2.py：仅实现ros可视化，发送/joint_states话题

joint_state_publisher3.py：实现simulink与ros联合仿真可视化，发送/joint_states1话题，需要在simulink中订阅。


launch文件夹中：

display.launch：gui工具可视化

display1.launch：simulink与ros联合仿真可视化，包含joint_state_publisher3.py，可改成joint_state_publisher2.py
