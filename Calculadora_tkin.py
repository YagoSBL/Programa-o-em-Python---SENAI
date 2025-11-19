import tkinter as tk

def mostrar_resultado_ad():
    n1_ = float(n1.get())
    n2_ = float(n2.get())
    soma = n1_ + n2_
    resultado.config(text=soma)

def mostrar_resultado_sub():
    n1_ = float(n1.get())
    n2_ = float(n2.get())
    sub = n1_ - n2_
    resultado.config(text=sub)

def mostrar_resultado_div():
    n1_ = float(n1.get())
    n2_ = float(n2.get())
    div = n1_ / n2_
    resultado.config(text=div)

def mostrar_resultado_mult():
    n1_ = float(n1.get())
    n2_ = float(n2.get())
    mult = n1_ * n2_
    resultado.config(text=mult)



root = tk.Tk()
root.geometry('250x390')

n1_label = tk.Label(root,text='Número 1', font=('Times new roman', 12))
n1_label.grid(pady=5, column=1 , row=1)

n1 = tk.Entry(root, font=('Times new roman', 12))
n1.grid(row=1,column=2, padx=5)

n2_label = tk.Label(root,text='Número 2', font=('Times new roman', 12))
n2_label.grid(pady=5, column=1 , row=3)

n2 = tk.Entry(root, font=('Times new roman', 12))
n2.grid(row=3,column=2, padx=5)

f=tk.Frame(root)
f.grid(columnspan=4)

btn_soma = tk.Button(f,text='+',font= ('Time news roman', 12), command= mostrar_resultado_ad)
btn_soma.grid(row=5,column=1,padx=5)

btn_sub = tk.Button(f,text='-',font= ('Time news roman', 12), command= mostrar_resultado_sub)
btn_sub.grid(row=5,column=2,padx=5)

btn_div = tk.Button(f,text='/',font= ('Time news roman', 12), command= mostrar_resultado_div)
btn_div.grid(row=5,column=3,padx=5)

btn_mult = tk.Button(f,text='x',font= ('Time news roman', 12), command= mostrar_resultado_mult)
btn_mult.grid(row=5,column=4,padx=5)

resultado = tk.Label(f,text='=',font=('Time news roman', 12))
resultado.grid(row=6,column=2)





root.mainloop()