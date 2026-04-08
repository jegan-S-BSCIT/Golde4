import os
import glob

directory = "c:/Users/LENOVO/OneDrive/Desktop/Golde4"
html_files = glob.glob(os.path.join(directory, "*.html"))

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Fix the querySelector to include .ux-reveal so the footer columns animate!
    old_query = "document.querySelectorAll('section, .glass-card, h1, h2, h3');"
    new_query = "document.querySelectorAll('section, .glass-card, h1, h2, h3, .ux-reveal');"
    
    if old_query in html:
        html = html.replace(old_query, new_query)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Fixed observers in {os.path.basename(file_path)}")

print("Footer visibility fixed globally.")
