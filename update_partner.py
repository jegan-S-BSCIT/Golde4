import os

file_path = "c:/Users/LENOVO/OneDrive/Desktop/Golde4/partner.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Quotes
old_quotes = """                    const quotes = [
                        "Grow your business as a trusted GOLDe5 Partner.",
                        "Empower your network with premium digital gold.",
                        "Zero setup cost. High earning potential.",
                        "Secure your future with GOLDe5."
                    ];"""
new_quotes = """                    const quotes = [
                        "Grow your business as a trusted GOLDe5 Partner.",
                        "Join the future of digital gold.",
                        "Empower your network with premium digital gold.",
                        "Zero setup cost. High earning potential.",
                        "Secure your future with GOLDe5."
                    ];"""
if old_quotes in html:
    html = html.replace(old_quotes, new_quotes)

# 2. Hero Section
old_hero = """                        <p class="text-lg md:text-xl text-on-surface-variant/80 font-medium max-w-2xl leading-relaxed">
                            At GOLDe5, we believe in growing together. Join our partner network and be part of the future of digital precious-metal investing.
                        </p>
                        <p class="text-sm font-bold text-[#D4AF37] uppercase tracking-widest border-l-4 border-[#D4AF37] pl-4 py-1">
                            Choose your path. Start your journey today.
                        </p>
                        
                        <div class="pt-4">
                            <button onclick="document.getElementById('partner-form').scrollIntoView({behavior: 'smooth'})" class="bullion-gradient text-[#111] px-8 py-4 rounded-xl font-headline font-extrabold text-sm tracking-wide active:scale-95 transition-all duration-300 shadow-[0_0_20px_rgba(212,175,55,0.4)] hover:shadow-[0_0_30px_rgba(212,175,55,0.8)] hover:brightness-110 flex items-center justify-center gap-2 group">
                                Start Partnership
                                <span class="material-symbols-outlined text-sm group-hover:translate-x-1 transition-transform">arrow_forward</span>
                            </button>
                        </div>"""
new_hero = """                        <p class="text-lg md:text-xl text-on-surface-variant/80 font-medium max-w-2xl leading-relaxed">
                            At GOLDe5, we believe in growing together. Join our partner network and be part of the future of digital precious metal investing. Whether you're a business owner or an individual with a strong network, our partnership programs are designed for long-term growth and rewarding income.
                        </p>
                        <p class="text-sm font-bold text-[#D4AF37] uppercase tracking-widest border-l-4 border-[#D4AF37] pl-4 py-1">
                            Choose your path. Start your journey today.
                        </p>
                        
                        <div class="pt-4">
                            <button onclick="document.getElementById('partner-form').scrollIntoView({behavior: 'smooth'})" class="bullion-gradient text-[#111] px-8 py-4 rounded-xl font-headline font-extrabold text-sm tracking-wide active:scale-95 transition-all duration-300 shadow-[0_0_20px_rgba(212,175,55,0.4)] hover:shadow-[0_0_30px_rgba(212,175,55,0.8)] hover:brightness-110 flex items-center justify-center gap-2 group">
                                Start Your Partnership
                                <span class="material-symbols-outlined text-sm group-hover:translate-x-1 transition-transform">arrow_forward</span>
                            </button>
                        </div>"""
if old_hero in html:
    html = html.replace(old_hero, new_hero)


# 3. Retail Card
old_retail = """                        <p class="text-on-surface-variant/80 text-sm leading-relaxed mb-8 flex-grow">
                            Designed for business owners and financial advisors wanting to offer our products directly to their local client base.
                        </p>

                        <div class="space-y-6 mb-10 w-full">
                            <div>
                                <h4 class="text-[#D4AF37] text-xs font-bold uppercase tracking-widest mb-3">What You Do</h4>
                                <ul class="space-y-2 text-sm text-gray-300">
                                    <li class="flex items-start gap-2">
                                        <span class="material-symbols-outlined text-[#D4AF37] text-sm mt-[2px]">check_circle</span>
                                        Assist customers in gold & silver investment
                                    </li>
                                    <li class="flex items-start gap-2">
                                        <span class="material-symbols-outlined text-[#D4AF37] text-sm mt-[2px]">check_circle</span>
                                        Support account setup
                                    </li>
                                    <li class="flex items-start gap-2">
                                        <span class="material-symbols-outlined text-[#D4AF37] text-sm mt-[2px]">check_circle</span>
                                        Guide savings plans
                                    </li>
                                    <li class="flex items-start gap-2">
                                        <span class="material-symbols-outlined text-[#D4AF37] text-sm mt-[2px]">check_circle</span>
                                        Build customer relationships
                                    </li>
                                </ul>
                            </div>
                            <div>
                                <h4 class="text-white text-xs font-bold uppercase tracking-widest mb-3">Benefits</h4>
                                <ul class="space-y-2 text-sm text-gray-300">
                                    <li class="flex items-start gap-2 font-medium">
                                        <span class="material-symbols-outlined text-green-400 text-sm mt-[2px]">task_alt</span>
                                        Exclusive regional opportunities
                                    </li>
                                    <li class="flex items-start gap-2 font-medium">
                                        <span class="material-symbols-outlined text-green-400 text-sm mt-[2px]">task_alt</span>
                                        High earning potential
                                    </li>
                                    <li class="flex items-start gap-2 font-medium">
                                        <span class="material-symbols-outlined text-green-400 text-sm mt-[2px]">task_alt</span>
                                        Training & onboarding support
                                    </li>
                                    <li class="flex items-start gap-2 font-medium">
                                        <span class="material-symbols-outlined text-green-400 text-sm mt-[2px]">task_alt</span>
                                        Marketing assistance
                                    </li>
                                </ul>
                            </div>"""
new_retail = """                        <p class="text-on-surface-variant/80 text-sm leading-relaxed mb-8 flex-grow">
                            Designed for businesses, advisors, and financial professionals who want to offer gold investment solutions directly to their local clients.
                        </p>

                        <div class="space-y-6 mb-10 w-full">
                            <div>
                                <h4 class="text-[#D4AF37] text-xs font-bold uppercase tracking-widest mb-3">Your Role</h4>
                                <ul class="space-y-2 text-sm text-gray-300">
                                    <li class="flex items-start gap-2">
                                        <span class="material-symbols-outlined text-[#D4AF37] text-sm mt-[2px]">check_circle</span>
                                        Assist customers in starting their gold & silver investment journey
                                    </li>
                                    <li class="flex items-start gap-2">
                                        <span class="material-symbols-outlined text-[#D4AF37] text-sm mt-[2px]">check_circle</span>
                                        Support account setup and transactions
                                    </li>
                                    <li class="flex items-start gap-2">
                                        <span class="material-symbols-outlined text-[#D4AF37] text-sm mt-[2px]">check_circle</span>
                                        Guide customers on savings plans and future offerings
                                    </li>
                                    <li class="flex items-start gap-2">
                                        <span class="material-symbols-outlined text-[#D4AF37] text-sm mt-[2px]">check_circle</span>
                                        Build long-term customer relationships
                                    </li>
                                </ul>
                            </div>
                            <div>
                                <h4 class="text-white text-xs font-bold uppercase tracking-widest mb-3">Benefits</h4>
                                <ul class="space-y-2 text-sm text-gray-300">
                                    <li class="flex items-start gap-2 font-medium">
                                        <span class="material-symbols-outlined text-[#D4AF37] text-sm mt-[2px]">task_alt</span>
                                        Exclusive regional opportunities
                                    </li>
                                    <li class="flex items-start gap-2 font-medium">
                                        <span class="material-symbols-outlined text-[#D4AF37] text-sm mt-[2px]">task_alt</span>
                                        Higher earning potential with performance bonuses
                                    </li>
                                    <li class="flex items-start gap-2 font-medium">
                                        <span class="material-symbols-outlined text-[#D4AF37] text-sm mt-[2px]">task_alt</span>
                                        Training & onboarding support
                                    </li>
                                    <li class="flex items-start gap-2 font-medium">
                                        <span class="material-symbols-outlined text-[#D4AF37] text-sm mt-[2px]">task_alt</span>
                                        Marketing and branding assistance
                                    </li>
                                </ul>
                            </div>"""
if old_retail in html:
    html = html.replace(old_retail, new_retail)

# 4. Affiliate Card
old_affil = """                        <p class="text-on-surface-variant/80 text-sm leading-relaxed mb-8 flex-grow">
                            Perfect for digital influencers and networking professionals who want to earn passive income.
                        </p>

                        <div class="space-y-6 mb-10 w-full">
                            <div>
                                <h4 class="text-[#D4AF37] text-xs font-bold uppercase tracking-widest mb-3">What You Do</h4>
                                <ul class="space-y-2 text-sm text-gray-300">
                                    <li class="flex items-start gap-2">
                                        <span class="material-symbols-outlined text-[#D4AF37] text-sm mt-[2px]">check_circle</span>
                                        Introduce GOLDe5 to users
                                    </li>
                                    <li class="flex items-start gap-2">
                                        <span class="material-symbols-outlined text-[#D4AF37] text-sm mt-[2px]">check_circle</span>
                                        Help them start investing
                                    </li>
                                    <li class="flex items-start gap-2">
                                        <span class="material-symbols-outlined text-[#D4AF37] text-sm mt-[2px]">check_circle</span>
                                        Earn rewards for referrals
                                    </li>
                                </ul>
                            </div>
                            <div>
                                <h4 class="text-white text-xs font-bold uppercase tracking-widest mb-3">Benefits</h4>
                                <ul class="space-y-2 text-sm text-gray-300">
                                    <li class="flex items-start gap-2 font-medium">
                                        <span class="material-symbols-outlined text-green-400 text-sm mt-[2px]">task_alt</span>
                                        Zero setup cost
                                    </li>
                                    <li class="flex items-start gap-2 font-medium">
                                        <span class="material-symbols-outlined text-green-400 text-sm mt-[2px]">task_alt</span>
                                        Commission-based earnings
                                    </li>
                                    <li class="flex items-start gap-2 font-medium">
                                        <span class="material-symbols-outlined text-green-400 text-sm mt-[2px]">task_alt</span>
                                        Marketing tools provided
                                    </li>
                                    <li class="flex items-start gap-2 font-medium">
                                        <span class="material-symbols-outlined text-green-400 text-sm mt-[2px]">task_alt</span>
                                        Flexible work
                                    </li>
                                </ul>
                            </div>"""
new_affil = """                        <p class="text-on-surface-variant/80 text-sm leading-relaxed mb-8 flex-grow">
                            Ideal for digital influencers, marketers, and individuals who want to earn by promoting GOLDe5.
                        </p>

                        <div class="space-y-6 mb-10 w-full">
                            <div>
                                <h4 class="text-[#D4AF37] text-xs font-bold uppercase tracking-widest mb-3">Your Role</h4>
                                <ul class="space-y-2 text-sm text-gray-300">
                                    <li class="flex items-start gap-2">
                                        <span class="material-symbols-outlined text-[#D4AF37] text-sm mt-[2px]">check_circle</span>
                                        Introduce GOLDe5 to individuals and businesses
                                    </li>
                                    <li class="flex items-start gap-2">
                                        <span class="material-symbols-outlined text-[#D4AF37] text-sm mt-[2px]">check_circle</span>
                                        Help users begin their investment journey
                                    </li>
                                    <li class="flex items-start gap-2">
                                        <span class="material-symbols-outlined text-[#D4AF37] text-sm mt-[2px]">check_circle</span>
                                        Earn commission & rewards for successful referrals
                                    </li>
                                </ul>
                            </div>
                            <div>
                                <h4 class="text-white text-xs font-bold uppercase tracking-widest mb-3">Benefits</h4>
                                <ul class="space-y-2 text-sm text-gray-300">
                                    <li class="flex items-start gap-2 font-medium">
                                        <span class="material-symbols-outlined text-[#D4AF37] text-sm mt-[2px]">task_alt</span>
                                        Zero setup cost
                                    </li>
                                    <li class="flex items-start gap-2 font-medium">
                                        <span class="material-symbols-outlined text-[#D4AF37] text-sm mt-[2px]">task_alt</span>
                                        Commission-based earnings
                                    </li>
                                    <li class="flex items-start gap-2 font-medium">
                                        <span class="material-symbols-outlined text-[#D4AF37] text-sm mt-[2px]">task_alt</span>
                                        Marketing tools and support
                                    </li>
                                    <li class="flex items-start gap-2 font-medium">
                                        <span class="material-symbols-outlined text-[#D4AF37] text-sm mt-[2px]">task_alt</span>
                                        Flexible work from anywhere
                                    </li>
                                </ul>
                            </div>"""
if old_affil in html:
    html = html.replace(old_affil, new_affil)

# 5. Form Titles & Placeholders & Success alert
old_form = """                    <div class="w-full lg:w-5/12 space-y-8">
                        <h2 class="text-3xl md:text-5xl font-extrabold font-headline leading-tight text-white mb-6">
                            Become a <br/><span class="text-[#D4AF37]">Partner Today</span>
                        </h2>
                        <p class="text-on-surface-variant/80 text-lg leading-relaxed mb-8">
                            Fill out the form to express your interest
                        </p>"""
new_form = """                    <div class="w-full lg:w-5/12 space-y-8">
                        <h2 class="text-3xl md:text-5xl font-extrabold font-headline leading-tight text-white mb-6">
                            Start Your Partnership <br/><span class="text-[#D4AF37]">Journey Today</span>
                        </h2>
                        <p class="text-on-surface-variant/80 text-lg leading-relaxed mb-8">
                            Fill in your details and our team will connect with you.
                        </p>"""
if old_form in html:
    html = html.replace(old_form, new_form)

old_inputs = """                            <form class="space-y-6 relative z-10 w-full" onsubmit="event.preventDefault(); alert('Enquiry Submitted!');">
                                
                                <div class="space-y-2 w-full">
                                    <label class="text-xs font-bold text-gray-400 uppercase tracking-widest pl-1" for="fullName">Full Name</label>
                                    <input type="text" id="fullName" placeholder="John Doe" class="w-full bg-[#111] border border-white/10 rounded-xl px-4 py-3 text-white placeholder-gray-600 focus:outline-none focus:border-[#D4AF37] focus:ring-1 focus:ring-[#D4AF37] transition-colors" required>
                                </div>
                                    
                                <div class="space-y-2 w-full">
                                    <label class="text-xs font-bold text-gray-400 uppercase tracking-widest pl-1" for="email">Email Address</label>
                                    <input type="email" id="email" placeholder="john@example.com" class="w-full bg-[#111] border border-white/10 rounded-xl px-4 py-3 text-white placeholder-gray-600 focus:outline-none focus:border-[#D4AF37] focus:ring-1 focus:ring-[#D4AF37] transition-colors" required>
                                </div>

                                <div class="space-y-2 w-full">
                                    <label class="text-xs font-bold text-gray-400 uppercase tracking-widest pl-1" for="phone">Phone Number</label>
                                    <input type="tel" id="phone" placeholder="+1 (555) 000-0000" class="w-full bg-[#111] border border-white/10 rounded-xl px-4 py-3 text-white placeholder-gray-600 focus:outline-none focus:border-[#D4AF37] focus:ring-1 focus:ring-[#D4AF37] transition-colors" required>
                                </div>"""
new_inputs = """                            <form class="space-y-6 relative z-10 w-full" onsubmit="event.preventDefault(); alert('Thank you! Our team will contact you shortly.');">
                                
                                <div class="space-y-2 w-full">
                                    <label class="text-xs font-bold text-gray-400 uppercase tracking-widest pl-1" for="fullName">Full Name</label>
                                    <input type="text" id="fullName" placeholder="Enter your full name" class="w-full bg-[#111] border border-white/10 rounded-xl px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:border-[#D4AF37] focus:ring-1 focus:ring-[#D4AF37] transition-colors" required>
                                </div>
                                    
                                <div class="space-y-2 w-full">
                                    <label class="text-xs font-bold text-gray-400 uppercase tracking-widest pl-1" for="email">Email Address</label>
                                    <input type="email" id="email" placeholder="Enter your email address" class="w-full bg-[#111] border border-white/10 rounded-xl px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:border-[#D4AF37] focus:ring-1 focus:ring-[#D4AF37] transition-colors" required>
                                </div>

                                <div class="space-y-2 w-full">
                                    <label class="text-xs font-bold text-gray-400 uppercase tracking-widest pl-1" for="phone">Phone Number</label>
                                    <input type="tel" id="phone" placeholder="Enter your phone number" class="w-full bg-[#111] border border-white/10 rounded-xl px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:border-[#D4AF37] focus:ring-1 focus:ring-[#D4AF37] transition-colors" required>
                                </div>

                                <div class="space-y-2 w-full">
                                    <label class="text-xs font-bold text-gray-400 uppercase tracking-widest pl-1" for="city">State / City</label>
                                    <input type="text" id="city" placeholder="Enter your city/state" class="w-full bg-[#111] border border-white/10 rounded-xl px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:border-[#D4AF37] focus:ring-1 focus:ring-[#D4AF37] transition-colors" required>
                                </div>"""
if old_inputs in html:
    html = html.replace(old_inputs, new_inputs)

old_message = """                                <div class="space-y-2 w-full">
                                    <label class="text-xs font-bold text-gray-400 uppercase tracking-widest pl-1" for="message">Message</label>
                                    <textarea id="message" rows="4" placeholder="Tell us about yourself and how you plan to partner with us..." class="w-full bg-[#111] border border-white/10 rounded-xl px-4 py-3 text-white placeholder-gray-600 focus:outline-none focus:border-[#D4AF37] focus:ring-1 focus:ring-[#D4AF37] transition-colors resize-none" required></textarea>
                                </div>

                                <button type="submit" class="w-full mt-6 bullion-gradient text-[#111] py-4 rounded-xl font-headline font-extrabold text-sm md:text-base tracking-wide active:scale-[0.98] transition-all duration-300 shadow-[0_0_15px_rgba(212,175,55,0.3)] hover:shadow-[0_0_30px_rgba(212,175,55,0.6)] hover:brightness-110 flex items-center justify-center gap-2 group">
                                    Send Enquiry
                                    <span class="material-symbols-outlined text-sm group-hover:translate-x-1 transition-transform">send</span>
                                </button>
                            </form>
                        </div>
                    </div>"""
new_message = """                                <div class="space-y-2 w-full">
                                    <label class="text-xs font-bold text-gray-400 uppercase tracking-widest pl-1" for="message">Message / Additional Details</label>
                                    <textarea id="message" rows="4" placeholder="Tell us about your experience or interest" class="w-full bg-[#111] border border-white/10 rounded-xl px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:border-[#D4AF37] focus:ring-1 focus:ring-[#D4AF37] transition-colors resize-none" required></textarea>
                                </div>

                                <button type="submit" class="w-full mt-6 bullion-gradient text-[#111] py-4 rounded-xl font-headline font-extrabold text-sm md:text-base tracking-wide active:scale-[0.98] transition-all duration-300 shadow-[0_0_15px_rgba(212,175,55,0.3)] hover:shadow-[0_0_30px_rgba(212,175,55,0.6)] hover:brightness-110 flex items-center justify-center gap-2 group">
                                    Apply Now
                                    <span class="material-symbols-outlined text-sm group-hover:translate-x-1 transition-transform">send</span>
                                </button>
                                
                                <p class="text-gray-500 text-[11px] text-center w-full mt-4 flex justify-center gap-1 items-center font-medium">
                                    <span class="material-symbols-outlined text-[13px]">lock</span> Your information is <span>सुरक्षित</span> and will not be shared.
                                </p>
                            </form>
                        </div>
                    </div>"""
if old_message in html:
    html = html.replace(old_message, new_message)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)
