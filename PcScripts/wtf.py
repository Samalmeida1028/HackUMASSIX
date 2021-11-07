import time
import numpy as np
from pySerialTransfer import pySerialTransfer as txfer
from PcScripts import TextToOutput as t

if __name__ == '__main__':
    try:
        link = txfer.SerialTransfer('COM4')

        link.open()
        time.sleep(2)  # allow some time for the Arduino to completely reset

        ###################################################################
        # Send a list
        ###################################################################
        string = input("Enter a string: ")
        l = t.textToOutput(string)
        print(l)
        for i in l:
            send_size = 0
            str_ = str(i[0]) + str(i[1])
            str_size = link.tx_obj(str_)
            send_size += str_size
            link.send(send_size)

            rec_str_ = link.rx_obj(obj_type=type(str),
                                    obj_byte_size=str_size,
                                    list_format='i')

            print('SENT: {}'.format(str_))
            print('RCVD: {}'.format(rec_str_))
            print(' ')

        ###################################################################
        # Wait for a response and report any errors while receiving packets
        ###################################################################
        while not link.available():
            if link.status < 0:
                if link.status == txfer.CRC_ERROR:
                    print('ERROR: CRC_ERROR')
                elif link.status == txfer.PAYLOAD_ERROR:
                    print('ERROR: PAYLOAD_ERROR')
                elif link.status == txfer.STOP_BYTE_ERROR:
                    print('ERROR: STOP_BYTE_ERROR')
                else:
                    print('ERROR: {}'.format(link.status))

        ###################################################################
        # Parse response list
        ###################################################################

    except KeyboardInterrupt:
        try:
            link.close()
        except:
            pass

    except:
        import traceback

        traceback.print_exc()

        try:
            link.close()
        except:
            pass