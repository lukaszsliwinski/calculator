# Calculator

## About
Simply calculator application in Python and Kivy framework. Calculator is based on Codemy course (https://www.youtube.com/watch?v=Lu-HP4eOYM4) and expanded by me with functions such as power, square root, reciprocal, absolute and factorial. The app was made for practice programming in Python and Kivy.

## Used technologies
Python 3.8<br>
Kivy 2.0

## Setup and run (Windows)
Instalation:<br>
1 Install Python 3.8 from website:<br>
&emsp;https://www.python.org/downloads/release/python-380/<br>
&emsp;Important - remember to mark "Add Python 3.8 to PATH"!<br>
&emsp;![alt text](https://github.com/lukaszsliwinski/english_dictionary_kivy/blob/master/add-python-to-path.png?raw=true)<br><br>
2 Download repository
```bash
git clone https://github.com/lukaszsliwinski/calculator
```
3 Go into main directory
```bash
cd calculator
```
4 Create virtual environment with Python 3.8 (you can use any name)
```bash
py -3.8 -m venv name
```
&emsp;This may take a while<br><br>
5 Run virtual environment
```bash
name\scripts\activate
```
&emsp;Important! Keep virtual environment running always when you use app. To deactivate venv use:
```bash
deactivate
```
6 With venv kept running install Kivy 2.0
```bash
python -m pip install kivy[full]
```
&emsp;This may take a while<br><br>
7 In main directory run eng.py file
```bash
python calc.py
```