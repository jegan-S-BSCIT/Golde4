import os
import re
import glob

def fix_overflow_and_responsiveness(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # 1. Ensure body has overflow-x-hidden to prevent horizontal scroll on mobile
    if '<body' in content and 'overflow-x-hidden' not in content:
        content = re.sub(r'(<body[^>]*)class="([^"]*)"', r'\1class="\2 overflow-x-hidden"', content)

    # 2. Add 'will-change: transform, opacity;' to `.ux-reveal` css class to utilize GPU
    if '.ux-reveal {' in content and 'will-change:' in content:
        # Check if gpu hint is applied
        content = content.replace('will-change: opacity, transform;', 'will-change: transform, opacity;')
    
    # Check if there are tables or large pre elements that might overflow, wrap them if possible.
    # Generally, the layout utilizes Tailwind grid and flex successfully.
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed: {filepath}")

def main():
    html_files = glob.glob('*.html')
    for f in html_files:
        fix_overflow_and_responsiveness(f)

if __name__ == '__main__':
    main()
