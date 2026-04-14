import os
import glob
import re

new_footer_html = """    <!-- Premium Fintech Footer -->
    <footer class="bg-[#0B0B0B] border-t border-[#D4AF37]/10 pt-24 pb-12 mt-auto relative overflow-hidden">
        
        <!-- Subtle Glow Background for ultra-premium feel -->
        <div class="absolute top-0 left-1/2 -translate-x-1/2 w-[800px] h-[400px] bg-[#D4AF37]/5 blur-[150px] pointer-events-none z-0"></div>

        <div class="max-w-7xl mx-auto px-6 md:px-8 relative z-10 space-y-16">
            
            <!-- 5-Column Grid Layout -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-12 lg:gap-8">
                
                <!-- Column 1: Logo Section & Socials (Spans wider slightly or standard 1 col) -->
                <div class="lg:col-span-1 space-y-8 ux-reveal">
                    <div>
                        <!-- Logo Placeholder space -->
                        <a href="index.html" class="inline-block group focus:outline-none">
                            <h2 class="text-3xl font-black text-[#D4AF37] font-headline tracking-tighter group-hover:drop-shadow-[0_0_15px_rgba(212,175,55,0.6)] transition-all duration-300">GOLDe5</h2>
                            <p class="text-[#d0c5af] text-[9px] font-medium tracking-[0.3em] font-body uppercase leading-tight mt-1 group-hover:text-white transition-colors duration-300">Grow in Grams</p>
                        </a>
                        <p class="text-gray-400 text-sm leading-relaxed mt-6">
                            The pinnacle of private metal banking. Secure, liquid, and globally accessible.
                        </p>
                    </div>

                    <!-- Social Icons -->
                    <div class="flex flex-wrap gap-3">
                        <!-- Facebook -->
                        <a href="#" class="w-10 h-10 rounded-full bg-white/5 border border-white/5 flex items-center justify-center text-[#D4AF37] hover:bg-[#D4AF37] hover:text-[#0B0B0B] hover:shadow-[0_0_20px_rgba(212,175,55,0.5)] hover:scale-110 transition-all duration-300">
                            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M22 12c0-5.52-4.48-10-10-10S2 6.48 2 12c0 4.84 3.44 8.87 8 9.8V15H8v-3h2V9.5c0-2.03 1.23-3.14 3.06-3.14.87 0 1.62.06 1.84.09v2.1l-1.26.01c-.99 0-1.18.47-1.18 1.16V12h2.46l-.32 3h-2.14v6.8C18.56 20.87 22 16.84 22 12z"/></svg>
                        </a>
                        <!-- Instagram -->
                        <a href="#" class="w-10 h-10 rounded-full bg-white/5 border border-white/5 flex items-center justify-center text-[#D4AF37] hover:bg-[#D4AF37] hover:text-[#0B0B0B] hover:shadow-[0_0_20px_rgba(212,175,55,0.5)] hover:scale-110 transition-all duration-300">
                            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M7.8 2h8.4C19.4 2 22 4.6 22 7.8v8.4a5.8 5.8 0 0 1-5.8 5.8H7.8C4.6 22 2 19.4 2 16.2V7.8A5.8 5.8 0 0 1 7.8 2zm-.2 2A3.6 3.6 0 0 0 4 7.6v8.8C4 18.4 5.6 20 7.6 20h8.8a3.6 3.6 0 0 0 3.6-3.6V7.6C20 5.6 18.4 4 16.4 4H7.6zm9.65 1.5a1.25 1.25 0 0 1 0 2.5 1.25 1.25 0 0 1 0-2.5zM12 7a5 5 0 1 1 0 10 5 5 0 0 1 0-10zm0 2a3 3 0 1 0 0 6 3 3 0 0 0 0-6z"/></svg>
                        </a>
                        <!-- Twitter (X) -->
                        <a href="#" class="w-10 h-10 rounded-full bg-white/5 border border-white/5 flex items-center justify-center text-[#D4AF37] hover:bg-[#D4AF37] hover:text-[#0B0B0B] hover:shadow-[0_0_20px_rgba(212,175,55,0.5)] hover:scale-110 transition-all duration-300">
                            <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
                        </a>
                        <!-- YouTube -->
                        <a href="#" class="w-10 h-10 rounded-full bg-white/5 border border-white/5 flex items-center justify-center text-[#D4AF37] hover:bg-[#D4AF37] hover:text-[#0B0B0B] hover:shadow-[0_0_20px_rgba(212,175,55,0.5)] hover:scale-110 transition-all duration-300">
                            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M21.582 6.186a2.665 2.665 0 0 0-1.876-1.884C18.04 3.864 12 3.864 12 3.864s-6.04 0-7.706.438a2.665 2.665 0 0 0-1.876 1.884C2 7.86 2 12 2 12s0 4.14.418 5.814a2.665 2.665 0 0 0 1.876 1.884c1.667.438 7.706.438 7.706.438s6.04 0 7.706-.438a2.665 2.665 0 0 0 1.876-1.884C22 16.14 22 12 22 12s0-4.14-.418-5.814zM9.99 15.422v-6.85l6.02 3.426-6.02 3.424z"/></svg>
                        </a>
                        <!-- LinkedIn -->
                        <a href="#" class="w-10 h-10 rounded-full bg-white/5 border border-white/5 flex items-center justify-center text-[#D4AF37] hover:bg-[#D4AF37] hover:text-[#0B0B0B] hover:shadow-[0_0_20px_rgba(212,175,55,0.5)] hover:scale-110 transition-all duration-300">
                            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.924 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
                        </a>
                        <!-- WhatsApp -->
                        <a href="#" class="w-10 h-10 rounded-full bg-white/5 border border-white/5 flex items-center justify-center text-[#D4AF37] hover:bg-[#D4AF37] hover:text-[#0B0B0B] hover:shadow-[0_0_20px_rgba(212,175,55,0.5)] hover:scale-110 transition-all duration-300">
                            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M12.031 0C5.405 0 .016 5.39.016 12.016c0 2.122.553 4.195 1.603 6.012L.016 24l6.115-1.603a11.93 11.93 0 0 0 5.9 1.559h.005c6.626 0 12.015-5.39 12.015-12.016S18.657 0 12.031 0zm0 21.956c-1.787 0-3.535-.48-5.068-1.39l-.363-.215-3.766.988.997-3.673-.236-.375A9.972 9.972 0 0 1 2.022 12.01c0-5.516 4.49-10.007 10.01-10.007 5.516 0 10.006 4.49 10.006 10.006s-4.49 10.007-10.007 10.007zm5.502-7.518c-.302-.151-1.786-.883-2.064-.984-.277-.101-.48-.151-.682.151-.202.302-.782.984-.959 1.185-.176.202-.353.227-.655.076-1.464-.738-2.529-1.316-3.504-2.998-.176-.302.264-.265.852-1.439.076-.151.038-.277-.019-.428-.057-.151-.682-1.639-.933-2.244-.244-.589-.492-.51-.682-.519l-.58-.009c-.202 0-.53.076-.807.378-.277.302-1.06 1.034-1.06 2.518s1.085 2.915 1.236 3.116c.151.202 2.124 3.242 5.143 4.544 2.127.918 2.802.756 3.307.655.679-.136 1.786-.731 2.038-1.437.252-.706.252-1.311.176-1.438-.076-.126-.277-.202-.579-.353z"/></svg>
                        </a>
                    </div>
                </div>

                <!-- Column 2: COMPANY -->
                <div class="lg:col-span-1 space-y-6 ux-reveal" style="animation-delay: 0.1s;">
                    <h5 class="text-[#D4AF37] font-bold font-headline uppercase text-[11px] tracking-[0.2em] relative inline-block">Company<div class="absolute -bottom-2 left-0 w-8 h-px bg-[#D4AF37]"></div></h5>
                    <ul class="space-y-4 text-sm text-gray-300 font-medium">
                        <li><a class="hover:text-[#D4AF37] hover:translate-x-1 inline-block transition-all duration-300" href="#">About Us</a></li>
                        <li><a class="hover:text-[#D4AF37] hover:translate-x-1 inline-block transition-all duration-300" href="#">FAQ</a></li>
                        <li><a class="hover:text-[#D4AF37] hover:translate-x-1 inline-block transition-all duration-300" href="#">Contact Us</a></li>
                        <li><a class="hover:text-[#D4AF37] hover:translate-x-1 inline-block transition-all duration-300" href="#">Careers</a></li>
                    </ul>
                </div>

                <!-- Column 3: EXPLORE -->
                <div class="lg:col-span-1 space-y-6 ux-reveal" style="animation-delay: 0.2s;">
                    <h5 class="text-[#D4AF37] font-bold font-headline uppercase text-[11px] tracking-[0.2em] relative inline-block">Explore<div class="absolute -bottom-2 left-0 w-8 h-px bg-[#D4AF37]"></div></h5>
                    <ul class="space-y-4 text-sm text-gray-300 font-medium">
                        <li><a class="hover:text-[#D4AF37] hover:translate-x-1 inline-block transition-all duration-300" href="gold-sip.html">SIP</a></li>
                        <li><a class="hover:text-[#D4AF37] hover:translate-x-1 inline-block transition-all duration-300" href="coins-bars.html">Shop</a></li>
                        <li><a class="hover:text-[#D4AF37] hover:translate-x-1 inline-block transition-all duration-300" href="#">Marketplace</a></li>
                    </ul>
                </div>

                <!-- Column 4: PARTNERS -->
                <div class="lg:col-span-1 space-y-6 ux-reveal" style="animation-delay: 0.3s;">
                    <h5 class="text-[#D4AF37] font-bold font-headline uppercase text-[11px] tracking-[0.2em] relative inline-block">Partners<div class="absolute -bottom-2 left-0 w-8 h-px bg-[#D4AF37]"></div></h5>
                    <ul class="space-y-4 text-sm text-gray-300 font-medium">
                        <li><a class="hover:text-[#D4AF37] hover:translate-x-1 inline-block transition-all duration-300" href="investor.html">Investors</a></li>
                        <li><a class="hover:text-[#D4AF37] hover:translate-x-1 inline-block transition-all duration-300" href="partner.html">Retail Partners</a></li>
                        <li><a class="hover:text-[#D4AF37] hover:translate-x-1 inline-block transition-all duration-300" href="partner.html">Affiliate Partners</a></li>
                    </ul>
                </div>

                <!-- Column 5: LEGAL -->
                <div class="lg:col-span-1 space-y-6 ux-reveal" style="animation-delay: 0.4s;">
                    <h5 class="text-[#D4AF37] font-bold font-headline uppercase text-[11px] tracking-[0.2em] relative inline-block">Legal<div class="absolute -bottom-2 left-0 w-8 h-px bg-[#D4AF37]"></div></h5>
                    <ul class="space-y-4 text-sm text-gray-300 font-medium">
                        <li><a class="hover:text-[#D4AF37] hover:translate-x-1 inline-block transition-all duration-300" href="terms.html">Terms & Conditions</a></li>
                        <li><a class="hover:text-[#D4AF37] hover:translate-x-1 inline-block transition-all duration-300" href="terms.html">Privacy Policy</a></li>
                        <li><a class="hover:text-[#D4AF37] hover:translate-x-1 inline-block transition-all duration-300" href="terms.html">Cyber Advisory</a></li>
                        <li><a class="hover:text-[#D4AF37] hover:translate-x-1 inline-block transition-all duration-300" href="terms.html">Disclaimer</a></li>
                    </ul>
                </div>

            </div>

            <!-- Bottom Section (Copyright + Status) -->
            <div class="pt-8 mt-12 border-t border-white/10 flex flex-col md:flex-row justify-between items-center gap-6 ux-reveal">
                <p class="text-gray-400 text-xs font-semibold tracking-wider uppercase">
                    © 2026 GOLDe5. All rights reserved.
                </p>
                <div class="flex items-center gap-3 px-4 py-2 bg-white/5 border border-white/5 rounded-full cursor-default hover:bg-white/10 transition-colors">
                    <span class="w-2 h-2 rounded-full bg-green-500 shadow-[0_0_8px_#22c55e] animate-pulse"></span>
                    <span class="text-[10px] font-black text-gray-300 tracking-widest uppercase">Network Status: Operational</span>
                </div>
            </div>

            <!-- Disclaimer -->
            <div class="pt-4 text-center pb-8 ux-reveal">
                <p class="text-gray-500 text-[10px] sm:text-xs font-medium max-w-4xl mx-auto leading-relaxed border-t border-white/5 pt-6">
                    Investments are subject to market risks. Returns are not guaranteed and may vary. Please read all related documents carefully before investing.
                </p>
            </div>

        </div>
    </footer>"""

directory = "c:/Users/LENOVO/OneDrive/Desktop/Golde4"
html_files = glob.glob(os.path.join(directory, "*.html"))

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Find the footer. Usually starts with <!-- Footer --> or <footer
    # and ends with </footer>
    
    # We will use regex to cautiously replace it:
    pattern = re.compile(r'(<!--\s*Footer\s*-->\s*)?<footer.*?</footer>', re.IGNORECASE | re.DOTALL)
    
    if pattern.search(html):
        html = pattern.sub(new_footer_html, html)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Updated footer in {os.path.basename(file_path)}")
    else:
        print(f"No footer tag found in {os.path.basename(file_path)}")
