class data:
  def __init__(self, Temperature, Humidity,Pressure):
    self.Temperature = Temperature
    self.Humidity = Humidity
    self.Pressure = Pressure
txtdata = open("1.txt", "r")
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
        # print(getdata)
        # print(Pressure)
        # print(addr)
        newobj=data(Temp,humidity,Pressure)
        sensorsdic.setdefault(addr,[]).append(newobj)

    # break
print(len(sensorsdic["fd00::206:6:6:6"]))
