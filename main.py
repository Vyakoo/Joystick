import socket

from time import sleep
from random import randint

from plyer import accelerometer 

import kivy
from kivy.app import App
from kivy.core.window import Window

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from threading import Thread

acceler = 0



kivy.require('1.5.1')
Window.size = (640, 360)

class MyApp(App):

    def build(self):
        layout = BoxLayout()

        gas = Button(text='gas', 
            font_size = 15, 
            size_hint=(None, None),
            pos_hint={'x':.5, 'y':.4}, 
            size=(320, 180),
            on_press=self.gas)

        stop = Button(text='stop', 
            font_size = 15, 
            size_hint=(None, None),
            pos_hint={'x':.0, 'y':.4}, 
            size=(315, 180),
            on_press=self.stop)

        layout.add_widget(gas)
        layout.add_widget(stop)


        return layout


    # def stop(self, widget):
    #     sock.send(bytes(12))  # отправляем сообщение
        


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

start_accelerometer()
th = Thread(target=update_accelerometer, daemon=True)
th.start()

if __name__ == "__main__":
    MyApp().run()