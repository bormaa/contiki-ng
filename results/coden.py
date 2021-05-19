import random
import matplotlib.pyplot as plt
import numpy as np

random.seed(10)
temp_actual = 25
hum_actual = 40
press_actual = 101000
temp_sum = 0
hum_sum = 0
press_sum = 0
temp_err = []
hum_err = []
press_err = []

class data:
  def __init__(self, Temperature, Humidity,Pressure):
    self.Temperature = Temperature
    self.Humidity = Humidity
    self.Pressure = Pressure


txtdata = open("25-100run.txt", "r")
sensorsdic={}
for line in txtdata:
    splitarray=line.split("	")
    if splitarray[2][0]=="f":
        splitaddr=splitarray[2].split("[")
        addr=splitaddr[0].strip()
        getdata=splitaddr[1].split(":")
        Temp=getdata[3].split(",")[0].strip()
        humidity=getdata[4].split(",")[0].strip()
        Pressure=getdata[5].split("\n")[0].strip()
        #print(Pressure)
        # print(getdata)
        # print(Pressure)
        # print(addr)
        newobj=data(float(Temp), float(humidity), float(Pressure))
        sensorsdic.setdefault(addr,[]).append(newobj)

    # break

# print(len(sensorsdic["fd00::206:6:6:6"]))
keys = sensorsdic.keys()
num_sensors = len(keys)
# print(sensorsdic.values())
first_key = list(sensorsdic)[0]
print(first_key)
#print(sensorsdic)
rounds = len(sensorsdic[first_key])

v = rounds * []
for i in range(rounds):
  v.append(random.gauss(0, 1))

for i in range(rounds):
    for key in keys:
        temp_sum += sensorsdic[key][i].Temperature
        hum_sum += sensorsdic[key][i].Humidity
        press_sum += sensorsdic[key][i].Pressure
    temp_err.append(abs(((temp_sum / num_sensors) + v[i]) - temp_actual))
    hum_err.append(abs(((hum_sum / num_sensors) + v[i]) - hum_actual))
    press_err.append(abs(((press_sum / num_sensors) + v[i]) - press_actual))
    temp_sum = 0
    hum_sum = 0
    press_sum = 0
temp_mn = min(temp_err)
temp_mx = max(temp_err)
temp_avg = sum(temp_err) / rounds
print("min temperature "+str(temp_mn))
print("max temperature "+str(temp_mx))
print("average temperature "+str(temp_avg))

hum_mn = min(hum_err)
hum_mx = max(hum_err)
hum_avg = sum(hum_err) / rounds
print("min humidity "+str(hum_mn))
print("max humidity "+str(hum_mx))
print("average humidity "+str(hum_avg))

press_mn = min(press_err)
press_mx = max(press_err)
press_avg = sum(press_err) / rounds

print("min pressure "+str(press_mn))
print("max pressure "+str(press_mx))
print("average pressure "+str(press_avg))
yt,yh,yp=[],[],[]
steptemp=0
stephum=0
steppress=0
for i in range(len(temp_err)):
    steptemp+=temp_err[i]
    stephum+=hum_err[i]
    steppress+=press_err[i]
    yt.append(steptemp/(i+1))
    yh.append(stephum/(i+1))
    yp.append(steppress/(i+1))

# print(yt)
# print(yh)
# print(yp)
X = np.array(list(range(rounds))).reshape((-1, 1))
yt=np.array(yt)+temp_actual
yh=np.array(yh)+hum_actual
yp=np.array(yp)+press_actual
#plot the values with increase of number of rounds
# print(yt)
# print(yh)
# print(yp)   
# plt.plot(X, yp, 'b') # plot x with the predicted y with color b
# plt.show() # this method called to plot the graph
