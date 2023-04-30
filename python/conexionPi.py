import serial
import datetime
import json

class DataPoint:
    def __init__(self, id, port, date, time, value):
        self.id = id
        self.port = port
        self.date = date
        self.time = time
        self.value = value

    def to_dict(self):
        return {
            'id': self.id,
            'port': self.port,
            'date': str(self.date),
            'time': str(self.time),
            'value': self.value,
        }

ser = serial.Serial('COM3', 19200)

data_points = []
id = 1
while id < 100:
    data = ser.readline().rstrip().decode()
    now = datetime.datetime.now()
    # Formatear la fecha y hora actual para obtener solo el día y la hora
    date = now.strftime("%d-%m-%Y")  # formato para el día: dd-mm-aaaa
    time = now.strftime("%H:%M:%S")  # formato para la hora: HH:MM:SS
    
    data_point = DataPoint(id, 'COM3', date, time,  data)
    data_points.append(data_point.to_dict())
    id += 1

    # Guarda los datos cada 10 puntos para reducir el acceso a disco
    #if id % 10 == 0:
    with open('data_points.json', 'w') as f:
        json.dump(data_points, f)