import os
import re

def main():
    os.makedirs('components', exist_ok=True)
    
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
        
    start_marker = "<!-- Top Navigation Bar -->"
    end_marker = "<main"
    
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker, start_idx)
    
    if start_idx == -1 or end_idx == -1:
        print("Could not find header boundaries.")
        return
        
    # The header block to extract
    header_html = content[start_idx:end_idx].strip()
    
    # Save the component
    with open('components/header.html', 'w', encoding='utf-8') as f:
        f.write(header_html)
    
    print("Created components/header.html successfully.")
    
    replacement_str = """<!-- GLOBAL HEADER INJECTED -->
    <div id="header-placeholder"></div>
    <script>
      fetch("components/header.html")
        .then(res => res.text())
        .then(data => {
          document.getElementById("header-placeholder").innerHTML = data;
          
          // Execute script tags inside fetched HTML (the quote slider JS)
          const scripts = document.getElementById("header-placeholder").querySelectorAll("script");
          scripts.forEach(oldScript => {
            const newScript = document.createElement("script");
            Array.from(oldScript.attributes).forEach(attr => newScript.setAttribute(attr.name, attr.value));
            newScript.appendChild(document.createTextNode(oldScript.innerHTML));
            oldScript.parentNode.replaceChild(newScript, oldScript);
          });
          
          // Add active class logic
          const currentPath = window.location.pathname.split('/').pop() || 'index.html';
          const navLinks = document.querySelectorAll('#header-placeholder a');
          navLinks.forEach(link => {
            const href = link.getAttribute('href');
            // Basic matching, drop trailing slashes/hashes
            const cleanHref = href ? href.split('#')[0].split('?')[0] : '';
            if (cleanHref && currentPath === cleanHref) {
              link.classList.add('text-[#f2ca50]', 'border-[#f2ca50]');
              link.classList.remove('text-gray-400', 'border-transparent');
            } else if (cleanHref) {
              link.classList.remove('text-[#f2ca50]', 'border-[#f2ca50]');
              link.classList.add('text-gray-400', 'border-transparent');
            }
          });
        });
    </script>
    """
    
    for filename in os.listdir('.'):
        if filename.endswith('.html'):
            with open(filename, 'r', encoding='utf-8') as f:
                f_content = f.read()
                
            f_start = f_content.find("<!-- Top Navigation Bar -->")
            f_end = f_content.find("<main", f_start)
            
            if f_start != -1 and f_end != -1:
                new_content = f_content[:f_start] + replacement_str + f_content[f_end:]
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated header in {filename}")
            else:
                print(f"Header markers not found in {filename}, skipping.")

if __name__ == '__main__':
    main()
