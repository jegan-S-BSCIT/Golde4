import re
import os

path = r"c:\Users\LENOVO\OneDrive\Desktop\Golde4\about.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Extract the Trust Logos Banner
trust_match = re.search(r'(<!-- Partner / Trust Logos Banner -->\s*<div class="border-t border-white/5 bg-\[#0a0f18\] py-10 relative overflow-hidden">.*?</div>\s*</div>)', html, re.DOTALL)
if trust_match:
    trust_banner = trust_match.group(1)
    # Remove it from its current position
    html = html.replace(trust_banner, "")
else:
    # Try a looser match if needed
    trust_match_2 = re.search(r'(<!-- Partner / Trust Logos Banner -->.*?(?:</div>\s*){3})', html, re.DOTALL)
    if trust_match_2:
        trust_banner = trust_match_2.group(1)
        html = html.replace(trust_banner, "")
    else:
        print("Could not find Trust Banner")
        exit()

# 2. Insert the Trust Logos Banner precisely after Section 5
# Look for Section 5 end
sec5_end = re.search(r'(<!-- Section 5: Core Commitments -->.*?</section>)', html, re.DOTALL)
if sec5_end:
    section_5_block = sec5_end.group(1)
    # Re-insert section 5 followed by the trust banner
    html = html.replace(section_5_block, section_5_block + "\n\n" + trust_banner)
else:
    print("Could not find Section 5")
    exit()

# 3. Ensure the footer attaches directly to main. 
# Right now, `</main>` is before the footer. Let's make sure there's no random spacing.
# The user complained about empty space after "What is GOLDe5?"
# Let's remove any stray 100vh if it exists in the sections.
html = re.sub(r'min-h-\[100vh\]', '', html) # removes min-h-[100vh] if injected into a section improperly

# Save fixes
with open(path, "w", encoding="utf-8") as f:
    f.write(html)
print("Fixes applied successfully to about.html")
