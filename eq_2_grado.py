from tkinter import *
from typing_extensions import Literal
import math

root = Tk()
root.title("Risolutore equazioni di 2 grado")

def temp_text_a(e):
    a_box.delete(0,"end")
def temp_text_b(e):
    b_box.delete(0,"end")
def temp_text_c(e):
    c_box.delete(0,"end")
        
def store_values():
    a = int(a_box.get())
    b = int(b_box.get())
    c = int(c_box.get())
    print("a: " + str(a))
    print("b: " + str(b))
    print("c: " + str(c))
    
    delta = b**2-4*a*c

    num_primi = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    
    print("delta: " + str(delta))
    if delta > 0:        
        num_scomposizione = []
        for num in num_primi:
            while ".00" in (str(round(delta/(num**2), 3)) + "00") and ((delta/num) >= 1):
                print("yes", num)
                num_scomposizione.append(num)
                delta = delta/(num**2)
                if delta == 1:
                    break

        print("resto: " + str(delta))
        print(num_scomposizione)

        caso = 0

        prod_num_s = 1
        for num_s in num_scomposizione:
            if len(num_scomposizione) == 0:
                delta_root = u"\u221A" + str(int(delta)) + "/" + str(2*a)
                caso = 1
            if len(num_scomposizione) == 1 and delta != 1:
                delta_root = str(int(num_s/2*a)) + u"\u221A" + str(int(delta))
                caso = 2
            if len(num_scomposizione) == 1 and delta == 1:
                delta_root = num_s/(2*a)
                caso = 3
            if len(num_scomposizione) > 1 and delta == 1:
                prod_num_s = num_s * prod_num_s
                delta_root = str(prod_num_s/(2*a))
                caso = 4
            if len(num_scomposizione) > 1 and delta != 1:
                prod_num_s = num_s * prod_num_s
                delta_root = str(prod_num_s/(2*a)) + u"\u221A" + str(int(delta))
                caso = 5
        
        if caso == 1:
            sol1 = str(-b/(2*a)) + " + " + delta_root
            sol2 = str(-b/(2*a)) + " - " + delta_root
        if caso == 2:
            sol1 = str(-b/(2*a)) + " + " + delta_root
            sol2 = str(-b/(2*a)) + " - " + delta_root
        if caso == 3:
            delta_root = float(delta_root)
            sol1 = str(-b/(2*a) + delta_root)
            sol2 = str(-b/(2*a) - delta_root)
        if caso == 4:
            delta_root = float(delta_root)
            sol1 = str(-b/(2*a) + delta_root)
            sol2 = str(-b/(2*a) - delta_root)
        if caso == 5:
            sol1 = str(-b/(2*a)) + " + " + delta_root
            sol2 = str(-b/(2*a)) + " - " + delta_root
    
    if delta == 0:
        sol1 = str(-b/(2*a))
        sol2 = str(-b/(2*a))
    
    if delta < 0:
        sol1 = "non esiste nel campo R"
        sol2 = "non esiste nel campo R"
        
    sol_1 = Label(root, text="x = " + str(sol1))
    sol_2 = Label(root, text="x = " + str(sol2))
    sol_1.grid(row=2, column=0, columnspan=5)    
    sol_2.grid(row=3, column=0, columnspan=5)    
    
a_box = Entry(root, width=10, justify=RIGHT)
a_box.insert(0,"+              0")
text_a = Label(root, text="x^2", justify=LEFT)
b_box = Entry(root, width=10, justify=RIGHT)
b_box.insert(0, "+              0")
text_b = Label(root, text="x", justify=LEFT)
c_box = Entry(root, width=10, justify=RIGHT)
c_box.insert(0, "+              0")
sol = Button(root, text="soluzione", command=store_values)




a_box.grid(row=0, column=0, padx=5)
text_a.grid(row=0, column=1)
b_box.grid(row=0, column=2, padx=5)
text_b.grid(row=0, column=3)
c_box.grid(row=0, column=4, pady=5)
sol.grid(row=1, column=0,columnspan=5, pady=10)


a_box.bind("<FocusIn>", temp_text_a)
b_box.bind("<FocusIn>", temp_text_b)
c_box.bind("<FocusIn>", temp_text_c)

root.mainloop()

