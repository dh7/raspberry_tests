import pifacecad
import socket

cad = pifacecad.PiFaceCAD()

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
"""sock.sendto(bytes("800","utf-8"),("127.0.0.1",3007))
sock.sendto(bytes("1200","utf-8"),("127.0.0.1",3007))
"""
sock.bind(("127.0.0.1",3007))
sock.setblocking(0)

frequency = 1000

def print_flag(event):
    global frequency
    flag = event.interrupt_flag
    print(flag)
    if (flag == 64):
        frequency = frequency + 1
    if (flag == 128):
        frequency = frequency - 1
    
listener = pifacecad.SwitchEventListener()
listener.register(0, pifacecad.IODIR_ON, print_flag)
listener.register(1, pifacecad.IODIR_ON, print_flag)
listener.register(2, pifacecad.IODIR_ON, print_flag)
listener.register(3, pifacecad.IODIR_ON, print_flag)
listener.register(4, pifacecad.IODIR_ON, print_flag)
listener.register(5, pifacecad.IODIR_ON, print_flag)
listener.register(6, pifacecad.IODIR_ON, print_flag)
listener.register(7, pifacecad.IODIR_ON, print_flag)
listener.register(8, pifacecad.IODIR_ON, print_flag)
listener.register(9, pifacecad.IODIR_ON, print_flag)
listener.activate()

cad.lcd.backlight_on()
cad.lcd.write("Hello World! :-)\n_@_d_h_7_n_e_t_")

while True:
    data, addr = sock.recvfrom(1024)
    cad.lcd.clear()
    cad.lcd.write("freq. = " + str(frequency) +"Hz\n")
    cad.lcd.write(str(data))
    
     