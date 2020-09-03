from tkinter import *
from tkinter import filedialog as fd
import tkinter.ttk as ttk
from ttkthemes import ThemedTk
from ttkthemes import ThemedStyle
from tkinter import ttk
import time
import re
import requests
from configparser import ConfigParser
import sys, argparse
import pyglet

pyglet.font.add_file('googlesans.ttf')
config = 'config.ini'
cparser = ConfigParser()
cparser.read(config)
api = cparser['stuff']['apikey']
city = cparser['stuff']['city']
parser = argparse.ArgumentParser()
parser.add_argument('city', nargs='?')
args = parser.parse_args()
if(args.city != None):
    site='http://api.openweathermap.org/data/2.5/weather?q=' + args.city + '&appid=' + api
else:
    site='http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api

degree = u"\N{DEGREE SIGN}"

base = Tk()
base.title("TheRagingBeast")
base.geometry("300x300")
base.configure(bg="Black")

def temp():
    final = requests.get(site)
    js = final.json()
    temp = js['main']['temp']
    finaltemp = (temp - 273.15)
    return str(round(finaltemp))+degree

def city():
    final = requests.get(site)
    js = final.json()
    city = js['name']
    return city.upper()

def icon():
    final = requests.get(site)
    js = final.json()
    icon = js['weather'][0]['icon']
    return icon

def cond():
    final = requests.get(site)
    js = final.json()
    cond = js['weather'][0]['main']
    return cond

def humid():
    final = requests.get(site)
    js = final.json()
    hum = js['main']['humidity']
    return str(hum)

def real_feel():
    final = requests.get(site)
    js = final.json()
    real_feel = js['main'] ['feels_like']
    feelslike = (real_feel - 273.15)
    return str(round(feelslike))+degree

canvas = Canvas(base, width=300, height=250)
canvas.pack(expand='yes',fill='both')
canvas.configure(bg="gray", highlightthickness=0)
canvas.create_text(50,10,text=temp(),font=('Google Sans', 100),anchor='nw',fill='Black')
canvas.create_text(70,20,text=city(),font=('Google Sans', 14),fill='Black')
ic = PhotoImage(file='icons/{}.png'.format(icon()))
canvas.create_image(127,170, image=ic)
canvas.create_text(125,210,text=cond(),font=('Google Sans', 14),fill='Black')
canvas.create_text(130,240,text="Humidity :" + r'    ' + humid(), font=('Google Sans', 15),fill='Black')
canvas.create_text(130,265,text="RealFeel :" + r'    ' + real_feel(), font=('Google Sans', 15),fill='Black')


base.mainloop()