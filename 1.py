#Дан текстовий файл f. Отримати копію цього файлу.
import shutil
import os
while True:
    button=int(input('Enter your choice:\n1)To make a copy\n2)To watch file\n3)To close file'))
    if button==1:
        shutil.copyfile("text.txt", "test3.txt")
    elif button==2:
        f = open("test3.txt")
        print(f.read())
        f.close()
    elif button==3:
        break