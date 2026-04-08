# Design System Specification

## 1. Overview & Creative North Star: "The Gilded Vault"
This design system is built upon the philosophy of **"The Gilded Vault."** In the world of high-end fintech, trust isn't just earned through security protocols—it is felt through the weight, depth, and tactile quality of the interface. 

We are moving away from the "flat" web. To achieve a premium, editorial feel, we utilize **Tonal Layering** and **Intentional Asymmetry**. By overlapping high-fidelity glass surfaces over deep, charcoal voids, we create a sense of physical space. This system rejects generic templates in favor of a bespoke dashboard experience where typography feels curated and every element has a luminous, intentional glow.

---

## 2. Colors & Surface Architecture
The palette is rooted in the "Deep Black" spectrum to evoke the feeling of a private banking suite.

### Core Palette
*   **Primary (Luxury Gold):** `#f2ca50` / `primary` — Used for high-value brand moments and critical CTAs.
*   **Primary Container (Old Gold):** `#d4af37` / `primary_container` — The foundation for gold-based surfaces.
*   **Surface (Deep Black):** `#131313` / `surface` — The base "floor" of the application.
*   **Tertiary (Midnight Depth):** `#c7cbff` / `tertiary` — Subtle dark blue accents used to add chromatic depth to shadows and secondary icons.

### The "No-Line" Rule
**Explicit Instruction:** Designers are prohibited from using 1px solid borders to section content. Traditional borders create a "boxed-in" feel that contradicts luxury. Boundaries must be defined through:
1.  **Tonal Shifts:** Placing a `surface_container_high` card on a `surface` background.
2.  **Luminous Depth:** Using the `0 0 10px rgba(212, 175, 55, 0.4)` glow to define the edge of an active element.

### Surface Hierarchy & Nesting
Treat the UI as a series of physical layers. 
*   **Base:** `surface_container_lowest` (#0e0e0e) for the deepest background.
*   **Sections:** `surface_container_low` (#1c1b1b) for sidebars or secondary content areas.
*   **Cards:** `surface_container_high` (#2a2a2a) for main content modules.
*   **Interaction:** `surface_bright` (#3a3939) for hovered or active states.

### The "Glass & Gradient" Rule
For elevated components like modals or floating navigation, use **Glassmorphism**:
*   **Fill:** `primary_container` at 10-15% opacity.
*   **Effect:** `backdrop-blur: 20px`.
*   **Visual Soul:** Use a linear gradient (`135deg, #D4AF37, #E6C65C`) for Primary CTAs to provide a metallic shimmer that flat colors cannot replicate.

---

## 3. Typography
The system uses a dual-typeface strategy to balance institutional authority with modern precision.

### The Scale
*   **Display (Manrope):** `display-lg` (3.5rem) to `display-sm` (2.25rem). Use sparingly for "Gold Balance" or "Portfolio Value." These should feel cinematic.
*   **Headline (Manrope):** `headline-lg` (2rem) down to `headline-sm`. Used for page titles and section headers.
*   **Body (Inter):** `body-lg` (1rem) to `body-sm` (0.75rem). Inter provides the high-legibility required for financial data and regulatory text.
*   **Labels (Inter):** `label-md` (0.75rem). Specifically for micro-copy and data captions.

### Editorial Hierarchy
To break the grid, use a "High-Contrast" scale. Pair a `display-lg` value in `on_surface` (White) with a `label-md` value in `on_surface_variant` (Light Gray) directly beneath it. The stark difference in scale creates a sophisticated, magazine-like aesthetic.

---

## 4. Elevation & Depth
In this system, depth is a functional tool for hierarchy, not just decoration.

### The Layering Principle
Stacking surfaces is our primary method of organization. A `surface_container_highest` element should only ever sit on top of a `surface_container_low` or `surface`. This creates a natural "lift" without the clutter of lines.

### Ambient Shadows & Glows
*   **Standard Shadows:** Use extra-diffused, low-opacity shadows. Color: `rgba(0, 0, 0, 0.6)` with a blur of 30px-50px.
*   **Signature Glow:** For active gold assets, apply a `surface_tint` glow: `box-shadow: 0 4px 20px rgba(233, 195, 73, 0.15)`.

### The "Ghost Border" Fallback
If accessibility requires a container boundary, use the `outline_variant` token at **15% opacity**. It should be felt, not seen.

---

## 5. Components

### Buttons (The "Bullion" Style)
*   **Primary:** `linear-gradient(135deg, #D4AF37, #E6C65C)`. On hover, add a `shimmer` animation (a moving white highlight at 20% opacity) and a `0.25rem` lift.
*   **Secondary:** Ghost style. No background fill, `outline_variant` border (20% opacity), text in `primary`.

### Cards & Lists
*   **Forbid Dividers:** Do not use horizontal lines between list items. Use 16px or 24px of vertical whitespace (Spacing Scale) and a subtle background change (`surface_container_low` to `surface_container_high`) to separate data rows.
*   **Interactive Cards:** On hover, cards should transition to a Glassmorphism state with a subtle gold "inner glow."

### Data Visualization
*   **Bullion Growth:** Use `Green (#00C853)` for upward trends, but apply it to thin, high-fidelity sparklines.
*   **Market Dip:** Use `Red (#FF3D00)` for downward trends.
*   **Context:** All charts should sit on a `surface_container_lowest` background to maximize the "glow" of the data lines.

### Specialized Fintech Components
*   **Metal Switcher:** A bespoke toggle to switch between Gold, Silver, and Platinum, using metallic textures rather than standard radio buttons.
*   **Purity Badge:** A small, high-contrast label (`label-sm`) using `primary_fixed` background and `on_primary_fixed` text to denote gold carats (e.g., "24K").

---

## 6. Do’s and Don’ts

### Do
*   **DO** use whitespace as a luxury. Give elements more room than you think they need.
*   **DO** use "Manrope" for all large numbers. Financial figures are the hero of the platform.
*   **DO** use subtle Dark Blue (`tertiary_container`) in the background of gold charts to create a "Jewelry Box" effect.

### Don’t
*   **DON'T** use 100% opaque white for body text. Use `on_surface_variant` (#B0B0B0) to reduce eye strain and maintain the "dark mode" premium feel.
*   **DON'T** use sharp corners. Stick to the `md` (0.375rem) or `lg` (0.5rem) roundedness scale to keep the UI feeling approachable yet modern.
*   **DON'T** use standard "Blue" for links. Every interactive element should be gold or a tinted variant.