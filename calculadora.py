from tkinter import Tk, Entry, Button, END

def insere_caractere(caractere):
    entrada.insert(END, caractere)
    global expressao
    expressao = entrada.get()

def limpa_entrada():
    entrada.delete(0, END)

def efetua_calculo():
    entrada.delete(0, END)
    calculo = eval(expressao)
    entrada.insert(END, format(calculo, 'n'))


calculadora = Tk()
calculadora.title('Calculadora')
calculadora.geometry('207x170')
calculadora.resizable(False, False)


entrada = Entry(calculadora)
entrada.place(x=0, y=0, width=250)


b1 = Button(calculadora, text='1', width=5, command=lambda  : insere_caractere(1))
b2 = Button(calculadora, text='2', width=5, command=lambda  : insere_caractere(2))
b3 = Button(calculadora, text='3', width=5, command=lambda  : insere_caractere(3))
b4 = Button(calculadora, text='4', width=5, command=lambda  : insere_caractere(4))
b5 = Button(calculadora, text='5', width=5, command=lambda  : insere_caractere(5))
b6 = Button(calculadora, text='6', width=5, command=lambda  : insere_caractere(6))
b7 = Button(calculadora, text='7', width=5, command=lambda  : insere_caractere(7))
b8 = Button(calculadora, text='8', width=5, command=lambda  : insere_caractere(8))
b9 = Button(calculadora, text='9', width=5, command=lambda  : insere_caractere(9))
b10 = Button(calculadora, text='+', width=5, command=lambda : insere_caractere('+'))
b11 = Button(calculadora, text='-', width=5, command=lambda : insere_caractere('-'))
b12 = Button(calculadora, text='*', width=5, command=lambda : insere_caractere('*'))
b13 = Button(calculadora, text='/', width=5, command=lambda : insere_caractere('/'))
b14 = Button(calculadora, text='Limpar', width=5, command=limpa_entrada)
b15 = Button(calculadora, text='=', width=5, command=efetua_calculo)
b16 = Button(calculadora, text='0', width=5, command=lambda : insere_caractere(0))


b1.place(x=5, y=25)
b2.place(x=55, y=25)
b3.place(x=105, y=25)
b4.place(x=5, y=60)
b5.place(x=55, y=60)
b6.place(x=105, y=60)
b7.place(x=5, y=95)
b9.place(x=105, y=95)
b10.place(x=155, y=25)
b11.place(x=155, y=60)
b12.place(x=155, y=95)
b13.place(x=155, y=130)
b14.place(x=55, y=130)
b15.place(x=105, y=130)
b16.place(x=5, y=130)


calculadora.mainloop()
