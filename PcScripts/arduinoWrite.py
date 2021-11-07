import time
from pySerialTransfer import pySerialTransfer as txfer
from PcScripts import TextToOutput as t

if __name__ == '__main__':
    try:
        link = txfer.SerialTransfer('COM4')

        link.open()
        time.sleep(2)  # allow some time for the Arduino to completely reset
        send_size = 0

        ###################################################################
        # Send a list
        ###################################################################
        string = input("Enter a string: ")
        l = t.textToOutput(string)
        print(l)
        list_size = link.tx_obj(l)
        send_size += list_size
        link.send(send_size)

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

        # ###################################################################
        # Parse response list
        # ###################################################################
        rec_list_ = link.rx_obj(obj_type=type(l),
                                obj_byte_size=list_size,
                                list_format='i')

        print('SENT: {}'.format(l))
        print('RCVD: {}'.format(rec_list_))
        print(' ')

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