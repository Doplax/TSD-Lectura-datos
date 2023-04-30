import machine
import utime
import ujson

adc = machine.ADC(26)  # Configura el pin 28 como entrada analógica
uart = machine.UART(0, baudrate=1115200)
while True:
    valor_adc = adc.read_u16()  # Lee el valor analógico en el pin 28
    data = {"valor": valor_adc}
    uart.write(ujson.dumps(data) + "\n")  # Envía los datos a través del puerto serial
    utime.sleep(1)
    print(valor_adc)
