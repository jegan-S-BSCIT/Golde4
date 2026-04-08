import re
import os

ABOUT_CONTENT = """        <!-- Section 1: Hero -->
        <section class="relative min-h-[60vh] md:min-h-[70vh] flex items-center overflow-hidden border-b border-[#D4AF37]/10">
            <div class="absolute inset-0 bg-[#0B0B0B] z-0">
                <img src="https://images.unsplash.com/photo-1616423640778-28d1b17baf62?q=80&w=2000" alt="finance elements" class="w-full h-full object-cover opacity-20 mix-blend-luminosity" />
                <div class="absolute inset-0 bg-gradient-to-r from-[#0B0B0B] via-[#0B0B0B]/80 to-transparent"></div>
            </div>
            <!-- Glow -->
            <div class="absolute top-[20%] left-[10%] w-[500px] h-[500px] bg-[#D4AF37]/10 rounded-full blur-[120px] pointer-events-none"></div>

            <div class="max-w-7xl mx-auto px-6 md:px-8 relative z-10 w-full py-20">
                <div class="w-full md:w-1/2 space-y-8 ux-reveal">
                    <div class="inline-flex items-center gap-3 px-4 py-2 rounded-full border border-[#D4AF37]/30 bg-[#D4AF37]/5 shadow-[0_0_15px_rgba(212,175,55,0.1)]">
                        <span class="w-2 h-2 rounded-full bg-[#D4AF37] animate-pulse"></span>
                        <span class="text-[#D4AF37] font-bold text-xs uppercase tracking-[0.2em]">About GOLDe5</span>
                    </div>
                    <h1 class="text-5xl md:text-7xl font-black font-headline leading-[1.1] text-white">
                        Built on Trust.<br><span class="text-transparent bg-clip-text bullion-gradient">Driven by Value.</span>
                    </h1>
                    <p class="text-xl md:text-2xl text-gray-400 font-medium leading-relaxed max-w-xl">
                        A next-generation platform redefining precious metal investing.
                    </p>
                </div>
            </div>
        </section>

        <!-- Section 2: Founders Story -->
        <section class="py-24 bg-[#0B0B0B] relative">
            <div class="max-w-4xl mx-auto px-6 md:px-8 text-center space-y-12 ux-reveal">
                <h2 class="text-4xl md:text-5xl font-black font-headline text-white">Our Story</h2>
                <div class="space-y-6 text-gray-400 text-lg md:text-xl leading-relaxed font-medium">
                    <p>
                        GOLDe5 is a visionary venture founded by three diverse minds — Albert John, Prakash Keme, and Basheer Kajamoideen. Bringing together decades of expertise across global finance, precious metallurgy, and secure digital architecture, our mission was simple: make wealth preservation natively accessible.
                    </p>
                    <p>
                        We recognized that physical gold and silver have always been the ultimate measure of wealth, yet modern accessibility remained disjointed. By combining traditional asset security with next-generation digital liquidity, we created a platform that bridges the gap.
                    </p>
                </div>
                <div class="pt-8 text-center">
                    <blockquote class="text-2xl md:text-4xl font-headline font-bold text-[#D4AF37] italic leading-relaxed">
                        “Trust knows no boundaries when built on value.”
                    </blockquote>
                </div>
            </div>
        </section>

        <!-- Section 3: What is GOLDe5? -->
        <section class="py-24 bg-[#0F0F0F] border-y border-[#D4AF37]/5 relative overflow-hidden">
            <div class="absolute left-0 bottom-0 w-[400px] h-[400px] bg-[#D4AF37]/5 rounded-full blur-[100px] pointer-events-none"></div>
            
            <div class="max-w-7xl mx-auto px-6 md:px-8 relative z-10">
                <div class="text-center space-y-4 mb-20 ux-reveal">
                    <h2 class="text-4xl md:text-5xl font-black font-headline text-white">What is GOLDe5?</h2>
                    <div class="w-24 h-1 bg-[#D4AF37] mx-auto rounded-full"></div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
                    <!-- Card 1 -->
                    <div class="glass-card rounded-[1.5rem] p-8 space-y-6 ux-reveal flex flex-col h-full" style="animation-delay: 0.1s;">
                        <div class="w-16 h-16 rounded-full bg-[#D4AF37]/10 flex items-center justify-center border border-[#D4AF37]/20 text-[#D4AF37]">
                            <span class="material-symbols-outlined text-3xl">workspace_premium</span>
                        </div>
                        <h3 class="text-2xl font-bold font-headline text-white">Gold & Silver</h3>
                        <p class="text-gray-400 leading-relaxed font-medium flex-1">Our primary investment focus. Secure, vault-audited precious metals available at fractional granularity.</p>
                    </div>
                    <!-- Card 2 -->
                    <div class="glass-card rounded-[1.5rem] p-8 space-y-6 ux-reveal flex flex-col h-full" style="animation-delay: 0.2s;">
                        <div class="w-16 h-16 rounded-full bg-[#D4AF37]/10 flex items-center justify-center border border-[#D4AF37]/20 text-[#D4AF37]">
                            <span class="material-symbols-outlined text-3xl">category</span>
                        </div>
                        <h3 class="text-2xl font-bold font-headline text-white">Platinum & Palladium</h3>
                        <p class="text-gray-400 leading-relaxed font-medium flex-1">Extended high-growth opportunities for diversified resilient portfolios.</p>
                    </div>
                    <!-- Card 3 -->
                    <div class="glass-card rounded-[1.5rem] p-8 space-y-6 ux-reveal flex flex-col h-full" style="animation-delay: 0.3s;">
                        <div class="w-16 h-16 rounded-full bg-[#D4AF37]/10 flex items-center justify-center border border-[#D4AF37]/20 text-[#D4AF37]">
                            <span class="material-symbols-outlined text-3xl">trending_up</span>
                        </div>
                        <h3 class="text-2xl font-bold font-headline text-white">Future Expansion</h3>
                        <p class="text-gray-400 leading-relaxed font-medium flex-1">Broader metal-based investments continuously expanding alongside global industrial demand.</p>
                    </div>
                    <!-- Card 4 -->
                    <div class="glass-card rounded-[1.5rem] p-8 space-y-6 ux-reveal flex flex-col h-full" style="animation-delay: 0.4s;">
                        <div class="w-16 h-16 rounded-full bg-[#D4AF37]/10 flex items-center justify-center border border-[#D4AF37]/20 text-[#D4AF37]">
                            <span class="material-symbols-outlined text-3xl">devices</span>
                        </div>
                        <h3 class="text-2xl font-bold font-headline text-white">Digital Access</h3>
                        <p class="text-gray-400 leading-relaxed font-medium flex-1">Traditional assets supercharged with modern technology. Immediate liquidity and real-time tracking.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Section 4: What GOLDe5 Does & Sectors -->
        <section class="py-24 bg-[#0B0B0B] relative">
            <div class="max-w-7xl mx-auto px-6 md:px-8">
                <div class="flex flex-col lg:flex-row gap-16 lg:gap-24 items-center">
                    
                    <!-- Left: Text & Bullets -->
                    <div class="w-full lg:w-1/2 space-y-12 ux-reveal">
                        <h2 class="text-4xl md:text-5xl font-black font-headline text-white">What GOLDe5 Does</h2>
                        
                        <ul class="space-y-6">
                            <li class="flex items-start gap-5">
                                <div class="w-8 h-8 rounded-full bg-[#D4AF37] flex items-center justify-center text-[#111] shrink-0 mt-1 shadow-[0_0_10px_rgba(212,175,55,0.4)]">
                                    <span class="material-symbols-outlined text-[20px] font-bold">check</span>
                                </div>
                                <p class="text-xl text-gray-300 font-medium">Own gold & silver in secure, audited vaults instantly.</p>
                            </li>
                            <li class="flex items-start gap-5">
                                <div class="w-8 h-8 rounded-full bg-[#D4AF37] flex items-center justify-center text-[#111] shrink-0 mt-1 shadow-[0_0_10px_rgba(212,175,55,0.4)]">
                                    <span class="material-symbols-outlined text-[20px] font-bold">check</span>
                                </div>
                                <p class="text-xl text-gray-300 font-medium">Access highly curated metal-based industry investment opportunities.</p>
                            </li>
                            <li class="flex items-start gap-5">
                                <div class="w-8 h-8 rounded-full bg-[#D4AF37] flex items-center justify-center text-[#111] shrink-0 mt-1 shadow-[0_0_10px_rgba(212,175,55,0.4)]">
                                    <span class="material-symbols-outlined text-[20px] font-bold">check</span>
                                </div>
                                <p class="text-xl text-gray-300 font-medium">Diversify effortlessly into related industrial and core material sectors.</p>
                            </li>
                            <li class="flex items-start gap-5">
                                <div class="w-8 h-8 rounded-full bg-[#D4AF37] flex items-center justify-center text-[#111] shrink-0 mt-1 shadow-[0_0_10px_rgba(212,175,55,0.4)]">
                                    <span class="material-symbols-outlined text-[20px] font-bold">check</span>
                                </div>
                                <p class="text-xl text-gray-300 font-medium">Track your granular portfolio growth in absolute real time.</p>
                            </li>
                        </ul>
                    </div>

                    <!-- Right: Sectors -->
                    <div class="w-full lg:w-1/2 ux-reveal" style="animation-delay: 0.2s;">
                        <div class="glass-card rounded-[2rem] p-10 md:p-14 border border-[#D4AF37]/20 shadow-[0_20px_50px_rgba(0,0,0,0.8)] relative overflow-hidden">
                            <div class="absolute -top-10 -right-10 w-40 h-40 bg-[#D4AF37]/10 rounded-full blur-[40px] pointer-events-none"></div>
                            
                            <h3 class="text-2xl font-bold font-headline text-white mb-8 relative z-10">Example Sectors</h3>
                            <div class="flex flex-wrap gap-4 relative z-10">
                                <span class="px-6 py-3 rounded-full bg-white/5 border border-white/10 text-gray-300 font-semibold hover:border-[#D4AF37]/50 hover:bg-[#D4AF37]/10 transition-all cursor-default">💎 Jewellery</span>
                                <span class="px-6 py-3 rounded-full bg-white/5 border border-white/10 text-gray-300 font-semibold hover:border-[#D4AF37]/50 hover:bg-[#D4AF37]/10 transition-all cursor-default">🔌 Electronics</span>
                                <span class="px-6 py-3 rounded-full bg-white/5 border border-white/10 text-gray-300 font-semibold hover:border-[#D4AF37]/50 hover:bg-[#D4AF37]/10 transition-all cursor-default">🔋 Renewable Energy</span>
                                <span class="px-6 py-3 rounded-full bg-white/5 border border-white/10 text-gray-300 font-semibold hover:border-[#D4AF37]/50 hover:bg-[#D4AF37]/10 transition-all cursor-default">🚗 Automotive</span>
                                <span class="px-6 py-3 rounded-full bg-white/5 border border-white/10 text-gray-300 font-semibold hover:border-[#D4AF37]/50 hover:bg-[#D4AF37]/10 transition-all cursor-default">⚙️ Refining</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Section 5: Core Commitments -->
        <section class="py-24 bg-[#080808] border-y border-[#D4AF37]/5">
            <div class="max-w-7xl mx-auto px-6 md:px-8">
                <div class="text-center space-y-4 mb-20 ux-reveal">
                    <h2 class="text-4xl md:text-5xl font-black font-headline text-white">Core Commitments</h2>
                    <div class="w-24 h-1 bg-[#D4AF37] mx-auto rounded-full"></div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                    <!-- Mission -->
                    <div class="glass-card rounded-[2rem] p-10 text-center flex flex-col h-full ux-reveal" style="animation-delay: 0.1s;">
                        <h4 class="text-sm font-bold uppercase tracking-[0.3em] text-[#D4AF37] mb-8">Mission</h4>
                        <p class="text-xl text-gray-300 font-medium leading-relaxed flex-grow">
                            To make precious-metal investing simple, secure, and accessible to everyone.
                        </p>
                    </div>
                    <!-- Vision -->
                    <div class="glass-card rounded-[2rem] p-10 text-center flex flex-col h-full border border-[#D4AF37]/30 shadow-[0_10px_30px_rgba(212,175,55,0.15)] bg-gradient-to-b from-[#181818] to-[#0A0A0A] ux-reveal" style="animation-delay: 0.2s;">
                        <h4 class="text-sm font-bold uppercase tracking-[0.3em] text-[#D4AF37] mb-8">Vision</h4>
                        <p class="text-xl text-gray-300 font-medium leading-relaxed flex-grow">
                            To become a heavily trusted global platform for core metal-based wealth creation.
                        </p>
                    </div>
                    <!-- Promise -->
                    <div class="glass-card rounded-[2rem] p-10 text-center flex flex-col h-full ux-reveal" style="animation-delay: 0.3s;">
                        <h4 class="text-sm font-bold uppercase tracking-[0.3em] text-[#D4AF37] mb-8">Promise</h4>
                        <p class="text-xl text-gray-300 font-medium leading-relaxed flex-grow">
                            At GOLDe5, <span class="text-[#D4AF37] font-bold block mt-4 text-3xl tracking-wide">Every Gram Matters.</span>
                        </p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Section 6: Trust / Credibility -->
        <section class="py-24 bg-[#0B0B0B] relative">
            <div class="max-w-7xl mx-auto px-6 md:px-8">
                <div class="grid grid-cols-1 md:grid-cols-3 gap-12 divide-y md:divide-y-0 md:divide-x divide-white/10">
                    <div class="px-8 text-center space-y-4 ux-reveal" style="animation-delay: 0.1s;">
                        <div class="text-6xl md:text-7xl font-black text-[#D4AF37] font-headline drop-shadow-[0_0_15px_rgba(212,175,55,0.3)]">12+</div>
                        <h5 class="text-lg text-gray-300 font-medium tracking-wide uppercase">Years Experience</h5>
                    </div>
                    <div class="px-8 text-center space-y-4 pt-12 md:pt-0 ux-reveal" style="animation-delay: 0.2s;">
                        <div class="text-6xl md:text-7xl font-black text-[#D4AF37] font-headline drop-shadow-[0_0_15px_rgba(212,175,55,0.3)]">4+</div>
                        <h5 class="text-lg text-gray-300 font-medium tracking-wide uppercase">Years SpixMatrix</h5>
                    </div>
                    <div class="px-8 text-center space-y-4 pt-12 md:pt-0 ux-reveal" style="animation-delay: 0.3s;">
                        <div class="text-6xl md:text-7xl font-black text-[#D4AF37] font-headline drop-shadow-[0_0_15px_rgba(212,175,55,0.3)]">ALL</div>
                        <h5 class="text-lg text-gray-300 font-medium tracking-wide uppercase flex flex-col gap-1">Multi-Metal <span>Expertise</span></h5>
                    </div>
                </div>
            </div>
        </section>

        <!-- Section 7: CTA Conversion -->
        <section class="py-32 relative overflow-hidden bg-[#0A0A0A] border-t border-[#D4AF37]/10">
            <div class="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0MCIgaGVpZ2h0PSI0MCI+PGRlZnM+PHBhdHRlcm4gaWQ9ImdyaWQiIHdpZHRoPSI0MCIgaGVpZ2h0PSI0MCIgcGF0dGVyblVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdHRoIGQ9Ik0gNDAgMCBMIDAgMCAwIDQwIiBmaWxsPSJub25lIiBzdHJva2U9InJnYmEoMjEyLCAxNzUsIDU1LCAwLjAxNSkiIHN0cm9rZS13aWR0aD0iMSIvPjwvcGF0dGVybj48L2RlZnM+PHJlY3Qgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSIgZmlsbD0idXJsKCNncmlkKSIvPjwvc3ZnPg==')] z-0"></div>
            <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full max-w-4xl h-[400px] bg-[#D4AF37]/10 rounded-full blur-[150px] pointer-events-none z-0"></div>
            
            <div class="max-w-5xl mx-auto px-6 md:px-8 text-center relative z-10 space-y-10 ux-reveal">
                <h2 class="text-5xl md:text-6xl font-black font-headline text-white tracking-tight">
                    Start Your Journey with <br/><span class="text-transparent bg-clip-text bullion-gradient inline-block mt-4">GOLDe5</span>
                </h2>
                <p class="text-2xl text-gray-300 font-medium mt-4">Invest in real assets. Grow with confidence.</p>
                
                <div class="pt-8 flex flex-col sm:flex-row items-center justify-center gap-6">
                    <a href="investor.html" class="w-full sm:w-auto text-center bullion-gradient text-[#111] px-10 py-5 rounded-xl font-headline font-extrabold text-lg tracking-wide active:scale-95 transition-all duration-300 shadow-[0_0_20px_rgba(212,175,55,0.4)] hover:shadow-[0_0_35px_rgba(212,175,55,0.8)] hover:brightness-110 flex items-center justify-center gap-3 group">
                        Get Started
                        <span class="material-symbols-outlined text-lg group-hover:translate-x-1 transition-transform">arrow_forward</span>
                    </a>
                    <a href="gold-sip.html" class="w-full sm:w-auto text-center bg-white/5 border border-white/20 text-white px-10 py-5 rounded-xl font-headline font-bold text-lg tracking-wide hover:bg-white/10 hover:border-white/40 active:scale-95 transition-all duration-300">
                        Explore Investments
                    </a>
                </div>
            </div>
        </section>\n"""

# read index.html to act as template
index_path = r"c:\Users\LENOVO\OneDrive\Desktop\Golde4\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    template = f.read()

# isolate the <main> block and replace it
import re

# Find everything up to <main class="flex-1 w-full"> (or variation)
header_match = re.search(r'^(.*?)<main[^>]*>', template, re.DOTALL | re.IGNORECASE)
if header_match:
    header = header_match.group(0)
    
    # Find everything after </main>
    footer_match = re.search(r'</main>(.*)$', template, re.DOTALL | re.IGNORECASE)
    if footer_match:
        footer = footer_match.group(1)
        
        # Construct about page
        about_html = header + "\n" + ABOUT_CONTENT + "\n</main>" + footer
        
        # update title
        about_html = about_html.replace("<title>GOLDe5 | Premium Wealth Management</title>", "<title>About Us - GOLDe5 | Premium Wealth Management</title>")
        
        # create about.html
        about_path = r"c:\Users\LENOVO\OneDrive\Desktop\Golde4\about.html"
        with open(about_path, "w", encoding="utf-8") as f:
            f.write(about_html)
        print("Successfully created about.html")
    else:
        print("Couldn't find </main>")
else:
    print("Couldn't find <main>")
