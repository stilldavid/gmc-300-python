# 3c53504952 000000 1000 3e3e

'''
  // pack address
  get_history_data_cmd += uint8_t((address >> 16) & 0x000000ff); // msb
  get_history_data_cmd += uint8_t((address >>  8) & 0x000000ff);
  get_history_data_cmd += uint8_t((address >>  0) & 0x000000ff); // lsb

  // pack length
  get_history_data_cmd += uint8_t((length >> 8) & 0x00ff);  // lsb
  get_history_data_cmd += uint8_t((length >> 0) & 0x00ff);  // msb
'''

import serial
import struct
import binascii

print 'getting version...'
s = serial.Serial( "/dev/tty.usbserial", 57600 )
s.write("<GETVER>>")
version = s.read(14)
print version

for i in range(0, 15):
  s.write("<SPIR")

  s.write(struct.pack('B', ((i * 4096) >> 16) & 0x00ff )) # msb
  s.write(struct.pack('B', ((i * 4096) >> 8) & 0x00ff ))
  s.write(struct.pack('B', ((i * 4096) >> 0) & 0x00ff ))  # lsb

  s.write(struct.pack('B', (4096 >> 8) & 0x00ff )) # lsb
  s.write(struct.pack('B', (4096 >> 0) & 0x00ff )) # msb

  s.write(">>")

  print('reading mem location ' + str(i))

  i = 0
  while i < 2048:
    if s.inWaiting() > 0: # check if there is a byte waiting
      r = struct.unpack('B', s.read(1))[0] #read the two bytes and unpack binary as hex and reverse them
      print r
      i = i + 1


s.close()
exit()
