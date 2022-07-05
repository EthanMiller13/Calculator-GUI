from tkinter import *

WINDOW_HEIGHT = 320
WINDOW_WIDTH = 285

root = Tk()
root.title("Calculator")
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.resizable(False, False)
root.attributes('-alpha',0.9)

operators = ['+', '-', '*', '/', "Ans"]
Ans = "0"
last_expression = ""
saved_expressions = 0
historyLbl_column = 4
evaluated = None
displayText = Entry(root, width=10, font=50, bd=2, background="#aeb1b5", foreground="black")

BUTTON_WIDTH = 8
BUTTON_HEIGHT = 3
BUTTON_BACKGROUND = "#383e45"  # HEX
BUTTON_FOREGROUND = "white"
BUTTON_FONT = "Arial 10 bold"

# DisplayText Operations
def press(char):
    global evaluated, operators
    text = displayText.get()
    if evaluated is True and char not in operators:
        clear_display()
    elif text == "Math Error" or text == "Syntax Error":
        clear_display()
    displayText.insert("end", char)
    evaluated = False


def clear_display():
    displayText.delete(0, "end")

def delete_last_char():
    global evaluated
    if evaluated is True:
        clear_display()
        evaluated = False
    else:
        displayText.delete(len(displayText.get())-1, "end")


clearBtn = Button(width=BUTTON_WIDTH, height=BUTTON_HEIGHT, text='C', padx=0, command=clear_display, background=BUTTON_BACKGROUND, foreground=BUTTON_FOREGROUND, font=BUTTON_FONT)
deleteBtn = Button(width=BUTTON_WIDTH, height=BUTTON_HEIGHT, text='Del', padx=0, command=delete_last_char, background=BUTTON_BACKGROUND, foreground=BUTTON_FOREGROUND, font=BUTTON_FONT)
AnsBtn = Button(width=BUTTON_WIDTH, height=BUTTON_HEIGHT, text='Ans', padx=0, command=lambda: press("Ans"), background=BUTTON_BACKGROUND, foreground=BUTTON_FOREGROUND, font=BUTTON_FONT)

clearBtn.grid(row=1, column=0, padx=0, sticky="nsew")
deleteBtn.grid(row=1, column=1, padx=0, sticky="nsew")
AnsBtn.grid(row=1, column=2, padx=0, sticky="nsew")

# Math Operations
def evaluate():
    global Ans, evaluated, last_expression, saved_expressions, historyLbl_column
    try:
        text = displayText.get()
        if "Ans" in text:
            if text[text.find("Ans")-1].isdigit():
                solution = str(eval(displayText.get().replace("Ans", '*' + Ans)))
            else:
                solution = str(eval(displayText.get().replace("Ans", Ans)))
        else:
            solution = str(eval(displayText.get()))
        Ans = solution
        evaluated = True
        if text != "" and text != Ans and not text.isdigit():
            last_expression = text + f" = {solution}"
            saved_expressions += 1

            new_expressionlBL = Label(root, width=30, font=50, bd=2, text=last_expression,
                                      background="#aeb1b5", foreground="black", border=3, anchor="w")
            if saved_expressions > 6:
                historyLbl_column += 1
                saved_expressions = 0
                new_expressionlBL.grid(row=saved_expressions - 1, column=4, sticky="nsew")
            else:
                new_expressionlBL.grid(row=saved_expressions - 1, column=4, sticky="nsew")
        clear_display()
        displayText.insert(0, solution)
    except SyntaxError:
        evaluated = True
        clear_display()
        displayText.insert(0, "Syntax Error")
    except Exception as error:
        clear_display()
        displayText.insert(0, "Math Error")

plusBtn = Button(width=BUTTON_WIDTH, height=BUTTON_HEIGHT, text='+', padx=0, command=lambda: press('+'), background=BUTTON_BACKGROUND, foreground=BUTTON_FOREGROUND, font=BUTTON_FONT)
minusBtn = Button(width=BUTTON_WIDTH, height=BUTTON_HEIGHT, text='-', padx=0, command=lambda: press('-'), background=BUTTON_BACKGROUND, foreground=BUTTON_FOREGROUND, font=BUTTON_FONT)
multiplyBtn = Button(width=BUTTON_WIDTH, height=BUTTON_HEIGHT, text='*', padx=0, command=lambda: press('*'), background=BUTTON_BACKGROUND, foreground=BUTTON_FOREGROUND, font=BUTTON_FONT)
divideBtn = Button(width=BUTTON_WIDTH, height=BUTTON_HEIGHT, text='/', padx=0, command=lambda: press('/'), background=BUTTON_BACKGROUND, foreground=BUTTON_FOREGROUND, font=BUTTON_FONT)
equalBtn = Button(width=BUTTON_WIDTH, height=BUTTON_HEIGHT, text='=', padx=0, command=evaluate, foreground=BUTTON_FOREGROUND)
decimalBtn = Button(width=BUTTON_WIDTH, height=BUTTON_HEIGHT, text='.', padx=0, command=lambda: press('.'), background=BUTTON_BACKGROUND, foreground=BUTTON_FOREGROUND, font=BUTTON_FONT)
#openingBracketsBtn = Button(width=BUTTON_WIDTH, height=BUTTON_HEIGHT, text='(', padx=0, command=lambda: press('('))
#closingBracketsBtn = Button(width=BUTTON_WIDTH, height=BUTTON_HEIGHT, text=')', padx=0, command=lambda: press(')'))

plusBtn.grid(row=4, column=3, padx=0, sticky="nsew")
minusBtn.grid(row=3, column=3, padx=0, sticky="nsew")
multiplyBtn.grid(row=2, column=3, padx=0, sticky="nsew")
divideBtn.grid(row=1, column=3, padx=0, sticky="nsew")
equalBtn.grid(row=5, column=3, padx=0, sticky="nsew")
equalBtn.configure(bg="#217ceb")
decimalBtn.grid(row=5, column=2, padx=0, sticky="nsew")
#openingBracketsBtn.grid(row=5, column=0, padx=0, sticky="nsew")
#closingBracketsBtn.grid(row=5, column=1, padx=0, sticky="nsew")

# Numbers
oneBtn = Button(width=BUTTON_WIDTH, height=BUTTON_HEIGHT, text='1', padx=0, command=lambda: press('1'), background=BUTTON_BACKGROUND, foreground=BUTTON_FOREGROUND, font=BUTTON_FONT)
twoBtn = Button(width=BUTTON_WIDTH, height=BUTTON_HEIGHT, text='2', padx=0, command=lambda: press('2'), background=BUTTON_BACKGROUND, foreground=BUTTON_FOREGROUND, font=BUTTON_FONT)
threeBtn = Button(width=BUTTON_WIDTH, height=BUTTON_HEIGHT, text='3', padx=0, command=lambda: press('3'), background=BUTTON_BACKGROUND, foreground=BUTTON_FOREGROUND, font=BUTTON_FONT)
fourBtn = Button(width=BUTTON_WIDTH, height=BUTTON_HEIGHT, text='4', padx=0, command=lambda: press('4'), background=BUTTON_BACKGROUND, foreground=BUTTON_FOREGROUND, font=BUTTON_FONT)
fiveBtn = Button(width=BUTTON_WIDTH, height=BUTTON_HEIGHT, text='5', padx=0, command=lambda: press('5'), background=BUTTON_BACKGROUND, foreground=BUTTON_FOREGROUND, font=BUTTON_FONT)
sixBtn = Button(width=BUTTON_WIDTH, height=BUTTON_HEIGHT, text='6', padx=0, command=lambda: press('6'), background=BUTTON_BACKGROUND, foreground=BUTTON_FOREGROUND, font=BUTTON_FONT)
sevenBtn = Button(width=BUTTON_WIDTH, height=BUTTON_HEIGHT, text='7', padx=0, command=lambda: press('7'), background=BUTTON_BACKGROUND, foreground=BUTTON_FOREGROUND, font=BUTTON_FONT)
eightBtn = Button(width=BUTTON_WIDTH, height=BUTTON_HEIGHT, text='8', padx=0, command=lambda: press('8'), background=BUTTON_BACKGROUND, foreground=BUTTON_FOREGROUND, font=BUTTON_FONT)
nineBtn = Button(width=BUTTON_WIDTH, height=BUTTON_HEIGHT, text='9', padx=0, command=lambda: press('9'), background=BUTTON_BACKGROUND, foreground=BUTTON_FOREGROUND, font=BUTTON_FONT)
zeroBtn = Button(width=BUTTON_WIDTH, height=BUTTON_HEIGHT, text='0', padx=0, command=lambda: press('0'), background=BUTTON_BACKGROUND, foreground=BUTTON_FOREGROUND, font=BUTTON_FONT)

oneBtn.grid(row=2, column=0, padx=0, sticky="nsew")
twoBtn.grid(row=2, column=1, padx=0, sticky="nsew")
threeBtn.grid(row=2, column=2, padx=0, sticky="nsew")
fourBtn.grid(row=3, column=0, padx=0, sticky="nsew")
fiveBtn.grid(row=3, column=1, padx=0, sticky="nsew")
sixBtn.grid(row=3, column=2, padx=0, sticky="nsew")
sevenBtn.grid(row=4, column=0, padx=0, sticky="nsew")
eightBtn.grid(row=4, column=1, padx=0, sticky="nsew")
nineBtn.grid(row=4, column=2, padx=0, sticky="nsew")
zeroBtn.grid(row=5, column=1, padx=0, sticky="nsew")

# History
history_shown = False
def show_history():
    global history_shown, last_expression, saved_expressions
    if history_shown is False:
        root.geometry(f"{2*WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        history_shown = True
    else:
        root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        history_shown = False

historyBtn = Button(width=BUTTON_WIDTH, height=BUTTON_HEIGHT, text='HIS', padx=0, background=BUTTON_BACKGROUND, foreground=BUTTON_FOREGROUND, command=show_history, font=BUTTON_FONT)

historyBtn.grid(row=5, column=0, padx=0, sticky="nsew")

# Grid The DisplayText
displayText.grid(row=0, column=0, columnspan=root.grid_size()[0], sticky="nsew")
press("0")

root.mainloop()
