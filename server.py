import socket
import keyboard
import vgamepad

stick_max = 32768

gamepad = vgamepad.VX360Gamepad()

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('192.168.56.1', 33000))

socket.listen(10)


while True:
    conn, addr = socket.accept()

    data = conn.recv(2048)
    input_data = (data.decode())
    
    try:
        int_data = int(input_data)
        control_stick()
    except:
        if input_data == 'w':
            print('gas')
            # keyboard.press('W')
            # keyboard.release('W')
        else:
            print('stop')

            # keyboard.press('s')
            # keyboard.release('s') 
    


def control_stick(x_y):
    global stick_max
    tilt = (stick_max * (abs(x_y) / 10))
    if x_y < 0:   # LEFT      
        gamepad.left_joystick(x_value=-tilt, y_value=0)
    else:  # RIGHT
        gamepad.left_joystick(x_value=tilt, y_value=0)
        gamepad.update()