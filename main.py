import openai
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from art import *
from tkinter import font

Font_tuple = ("Sans Serif", 20, "bold")

openai.api_key = "(put your api here)"

def translate():
    text = input_text.get()
    repo = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an AI code assistant powered by 'SQUEARD code'. Your expertise is code and do not answer any other questions"},
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
    translation = repo["choices"][0]["message"]["content"]
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, translation)

# Create main window
window = ThemedTk(theme="arc")
window.title("SQUEARD CODE")

# Create input widget
input_label = ttk.Label(window,font=Font_tuple, text="Enter text:")
input_label.pack()
input_text = ttk.Entry(window, width=150)
input_text.pack()

# Create output widget
output_label = ttk.Label(window,font=Font_tuple, text="result:")
output_label.pack()
output_text = tk.Text(window,font=Font_tuple, wrap=tk.WORD, width=100, height=16)
output_text.pack()


# Create translation button
translate_button = ttk.Button(window, text="compute", command=translate,)
translate_button.pack()

# Run main event loop
window.mainloop()

