from time import sleep
from random import shuffle
from keyboard import press, release, is_pressed
from threading import Thread

#       W,   A,   S,   D
Key = ["4", "5", "6", "7"]

# ----------------------------------------------------------------

def execute(x, y):
    while is_pressed(x):
        press(Key[y])
        sleep(0.1)
        release(Key[y])

def keypress():
    while True:
        execute("W", 0) # W
        execute("A", 1) # A
        execute("S", 2) # S
        execute("D", 3) # D

def shuffler():
    while True:
        sleep(120)
        release(Key)
        shuffle(Key)
        print("shufled")

# ----------------------------------------------------------------

Thread(target=shuffler).start()
Thread(target=keypress).start()