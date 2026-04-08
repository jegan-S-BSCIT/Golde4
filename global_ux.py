import os
import glob

css_block = """
<!-- GLOBAL UX STYLES -->
<style id="global-ux-styles">
    /* Reveal Animation Physics */
    .ux-reveal {
        opacity: 0;
        transform: translateY(30px) scale(0.98);
        transition: all 0.8s cubic-bezier(0.2, 0.8, 0.2, 1);
        will-change: opacity, transform;
    }
    .ux-revealed {
        opacity: 1;
        transform: translateY(0) scale(1);
    }
    
    /* Sticky Navbar Enhancement */
    nav { transition: all 0.4s cubic-bezier(0.2, 0.8, 0.2, 1) !important; }
    .nav-scrolled {
        background: rgba(5, 5, 5, 0.98) !important;
        height: 4.5rem !important; /* Shrink height */
        box-shadow: 0 15px 40px rgba(0,0,0,0.9), 0 1px 0 rgba(212,175,55,0.15) !important;
        backdrop-filter: blur(25px) !important;
    }
    
    /* Cards Global Hover & Tilt (Smooth overrides) */
    .glass-card {
        transition: transform 0.5s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.5s ease, border-color 0.3s ease !important;
    }
    .glass-card:hover {
        border-color: rgba(212, 175, 55, 0.4) !important;
        box-shadow: 0 20px 50px rgba(0,0,0,0.8), 0 0 30px rgba(212,175,55,0.1) !important;
        z-index: 10;
    }
    
    /* Input Animations */
    .input-focused > label { 
        color: #D4AF37 !important; 
        transform: translateY(-2px); 
        transition: all 0.3s cubic-bezier(0.2, 0.8, 0.2, 1); 
    }
    input, textarea, select { transition: all 0.3s ease !important; }
    input:focus, textarea:focus, select:focus { 
        box-shadow: 0 0 20px rgba(212,175,55,0.2) !important; 
        border-color: #D4AF37 !important;
    }
    
    /* Buttons Interactive Glow */
    button { transition: all 0.3s cubic-bezier(0.2, 0.8, 0.2, 1) !important; }
    button:hover { 
        box-shadow: 0 0 25px rgba(212, 175, 55, 0.6) !important; 
        transform: translateY(-2px) !important; 
    }
    button:active { transform: translateY(1px) scale(0.97) !important; }

    /* Nav Links Hover Underline */
    .nav-hover-line { position: relative; }
    .nav-hover-line::after {
        content: ''; position: absolute; width: 0; height: 2px;
        bottom: 0; left: 0; background-color: #f2ca50;
        transition: width 0.3s ease-out;
    }
    .nav-hover-line:hover::after { width: 100%; }

    /* Page Fade-in Transition */
    body { animation: pageFadeIn 0.6s cubic-bezier(0.2, 0.8, 0.2, 1) forwards; }
    @keyframes pageFadeIn { from { opacity: 0; filter: blur(10px); } to { opacity: 1; filter: blur(0px); } }
    
    /* Live Price Ticker Overlay */
    @keyframes tickerScroll {
        0% { transform: translateX(100%); }
        100% { transform: translateX(-100%); }
    }
</style>
"""

js_block = """
<!-- GLOBAL UX SCRIPT -->
<script id="global-ux-script">
document.addEventListener("DOMContentLoaded", () => {
    // 1. Intersection Observer for Smooth Sequential Reveals
    // Target sections, cards, and prominent text elements
    const revealElements = document.querySelectorAll('section, .glass-card, h1, h2, h3');
    
    const revealObserver = new IntersectionObserver((entries, observer) => {
        let delayCount = 0;
        entries.forEach(entry => {
            if(entry.isIntersecting) {
                // Add staggered delay based on rapid succession
                setTimeout(() => {
                    entry.target.classList.add('ux-revealed');
                }, delayCount * 100);
                delayCount++;
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.05, rootMargin: "0px 0px -50px 0px" });

    revealElements.forEach(el => {
        // Prevent double revealing if it's already animated by existing classes
        if(!el.classList.contains('animate-slide-up')) {
            el.classList.add('ux-reveal');
        }
        revealObserver.observe(el);
    });

    // 2. Sticky Navbar advanced effect
    const nav = document.querySelector('nav');
    if(nav) {
        window.addEventListener('scroll', () => {
            if(window.scrollY > 40) {
                nav.classList.add('nav-scrolled');
            } else {
                nav.classList.remove('nav-scrolled');
            }
        });
    }

    // 3. 3D Tilt Effect on Glass Cards
    const cards = document.querySelectorAll('.glass-card');
    cards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            // Only apply tilt on desktop devices
            if(window.innerWidth > 768) {
                const rect = card.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                const centerX = rect.width / 2;
                const centerY = rect.height / 2;
                // Sensible degrees for tilt
                const rotateX = ((y - centerY) / centerY) * -4; 
                const rotateY = ((x - centerX) / centerX) * 4;
                card.style.transform = `perspective(1000px) scale(1.02) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-8px)`;
                card.style.transition = 'none'; // Instant follow
            }
        });
        card.addEventListener('mouseleave', () => {
            card.style.transform = ''; // Clear inline styles to allow CSS transition to take over
            card.style.transition = 'transform 0.5s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.5s ease';
        });
    });

    // 4. Form Input Focus Glow Logic
    const inputs = document.querySelectorAll('input, textarea, select');
    inputs.forEach(input => {
        input.addEventListener('focus', () => {
            if(input.parentElement && input.parentElement.classList.contains('space-y-2')) {
                input.parentElement.classList.add('input-focused');
            }
        });
        input.addEventListener('blur', () => {
            if(input.parentElement) {
                input.parentElement.classList.remove('input-focused');
            }
        });
    });

    // 5. Parallax Hero Effect (Optional gentle background shift)
    const heroSection = document.querySelector('section:first-of-type');
    window.addEventListener('scroll', () => {
        if(heroSection && window.scrollY < window.innerHeight) {
            const bgElement = heroSection.querySelector('.absolute.inset-0 img');
            if(bgElement) {
                const yPos = window.scrollY * 0.3; // 30% speed of scroll
                bgElement.style.transform = `translateY(${yPos}px)`;
            }
        }
    });

});
</script>
"""

directory = "c:/Users/LENOVO/OneDrive/Desktop/Golde4"
html_files = glob.glob(os.path.join(directory, "*.html"))

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Avoid duplicate injections
    if "id=\"global-ux-styles\"" not in html:
        # Inject CSS before </head>
        html = html.replace("</head>", f"{css_block}</head>")
        
    if "id=\"global-ux-script\"" not in html:
        # Inject JS before </body>
        html = html.replace("</body>", f"{js_block}\n</body>")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)

print("Global UX changes applied successfully.")
