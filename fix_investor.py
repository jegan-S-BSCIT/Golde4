import io

def fix_investor_html():
    with io.open('investor.html', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_content = """<main class="flex-1 w-full bg-[#0B0B0B] overflow-x-hidden">
    <!-- SECTION 1: SMART GOLD PLANS -->
    <section class="max-w-7xl mx-auto px-6 md:px-8 py-20 animate-slide-up relative mt-10">
        <div class="flex flex-col md:flex-row gap-12 lg:gap-20 items-center">
            <!-- Left Info -->
            <div class="w-full md:w-1/2 space-y-6 shrink-0 relative z-10">
                <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#D4AF37]/10 border border-[#D4AF37]/20 w-max">
                    <span class="w-1.5 h-1.5 rounded-full bg-[#D4AF37] animate-pulse"></span>
                    <span class="text-[#D4AF37] text-[10px] font-bold tracking-widest uppercase">Coming Soon</span>
                </div>
                
                <h1 class="text-4xl md:text-5xl lg:text-7xl font-extrabold font-headline leading-[1.05] tracking-tight text-white mb-2 drop-shadow-md">
                    SMART GOLD <br/> <span class="text-transparent bg-clip-text bullion-gradient">PLANS</span>
                </h1>
                
                <p class="text-[#bbb] text-lg font-light leading-relaxed max-w-lg mb-6">
                    A smarter way to build your gold reserves. Commit to a structured plan and let discipline pay off magically.
                </p>
                
                <p class="text-xl font-medium text-white border-l-4 border-[#D4AF37] pl-4 py-1 italic shadow-sm">
                    "Pay for 9 months. <span class="text-[#D4AF37]">The 10th month is our golden bonus.</span>"
                </p>
                
                <p class="text-[#bbb] text-sm mt-8 opacity-80">
                    Smarter gold savings on the way. Focus your investments and unlock guaranteed multipliers.
                </p>
            </div>
            
            <!-- Right Image Area -->
            <div class="w-full md:w-1/2 relative h-[400px] md:h-[500px] flex items-center justify-end rounded-3xl overflow-hidden glass-card group">
                <img src="https://lh3.googleusercontent.com/aida-public/AB6AXuBZSmlN1AQgBOZL3N-ju7q3N7tLeRfWeCcMk1J1JLqeBPcwvazMBBR9Zi92ciyDxluw81xTCS_T-LG4H9JHq606Fj1IZj7NFgGrBXp_4mWJ6g0CGeXcS-sKLjIpyKoCtE4i7hlGAhSMUMB2qWtafPUZ8SLRvBpTz2zGhgasQEzfjEoH0CgsEyTKTZ_3PkVEQFxbz6RLS4AMPd6hTNpjzTImiMEW2fM4sICEj2M3J5bbiu0RSVj0rePew42u_art9hyx6kPPMvEac8ec" alt="Smart Gold Plans Visual" class="w-full h-full object-cover scale-105 group-hover:scale-100 transition-transform duration-[2s] mix-blend-screen opacity-90"/>
                <div class="absolute inset-0 bg-gradient-to-r from-[#0B0B0B] via-[#0B0B0B]/30 to-transparent pointer-events-none"></div>
                <div class="absolute inset-0 border border-white/5 rounded-3xl"></div>
            </div>
        </div>
    </section>

    <!-- SECTION 2: INVEST YOUR WAY -->
    <section class="max-w-7xl mx-auto px-6 md:px-8 py-20 flex flex-col md:flex-row items-center gap-12 lg:gap-20 animate-slide-up relative">
        <!-- Left Info -->
        <div class="w-full md:w-1/2 space-y-8 z-10 md:pr-10">
            <div class="space-y-4">
                <h2 class="text-4xl md:text-5xl lg:text-6xl font-extrabold font-headline leading-[1.05] tracking-tight text-white drop-shadow-sm">
                    Invest Your Way <br/>
                    <span class="text-[#D4AF37]">Grow with Metals</span>
                </h2>
            </div>
            
            <p class="text-[#bbb] text-base md:text-lg leading-relaxed max-w-lg">
                Your portfolio should adapt to your life, not the other way around. Experience complete freedom in how and when you save.
            </p>
            
            <ul class="space-y-4 text-white font-medium grid grid-cols-1 sm:grid-cols-2 gap-4">
                <li class="flex items-center gap-4 hover:translate-x-1 transition-transform bg-[#111] p-4 rounded-xl border border-white/5">
                    <span class="material-symbols-outlined text-[#D4AF37]">check_circle</span> Invest Anytime
                </li>
                <li class="flex items-center gap-4 hover:translate-x-1 transition-transform bg-[#111] p-4 rounded-xl border border-white/5">
                    <span class="material-symbols-outlined text-[#D4AF37]">check_circle</span> Any Amount
                </li>
                <li class="flex items-center gap-4 hover:translate-x-1 transition-transform bg-[#111] p-4 rounded-xl border border-white/5">
                    <span class="material-symbols-outlined text-[#D4AF37]">check_circle</span> No Limits
                </li>
                <li class="flex items-center gap-4 hover:translate-x-1 transition-transform bg-[#111] p-4 rounded-xl border border-white/5">
                    <span class="material-symbols-outlined text-[#D4AF37]">check_circle</span> No Schedule
                </li>
            </ul>
            
            <button class="bullion-gradient text-[#111] px-8 py-3.5 rounded-xl font-headline font-extrabold text-sm tracking-wide shadow-[0_0_15px_rgba(212,175,55,0.3)] hover:shadow-[0_0_25px_rgba(212,175,55,0.6)] hover:brightness-110 active:scale-95 transition-all mt-4 w-full sm:w-auto">
                Let's Get Started
            </button>
        </div>
        
        <!-- Right Image -->
        <div class="w-full md:w-1/2 relative h-[450px] md:h-[550px] rounded-[2.5rem] overflow-hidden group shadow-[-20px_0_60px_rgba(0,0,0,0.8)]">
            <div class="absolute inset-0 bg-[#D4AF37]/5 animate-pulse"></div>
            <img class="w-full h-full object-cover scale-105 group-hover:scale-100 transition-transform duration-700 opacity-80 mix-blend-screen object-center" src="https://lh3.googleusercontent.com/aida-public/AB6AXuC_E2gAQ5ybNqnEbwXwcj_ZzRyxSpL7KdN7JYAvMUNBh5Q95Ft5F-0I98FvAwPCLg-O2DfkSJa8zw3aCxammEAHccRArHcR77viUG_EaOLS5vSZZXahZIlo90mgOegO0PbxCAil4MOBuWF4kDWHN78i4E2J1hbhs9A8affQsXsLEOAWfu2vIm7Re_6_upLGXlIAymuy6JL6bKHqOoPCfHB6eJ3ZRHoFTq9hAH1lrJ-AIBSsCn6tDQbSjpTK0y_9d7POwvf3-wibRSZM" alt="Digital Gold Interface"/>
            <div class="absolute inset-0 bg-gradient-to-t from-[#0B0B0B] via-transparent to-transparent opacity-90 pointer-events-none"></div>
            <div class="absolute inset-0 border border-white/10 rounded-[2.5rem] mix-blend-overlay"></div>
        </div>
    </section>

    <!-- SECTION 3: FLEXIBLE INVESTOR -->
    <section class="max-w-7xl mx-auto px-6 md:px-8 py-20 animate-slide-up relative bg-[#111]/40 rounded-[2rem] border border-[#222] my-10 shadow-[0_10px_40px_rgba(0,0,0,0.5)]">
        <div class="absolute -top-32 -right-32 w-64 h-64 bg-[#D4AF37]/5 rounded-full blur-[80px] pointer-events-none"></div>
        
        <div class="text-center mb-16 space-y-4">
            <span class="text-[#D4AF37] font-bold tracking-[0.3em] uppercase text-[10px]">Investment Options</span>
            <h2 class="text-4xl md:text-5xl font-extrabold font-headline tracking-tight text-white mb-2">Flexible Investor</h2>
            <p class="text-[#bbb] leading-relaxed max-w-2xl mx-auto text-base md:text-lg">
                Build a resilient portfolio that bends, not breaks. Invest at your own pace without rigid requirements while gaining exposure across critical metal sectors.
            </p>
        </div>
        
        <!-- Asset Chips / Cards Grid -->
        <div class="grid grid-cols-2 lg:grid-cols-4 gap-6 mb-16">
            <div class="glass-card hover:-translate-y-2 transition-all border border-[#222] rounded-[1.5rem] p-8 text-center space-y-5 bg-[#0a0a0a] group">
                <div class="w-16 h-16 mx-auto rounded-full bg-[#D4AF37]/10 flex items-center justify-center text-[#D4AF37] group-hover:bg-[#D4AF37]/20 transition-colors shadow-[0_0_15px_rgba(212,175,55,0.1)]">
                    <span class="material-symbols-outlined text-3xl">pentagon</span>
                </div>
                <h3 class="text-white font-bold tracking-wide text-lg group-hover:text-[#D4AF37] transition-colors">Gold</h3>
            </div>
            
            <div class="glass-card hover:-translate-y-2 transition-all border border-[#222] rounded-[1.5rem] p-8 text-center space-y-5 bg-[#0a0a0a] group">
                <div class="w-16 h-16 mx-auto rounded-full bg-white/5 flex items-center justify-center text-white group-hover:bg-white/10 transition-colors shadow-[0_0_15px_rgba(255,255,255,0.1)]">
                    <span class="material-symbols-outlined text-3xl">circle</span>
                </div>
                <h3 class="text-white font-bold tracking-wide text-lg group-hover:text-gray-300 transition-colors">Silver</h3>
            </div>
            
            <div class="glass-card hover:-translate-y-2 transition-all border border-[#222] rounded-[1.5rem] p-8 text-center space-y-5 bg-[#0a0a0a] group">
                <div class="w-16 h-16 mx-auto rounded-full bg-[#D4AF37]/10 flex items-center justify-center text-[#D4AF37] group-hover:bg-[#D4AF37]/20 transition-colors shadow-[0_0_15px_rgba(212,175,55,0.1)]">
                    <span class="material-symbols-outlined text-3xl">hexagon</span>
                </div>
                <h3 class="text-white font-bold tracking-wide text-base group-hover:text-[#D4AF37] transition-colors">Platinum & Palladium</h3>
            </div>
            
            <div class="glass-card hover:-translate-y-2 transition-all border border-[#222] rounded-[1.5rem] p-8 text-center space-y-5 bg-[#0a0a0a] group">
                <div class="w-16 h-16 mx-auto rounded-full bg-[#D4AF37]/10 flex items-center justify-center text-[#D4AF37] group-hover:bg-[#D4AF37]/20 transition-colors shadow-[0_0_15px_rgba(212,175,55,0.1)]">
                    <span class="material-symbols-outlined text-3xl">factory</span>
                </div>
                <h3 class="text-white font-bold tracking-wide text-base group-hover:text-[#D4AF37] transition-colors">Metal Industries</h3>
            </div>
        </div>
        
        <div class="text-center pb-2">
            <button class="bg-transparent border border-[#D4AF37]/30 text-[#D4AF37] px-8 py-3 rounded-xl font-headline font-semibold text-sm hover:bg-[#D4AF37]/10 hover:border-[#D4AF37]/50 transition-all flex items-center justify-center mx-auto gap-2">
                <span>How it works?</span>
                <span class="material-symbols-outlined text-[18px]">expand_more</span>
            </button>
        </div>
    </section>

    <!-- SECTION 4: COMPARISON TABLE -->
    <section class="max-w-5xl mx-auto px-6 md:px-8 py-24 animate-slide-up text-center border-y border-[#222] mt-10">
        <h2 class="text-3xl md:text-5xl font-extrabold font-headline tracking-tight text-white mb-16">
            Traditional vs <span class="text-[#D4AF37]">GOLDe5 Investor</span>
        </h2>
        
        <div class="glass-card rounded-[2rem] overflow-x-auto shadow-[0_10px_40px_rgba(0,0,0,0.8)] border border-[#222]">
            <table class="w-full text-left border-collapse min-w-[700px]">
                <thead>
                    <tr class="border-b border-[#333] text-xs font-bold uppercase tracking-widest text-white/40 bg-[#111]">
                        <th class="py-6 px-8 font-headline w-1/3 text-left">Feature</th>
                        <th class="py-6 px-8 font-headline w-1/3 text-center">Traditional</th>
                        <th class="py-6 px-8 font-headline w-1/3 text-center bg-[#D4AF37]/10 text-[#D4AF37] rounded-tr-[2rem]">GOLDe5</th>
                    </tr>
                </thead>
                <tbody class="text-sm">
                    <tr class="border-b border-[#222] hover:bg-white/[0.02] transition-colors">
                        <td class="py-5 px-8 text-white font-medium">Investment Schedule</td>
                        <td class="py-5 px-8 text-[#bbb] text-center">Fixed</td>
                        <td class="py-5 px-8 text-[#D4AF37] font-bold text-center bg-[#D4AF37]/5">Anytime</td>
                    </tr>
                    <tr class="border-b border-[#222] hover:bg-white/[0.02] transition-colors">
                        <td class="py-5 px-8 text-white font-medium">Flexibility</td>
                        <td class="py-5 px-8 text-[#bbb] text-center">Limited</td>
                        <td class="py-5 px-8 text-[#D4AF37] font-bold text-center bg-[#D4AF37]/5">Full</td>
                    </tr>
                    <tr class="border-b border-[#222] hover:bg-white/[0.02] transition-colors">
                        <td class="py-5 px-8 text-white font-medium">Investment Amount</td>
                        <td class="py-5 px-8 text-[#bbb] text-center">Structured</td>
                        <td class="py-5 px-8 text-[#D4AF37] font-bold text-center bg-[#D4AF37]/5">Any amount</td>
                    </tr>
                    <tr class="border-b border-[#222] hover:bg-white/[0.02] transition-colors">
                        <td class="py-5 px-8 text-white font-medium">Asset Exposure</td>
                        <td class="py-5 px-8 text-[#bbb] text-center">Single</td>
                        <td class="py-5 px-8 text-[#D4AF37] font-bold text-center bg-[#D4AF37]/5">Multi-metal</td>
                    </tr>
                    <tr class="border-b border-[#222] hover:bg-white/[0.02] transition-colors">
                        <td class="py-5 px-8 text-white font-medium">Diversification</td>
                        <td class="py-5 px-8 text-[#bbb] text-center">Low</td>
                        <td class="py-5 px-8 text-[#D4AF37] font-bold text-center bg-[#D4AF37]/5">High</td>
                    </tr>
                    <tr class="border-b border-[#222] hover:bg-white/[0.02] transition-colors">
                        <td class="py-5 px-8 text-white font-medium">Control</td>
                        <td class="py-5 px-8 text-[#bbb] text-center">Limited</td>
                        <td class="py-5 px-8 text-[#D4AF37] font-bold text-center bg-[#D4AF37]/5">Full</td>
                    </tr>
                    <tr class="border-b border-[#222] hover:bg-white/[0.02] transition-colors">
                        <td class="py-5 px-8 text-white font-medium">Liquidity</td>
                        <td class="py-5 px-8 text-[#bbb] text-center">Restricted</td>
                        <td class="py-5 px-8 text-[#D4AF37] font-bold text-center bg-[#D4AF37]/5">Flexible</td>
                    </tr>
                    <tr class="hover:bg-[#111] transition-colors">
                        <td class="py-5 px-8 text-white font-medium rounded-bl-[2rem]">Management</td>
                        <td class="py-5 px-8 text-[#bbb] text-center">Basic</td>
                        <td class="py-5 px-8 text-[#D4AF37] font-bold text-center bg-[#D4AF37]/5 rounded-br-[2rem]">Strategically Managed</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </section>

    <!-- SECTION 5: SMART METAL ALLOCATION ENGINE -->
    <section class="max-w-7xl mx-auto px-6 md:px-8 py-24 flex flex-col-reverse md:flex-row items-center gap-12 lg:gap-20 animate-slide-up relative">
        <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-[#D4AF37]/5 via-transparent to-transparent opacity-80 blur-3xl pointer-events-none"></div>
        
        <!-- Left Visual Content -->
        <div class="w-full md:w-1/2 py-8 relative flex flex-col justify-center items-center md:items-start">
            <div class="flex flex-col gap-6 w-full max-w-sm">
                <div class="glass-card border border-[#D4AF37]/30 bg-[#111] p-6 rounded-2xl flex items-center gap-5 hover:-translate-y-1 transition-transform z-20 shadow-[0_15px_30px_rgba(0,0,0,0.6)] ml-0 md:ml-8">
                    <div class="w-12 h-12 bg-[#D4AF37]/10 flex items-center justify-center rounded-full text-[#D4AF37] shrink-0">
                        <span class="material-symbols-outlined text-2xl">insert_chart</span>
                    </div>
                    <div>
                        <h4 class="text-white font-bold font-headline">Predictive Balancing</h4>
                        <p class="text-[#bbb] text-xs mt-1">Adapting to global markets automatically.</p>
                    </div>
                </div>
                <div class="glass-card border border-[#222] bg-[#111] p-6 rounded-2xl flex items-center gap-5 hover:-translate-y-1 transition-transform z-10 mr-0 md:mr-8">
                    <div class="w-12 h-12 bg-white/5 flex items-center justify-center rounded-full text-white shrink-0">
                        <span class="material-symbols-outlined text-2xl">layers</span>
                    </div>
                    <div>
                        <h4 class="text-white font-bold font-headline">Multi-Metal Spread</h4>
                        <p class="text-[#bbb] text-xs mt-1">Gold, Silver, & Platinum fusion.</p>
                    </div>
                </div>
            </div>
            
            <div class="inline-block relative mt-16 md:ml-12 text-center md:text-left">
                <span class="material-symbols-outlined absolute -top-5 -left-8 text-[#D4AF37]/20 text-5xl rotate-180 select-none">format_quote</span>
                <h3 class="text-3xl font-extrabold font-headline italic text-white z-10 relative leading-tight">
                    Not one metal.<br/>
                    <span class="text-transparent bg-clip-text bullion-gradient">Smarter mix.</span>
                </h3>
                <span class="material-symbols-outlined absolute -bottom-4 -right-8 text-[#D4AF37]/20 text-5xl select-none">format_quote</span>
            </div>
        </div>

        <!-- Right Info Content -->
        <div class="w-full md:w-1/2 space-y-8 z-10">
            <h2 class="text-4xl md:text-5xl lg:text-6xl font-extrabold font-headline tracking-tight text-white drop-shadow-md leading-[1.05]">
                Smart Metal <br/>
                Allocation Engine
            </h2>
            
            <p class="text-[#bbb] text-base md:text-lg leading-relaxed">
                A proprietary algorithmic bridge allocating funds optimally across precious metals. Automatically adjusting to global market demands to maximize stability.
            </p>
            
            <ul class="space-y-6 pt-2">
                <li class="flex items-start gap-5 bg-[#111] p-5 rounded-2xl border border-white/5">
                    <div class="mt-1 w-8 h-8 rounded-full bg-[#D4AF37]/10 flex items-center justify-center shrink-0 border border-[#D4AF37]/30">
                        <span class="material-symbols-outlined text-[#D4AF37] text-sm">shield</span>
                    </div>
                    <div>
                        <h4 class="text-white font-bold tracking-wide text-[15px]">Risk reduction</h4>
                        <p class="text-[#bbb] text-sm mt-1.5">Hedge inflation with automated diversification across assets.</p>
                    </div>
                </li>
                <li class="flex items-start gap-5 bg-[#111] p-5 rounded-2xl border border-white/5">
                    <div class="mt-1 w-8 h-8 rounded-full bg-[#D4AF37]/10 flex items-center justify-center shrink-0 border border-[#D4AF37]/30">
                        <span class="material-symbols-outlined text-[#D4AF37] text-sm">trending_up</span>
                    </div>
                    <div>
                        <h4 class="text-white font-bold tracking-wide text-[15px]">Better growth opportunities</h4>
                        <p class="text-[#bbb] text-sm mt-1.5">Capitalize on real-time multi-asset shifts in the market.</p>
                    </div>
                </li>
                <li class="flex items-start gap-5 bg-[#111] p-5 rounded-2xl border border-white/5">
                    <div class="mt-1 w-8 h-8 rounded-full bg-[#D4AF37]/10 flex items-center justify-center shrink-0 border border-[#D4AF37]/30">
                        <span class="material-symbols-outlined text-[#D4AF37] text-sm">pie_chart</span>
                    </div>
                    <div>
                        <h4 class="text-white font-bold tracking-wide text-[15px]">Diversified allocation</h4>
                        <p class="text-[#bbb] text-sm mt-1.5">Your capital optimally split automatically across strategic metals.</p>
                    </div>
                </li>
            </ul>
        </div>
    </section>
</main>

<footer class="bg-[#0B0B0B] border-t border-[#D4AF37]/10 pt-24 pb-12 mt-auto relative overflow-hidden">
    <div class="absolute top-0 left-1/2 -translate-x-1/2 w-[800px] h-[400px] bg-[#D4AF37]/5 blur-[150px] pointer-events-none z-0"></div>
    <div class="max-w-7xl mx-auto px-6 md:px-8 relative z-10 space-y-16">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 lg:gap-8">
            <div class="lg:col-span-1 space-y-8 ux-reveal">
                <div>
                    <a href="index.html" class="inline-block group focus:outline-none">
                        <h2 class="text-3xl font-black text-[#D4AF37] font-headline tracking-tighter group-hover:drop-shadow-[0_0_15px_rgba(212,175,55,0.6)] transition-all duration-300">GOLDe5</h2>
                        <p class="text-[#d0c5af] text-[9px] font-medium tracking-[0.3em] font-body uppercase leading-tight mt-1 group-hover:text-white transition-colors duration-300">Grow in Grams</p>
                    </a>
                    <p class="text-gray-400 text-sm leading-relaxed mt-6">
                        The pinnacle of private metal banking. Secure, liquid, and globally accessible.
                    </p>
                </div>
                <div class="flex flex-wrap gap-3">
                    <a href="#" class="w-10 h-10 rounded-full bg-white/5 border border-white/5 flex items-center justify-center text-[#D4AF37] hover:bg-[#D4AF37] hover:text-[#0B0B0B] hover:shadow-[0_0_20px_rgba(212,175,55,0.5)] hover:scale-110 transition-all duration-300">
                        <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M22 12c0-5.52-4.48-10-10-10S2 6.48 2 12c0 4.84 3.44 8.87 8 9.8V15H8v-3h2V9.5c0-2.03 1.23-3.14 3.06-3.14.87 0 1.62.06 1.84.09v2.1l-1.26.01c-.99 0-1.18.47-1.18 1.16V12h2.46l-.32 3h-2.14v6.8C18.56 20.87 22 16.84 22 12z"/></svg>
                    </a>
                    <a href="#" class="w-10 h-10 rounded-full bg-white/5 border border-white/5 flex items-center justify-center text-[#D4AF37] hover:bg-[#D4AF37] hover:text-[#0B0B0B] hover:shadow-[0_0_20px_rgba(212,175,55,0.5)] hover:scale-110 transition-all duration-300">
                        <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M7.8 2h8.4C19.4 2 22 4.6 22 7.8v8.4a5.8 5.8 0 0 1-5.8 5.8H7.8C4.6 22 2 19.4 2 16.2V7.8A5.8 5.8 0 0 1 7.8 2zm-.2 2A3.6 3.6 0 0 0 4 7.6v8.8C4 18.4 5.6 20 7.6 20h8.8a3.6 3.6 0 0 0 3.6-3.6V7.6C20 5.6 18.4 4 16.4 4H7.6zm9.65 1.5a1.25 1.25 0 0 1 0 2.5 1.25 1.25 0 0 1 0-2.5zM12 7a5 5 0 1 1 0 10 5 5 0 0 1 0-10zm0 2a3 3 0 1 0 0 6 3 3 0 0 0 0-6z"/></svg>
                    </a>
                    <a href="#" class="w-10 h-10 rounded-full bg-white/5 border border-white/5 flex items-center justify-center text-[#D4AF37] hover:bg-[#D4AF37] hover:text-[#0B0B0B] hover:shadow-[0_0_20px_rgba(212,175,55,0.5)] hover:scale-110 transition-all duration-300">
                        <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
                    </a>
                    <a href="#" class="w-10 h-10 rounded-full bg-white/5 border border-white/5 flex items-center justify-center text-[#D4AF37] hover:bg-[#D4AF37] hover:text-[#0B0B0B] hover:shadow-[0_0_20px_rgba(212,175,55,0.5)] hover:scale-110 transition-all duration-300">
                        <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M21.582 6.186a2.665 2.665 0 0 0-1.876-1.884C18.04 3.864 12 3.864 12 3.864s-6.04 0-7.706.438a2.665 2.665 0 0 0-1.876 1.884C2 7.86 2 12 2 12s0 4.14.418 5.814a2.665 2.665 0 0 0 1.876 1.884c1.667.438 7.706.438 7.706.438s6.04 0 7.706-.438a2.665 2.665 0 0 0 1.876-1.884C22 16.14 22 12 22 12s0-4.14-.418-5.814zM9.99 15.422v-6.85l6.02 3.426-6.02 3.424z"/></svg>
                    </a>
                    <a href="#" class="w-10 h-10 rounded-full bg-white/5 border border-white/5 flex items-center justify-center text-[#D4AF37] hover:bg-[#D4AF37] hover:text-[#0B0B0B] hover:shadow-[0_0_20px_rgba(212,175,55,0.5)] hover:scale-110 transition-all duration-300">
                        <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.924 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
                    </a>
                </div>
            </div>
            
            <div class="lg:col-span-1 space-y-6 ux-reveal" style="animation-delay: 0.1s;">
                <h5 class="text-[#D4AF37] font-bold font-headline uppercase text-[11px] tracking-[0.2em] relative inline-block">Company<div class="absolute -bottom-2 left-0 w-8 h-px bg-[#D4AF37]"></div></h5>
                <ul class="space-y-4 text-sm text-[#777] font-medium transition-colors">
                    <li><a class="hover:text-[#D4AF37] hover:translate-x-1 inline-block transition-all duration-300" href="#">About Us</a></li>
                    <li><a class="hover:text-[#D4AF37] hover:translate-x-1 inline-block transition-all duration-300" href="#">FAQ</a></li>
                    <li><a class="hover:text-[#D4AF37] hover:translate-x-1 inline-block transition-all duration-300" href="#">Contact Us</a></li>
                    <li><a class="hover:text-[#D4AF37] hover:translate-x-1 inline-block transition-all duration-300" href="#">Careers</a></li>
                </ul>
            </div>
            
            <div class="lg:col-span-1 space-y-6 ux-reveal" style="animation-delay: 0.2s;">
                <h5 class="text-[#D4AF37] font-bold font-headline uppercase text-[11px] tracking-[0.2em] relative inline-block">Explore<div class="absolute -bottom-2 left-0 w-8 h-px bg-[#D4AF37]"></div></h5>
                <ul class="space-y-4 text-sm text-[#777] font-medium transition-colors">
                    <li><a class="hover:text-[#D4AF37] hover:translate-x-1 inline-block transition-all duration-300" href="gold-sip.html">SIP</a></li>
                    <li><a class="hover:text-[#D4AF37] hover:translate-x-1 inline-block transition-all duration-300" href="coins-bars.html">Shop</a></li>
                    <li><a class="hover:text-[#D4AF37] hover:translate-x-1 inline-block transition-all duration-300" href="#">Marketplace</a></li>
                </ul>
            </div>
            
            <div class="lg:col-span-1 space-y-6 ux-reveal" style="animation-delay: 0.3s;">
                <h5 class="text-[#D4AF37] font-bold font-headline uppercase text-[11px] tracking-[0.2em] relative inline-block">Resources<div class="absolute -bottom-2 left-0 w-8 h-px bg-[#D4AF37]"></div></h5>
                <ul class="space-y-4 text-sm text-[#777] font-medium transition-colors">
                    <li><a class="hover:text-[#D4AF37] hover:translate-x-1 inline-block transition-all duration-300" href="investor.html">Investors & Partners</a></li>
                    <li><a class="hover:text-[#D4AF37] hover:translate-x-1 inline-block transition-all duration-300" href="terms.html">Terms & Conditions</a></li>
                    <li><a class="hover:text-[#D4AF37] hover:translate-x-1 inline-block transition-all duration-300" href="terms.html">Privacy Policy</a></li>
                    <li><a class="hover:text-[#D4AF37] hover:translate-x-1 inline-block transition-all duration-300" href="terms.html">Cyber Advisory</a></li>
                </ul>
            </div>
        </div>
        
        <div class="pt-8 mt-12 border-t border-white/10 flex flex-col md:flex-row justify-between items-center gap-6 ux-reveal">
            <p class="text-gray-400 text-xs font-semibold tracking-wider uppercase">
                © 2026 GOLDe5. All rights reserved.
            </p>
            <div class="flex items-center gap-3 px-4 py-2 bg-white/5 border border-white/5 rounded-full cursor-default hover:bg-white/10 transition-colors">
                <span class="w-2 h-2 rounded-full bg-green-500 shadow-[0_0_8px_#22c55e] animate-pulse"></span>
                <span class="text-[10px] font-black text-gray-300 tracking-widest uppercase">Network Status: Operational</span>
            </div>
        </div>
        <div class="pt-4 text-center pb-8 ux-reveal">
            <p class="text-gray-500 text-[10px] sm:text-xs font-medium max-w-4xl mx-auto leading-relaxed border-t border-white/5 pt-6">
                Investments are subject to market risks. Returns are not guaranteed and may vary. Please read all related documents carefully before investing.
            </p>
        </div>
    </div>
</footer>
"""
    lines = lines[:247] + [new_content + "\n"] + lines[628:]

    with io.open('investor.html', 'w', encoding='utf-8') as f:
        f.writelines(lines)

if __name__ == '__main__':
    fix_investor_html()
