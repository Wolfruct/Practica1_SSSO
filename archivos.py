import os
import random
from io import open

def cam_lin(line):
    aux = ""

    for l in line:
        if l in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
            aux = aux + str(random.randint(0,9))
        elif l in "0123456789":
            aux = aux + chr(random.randint(ord('A'),ord('Z')))
        else:
            aux = aux + l

    return aux

def cop(new_dir1, new_dir2):
    os.chdir(new_dir1)
    arc = os.listdir()

    for ar in arc:
        try:
            os.chdir(new_dir1)
            file = open(ar,'r')
            text = file.readlines()
            file.close()
            os.chdir(new_dir2)
            cfile = open(ar,'a')
            for line in text:
                n_line = cam_lin(line)
                cfile.write(n_line)
            cfile.close()
        except:
            os.chdir(new_dir2)
            os.mkdir(ar)
            cop(new_dir1 + "\{}".format(ar),new_dir2 + "\{}".format(ar))

    return


#Obtener la direccion de las carpetas
def ob_dir():

    dir_or = os.getcwd()
    dir_car1 = dir_or + "\datos1"
    try:
        os.mkdir('datos2')
    except:
        print('Archivo ya exixtente!')
    dir_car2 = dir_or + "\datos2"

    arc = os.listdir(dir_car1)
    
    for ar in arc:
        try:
            os.chdir(dir_car1)
            file = open(ar,'r')
            text = file.readlines()
            file.close()
            os.chdir(dir_car2)
            cfile = open(ar,'a')
            for line in text:
                n_line = cam_lin(line)
                cfile.write(n_line)
            cfile.close()
        except:
            os.chdir(dir_car2)
            os.mkdir(ar)
            cop(dir_car1 + "\{}".format(ar),dir_car2 + "\{}".format(ar))
            

ob_dir()