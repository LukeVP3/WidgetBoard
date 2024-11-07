import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Widget Board")
window.minsize(width=500, height=300)

#label
a_label = tk.Label(text="I am a Label", font=("Comic Sans", 24, 'bold'))
a_label.pack()

#Entry (textbox)
a_textbox = tk.Entry(width=30)
a_textbox.focus()
a_textbox.insert(index=tk.END, string='Some text to begin with')
a_textbox.pack(pady=(5, 5))

# Button
def button_click():
    a_label['text'] = f'{a_textbox.get()}'


button = tk.Button(text='Click Me', command=button_click)
button.pack(pady=(0, 5))


# Text (multi-line textbox)
text = tk.Text(width=30, height=5)

# Add some text to begin with
text.insert(index=tk.END, chars='Example of multi-line entry')
text.pack(pady=(0, 5))

#Spinbox
def spinbox_used():
    print(spinbox.get())
spinbox = tk.Spinbox(from_=0, to_=10, width=5, command=spinbox_used)
spinbox.pack(pady=(0, 5))

#Scale is a slide
def scale_used(value):
    print(value)
scale = tk.Scale(from_=0, to_=100, command=scale_used,
                orient=tk.HORIZONTAL, length=150, width=10,
                sliderlength=10, tickinterval=20)
scale.pack(pady=(0, 5))

#checkbutton
def checkbutton_used():
    print(checked_state.get())
checked_state = tk.BooleanVar()
checkbutton = tk.Checkbutton(text='Is On?', variable=checked_state,
                             command=checkbutton_used)
checkbutton.pack(pady=(0, 5))

#Radio Buttons
def radio_used():
    print(radio_state.get())
radio_state = tk.IntVar()
radiobutton1 = tk.Radiobutton(text='Option 1', value=1,
                              variable=radio_state, command=radio_used)
radiobutton2 = tk.Radiobutton(text='Option 2', value=2,
                              variable=radio_state, command=radio_used)

radiobutton1.pack()
radiobutton2.pack(pady=(0, 5))
radiobutton1.select()

#Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))
listbox = tk.Listbox(height=4)
fruits = ['Apple', 'Mango', 'Orange', 'Dragonfruit', 'Kiwi', 'Strawberry']
for i, fruit in enumerate(fruits): #enumerate goes through each one of the values in
    # the array and returns the value of the item in the area and the index value itself
    listbox.insert(i, fruit)
listbox.bind(sequence='<<ListboxSelect>>', func=listbox_used)
listbox.pack(pady=(0, 5))

#Combobox
def combobox_used(event):
    print(n.get())
n = tk.StringVar()
combobox = ttk.Combobox(width=30, textvariable=n)
combobox.bind(sequence='<<ComboboxSelected>>', func=combobox_used)
combobox['values'] = (' Synthwave',
                      ' Jazz',
                      ' Rock',
                      ' Metal',
                      ' Lofi',
                      ' Hip-Hop',
                      ' Dubstep')
combobox.pack(pady=(0, 5))

#We must be at the end
window.mainloop()