import socket

from time import sleep
from random import randint

from plyer import accelerometer 
import pygame
from threading import Thread

acceler = 0

pygame.init()

def gas(self, widget):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет
    sock.connect(('192.168.56.1', 33000))  # подключемся к серверному сокету
    text = 'w'
    sock.send(text.encode(encoding='UTF-8'))  # отправляем сообщение
    print('press')
    sock.close()

def stop(self, widget):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет
    sock.connect(('192.168.56.1', 33000))  # подключемся к серверному сокету
    text = 's'
    sock.send(text.encode(encoding='UTF-8'))  # отправляем сообщение
    print('press')
    sock.close()

def start_accelerometer():
    try:
        accelerometer.enable() #enable the accelerometer
        update()
    except:
        print("Failed to start accelerometer")

def update_accelerometer():
    global acceler
    while True:
        try:
            acceler = accelerometer.acceleration[1] # Y
            sleep(0.01)
        except:
            print('accelerometer error') #error







def Button(x, y, size_x, size_y, mouse, text):
    global dis
    f1 = pygame.font.Font(None, 36)
    if mouse[0] > x and mouse[0] < x + size_x and mouse[1] > y and mouse[1] < y + size_y:
            pygame.draw.rect(dis, (255, 0, 0), 
                (x, y, size_x, size_y))
            text1 = f1.render(text, True,
                  (180, 0, 0))
            dis.blit(text1, (x + 20, y + 20))
    else:
        pygame.draw.rect(dis, (0, 255, 0), 
                 (x, y, size_x, size_y))
        text1 = f1.render(text, True,
                  (180, 0, 0))
        dis.blit(text1, (x + 20, y + 20))

# start_accelerometer()
# th = Thread(target=update_accelerometer, daemon=True)
# th.start()

 
dis=pygame.display.set_mode((424, 714))
pygame.display.set_caption('Joystick')
 

game_over=False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
    mouse = pygame.mouse.get_pos()

    Button(150,40,140,140,mouse,'gas')
    Button(150,500,140,140,mouse,'break')

    pygame.display.update()
 
pygame.quit()
quit()