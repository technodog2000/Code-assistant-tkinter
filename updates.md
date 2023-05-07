07/05/2023

I have included basic code highlighting in responses, using the following code:
```
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
 ```
