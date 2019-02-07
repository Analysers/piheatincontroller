from heatController import heatController
import datetime


class pages():

    def __init__(self):
        self.HC = heatController()

    def showIndex(self):
        try:
            with open('./WWW/index.html', 'r') as index:
                return index.read()
        except Exception as e:
            raise e

    def getCss(self):
        try:
            with open("./WWW/css/style.css") as f:
                return f.read()
        except Exception as e:
            raise e

    def getStatus(self):
        return self.HC.relay.getStatus()

    def getNextStatus(self):
        return self.HC.nextStatus()

    def getTemp(self):
        return self.HC.getT()

    def getHum(self):
        return self.HC.getH()

    def getRommsPage(self):
        pass

    def getConsumption(self):
        pass

    def getForecast(self):
        pass

    def getOperationMode(self):
        pass

    def setRelayStatus(self, newdata):
        for key, value in newdata:
            if key == 's':
                self.HC.relay.setStatus(value[0])

    def setHT(self, newdata):
        data = {'room': '', 'time': '', 'temp': '', 'humidity': ''}
        for key, value in newdata:
            if key == 't':
                data['temp'] = value[0]
            elif key == 'h':
                data['humidity'] = value[0]
            elif key == 'r':
                data['room'] = value[0]
            else:
                print value[0]
        data['time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.HC.setDataFromSensor(data)

    def setAuto(self, *args):
        pass

    def setAlwaysOn(self, *args):
        pass

    def setAlwaysOff(self, *args):
        pass

    def setKT(self, *args):
        pass

    def setError(self):
        print 'gagagagagagag'
