import os
import re
import glob

def optimize_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # 1. Add Preconnects to head
    preconnects = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
"""
    if '<link rel="preconnect" href="https://fonts.googleapis.com">' not in content:
        # replace the first <head> match
        content = re.sub(r'(<head(?:>|\s[^>]*>))', r'\1' + preconnects, content, count=1)

    # 2. Add `loading="lazy"` and `decoding="async"` to all <img> tags that don't have them
    # Ignore hero images
    def img_replacer(match):
        img_tag = match.group(0)
        # Skip if it is a hero image or already has lazy
        if 'hero' in img_tag.lower():
            return img_tag
        if 'loading="lazy"' not in img_tag:
            img_tag = img_tag.replace('<img ', '<img loading="lazy" ')
        if 'decoding="async"' not in img_tag:
            img_tag = img_tag.replace('<img ', '<img decoding="async" ')
        return img_tag

    content = re.sub(r'<img [^>]+>', img_replacer, content)

    # 3. Add defer to non-essential scripts (not tailwindcdn)
    def script_replacer(match):
        script_tag = match.group(0)
        if 'src=' in script_tag and 'cdn.tailwindcss.com' not in script_tag and 'defer' not in script_tag:
            script_tag = script_tag.replace('<script ', '<script defer ')
        return script_tag

    content = re.sub(r'<script [^>]+>', script_replacer, content)

    # 4. Use font-display: swap in Google Fonts if missing
    def font_replacer(match):
        url = match.group(0)
        if '&display=swap' not in url and '&amp;display=swap' not in url:
            return url + '&amp;display=swap'
        return url
    
    content = re.sub(r'https://fonts\.googleapis\.com/css2\?[^"\'\s]+', font_replacer, content)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Optimized: {filepath}")

def main():
    html_files = glob.glob('*.html')
    # Also include files in components/
    html_files.extend(glob.glob('components/*.html'))
    
    for f in html_files:
        optimize_html_file(f)

if __name__ == '__main__':
    main()
