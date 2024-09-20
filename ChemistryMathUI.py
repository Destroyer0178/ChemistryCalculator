import tkinter
import ChemistryMath as CM

def clicked():
        word_num = str(CM.GetMolarMass([element_entry.get()]))
        result.config(text=word_num)

root = tkinter.Tk()

root.title("Molar Mass Calculator")
root.minsize(300,140)
heading = tkinter.Label(root,text="Enter a Molecule to find the Molar Mass")
heading.pack()
element_entry = tkinter.Entry(root,width=30)
element_entry.pack()
button = tkinter.Button(root,text="Enter",width=20,command=clicked)
button.pack()
result = tkinter.Label(root,text="")
result.pack()

root.mainloop()
