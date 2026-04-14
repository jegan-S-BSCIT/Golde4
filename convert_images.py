from PIL import Image
import os

images_map = {
    'g2.png': ('assets/images/products/gold-sip-dashboard.webp', 'assets/images/products/gold-sip-dashboard.jpg'),
    'g3.png': ('assets/images/products/gold-coins-product.webp', 'assets/images/products/gold-coins-product.jpg'),
    'g4.png': ('assets/images/vouchers/gift-voucher-card.webp', 'assets/images/vouchers/gift-voucher-card.jpg'),
    'g5.png': ('assets/images/jewellery/gold-jewellery-display.webp', 'assets/images/jewellery/gold-jewellery-display.jpg'),
    'screen.png': ('assets/images/hero/hero-gold-image.webp', 'assets/images/hero/hero-gold-image.jpg')
}

directories = [
    'assets/images/hero',
    'assets/images/products',
    'assets/images/vouchers',
    'assets/images/jewellery',
    'assets/images/icons'
]

for d in directories:
    os.makedirs(d, exist_ok=True)

for src, (webp_dst, jpg_dst) in images_map.items():
    if os.path.exists(src):
        try:
            img = Image.open(src).convert('RGB')
            # Reduce size to max 1200px width for optimization if too large
            if img.width > 1200:
                calc_height = int(1200 * img.height / img.width)
                img = img.resize((1200, calc_height), Image.Resampling.LANCZOS)
                
            img.save(webp_dst, 'webp', optimize=True, quality=80)
            img.save(jpg_dst, 'jpeg', optimize=True, quality=80)
            print(f"Processed: {src} -> {webp_dst} and {jpg_dst}")
        except Exception as e:
            print(f"Failed to process {src}: {e}")
    else:
        print(f"Source file not found: {src}")
