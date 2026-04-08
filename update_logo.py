import glob
import os

old_header_full = 'class="text-[#d0c5af] text-[9.5px] md:text-[10px] font-medium tracking-[0.28em] font-body uppercase leading-tight mt-[2px] group-hover:text-white transition-colors duration-300"'
new_header_full = 'class="text-[#d0c5af] text-[10px] md:text-[11px] font-medium tracking-normal font-body lowercase leading-tight mt-[2px] group-hover:text-white transition-colors duration-300"'

old_footer_full = 'class="text-[9px] text-gray-400 uppercase tracking-widest font-semibold ml-1"'
new_footer_full = 'class="text-[10px] text-gray-400 lowercase tracking-normal font-semibold ml-1"'

for filename in glob.glob('*.html'):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    updated = content.replace(old_header_full, new_header_full)
    updated = updated.replace(old_footer_full, new_footer_full)
    
    if updated != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(updated)
        print(f'Updated {filename}')
