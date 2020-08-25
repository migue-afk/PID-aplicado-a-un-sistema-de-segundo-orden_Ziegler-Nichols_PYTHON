#add of libraries
import numpy as np
import matplotlib.pyplot as plt
import control as crtl

#add transfer_fuction

num=[3,5]
den=[1,3,2,3]
sys1=crtl.tf(num,den)
t1,y1=crtl.step_response(sys1)
print(sys1)
plt.figure(1)
plt.plot(t1,y1,'b-',linewidth=1, label='Transfer Fcn')
plt.xlabel('Time')
plt.ylabel('Response (y)')
plt.legend(loc='best')
plt.show() 

#add PID
Pcr=6
Kp=3.0
Ti=0.5*Pcr
Td=0.125*Pcr
#----------------------------------------------------------
a=Kp*Ti*Td
b=Kp*Ti 
c=Kp
d=Ti
num1=[a,b,c]
den2=[0,d,0]
sys3=crtl.tf(num1,den2)
PID_app=crtl.series(sys1,sys3)
print(PID_app)
#Feedback
sys4=crtl.feedback(PID_app)
t2,y2=crtl.step_response(sys4)
#----------------------------------------------------------
plt.figure(2)
plt.plot(t2,y2,'r-',linewidth=1, label='Transfer')
plt.xlabel('Time')
plt.ylabel('Response (y)')
plt.legend(loc='best')
plt.show() 