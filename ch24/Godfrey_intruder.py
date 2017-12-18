import time
import winsound

class SystemMode():
    def __init__(self, pos=0):
        self.sysmode="inactive"

    def PressButton(self):
        if self.sysmode=="inactive":
            self.sysmode="active"


    def EnterPIN(self):
        self.sysmode="inactive"

    def SensorActivated(self):
        if self.sysmode=="active":
            self.sysmode="Alert"

    def TwoMin(self):
        if self.sysmode=="Alert":
            self.sysmode="BellRings"

A=SystemMode()
S=False
Q=True
while Q==True:
    i=input("PIN, Button,sensor or quit")
    if i=="PIN":
        A.EnterPIN()
        print(A.sysmode)
    if i== "button":
        A.PressButton()
        print(A.sysmode)
    if i == "sensor":
        A.SensorActivated()
        t0=time.time()
        S=True
        print(A.sysmode)
    if i=="quit":
        Q=False
    if S==True:
        if time.time()-t0>=10:
            A.TwoMin()
    if A.sysmode=="BellRings":
        winsound.Beep(1000, 10000)
