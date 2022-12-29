import math
from tkinter import *
from pygame import mixer
import speech_recognition

mixer.init()


def click(value):
    ex = entryField.get()
    answer = ''

    try:

        if value == 'C':
            ex = ex[0:len(ex) - 1]
            entryField.delete(0, END)
            entryField.insert(0, ex)  # for removing last element in entry field
            return

        elif value == 'CE':
            entryField.delete(0, END)
        elif value == "√":
            answer = math.sqrt(eval(ex))

        elif value == 'π':
            answer = math.pi

        elif value == 'cosθ':
            answer = math.cos(math.radians(eval(ex)))

        elif value == 'tanθ':
            answer = math.tan(math.radians(eval(ex)))

        elif value == 'sinθ':
            answer = math.sin(math.radians(eval(ex)))

        elif value == '2π':
            answer = math.pi * 2

        elif value == 'cosh':
            answer = math.cosh(math.radians(eval(ex)))

        elif value == 'tanh':
            answer = math.tanh(math.radians(eval(ex)))

        elif value == 'sinh':
            answer = math.sinh(math.radians(eval(ex)))

        elif value == chr(8731):
            answer = eval(ex) ** (1 / 3)

        elif value == 'x\u02b8':  # 7**2
            entryField.insert(END, '**')

        elif value == 'x\u00B3':
            answer = eval(ex) ** 3

        elif value == 'x\u00B2':
            answer = eval(ex) ** 2

        elif value == 'ln':
            answer = math.log2(eval(ex))

        elif value == 'deg':
            answer = math.degrees(eval(ex))

        elif value == 'e':
            answer = math.e

        elif value == 'log₁₀':
            answer = math.log10(eval(ex))

        elif value == 'x!':
            answer = math.factorial(int(ex))

        elif value == chr(247):  # 7/2=3.5
            entryField.insert(END, "/")
            return

        elif value == '=':
            answer = eval(ex)
        else:
            entryField.insert(END, value)
            return

        entryField.delete(0, END)
        entryField.insert(0, answer)

    except SyntaxError:
        pass


def findNumbers(t):
    l = []
    for num in t:
        try:
            l.append(int(num))
        except ValueError:
            pass
    return l


def audio():
    # print('hello')
    mixer.music.load('music1.mp3')
    mixer.music.play()
    sr = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as m:

        sr.adjust_for_ambient_noise(m, duration=5)
        print('say anything')
        voice = sr.listen(m)
        try:
            text = sr.recognize_google(voice)
            print(text)
            mixer.music.load('music2.mp3')
            mixer.music.play()
            text_list = text.split(' ')
            # print(text_list)
            for word in text_list:
                if word.upper() in operations.keys():
                    l = findNumbers(text_list)
                    print(l)
                    result = operations[word.upper()](l[0], l[1])  # (5.0,6.0)
                    entryField.delete(0, END)
                    entryField.insert(END, result)


        except:

            print('sorry , could not recognise')


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def mod(a, b):
    return a % b


def lcm(a, b):
    l = math.lcm(a, b)
    return l


def hcf(a, b):
    h = math.gcd(a, b)
    return h


operations = {'ADD': add, 'ADDITION': add, 'SUM': add, 'PLUS': add,
              'SUBTRACTION': sub, 'DIFFERENCE': sub, 'MINUS': sub, 'SUBTRACT': sub,
              'PRODUCT': mul, 'MULTIPLICATION': mul, 'MULTIPLY': mul,
              'DIVISION': div, 'DIV': div, 'DIVIDE': div,
              'LCM': lcm, 'HCF': hcf,
              'MOD': mod, 'REMAINDER': mod, 'MODULUS': mod}

root = Tk()
root.title('smart calculator')
root.config(bg='dodgerblue3')
root.geometry('680x480+100+100')

logoImage = PhotoImage(file='logo.png')
logoLabel = Label(root, image=logoImage, bg='dodgerblue3')
logoLabel.grid(row=0, column=0)

entryField = Entry(root, font=('arial', 20, 'bold'), bg='green', fg='black', bd=10, relief=FLAT, width=30)
entryField.grid(row=0, column=0, columnspan=8)

micImage = PhotoImage(file='microphone.png')
micLabel = Button(root, image=micImage, bd=0, bg='dodgerblue3', activebackground='dodgerblue3', command=audio)
micLabel.grid(row=0, column=7)

buttonTextList = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
                  "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
                  "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
                  "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
                  "0", ".", "%", "=", "log₁₀", "(", ")", "x!"]
rowvalue = 1
columnvalue = 0
for i in buttonTextList:
    button = Button(root, width=5, height=2, bd=2, relief=GROOVE, text=i, bg='dodgerblue3', fg='white',
                    font=('arial', 18, 'bold'), activebackground='red', command=lambda button=i: click(button))
    button.grid(row=rowvalue, column=columnvalue, pady=1)
    columnvalue += 1
    if columnvalue > 7:
        rowvalue += 1
        columnvalue = 0

root.mainloop()
