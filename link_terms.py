import re
import os

pages = ['index.html', 'about.html', 'partner.html', 'investor.html', 'gold-sip.html', 'coins-bars.html', 'gift-voucher.html', 'terms.html']
directory = r"c:\Users\LENOVO\OneDrive\Desktop\Golde4"

for page in pages:
    path = os.path.join(directory, page)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            html = f.read()
        
        # Link in footer
        # Currently the link is usually <a href="#">Terms & Conditions</a> or <a href="#">Terms of Service</a>
        html = re.sub(r'<a[^>]*>Terms & Conditions</a>', '<a class="hover:text-[#D4AF37] hover:translate-x-1 inline-block transition-all duration-300" href="terms.html">Terms & Conditions</a>', html)
        html = re.sub(r'<a[^>]*>Privacy Policy</a>', '<a class="hover:text-[#D4AF37] hover:translate-x-1 inline-block transition-all duration-300" href="terms.html">Privacy Policy</a>', html)
        html = re.sub(r'<a[^>]*>Cyber Advisory</a>', '<a class="hover:text-[#D4AF37] hover:translate-x-1 inline-block transition-all duration-300" href="terms.html">Cyber Advisory</a>', html)
        
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Updated links in {page}")
