import re

# Read index.html to extract common layout
with open('c:/Users/LENOVO/OneDrive/Desktop/Golde4/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract header and footer from index.html
nav_match = re.search(r'    <!-- Top Navigation Bar -->.*?    <main', text, re.DOTALL)
header_str = nav_match.group(0).replace('    <main', '')

footer_match = re.search(r'    <!-- Partner / Trust Logos Banner -->.*?    <script>', text, re.DOTALL)
footer_str = footer_match.group(0).replace('    <script>', '')

head_styles = """<!DOCTYPE html>
<html lang="en" class="dark scroll-smooth">
<head>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>{title} | GOLDe5</title>
    <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
    <script>
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    colors: {
                        black: "#0B0B0B",
                        gold: "#D4AF37",
                        "gold-glow": "rgba(212, 175, 55, 0.15)",
                    },
                    fontFamily: {
                        headline: ["Manrope", "sans-serif"],
                        body: ["Inter", "sans-serif"],
                    }
                }
            }
        }
    </script>
    <style>
        .material-symbols-outlined { font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24; }
        .glass-card {
            background: rgba(11, 11, 11, 0.6);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(212, 175, 55, 0.1);
            transition: all 0.4s ease;
        }
        .glass-card:hover {
            border-color: rgba(212, 175, 55, 0.4);
            box-shadow: 0 10px 40px rgba(212, 175, 55, 0.1);
            transform: translateY(-5px);
        }
        .gold-gradient { background: linear-gradient(135deg, #DFBD69, #926F34); }
        .gold-text-gradient {
            background: linear-gradient(135deg, #DFBD69, #D4AF37);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .ux-reveal { opacity: 0; transform: translateY(30px); transition: all 0.8s cubic-bezier(0.2, 0.8, 0.2, 1); }
        .ux-reveal.visible { opacity: 1; transform: translateY(0); }
        
        /* Contact Form specific styles */
        .form-input {
            width: 100%;
            background: rgba(255,255,255,0.02);
            border: 1px solid rgba(212,175,55,0.2);
            border-radius: 0.5rem;
            padding: 0.75rem 1rem;
            color: #fff;
            transition: all 0.3s ease;
        }
        .form-input:focus {
            outline: none;
            border-color: #D4AF37;
            box-shadow: 0 0 15px rgba(212,175,55,0.2);
            background: rgba(255,255,255,0.05);
        }
    </style>
</head>
<body class="bg-[#0B0B0B] text-white font-body selection:bg-gold/30 selection:text-gold overflow-x-hidden flex flex-col min-h-[100vh]">
"""

page_common_end = """
    <!-- INTERACTION SCRIPTS -->
    <script>
        // Scroll Animation Observer for fading in elements
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                }
            });
        }, { threshold: 0.1, rootMargin: "0px 0px -50px 0px" });

        document.querySelectorAll('.ux-reveal').forEach(el => observer.observe(el));
        
        // Mobile Menu Logic (If applicable from index)
        const mobileMenuToggle = document.querySelector('button[onclick*="mobile-menu"]');
        if (mobileMenuToggle && typeof mobileMenuToggle.onclick !== 'function') {
           // It relies on index.html's inline onclick, which works if elements are present.
        }
    </script>
</body>
</html>
"""

def generate_file(filename, title, content):
    final_html = head_styles.replace('{title}', title) + header_str + '    <main class="flex-1 w-full relative pt-40 pb-20">\n' + content + '\n    </main>\n' + footer_str + page_common_end
    with open(f'c:/Users/LENOVO/OneDrive/Desktop/Golde4/{filename}', 'w', encoding='utf-8') as f:
        f.write(final_html)
    print(f"Generated {filename}")

contact_content = """
        <!-- HERO SECTION -->
        <header class="relative text-center overflow-hidden mb-16">
            <div class="absolute inset-0 bg-[#0B0B0B] z-0">
                <div class="absolute top-[30%] left-[50%] -translate-x-1/2 w-[500px] h-[500px] bg-gold/5 rounded-full blur-[120px] pointer-events-none"></div>
            </div>
            <div class="relative z-10 max-w-3xl mx-auto px-6 ux-reveal">
                <h1 class="text-5xl md:text-6xl font-black font-headline tracking-tighter mb-4">
                    Contact <span class="gold-text-gradient">Us</span>
                </h1>
                <p class="text-xl text-gray-400 font-medium">
                    We're here to help you with your gold investment journey.
                </p>
            </div>
        </header>

        <!-- CONTACT SECTION -->
        <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 lg:grid-cols-3 gap-12 relative z-10">
            <!-- Left: Form -->
            <div class="lg:col-span-2 glass-card rounded-[1.5rem] p-8 md:p-10 ux-reveal" style="animation-delay: 0.1s;">
                <h2 class="text-2xl font-bold font-headline mb-8 text-gold">Send us a Message</h2>
                <form class="space-y-6">
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div class="space-y-2">
                            <label class="text-xs font-bold uppercase tracking-wider text-gray-400">Full Name</label>
                            <input type="text" class="form-input" placeholder="John Doe">
                        </div>
                        <div class="space-y-2">
                            <label class="text-xs font-bold uppercase tracking-wider text-gray-400">Email Address</label>
                            <input type="email" class="form-input" placeholder="john@example.com">
                        </div>
                    </div>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div class="space-y-2">
                            <label class="text-xs font-bold uppercase tracking-wider text-gray-400">Mobile Number</label>
                            <input type="tel" class="form-input" placeholder="+1 234 567 8900">
                        </div>
                        <div class="space-y-2">
                            <label class="text-xs font-bold uppercase tracking-wider text-gray-400">Subject</label>
                            <select class="form-input appearance-none bg-[#0e0e0e]">
                                <option>General Inquiry</option>
                                <option>Investment Assistance</option>
                                <option>Account Support</option>
                                <option>Partnership</option>
                            </select>
                        </div>
                    </div>
                    <div class="space-y-2">
                        <label class="text-xs font-bold uppercase tracking-wider text-gray-400">Message</label>
                        <textarea class="form-input min-h-[150px] resize-none" placeholder="How can we help you?"></textarea>
                    </div>
                    <button type="button" class="gold-gradient text-[#111] px-10 py-4 rounded-xl font-bold font-headline uppercase tracking-widest shadow-[0_0_20px_rgba(212,175,55,0.4)] hover:shadow-[0_0_35px_rgba(212,175,55,0.8)] hover:-translate-y-1 transition-all active:scale-95 w-full md:w-auto">
                        Send Message
                    </button>
                </form>
            </div>

            <!-- Right: Info -->
            <div class="space-y-6 ux-reveal" style="animation-delay: 0.2s;">
                <div class="glass-card rounded-[1.5rem] p-8 flex items-start gap-4">
                    <div class="w-12 h-12 rounded-full border border-gold/30 bg-gold/10 flex items-center justify-center text-gold shrink-0">
                        <span class="material-symbols-outlined">mail</span>
                    </div>
                    <div>
                        <h3 class="text-lg font-bold font-headline text-white mb-1">Email Support</h3>
                        <p class="text-gray-400 text-sm">support@golde5.com</p>
                        <p class="text-gray-400 text-sm">partners@golde5.com</p>
                    </div>
                </div>
                
                <div class="glass-card rounded-[1.5rem] p-8 flex items-start gap-4">
                    <div class="w-12 h-12 rounded-full border border-gold/30 bg-gold/10 flex items-center justify-center text-gold shrink-0">
                        <span class="material-symbols-outlined">call</span>
                    </div>
                    <div>
                        <h3 class="text-lg font-bold font-headline text-white mb-1">Phone Support</h3>
                        <p class="text-gray-400 text-sm">+1 800 555 0199</p>
                        <p class="text-gray-500 text-xs mt-2 uppercase tracking-wider">Mon–Sat: 9 AM – 6 PM</p>
                    </div>
                </div>
                
                <div class="glass-card rounded-[1.5rem] p-8 flex items-start gap-4">
                    <div class="w-12 h-12 rounded-full border border-gold/30 bg-gold/10 flex items-center justify-center text-gold shrink-0">
                        <span class="material-symbols-outlined">location_on</span>
                    </div>
                    <div>
                        <h3 class="text-lg font-bold font-headline text-white mb-1">Office Address</h3>
                        <p class="text-gray-400 text-sm leading-relaxed">
                            123 Wealth Avenue,<br/>Financial District,<br/>New York, NY 10004
                        </p>
                    </div>
                </div>
                
                <!-- Map Placeholder -->
                <div class="glass-card rounded-[1.5rem] h-48 relative overflow-hidden flex items-center justify-center group">
                    <div class="absolute inset-0 bg-gold/5 group-hover:bg-gold/10 transition-colors"></div>
                    <span class="material-symbols-outlined text-gold/30 text-6xl">map</span>
                    <div class="absolute inset-x-0 bottom-4 text-center">
                        <span class="text-xs text-gold uppercase tracking-widest font-bold">View on Map</span>
                    </div>
                </div>

            </div>
        </div>
"""

help_content = """
        <!-- HERO SECTION -->
        <header class="relative text-center overflow-hidden mb-16">
            <div class="absolute inset-0 bg-[#0B0B0B] z-0">
                <div class="absolute top-[30%] left-[50%] -translate-x-1/2 w-[500px] h-[500px] bg-gold/5 rounded-full blur-[120px] pointer-events-none"></div>
            </div>
            <div class="relative z-10 max-w-3xl mx-auto px-6 ux-reveal">
                <h1 class="text-5xl md:text-6xl font-black font-headline tracking-tighter mb-4">
                    Help <span class="gold-text-gradient">Center</span>
                </h1>
                <p class="text-xl text-gray-400 font-medium mb-10">
                    Find answers, guides, and support resources.
                </p>
                <!-- Search Bar -->
                <div class="max-w-2xl mx-auto relative group">
                    <input type="text" class="w-full bg-[#111] border border-white/10 rounded-full py-4 pl-12 pr-6 text-white text-lg focus:outline-none focus:border-gold transition-colors focus:shadow-[0_0_20px_rgba(212,175,55,0.2)]" placeholder="Search help articles...">
                    <span class="material-symbols-outlined absolute left-4 top-1/2 -translate-y-1/2 text-gray-500 group-focus-within:text-gold transition-colors">search</span>
                </div>
            </div>
        </header>

        <div class="max-w-7xl mx-auto px-6 space-y-20 relative z-10">
            <!-- Categories Grid -->
            <section class="ux-reveal" style="animation-delay: 0.1s;">
                <h2 class="text-2xl font-bold font-headline mb-8 text-white">Browse by Category</h2>
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                    <!-- Cards -->
                    <a href="#" class="glass-card p-6 rounded-[1rem] flex items-center gap-4 group">
                        <div class="w-12 h-12 rounded-xl bg-gold/10 flex items-center justify-center text-gold border border-gold/20 group-hover:scale-110 transition-transform">
                            <span class="material-symbols-outlined">person</span>
                        </div>
                        <div>
                            <h3 class="font-bold text-white group-hover:text-gold transition-colors">Account & Login</h3>
                            <p class="text-xs text-gray-400 mt-1">Profile, passwords, settings</p>
                        </div>
                    </a>
                    
                    <a href="#" class="glass-card p-6 rounded-[1rem] flex items-center gap-4 group">
                        <div class="w-12 h-12 rounded-xl bg-gold/10 flex items-center justify-center text-gold border border-gold/20 group-hover:scale-110 transition-transform">
                            <span class="material-symbols-outlined">badge</span>
                        </div>
                        <div>
                            <h3 class="font-bold text-white group-hover:text-gold transition-colors">KYC & Verification</h3>
                            <p class="text-xs text-gray-400 mt-1">Documents, identity checks</p>
                        </div>
                    </a>
                    
                    <a href="#" class="glass-card p-6 rounded-[1rem] flex items-center gap-4 group">
                        <div class="w-12 h-12 rounded-xl bg-gold/10 flex items-center justify-center text-gold border border-gold/20 group-hover:scale-110 transition-transform">
                            <span class="material-symbols-outlined">payments</span>
                        </div>
                        <div>
                            <h3 class="font-bold text-white group-hover:text-gold transition-colors">Payments & Tx</h3>
                            <p class="text-xs text-gray-400 mt-1">Deposits, refunds, limits</p>
                        </div>
                    </a>
                    
                    <a href="#" class="glass-card p-6 rounded-[1rem] flex items-center gap-4 group">
                        <div class="w-12 h-12 rounded-xl bg-gold/10 flex items-center justify-center text-gold border border-gold/20 group-hover:scale-110 transition-transform">
                            <span class="material-symbols-outlined">auto_graph</span>
                        </div>
                        <div>
                            <h3 class="font-bold text-white group-hover:text-gold transition-colors">Gold SIP</h3>
                            <p class="text-xs text-gray-400 mt-1">Recurring inputs, pausing</p>
                        </div>
                    </a>
                    
                    <a href="#" class="glass-card p-6 rounded-[1rem] flex items-center gap-4 group">
                        <div class="w-12 h-12 rounded-xl bg-gold/10 flex items-center justify-center text-gold border border-gold/20 group-hover:scale-110 transition-transform">
                            <span class="material-symbols-outlined">local_shipping</span>
                        </div>
                        <div>
                            <h3 class="font-bold text-white group-hover:text-gold transition-colors">Withdrawals</h3>
                            <p class="text-xs text-gray-400 mt-1">Physical delivery, tracking</p>
                        </div>
                    </a>
                    
                    <a href="#" class="glass-card p-6 rounded-[1rem] flex items-center gap-4 group">
                        <div class="w-12 h-12 rounded-xl bg-gold/10 flex items-center justify-center text-gold border border-gold/20 group-hover:scale-110 transition-transform">
                            <span class="material-symbols-outlined">security</span>
                        </div>
                        <div>
                            <h3 class="font-bold text-white group-hover:text-gold transition-colors">Security & Safety</h3>
                            <p class="text-xs text-gray-400 mt-1">Vaults, fraud, protection</p>
                        </div>
                    </a>
                </div>
            </section>

            <!-- Popular Articles & Guides -->
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-12">
                <section class="ux-reveal" style="animation-delay: 0.2s;">
                    <h2 class="text-2xl font-bold font-headline mb-6 text-white flex items-center gap-2">
                        <span class="material-symbols-outlined text-gold">description</span> Popular Articles
                    </h2>
                    <ul class="space-y-3">
                        <li>
                            <a href="#" class="flex justify-between items-center p-4 rounded-xl hover:bg-white/5 border border-transparent hover:border-gold/20 transition-all group">
                                <span class="text-gray-300 group-hover:text-white">How to start a Gold SIP?</span>
                                <span class="material-symbols-outlined text-gray-600 group-hover:text-gold text-sm transition-transform group-hover:translate-x-1">arrow_forward</span>
                            </a>
                        </li>
                        <li>
                            <a href="#" class="flex justify-between items-center p-4 rounded-xl hover:bg-white/5 border border-transparent hover:border-gold/20 transition-all group">
                                <span class="text-gray-300 group-hover:text-white">How to complete KYC quickly?</span>
                                <span class="material-symbols-outlined text-gray-600 group-hover:text-gold text-sm transition-transform group-hover:translate-x-1">arrow_forward</span>
                            </a>
                        </li>
                        <li>
                            <a href="#" class="flex justify-between items-center p-4 rounded-xl hover:bg-white/5 border border-transparent hover:border-gold/20 transition-all group">
                                <span class="text-gray-300 group-hover:text-white">How to withdraw gold physically?</span>
                                <span class="material-symbols-outlined text-gray-600 group-hover:text-gold text-sm transition-transform group-hover:translate-x-1">arrow_forward</span>
                            </a>
                        </li>
                        <li>
                            <a href="#" class="flex justify-between items-center p-4 rounded-xl hover:bg-white/5 border border-transparent hover:border-gold/20 transition-all group">
                                <span class="text-gray-300 group-hover:text-white">Troubleshooting payment issues</span>
                                <span class="material-symbols-outlined text-gray-600 group-hover:text-gold text-sm transition-transform group-hover:translate-x-1">arrow_forward</span>
                            </a>
                        </li>
                    </ul>
                </section>

                <section class="ux-reveal" style="animation-delay: 0.3s;">
                    <h2 class="text-2xl font-bold font-headline mb-6 text-white flex items-center gap-2">
                        <span class="material-symbols-outlined text-gold">school</span> Guides
                    </h2>
                    <div class="glass-card p-8 rounded-[1.5rem] relative overflow-hidden group">
                        <div class="absolute inset-0 bg-gold/5 group-hover:bg-gold/10 transition-colors"></div>
                        <div class="relative z-10 space-y-4">
                            <span class="inline-block px-3 py-1 bg-gold/20 text-gold text-xs font-bold uppercase rounded-full tracking-widest border border-gold/30">Tutorial</span>
                            <h3 class="text-2xl font-bold text-white group-hover:text-gold transition-colors">Getting Started with GOLDe5</h3>
                            <p class="text-gray-400 text-sm">A complete step-by-step tutorial to creating your account, funding it, and making your first investment.</p>
                            <a href="#" class="inline-flex items-center gap-2 text-gold font-bold uppercase tracking-widest text-xs pt-4 group-hover:gap-4 transition-all">
                                Read Guide <span class="material-symbols-outlined text-sm">arrow_forward</span>
                            </a>
                        </div>
                    </div>
                </section>
            </div>

            <!-- Need More Help? -->
            <section class="text-center bg-[#111] p-12 rounded-[2rem] border border-white/5 ux-reveal" style="animation-delay: 0.4s;">
                <h2 class="text-3xl font-bold font-headline mb-4 text-white">Need More Help?</h2>
                <p class="text-gray-400 mb-8 max-w-xl mx-auto">Can't find the answers you're looking for? Our dedicated support team is ready to assist you.</p>
                <a href="contact.html" class="inline-block gold-gradient text-[#111] px-10 py-4 rounded-xl font-bold font-headline uppercase tracking-widest shadow-[0_0_20px_rgba(212,175,55,0.4)] hover:shadow-[0_0_35px_rgba(212,175,55,0.8)] hover:-translate-y-1 transition-all active:scale-95">
                    Contact Support
                </a>
            </section>

        </div>
"""

faq_content = """
        <!-- HERO SECTION -->
        <header class="relative text-center overflow-hidden mb-16">
            <div class="absolute inset-0 bg-[#0B0B0B] z-0">
                <div class="absolute top-[30%] left-[50%] -translate-x-1/2 w-[500px] h-[500px] bg-gold/5 rounded-full blur-[120px] pointer-events-none"></div>
            </div>
            <div class="relative z-10 max-w-3xl mx-auto px-6 ux-reveal">
                <h1 class="text-5xl md:text-6xl font-black font-headline tracking-tighter mb-4">
                    <span class="gold-text-gradient">FAQs</span>
                </h1>
                <p class="text-xl text-gray-400 font-medium">
                    Quick answers to common questions about our platform and services.
                </p>
            </div>
        </header>

        <div class="max-w-4xl mx-auto px-6 relative z-10 mb-20">
            <!-- Tabs -->
            <div class="flex flex-wrap justify-center gap-3 mb-12 ux-reveal" style="animation-delay: 0.1s;">
                <button class="px-6 py-2.5 rounded-full border border-gold bg-gold/10 text-gold font-bold text-sm tracking-wide shadow-[0_0_15px_rgba(212,175,55,0.2)]">General</button>
                <button class="px-6 py-2.5 rounded-full border border-white/10 hover:border-white/30 text-gray-400 hover:text-white font-medium text-sm tracking-wide transition-all">Account</button>
                <button class="px-6 py-2.5 rounded-full border border-white/10 hover:border-white/30 text-gray-400 hover:text-white font-medium text-sm tracking-wide transition-all">Payments</button>
                <button class="px-6 py-2.5 rounded-full border border-white/10 hover:border-white/30 text-gray-400 hover:text-white font-medium text-sm tracking-wide transition-all">Investments</button>
                <button class="px-6 py-2.5 rounded-full border border-white/10 hover:border-white/30 text-gray-400 hover:text-white font-medium text-sm tracking-wide transition-all">Security</button>
            </div>

            <!-- Accordion -->
            <div class="glass-card rounded-[1.5rem] p-6 md:p-10 space-y-4 ux-reveal" style="animation-delay: 0.2s;">
                
                <!-- Q1 -->
                <div class="border border-white/10 rounded-xl overflow-hidden group">
                    <button class="w-full text-left px-6 py-5 flex justify-between items-center hover:bg-white/5 transition-colors focus:outline-none">
                        <span class="font-bold text-lg text-white group-hover:text-gold transition-colors">What is GOLDe5?</span>
                        <span class="material-symbols-outlined text-gold transition-transform duration-300 transform group-hover:rotate-180">expand_more</span>
                    </button>
                    <!-- Simulated Expanded State for first item -->
                    <div class="px-6 pb-5 pt-0 text-gray-400 leading-relaxed bg-white/5 border-t border-white/5">
                        GOLDe5 is a premium digital wealth management platform focused on precious metals. We allow users to buy, sell, accumulate, and redeem physically backed gold and silver digitally.
                    </div>
                </div>

                <!-- Q2 -->
                <div class="border border-white/10 rounded-xl overflow-hidden group">
                    <button class="w-full text-left px-6 py-5 flex justify-between items-center hover:bg-white/5 transition-colors focus:outline-none">
                        <span class="font-bold text-lg text-white group-hover:text-gold transition-colors">Is my gold safe?</span>
                        <span class="material-symbols-outlined text-gray-500 group-hover:text-gold transition-transform duration-300">expand_more</span>
                    </button>
                </div>

                <!-- Q3 -->
                <div class="border border-white/10 rounded-xl overflow-hidden group">
                    <button class="w-full text-left px-6 py-5 flex justify-between items-center hover:bg-white/5 transition-colors focus:outline-none">
                        <span class="font-bold text-lg text-white group-hover:text-gold transition-colors">Can I withdraw gold physically?</span>
                        <span class="material-symbols-outlined text-gray-500 group-hover:text-gold transition-transform duration-300">expand_more</span>
                    </button>
                </div>
                
                <!-- Q4 -->
                <div class="border border-white/10 rounded-xl overflow-hidden group">
                    <button class="w-full text-left px-6 py-5 flex justify-between items-center hover:bg-white/5 transition-colors focus:outline-none">
                        <span class="font-bold text-lg text-white group-hover:text-gold transition-colors">What is Gold SIP?</span>
                        <span class="material-symbols-outlined text-gray-500 group-hover:text-gold transition-transform duration-300">expand_more</span>
                    </button>
                </div>

            </div>

            <!-- Still Need Help -->
            <div class="mt-16 text-center ux-reveal" style="animation-delay: 0.3s;">
                <p class="text-gray-400 mb-6">Still need help?</p>
                <a href="contact.html" class="inline-flex items-center gap-2 border border-gold/50 text-gold px-8 py-3 rounded-full font-bold uppercase tracking-widest hover:bg-gold/10 transition-all">
                    <span class="material-symbols-outlined text-sm">chat</span> Contact Us
                </a>
            </div>
        </div>
"""

support_content = """
        <!-- HERO SECTION -->
        <header class="relative text-center overflow-hidden mb-16">
            <div class="absolute inset-0 bg-[#0B0B0B] z-0">
                <div class="absolute top-[30%] left-[50%] -translate-x-1/2 w-[600px] h-[600px] bg-gold/5 rounded-full blur-[150px] pointer-events-none"></div>
            </div>
            <div class="relative z-10 max-w-4xl mx-auto px-6 ux-reveal">
                <div class="inline-flex items-center justify-center p-3 rounded-full bg-gold/10 border border-gold/30 text-gold mb-6">
                    <span class="material-symbols-outlined text-3xl">headset_mic</span>
                </div>
                <h1 class="text-5xl md:text-7xl font-black font-headline tracking-tighter mb-4">
                    Support <span class="gold-text-gradient">Center</span>
                </h1>
                <p class="text-xl md:text-2xl text-gray-400 font-light mb-10">
                    We're here to assist you anytime. Let's get your questions answered.
                </p>
                <!-- Large Search Bar -->
                <div class="max-w-3xl mx-auto relative group shadow-[0_15px_40px_rgba(0,0,0,0.5)] rounded-full">
                    <input type="text" class="w-full bg-[#151515] border border-white/10 rounded-full py-5 pl-14 pr-8 text-white text-lg focus:outline-none focus:border-gold transition-all duration-300 focus:shadow-[0_0_25px_rgba(212,175,55,0.2)]" placeholder="Search your issue... (e.g. KYC limit, Withdraw)">
                    <span class="material-symbols-outlined absolute left-5 top-1/2 -translate-y-1/2 text-gray-500 text-2xl group-focus-within:text-gold transition-colors">search</span>
                    <button class="absolute right-2 top-1/2 -translate-y-1/2 gold-gradient text-[#111] px-6 py-3 rounded-full text-sm font-bold uppercase tracking-widest hover:brightness-110 shadow-lg">Search</button>
                </div>
            </div>
        </header>

        <div class="max-w-7xl mx-auto px-6 space-y-20 relative z-10">
            
            <!-- Quick Actions -->
            <section class="grid grid-cols-1 md:grid-cols-3 gap-6 ux-reveal" style="animation-delay: 0.1s;">
                <a href="contact.html" class="glass-card p-8 rounded-[1.5rem] text-center group hover:bg-[#111]">
                    <span class="material-symbols-outlined text-gold text-4xl mb-4 group-hover:scale-110 transition-transform">mail</span>
                    <h3 class="text-xl font-bold text-white mb-2 font-headline">Contact Support</h3>
                    <p class="text-sm text-gray-400">Email us directly for personalized assistance.</p>
                </a>
                <a href="faq.html" class="glass-card p-8 rounded-[1.5rem] text-center group hover:bg-[#111]">
                    <span class="material-symbols-outlined text-gold text-4xl mb-4 group-hover:scale-110 transition-transform">question_answer</span>
                    <h3 class="text-xl font-bold text-white mb-2 font-headline">View FAQs</h3>
                    <p class="text-sm text-gray-400">Find quick answers to common questions.</p>
                </a>
                <a href="help.html" class="glass-card p-8 rounded-[1.5rem] text-center group hover:bg-[#111]">
                    <span class="material-symbols-outlined text-gold text-4xl mb-4 group-hover:scale-110 transition-transform">menu_book</span>
                    <h3 class="text-xl font-bold text-white mb-2 font-headline">Browse Help Center</h3>
                    <p class="text-sm text-gray-400">Read in-depth guides and tutorials.</p>
                </a>
            </section>

            <!-- Popular Help Topics -->
            <section class="ux-reveal" style="animation-delay: 0.2s;">
                <h2 class="text-2xl font-bold font-headline mb-8 text-white flex items-center justify-between">
                    <span>Popular Help Topics</span>
                    <a href="help.html" class="text-sm font-bold text-gold uppercase tracking-widest hover:underline">View All</a>
                </h2>
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
                    <a href="help.html" class="bg-[#111] border border-white/5 hover:border-gold/30 p-6 rounded-[1rem] transition-all group hover:-translate-y-1">
                        <h4 class="font-bold text-white group-hover:text-gold mb-2">Account Issues</h4>
                        <p class="text-xs text-gray-400">Login trouble, updating profile, closing account.</p>
                    </a>
                    <a href="help.html" class="bg-[#111] border border-white/5 hover:border-gold/30 p-6 rounded-[1rem] transition-all group hover:-translate-y-1">
                        <h4 class="font-bold text-white group-hover:text-gold mb-2">Payments</h4>
                        <p class="text-xs text-gray-400">Failed deposits, refund timelines, supported methods.</p>
                    </a>
                    <a href="help.html" class="bg-[#111] border border-white/5 hover:border-gold/30 p-6 rounded-[1rem] transition-all group hover:-translate-y-1">
                        <h4 class="font-bold text-white group-hover:text-gold mb-2">Withdrawals</h4>
                        <p class="text-xs text-gray-400">Delivery fees, tracking physical gold, process.</p>
                    </a>
                    <a href="help.html" class="bg-[#111] border border-white/5 hover:border-gold/30 p-6 rounded-[1rem] transition-all group hover:-translate-y-1">
                        <h4 class="font-bold text-white group-hover:text-gold mb-2">Security</h4>
                        <p class="text-xs text-gray-400">2FA setup, suspicious activity, vault safety.</p>
                    </a>
                </div>
            </section>

            <!-- Bottom Contact Section -->
            <section class="glass-card rounded-[2rem] p-8 md:p-12 flex flex-col md:flex-row items-center justify-between gap-8 ux-reveal" style="animation-delay: 0.3s;">
                <div>
                    <h3 class="text-2xl font-bold font-headline text-white mb-2">Still facing issues?</h3>
                    <p class="text-gray-400 text-sm max-w-md">Our expert team is available to chat or pick up your call.<br/>Working hours: Mon-Sat, 9 AM to 6 PM.</p>
                    <div class="flex items-center gap-6 mt-6">
                        <div class="flex items-center gap-2 text-gold">
                            <span class="material-symbols-outlined text-xl">mail</span>
                            <span class="font-bold text-xs uppercase tracking-widest">support@golde5.com</span>
                        </div>
                        <div class="flex items-center gap-2 text-gold">
                            <span class="material-symbols-outlined text-xl">call</span>
                            <span class="font-bold text-xs uppercase tracking-widest">+1 800 555 0199</span>
                        </div>
                    </div>
                </div>
                <button class="gold-gradient text-[#111] px-8 py-4 rounded-xl font-bold font-headline uppercase tracking-widest shadow-[0_0_20px_rgba(212,175,55,0.4)] hover:shadow-[0_0_35px_rgba(212,175,55,0.8)] transition-all flex items-center justify-center gap-2 active:scale-95 whitespace-nowrap">
                    <span class="material-symbols-outlined text-lg">chat</span> Start Live Chat
                </button>
            </section>

        </div>
"""

generate_file("contact.html", "Contact Us", contact_content)
generate_file("help.html", "Help Center", help_content)
generate_file("faq.html", "FAQs", faq_content)
generate_file("support.html", "Support Center", support_content)
