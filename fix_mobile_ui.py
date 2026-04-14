import os
import glob
import re

def fix_mobile_ui():
    html_files = glob.glob('*.html') + glob.glob('components/*.html')
    
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        orig_content = content
        
        # 1. Viewport Meta: ensure proper scaling
        if '<meta name="viewport"' not in content and '<head>' in content:
            content = content.replace('<head>', '<head>\n<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">')
        elif 'width=device-width, initial-scale=1.0' in content:
            pass # already handled
            
        # 2. Fix whitespace-nowrap overflow globally
        # If it's applied in a large text tag, it breaks mobile.
        # We will change 'whitespace-nowrap' to 'whitespace-normal md:whitespace-nowrap'
        # unless it already contains md:whitespace-nowrap
        if 'whitespace-nowrap' in content:
            # We must be careful not to keep adding md:whitespace-nowrap over and over
            # So, change all `whitespace-nowrap` that aren't preceded by `md:` or `lg:`
            # Actually, simply remove `whitespace-nowrap` from headers.
            content = re.sub(r'(<(?:h1|h2|h3)[^>]+class="[^"]*)(whitespace-nowrap)([^"]*">)', r'\1whitespace-normal md:whitespace-nowrap\3', content)

            # Fix header.html ticker
            if 'components' in filepath or filepath == 'header.html':
                 content = content.replace('"whitespace-nowrap">Live Price', '"whitespace-normal sm:whitespace-nowrap text-center">Live Price')

        # 3. Add max-w-full to images to prevent horizontal overflow constraints if missing,
        # but only if they don't have w-full and are not already constrained.
        # Actually Tailwind w-full is 100%, which works.
        
        # 4. In index.html specifically, there are 10 bars in the chart.
        # A container with gap-1 and 10 items might break on small screens.
        # We should ensure the chart container permits scrolling or hides overflow.
        # Replace `flex items-end justify-between` -> `flex items-end justify-between overflow-x-auto` in chart container.
        if 'id="chart-container"' in content:
            content = content.replace('box-border overflow-hidden"', 'box-border overflow-x-auto overflow-y-hidden snap-x md:overflow-hidden"')
            # Also ensure items don't shrink unreadably:
            content = content.replace('flex-1 flex flex-col', 'flex-1 min-w-[30px] md:min-w-[40px] snap-center flex flex-col')
            
        if content != orig_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed UI overflow in {filepath}")

if __name__ == '__main__':
    fix_mobile_ui()
