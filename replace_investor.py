import os

html_sections = """    <!-- Flexible Investor Section -->
    <section class="max-w-7xl mx-auto px-8 py-20 animate-slide-up" style="animation-delay: 0.2s">
        <div class="flex flex-col md:flex-row gap-16 items-center">
            <div class="md:w-1/2 space-y-6">
                <span class="text-[#D4AF37] font-bold tracking-[0.3em] uppercase text-[10px]">Investment Options</span>
                <h2 class="text-4xl md:text-5xl font-extrabold font-headline tracking-tight text-white mb-2">Flexible Investor</h2>
                <p class="text-on-surface-variant/70 leading-relaxed font-medium">Build a resilient portfolio that bends, not breaks. Invest at your own pace without rigid requirements.</p>
            </div>
            <div class="md:w-1/2 w-full glass-card rounded-[2rem] p-8 md:p-10 relative overflow-hidden group">
                <div class="absolute -top-32 -right-32 w-64 h-64 bg-[#D4AF37]/10 rounded-full blur-[80px]"></div>
                <ul class="space-y-6 relative z-10">
                    <li class="flex items-center gap-4">
                        <div class="w-12 h-12 rounded-full border border-[#D4AF37]/20 bg-[#D4AF37]/10 flex items-center justify-center text-[#D4AF37] shadow-[0_0_15px_rgba(212,175,55,0.1)] group-hover:bg-[#D4AF37]/20 transition-all">
                            <span class="material-symbols-outlined">pentagon</span>
                        </div>
                        <span class="text-lg font-bold text-white tracking-wide">Gold</span>
                    </li>
                    <li class="flex items-center gap-4">
                        <div class="w-12 h-12 rounded-full border border-white/20 bg-white/10 flex items-center justify-center text-white shadow-[0_0_15px_rgba(255,255,255,0.1)] group-hover:bg-white/20 transition-all">
                            <span class="material-symbols-outlined">circle</span>
                        </div>
                        <span class="text-lg font-bold text-white tracking-wide">Silver</span>
                    </li>
                    <li class="flex items-center gap-4">
                        <div class="w-12 h-12 rounded-full border border-[#c7cbff]/20 bg-[#c7cbff]/10 flex items-center justify-center text-[#c7cbff] shadow-[0_0_15px_rgba(199,203,255,0.1)] group-hover:bg-[#c7cbff]/20 transition-all">
                            <span class="material-symbols-outlined">hexagon</span>
                        </div>
                        <span class="text-lg font-bold text-white tracking-wide">Platinum & Palladium</span>
                    </li>
                    <li class="flex items-center gap-4">
                        <div class="w-12 h-12 rounded-full border border-[#E6C65C]/20 bg-[#E6C65C]/10 flex items-center justify-center text-[#E6C65C] shadow-[0_0_15px_rgba(230,198,92,0.1)] group-hover:bg-[#E6C65C]/20 transition-all">
                            <span class="material-symbols-outlined">factory</span>
                        </div>
                        <span class="text-lg font-bold text-white tracking-wide">Metal-based industries</span>
                    </li>
                </ul>
            </div>
        </div>
    </section>

    <!-- How It Works Section -->
    <section class="py-24 relative bg-[#0a0a0a] border-y border-white/5 animate-slide-up" style="animation-delay: 0.3s">
        <div class="max-w-7xl mx-auto px-8">
            <div class="text-center mb-16 space-y-4">
                <span class="text-[#D4AF37] font-bold tracking-[0.3em] uppercase text-[10px]">Simple. Smart. Seamless.</span>
                <h2 class="text-4xl md:text-5xl font-extrabold font-headline tracking-tight text-white">How It Works</h2>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <!-- Card 1 -->
                <div class="glass-card p-10 rounded-[2rem] relative overflow-hidden group hover:-translate-y-2 transition-all">
                    <div class="text-[120px] font-black text-white/[0.02] absolute -bottom-10 -right-4 select-none pointer-events-none group-hover:text-white/[0.04] transition-colors">01</div>
                    <div class="relative z-10 space-y-6">
                        <div class="w-16 h-16 rounded-2xl bg-[#D4AF37]/10 border border-[#D4AF37]/20 flex items-center justify-center text-[#D4AF37] group-hover:bg-[#D4AF37]/20 transition-colors shadow-[0_0_20px_rgba(212,175,55,0.1)]">
                            <span class="material-symbols-outlined text-3xl">account_balance_wallet</span>
                        </div>
                        <h3 class="text-2xl font-bold font-headline text-white group-hover:text-[#D4AF37] transition-colors">Invest Anytime</h3>
                        <p class="text-on-surface-variant/70 text-sm leading-relaxed">Add funds anytime</p>
                    </div>
                </div>
                <!-- Card 2 -->
                <div class="glass-card p-10 rounded-[2rem] relative overflow-hidden group hover:-translate-y-2 transition-all">
                    <div class="text-[120px] font-black text-white/[0.02] absolute -bottom-10 -right-4 select-none pointer-events-none group-hover:text-white/[0.04] transition-colors">02</div>
                    <div class="relative z-10 space-y-6">
                        <div class="w-16 h-16 rounded-2xl bg-[#D4AF37]/10 border border-[#D4AF37]/20 flex items-center justify-center text-[#D4AF37] group-hover:bg-[#D4AF37]/20 transition-colors shadow-[0_0_20px_rgba(212,175,55,0.1)]">
                            <span class="material-symbols-outlined text-3xl">hub</span>
                        </div>
                        <h3 class="text-2xl font-bold font-headline text-white group-hover:text-[#D4AF37] transition-colors">Smart Allocation</h3>
                        <p class="text-on-surface-variant/70 text-sm leading-relaxed">Funds spread across metals</p>
                    </div>
                </div>
                <!-- Card 3 -->
                <div class="glass-card p-10 rounded-[2rem] relative overflow-hidden group hover:-translate-y-2 transition-all">
                    <div class="text-[120px] font-black text-white/[0.02] absolute -bottom-10 -right-4 select-none pointer-events-none group-hover:text-white/[0.04] transition-colors">03</div>
                    <div class="relative z-10 space-y-6">
                        <div class="w-16 h-16 rounded-2xl bg-[#D4AF37]/10 border border-[#D4AF37]/20 flex items-center justify-center text-[#D4AF37] group-hover:bg-[#D4AF37]/20 transition-colors shadow-[0_0_20px_rgba(212,175,55,0.1)]">
                            <span class="material-symbols-outlined text-3xl">trending_up</span>
                        </div>
                        <h3 class="text-2xl font-bold font-headline text-white group-hover:text-[#D4AF37] transition-colors">Portfolio Growth</h3>
                        <p class="text-on-surface-variant/70 text-sm leading-relaxed">Track and grow investment</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Traditional vs GOLDe5 Section -->
    <section class="max-w-7xl mx-auto px-8 py-24 animate-slide-up" style="animation-delay: 0.4s">
        <div class="text-center mb-16">
            <h2 class="text-3xl md:text-5xl font-extrabold font-headline tracking-tight text-white">Traditional vs <span class="text-[#D4AF37]">GOLDe5</span></h2>
        </div>
        
        <div class="glass-card rounded-[2rem] overflow-x-auto">
            <table class="w-full text-left border-collapse min-w-[700px]">
                <thead>
                    <tr class="border-b border-white/10 uppercase tracking-widest text-[#D4AF37] text-xs font-bold bg-white/5">
                        <th class="py-6 px-8 font-headline w-1/3">Feature</th>
                        <th class="py-6 px-8 font-headline text-white/50 w-1/3">Traditional</th>
                        <th class="py-6 px-8 font-headline bg-[#D4AF37]/10 text-white w-1/3 rounded-tr-[2rem]">GOLDe5</th>
                    </tr>
                </thead>
                <tbody class="text-sm">
                    <tr class="border-b border-white/5 hover:bg-white/[0.02] transition-colors">
                        <td class="py-5 px-8 text-gray-300 font-semibold">Investment Schedule</td>
                        <td class="py-5 px-8 text-white/50">Fixed</td>
                        <td class="py-5 px-8 font-bold text-[#D4AF37] bg-[#D4AF37]/5">Anytime</td>
                    </tr>
                    <tr class="border-b border-white/5 hover:bg-white/[0.02] transition-colors">
                        <td class="py-5 px-8 text-gray-300 font-semibold">Flexibility</td>
                        <td class="py-5 px-8 text-white/50">Limited</td>
                        <td class="py-5 px-8 font-bold text-[#D4AF37] bg-[#D4AF37]/5">Full</td>
                    </tr>
                    <tr class="border-b border-white/5 hover:bg-white/[0.02] transition-colors">
                        <td class="py-5 px-8 text-gray-300 font-semibold">Investment Amount</td>
                        <td class="py-5 px-8 text-white/50">Structured</td>
                        <td class="py-5 px-8 font-bold text-[#D4AF37] bg-[#D4AF37]/5">Any amount</td>
                    </tr>
                    <tr class="border-b border-white/5 hover:bg-white/[0.02] transition-colors">
                        <td class="py-5 px-8 text-gray-300 font-semibold">Asset Exposure</td>
                        <td class="py-5 px-8 text-white/50">Single</td>
                        <td class="py-5 px-8 font-bold text-[#D4AF37] bg-[#D4AF37]/5">Multi-metal</td>
                    </tr>
                    <tr class="border-b border-white/5 hover:bg-white/[0.02] transition-colors">
                        <td class="py-5 px-8 text-gray-300 font-semibold">Diversification</td>
                        <td class="py-5 px-8 text-white/50">Low</td>
                        <td class="py-5 px-8 font-bold text-[#D4AF37] bg-[#D4AF37]/5">High</td>
                    </tr>
                    <tr class="border-b border-white/5 hover:bg-white/[0.02] transition-colors">
                        <td class="py-5 px-8 text-gray-300 font-semibold">Control</td>
                        <td class="py-5 px-8 text-white/50">Limited</td>
                        <td class="py-5 px-8 font-bold text-[#D4AF37] bg-[#D4AF37]/5">Full</td>
                    </tr>
                    <tr class="border-b border-white/5 hover:bg-white/[0.02] transition-colors">
                        <td class="py-5 px-8 text-gray-300 font-semibold">Liquidity</td>
                        <td class="py-5 px-8 text-white/50">Restricted</td>
                        <td class="py-5 px-8 font-bold text-[#D4AF37] bg-[#D4AF37]/5">Flexible</td>
                    </tr>
                    <tr class="border-b border-white/5 hover:bg-white/[0.02] transition-colors">
                        <td class="py-5 px-8 text-gray-300 font-semibold">Management</td>
                        <td class="py-5 px-8 text-white/50">Basic</td>
                        <td class="py-5 px-8 font-bold text-[#D4AF37] bg-[#D4AF37]/5">Strategically managed</td>
                    </tr>
                    <tr class="border-b border-white/5 hover:bg-white/[0.02] transition-colors">
                        <td class="py-5 px-8 text-gray-300 font-semibold">Growth</td>
                        <td class="py-5 px-8 text-white/50">Linear</td>
                        <td class="py-5 px-8 font-bold text-[#D4AF37] bg-[#D4AF37]/5">Dynamic</td>
                    </tr>
                    <tr class="hover:bg-white/[0.02] transition-colors">
                        <td class="py-5 px-8 text-gray-300 font-semibold">Transparency</td>
                        <td class="py-5 px-8 text-white/50 pb-5">Limited</td>
                        <td class="py-5 px-8 font-bold text-[#D4AF37] bg-[#D4AF37]/5 rounded-br-[2rem]">Real-time tracking</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </section>

    <!-- Smart Metal Allocation Engine Section -->
    <section class="py-24 bg-[#111] border-y border-white/5 relative overflow-hidden animate-slide-up" style="animation-delay: 0.5s">
        <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-[#D4AF37]/10 via-transparent to-transparent opacity-50 blur-3xl pointer-events-none"></div>
        <div class="max-w-4xl mx-auto px-8 relative z-10 text-center space-y-10">
            <div class="space-y-4">
                <h2 class="text-4xl md:text-5xl font-extrabold font-headline tracking-tight text-white">Smart Metal Allocation Engine</h2>
                <p class="text-on-surface-variant/80 text-lg font-light leading-relaxed max-w-2xl mx-auto">
                    A proprietary algorithmic bridge allocating funds optimally across precious metals, adjusting to global market demands.
                </p>
            </div>
            
            <div class="flex justify-center items-center gap-6 md:gap-10 py-8 flex-wrap">
                <div class="flex flex-col items-center group">
                    <div class="w-16 h-16 rounded-full border border-white/10 bg-white/5 flex items-center justify-center text-[#D4AF37] group-hover:scale-110 transition-all shadow-lg">
                        <span class="material-symbols-outlined text-3xl">pentagon</span>
                    </div>
                </div>
                <div class="w-10 h-[1px] bg-white/20 hidden md:block"></div>
                <div class="flex flex-col items-center group">
                    <div class="w-16 h-16 rounded-full border border-white/10 bg-white/5 flex items-center justify-center text-white group-hover:scale-110 transition-all shadow-lg">
                        <span class="material-symbols-outlined text-3xl">circle</span>
                    </div>
                </div>
                <div class="w-10 h-[1px] bg-white/20 hidden md:block"></div>
                <div class="flex flex-col items-center group">
                    <div class="w-16 h-16 rounded-full border border-white/10 bg-white/5 flex items-center justify-center text-[#c7cbff] group-hover:scale-110 transition-all shadow-lg">
                        <span class="material-symbols-outlined text-3xl">hexagon</span>
                    </div>
                </div>
                <div class="w-10 h-[1px] bg-white/20 hidden md:block"></div>
                <div class="flex flex-col items-center group">
                    <div class="w-16 h-16 rounded-full border border-white/10 bg-white/5 flex items-center justify-center text-[#E6C65C] group-hover:scale-110 transition-all shadow-lg">
                        <span class="material-symbols-outlined text-3xl">factory</span>
                    </div>
                </div>
            </div>

            <div class="inline-block relative">
                <span class="material-symbols-outlined absolute -top-4 -left-6 text-[#D4AF37]/40 text-4xl rotate-180">format_quote</span>
                <h3 class="text-2xl md:text-3xl font-extrabold font-headline italic text-transparent bg-clip-text bullion-gradient">
                    "Not one metal.<br class="md:hidden"/> Smarter mix"
                </h3>
                <span class="material-symbols-outlined absolute -bottom-4 -right-6 text-[#D4AF37]/40 text-4xl">format_quote</span>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="max-w-4xl mx-auto px-8 py-32 text-center animate-slide-up" style="animation-delay: 0.6s">
        <h2 class="text-4xl md:text-6xl font-extrabold font-headline tracking-tight text-white mb-6">
            Start Investing <br/><span class="text-transparent bg-clip-text bullion-gradient">Without Limits</span>
        </h2>
        <p class="text-on-surface-variant/80 text-xl font-medium mb-12">
            No schedules. No pressure. Just smart growth.
        </p>
        <div class="flex flex-col sm:flex-row justify-center items-center gap-6">
            <button class="w-full sm:w-auto bullion-gradient text-[#111] px-10 py-4 rounded-xl font-headline font-extrabold text-sm md:text-base tracking-wide shadow-[0_0_20px_rgba(212,175,55,0.4)] hover:shadow-[0_0_30px_rgba(212,175,55,0.7)] hover:brightness-110 transition-all duration-300">
                Start Now
            </button>
            <button class="w-full sm:w-auto border-2 border-[#D4AF37]/30 text-[#D4AF37] px-10 py-4 rounded-xl font-headline font-extrabold text-sm md:text-base tracking-wide hover:bg-[#D4AF37]/10 transition-colors duration-300 flex items-center justify-center gap-2">
                <span class="material-symbols-outlined">download</span> Download App
            </button>
        </div>
    </section>
"""

file_path = "c:/Users/LENOVO/OneDrive/Desktop/Golde4/investor.html"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

hero_end_marker = "</section>\n<!-- Stats/Trust Bar Section -->"
footer_marker = "<!-- Footer -->"

if hero_end_marker in html and footer_marker in html:
    parts_1 = html.split(hero_end_marker)
    first_half = parts_1[0] + "</section>\n"
    
    parts_2 = parts_1[1].split(footer_marker)
    second_half = "\n" + footer_marker + parts_2[1]
    
    final_html = first_half + html_sections + second_half
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(final_html)
    print("Replacement success.")
else:
    print("Could not find markers to replace.")
