from PcScripts import TextToOutput as t
from pySerialTransfer import pySerialTransfer as txfer

string = input("Enter a string: ") # Taking input from user
l = t.textToOutput(string)
print(l)
for i in l:
    link = txfer.SerialTransfer('COM4')
    link.open()
    send_size = 0

    ints = [i[0], i[1]]
    size = link.tx_obj(ints)
    send_size += size
    link.send(send_size)

    res_strs = link.rx_obj(obj_type=type(int),
                           obj_byte_size=size,
                           start_pos=size)

    print('SENT: {}'.format(ints))
    print('RCVD: {}'.format(res_strs))
    print(' ')
    link.close()