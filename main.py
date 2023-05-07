import openai
import tkinter as tk
import tkinter.scrolledtext as st
from tkinter import ttk
from ttkthemes import ThemedTk
from art import *

Font_tuple = ("Sans Serif", 20, "bold")

openai.api_key = "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"

def compute():
    text = input_text.get()
    repo = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an AI code assistant powered by 'SQUEARD code'. Your expertise is code and do not answer any other questions. If you wish to write code, begin the code with ``` and close it with ```"},
            {"role": "user", "content": "how to make a http request?"},
            {"role": "assistant", "content": '''
            import requests

response = requests.get('https://www.example.com')

print(response.status_code)  # prints the HTTP status code
print(response.content)      # prints the response body
'''
            },
            {"role": "user", "content": f"{text}"}
        ]
    )
    compute_output = repo["choices"][0]["message"]["content"]
    output_text.delete(1.0, tk.END)
    
    code_tag = False
    code_start = 1.0
    for line in compute_output.split("\n"):
        if line.strip() == "```":
            if code_tag:
                output_text.tag_add("code", code_start, output_text.index(tk.INSERT))
            else:
                code_start = output_text.index(tk.INSERT)
            code_tag = not code_tag
        else:
            output_text.insert(tk.END, line + "\n")

# Create main window
window = ThemedTk(theme="arc")
window.title("SQUEARD CODE")

# Create input widget
input_label = ttk.Label(window, font=Font_tuple, text="Enter text:")
input_label.pack()
input_text = ttk.Entry(window, width=150)
input_text.pack()

# Create output widget
output_label = ttk.Label(window, font=Font_tuple, text="result:")
output_label.pack()
output_text = st.ScrolledText(window, font=Font_tuple, wrap=tk.WORD, width=100, height=16)
output_text.pack()

# Configure custom code tag for syntax highlighting
output_text.tag_configure("code", foreground="white", background="black")

# Create translation button
compute_button = ttk.Button(window, text="compute", command=compute)
compute_button.pack()

# Run main event loop
window.mainloop()
