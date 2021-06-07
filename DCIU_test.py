import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from matplotlib import style

import serial #Import Serial Library
import time as tm
from time import sleep
#arduinoSerialData = serial.Serial('/dev/ttyACM0',9600) #Create Serial port object called arduinoSerialData
DCIU_serial_data = serial.Serial('/dev/ttyUSB0',1000000)
DCIU_output_file = open("DCIU_result.txt","w")
style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

data_receving_from_arduino_as_string =[]
time = []
distances = []
count = 0


number_of_analog_pins = 5
numberof_of_values_to_store = 10
Voltages = np.zeros((number_of_analog_pins,numberof_of_values_to_store))


# def print_values():
#   while (arduinoSerialData.inWaiting()>0): #Check if data is on the serial port
#    new_data_as_string = arduinoSerialData.readline()
#    new_data_string = new_data_as_string.strip()  
#    new_data = new_data_string.decode('utf-8')
#    new_data = new_data.split(',')
#    print(new_data)

   # if (new_data !=''):
   #  data = [int(i) for i in new_data]
   #  print(data)
   #  sleep(0.1)

def print_dciu_data(data_file):
  
  while (DCIU_serial_data.inWaiting()>0): #Check if data is on the serial port
   new_data_as_string = DCIU_serial_data.readline()
   new_data_string = new_data_as_string.strip()

   # data_file.write(new_data_string)
   # data_file.write("\n")
   # print(new_data_string) 
   idx = new_data_string.find('Time')

   if(idx == 0): #The line contains Time at its begining
    try:
      ADC_data = new_data_string.decode('utf-8')
    except UnicodeDecodeError:
      ADC_data = new_data_string

    # ADC_data = ADC_data.replace(",",'')
    ADC_data = ADC_data.replace(':', ',')
    ADC_data = ADC_data.replace('Time', '')
    # ADC_data = ADC_data.replace('  ', '')
    ADC_data = ADC_data.replace(',', ' ')
    ADC_data = ADC_data.replace('  ', ', ')
    ADC_data = ADC_data.replace(', ,  ', '')
    ADC_data = ADC_data.replace('  ', ' ')


    # ADC_data = ADC_data.replace('     ', '')
    # ADC_data = ADC_data.replace('   ', ' ')
    # ADC_data = ADC_data.replace('  ', ' ')
    # ADC_data = ADC_data.replace(' ', ', ')
    # print(ADC_data)
    data_file.write(ADC_data)
    data_file.write("\n")

    # ADC_data = new_data_string.removesuffix('Time')
    # print(ADC_data)
    # new_data = new_data_string.decode('utf-8')
    # new_data = new_data_string
   
   if(len(new_data_string)<20):
    print(new_data_string)
    return new_data_string


  #print("Command Sent")

def command_DCIU(value):
  value_str = str(value)
  DCIU_serial_data.write(value_str.encode())
  print("Command sent")

#command the arduino
start_time = tm.time()
sleep(0.1)
print_dciu_data(DCIU_output_file)
print("Test Started")
next_time = tm.time() - start_time




command_DCIU('ST')
print("Command Idle sent by the tester")
feedback = None

command_DCIU('ST')
print("Command start sent by the tester")
feedback = None

start_time = tm.time()
while(next_time <100 and feedback != "Start succeeded." and feedback != "DCIU_cant_rn"):
  feedback = print_dciu_data(DCIU_output_file)
  next_time = tm.time() - start_time
  # print(next_time)

command_DCIU('T1')
print("T1 sent by the tester")
feedback = None
start_time = tm.time()
while(next_time <100 and feedback != "T1 succeeded." and feedback != "DCIU_cant_rn"):
  feedback = print_dciu_data(DCIU_output_file)
  next_time = tm.time() - start_time
  # print(next_time)


  
command_DCIU('T2')
print("T2 sent by the tester")
feedback = None
start_time = tm.time()
while(next_time <100 and feedback != "T2 succeeded." and feedback != "DCIU_cant_rn"):
  feedback = print_dciu_data(DCIU_output_file)
  next_time = tm.time() - start_time
  # print(next_time)


command_DCIU('T3')
print("T3 sent by the tester")
feedback = None
start_time = tm.time()
while(next_time <100 and feedback != "T3 succeeded." and feedback != "DCIU_cant_rn"):
  feedback = print_dciu_data(DCIU_output_file)
  next_time = tm.time() - start_time
  # print(next_time)

command_DCIU('T4')
print("T4 sent by the tester")
feedback = None
start_time = tm.time()
while(next_time <100 and feedback != "T4 succeeded." and feedback != "DCIU_cant_rn"):
  feedback = print_dciu_data(DCIU_output_file)
  next_time = tm.time() - start_time
  # print(next_time)

command_DCIU('T5')
print("T5 sent by the tester")
feedback = None
start_time = tm.time()
while(next_time <100 and feedback != "T5 succeeded." and feedback != "DCIU_cant_rn"):
  feedback = print_dciu_data(DCIU_output_file)
  next_time = tm.time() - start_time
  # print(next_time)


command_DCIU('ID')
print("ID sent by the tester")
feedback = None
start_time = tm.time()
while(next_time <5 and feedback != "ID succeeded." and feedback != "DCIU_cant_rn"):  #Check what Idle feedbak is
  feedback = print_dciu_data(DCIU_output_file)
  next_time = tm.time() - start_time
  # print(next_time)


DCIU_output_file.close()










