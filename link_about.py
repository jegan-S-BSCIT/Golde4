import glob
import os

html_files = glob.glob(os.path.join(r"c:\Users\LENOVO\OneDrive\Desktop\Golde4", "*.html"))

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the About Us link
    new_content = content.replace('href="#">About Us', 'href="about.html">About Us')
    
    if content != new_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
