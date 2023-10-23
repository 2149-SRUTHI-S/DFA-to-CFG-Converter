# By Sruthi Sivasankararaj

import tkinter as tk

def dfa_to_cfg(dfa):
    # Replace this function with your actual DFA to CFG conversion logic
    # This is a simplified example
    cfg = "S -> 0S1 | 1A | ε\nA -> 0A | 1S"
    return cfg

def convert_dfa():
    dfa_input = dfa_text.get("1.0", "end-1c")
    cfg_output = dfa_to_cfg(dfa_input)
    cfg_text.delete("1.0", "end")
    cfg_text.insert("end", cfg_output)

def clear_input():
    dfa_text.delete("1.0", "end")

# Create the tkinter GUI
window = tk.Tk()
window.title("DFA to CFG Converter")

# Create a text widget for DFA input
dfa_text = tk.Text(window, width=40, height=10)
dfa_text.grid(row=0, column=0, padx=10, pady=10)

# Create a text widget for CFG output
cfg_text = tk.Text(window, width=40, height=10)
cfg_text.grid(row=0, column=1, padx=10, pady=10)

# Create a button to initiate the conversion
convert_button = tk.Button(window, text="Convert DFA to CFG", command=convert_dfa)
convert_button.grid(row=1, column=0, columnspan=2)

# Button to clear input
clear_button = tk.Button(window, text="Clear Input", command=clear_input)
clear_button.grid(row=2, column=0, columnspan=2)

# Start the tkinter main loop
window.mainloop()
