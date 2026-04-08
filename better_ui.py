import os

file_path = "c:/Users/LENOVO/OneDrive/Desktop/Golde4/partner.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Hero Background Image
old_hero_bg = """            <!-- Background Image overlay -->
            <div class="absolute inset-0 bg-[#0B0B0B] z-0">
                <div class="absolute inset-0 opacity-20" style="background-image: radial-gradient(#D4AF37 1px, transparent 1px); background-size: 40px 40px;"></div>
                <div class="absolute inset-0 bg-gradient-to-b from-[#0B0B0B]/80 via-[#0B0B0B]/40 to-[#0B0B0B]"></div>
            </div>"""
new_hero_bg = """            <!-- Background Image overlay -->
            <div class="absolute inset-0 bg-[#0B0B0B] z-0">
                <img src="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=2000" alt="business architecture" class="w-full h-full object-cover opacity-30 mix-blend-luminosity" />
                <div class="absolute inset-0 bg-gradient-to-b from-[#0B0B0B]/90 via-[#0B0B0B]/50 to-[#0B0B0B] border-b border-[#D4AF37]/10"></div>
            </div>"""
if old_hero_bg in html:
    html = html.replace(old_hero_bg, new_hero_bg)

# 2. Update .glass-card CSS for a more premium look
old_glass_card = """        .glass-card {
            background: rgba(30, 30, 30, 0.4);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(212, 175, 55, 0.1);
            transition: all 0.4s cubic-bezier(0.2, 0.8, 0.2, 1);
        }"""
new_glass_card = """        .glass-card {
            background: linear-gradient(180deg, rgba(30, 30, 30, 0.6) 0%, rgba(15, 15, 15, 0.8) 100%);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(212, 175, 55, 0.15);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5), inset 0 1px 1px rgba(255, 255, 255, 0.05);
            transition: all 0.4s cubic-bezier(0.2, 0.8, 0.2, 1);
        }"""
if old_glass_card in html:
    html = html.replace(old_glass_card, new_glass_card)

# 3. Enhance "Why Choose" cards
# These cards are currently: "p-4 rounded-xl bg-white/5 border border-white/10"
for i in range(5):
    html = html.replace(
        """class="p-4 rounded-xl bg-white/5 border border-white/10 hover:border-[#D4AF37]/30 transition-colors flex items-center justify-center gap-3""",
        """class="glass-card p-5 rounded-2xl flex items-center justify-center gap-4 group" cursor-pointer"""
    )
    html = html.replace(
        """class="p-4 rounded-xl bg-white/5 border border-white/10 hover:border-[#D4AF37]/30 transition-colors flex items-center justify-center gap-3 lg:col-span-2""",
        """class="glass-card p-5 rounded-2xl flex items-center justify-center gap-4 group lg:col-span-2" cursor-pointer"""
    )

# 4. Enhance Form Inputs background color
# Replace bg-[#111] border border-white/10 with better styling
html = html.replace("""bg-[#111] border border-white/10""", """bg-white/[0.03] border border-white/10 hover:border-white/20 hover:bg-white/[0.05]""")

# Write back
with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)
