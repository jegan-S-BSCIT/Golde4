import re
import os

TERMS_CONTENT = """
        <!-- HERO SECTION -->
        <section class="relative pt-32 pb-20 px-8 flex items-center overflow-hidden bg-[#0A0A0A] border-b border-[#D4AF37]/10">
            <div class="absolute inset-0 bg-[#0B0B0B] z-0">
                <div class="absolute top-[20%] left-[50%] -translate-x-1/2 w-[600px] h-[600px] bg-[#D4AF37]/5 rounded-full blur-[150px] pointer-events-none"></div>
            </div>
            <div class="max-w-7xl mx-auto w-full relative z-10 text-center space-y-6 ux-reveal">
                <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full border border-[#D4AF37]/30 bg-[#D4AF37]/5 mx-auto">
                    <span class="material-symbols-outlined text-[#D4AF37] text-sm">gavel</span>
                    <span class="text-[#D4AF37] font-bold text-xs uppercase tracking-[0.2em]">Compliance & Safety</span>
                </div>
                <h1 class="text-5xl md:text-6xl font-black font-headline text-white tracking-tight">Terms & Conditions</h1>
                <p class="text-xl text-gray-400 font-medium max-w-2xl mx-auto">Please review all legal documents carefully before using the GOLDe5 platform.</p>
            </div>
        </section>

        <!-- LEGAL TABS AND CONTENT -->
        <section class="max-w-5xl mx-auto px-6 md:px-8 py-16 w-full relative z-10">
            <!-- TABS -->
            <div class="flex overflow-x-auto hide-scrollbar gap-4 border-b border-[#D4AF37]/20 pb-4 mb-8 sticky top-20 z-40 bg-[#0B0B0B]/90 backdrop-blur-xl pt-4">
                <button onclick="switchTab('terms')" id="tab-terms" class="tab-btn px-6 py-3 rounded-xl font-bold tracking-wide whitespace-nowrap transition-all duration-300 bullion-gradient text-[#111] shadow-[0_0_15px_rgba(212,175,55,0.3)]">Terms & Conditions</button>
                <button onclick="switchTab('privacy')" id="tab-privacy" class="tab-btn px-6 py-3 rounded-xl font-bold tracking-wide whitespace-nowrap transition-all duration-300 bg-white/5 text-gray-400 hover:text-[#D4AF37] border border-transparent hover:border-[#D4AF37]/30">Privacy Policy</button>
                <button onclick="switchTab('cyber')" id="tab-cyber" class="tab-btn px-6 py-3 rounded-xl font-bold tracking-wide whitespace-nowrap transition-all duration-300 bg-white/5 text-gray-400 hover:text-[#D4AF37] border border-transparent hover:border-[#D4AF37]/30">Cyber Fraud Advisory</button>
                <button onclick="switchTab('disclaimer')" id="tab-disclaimer" class="tab-btn px-6 py-3 rounded-xl font-bold tracking-wide whitespace-nowrap transition-all duration-300 bg-white/5 text-gray-400 hover:text-[#D4AF37] border border-transparent hover:border-[#D4AF37]/30">Disclaimer</button>
            </div>

            <!-- CONTENT WINDOW -->
            <div class="glass-card rounded-[1.5rem] p-6 text-gray-300 border border-[#D4AF37]/20 relative">
                
                <!-- PROGRESS BAR -->
                <div class="absolute top-0 left-0 w-full h-1 bg-white/5 rounded-t-[1.5rem] overflow-hidden">
                    <div id="scroll-progress" class="h-full bg-gradient-to-r from-[#D4AF37] to-[#F2CA50] w-0 transition-all duration-300"></div>
                </div>
                
                <div id="scroll-container" class="max-h-[60vh] overflow-y-auto pr-4 space-y-4 pt-4 hide-scrollbar custom-scrollbar" onscroll="updateScrollProgress()">
                    
                    <!-- TAB 1: TERMS -->
                    <div id="content-terms" class="tab-content active space-y-4">
                        <div class="mb-8">
                            <h2 class="text-2xl font-bold font-headline text-white mb-2">Terms & Conditions</h2>
                            <p class="text-sm text-gray-500 font-medium">Last updated: April 14, 2026</p>
                            <p class="mt-4 text-sm leading-relaxed">These Terms & Conditions (“Terms”) govern your access to and use of the GOLDe5 website, mobile application, and all associated services...</p>
                            <p class="mt-2 text-sm leading-relaxed">By accessing, registering, or using the Platform in any manner, you acknowledge that you have read, understood, and agreed to be legally bound by these Terms...</p>
                        </div>
                        
                        <!-- Accordion Items generation script will handle this, but HTML is robust -->
                        <div class="accordion-item border border-white/10 rounded-xl overflow-hidden bg-white/5">
                            <button class="accordion-header w-full px-6 py-4 flex justify-between items-center font-bold text-lg text-white hover:bg-white/5 transition-colors focus:outline-none">
                                <span>01. Definitions</span>
                                <span class="material-symbols-outlined text-[#D4AF37] transform transition-transform duration-300">expand_more</span>
                            </button>
                            <div class="accordion-body px-6 pb-4 hidden text-sm leading-relaxed text-gray-400 space-y-2">
                                <p>“Company”, “GOLDe5”, “We”, “Us”, or “Our” refers to GOLDe5, a platform operated by SpixCapital...</p>
                                <p>“User”, “You”, or “Customer” refers to any individual or entity accessing or using the Platform.</p>
                                <p>“Metals” refers to precious metals including gold, silver, platinum, palladium...</p>
                                <p>“Account” means a registered user profile created to access services.</p>
                                <p>“Vault” refers to secure storage facilities operated directly or through authorized third-party providers.</p>
                                <p>“Platform” includes all digital interfaces provided by GOLDe5 including website, mobile applications, and backend systems.</p>
                            </div>
                        </div>

                        <div class="accordion-item border border-white/10 rounded-xl overflow-hidden bg-white/5">
                            <button class="accordion-header w-full px-6 py-4 flex justify-between items-center font-bold text-lg text-white hover:bg-white/5 transition-colors focus:outline-none">
                                <span>02. Regulatory Status & Platform Nature</span>
                                <span class="material-symbols-outlined text-[#D4AF37] transform transition-transform duration-300">expand_more</span>
                            </button>
                            <div class="accordion-body px-6 pb-4 hidden text-sm leading-relaxed text-gray-400 space-y-2">
                                <p>GOLDe5 operates as a technology-enabled execution platform that facilitates transactions in precious metals and related services...</p>
                                <p>GOLDe5 does not function as a stock exchange, broker, sub-broker, portfolio manager, investment advisor, or collective investment scheme, and is not registered with the Securities and Exchange Board of India (SEBI) in such capacities.</p>
                            </div>
                        </div>

                        <div class="accordion-item border border-white/10 rounded-xl overflow-hidden bg-white/5">
                            <button class="accordion-header w-full px-6 py-4 flex justify-between items-center font-bold text-lg text-white hover:bg-white/5 transition-colors focus:outline-none">
                                <span>03. Acceptance of Terms</span>
                                <span class="material-symbols-outlined text-[#D4AF37] transform transition-transform duration-300">expand_more</span>
                            </button>
                            <div class="accordion-body px-6 pb-4 hidden text-sm leading-relaxed text-gray-400">
                                <p>By using the Platform, you confirm your acceptance of these Terms. If you do not agree, you must discontinue use immediately. We reserve the right to modify or update these Terms at any time. Continued use after such updates constitutes acceptance of the revised Terms.</p>
                            </div>
                        </div>

                        <div class="accordion-item border border-white/10 rounded-xl overflow-hidden bg-white/5">
                            <button class="accordion-header w-full px-6 py-4 flex justify-between items-center font-bold text-lg text-white hover:bg-white/5 transition-colors focus:outline-none">
                                <span>04. Eligibility, Registration & KYC</span>
                                <span class="material-symbols-outlined text-[#D4AF37] transform transition-transform duration-300">expand_more</span>
                            </button>
                            <div class="accordion-body px-6 pb-4 hidden text-sm leading-relaxed text-gray-400">
                                <p>To use GOLDe5 services, you must be at least 18 years of age, legally capable of entering into binding contracts, and provide accurate and complete registration details. KYC, identity verification, and AML checks are mandatory and may include submission of government-issued identification, PAN, Aadhaar with consent, and other documents.</p>
                            </div>
                        </div>

                        <div class="accordion-item border border-white/10 rounded-xl overflow-hidden bg-white/5">
                            <button class="accordion-header w-full px-6 py-4 flex justify-between items-center font-bold text-lg text-white hover:bg-white/5 transition-colors focus:outline-none">
                                <span>05. Account Security & Responsibility</span>
                                <span class="material-symbols-outlined text-[#D4AF37] transform transition-transform duration-300">expand_more</span>
                            </button>
                            <div class="accordion-body px-6 pb-4 hidden text-sm leading-relaxed text-gray-400">
                                <p>Users are solely responsible for maintaining the confidentiality of their login credentials and account access. You agree not to share passwords, OTPs, or access details and to immediately notify us of any unauthorized activity. GOLDe5 shall not be liable for losses arising due to user negligence or unauthorized access.</p>
                            </div>
                        </div>

                        <div class="accordion-item border border-white/10 rounded-xl overflow-hidden bg-white/5">
                            <button class="accordion-header w-full px-6 py-4 flex justify-between items-center font-bold text-lg text-white hover:bg-white/5 transition-colors focus:outline-none">
                                <span>06. Execution-Only Model</span>
                                <span class="material-symbols-outlined text-[#D4AF37] transform transition-transform duration-300">expand_more</span>
                            </button>
                            <div class="accordion-body px-6 pb-4 hidden text-sm leading-relaxed text-gray-400">
                                <p>GOLDe5 operates strictly as an execution-only platform. All decisions relating to purchase, sale, holding, or redemption are made independently by users at their own discretion. GOLDe5 does not influence, recommend, or advise users on financial decisions.</p>
                            </div>
                        </div>
                        
                        <div class="accordion-item border border-white/10 rounded-xl overflow-hidden bg-white/5">
                            <button class="accordion-header w-full px-6 py-4 flex justify-between items-center font-bold text-lg text-white hover:bg-white/5 transition-colors focus:outline-none">
                                <span>07. Purchase, Sale & Pricing</span>
                                <span class="material-symbols-outlined text-[#D4AF37] transform transition-transform duration-300">expand_more</span>
                            </button>
                            <div class="accordion-body px-6 pb-4 hidden text-sm leading-relaxed text-gray-400">
                                <p>All metal prices displayed on the Platform are market-linked, dynamic, and subject to real-time fluctuations. Orders are confirmed only after successful payment processing. Prices may include applicable taxes, storage fees, and delivery charges. GOLDe5 does not guarantee price stability or appreciation.</p>
                            </div>
                        </div>

                        <div class="accordion-item border border-white/10 rounded-xl overflow-hidden bg-white/5">
                            <button class="accordion-header w-full px-6 py-4 flex justify-between items-center font-bold text-lg text-white hover:bg-white/5 transition-colors focus:outline-none">
                                <span>08-32. Continued Terms</span>
                                <span class="material-symbols-outlined text-[#D4AF37] transform transition-transform duration-300">expand_more</span>
                            </button>
                            <div class="accordion-body px-6 pb-4 hidden text-sm leading-relaxed text-gray-400 space-y-4">
                                <p><strong>08. Nature of Holdings & Ownership:</strong> User holdings may include allocated physical metals stored securely in vaults or digital/value-linked representations backed by underlying assets...</p>
                                <p><strong>09. No Collective Investment Scheme:</strong> GOLDe5 does not operate any collective investment scheme. User holdings are maintained individually...</p>
                                <p><strong>10. Platform Function & Asset Handling:</strong> GOLDe5 facilitates transactions and may undertake backend activities such as procurement, inventory management, hedging...</p>
                                <p><strong>11. Market Exposure Clarification:</strong> GOLDe5 may maintain operational exposure to metal-linked markets or instruments...</p>
                                <p><strong>12. Storage, Vaulting & Insurance:</strong> All physical metals are stored in secure vaults managed by authorized partners...</p>
                                <p><strong>13. Delivery & Redemption:</strong> Users may request cash redemption or physical delivery subject to conditions...</p>
                                <p><strong>14. Liquidity & Redemption Risk:</strong> While GOLDe5 aims to provide continuous liquidity, redemption availability is not guaranteed...</p>
                                <p><strong>15. No Assured Returns:</strong> GOLDe5 does not provide fixed, guaranteed, or assured returns...</p>
                                <p><strong>16. Value Fluctuation & Risk Disclosure:</strong> Precious metals are subject to global price volatility...</p>
                                <p><strong>17-21:</strong> No Investment Advice, Fees & Taxes, Promotions, Third-Party Providers, Privacy...</p>
                                <p><strong>22-25:</strong> Liability Limitation, Indemnity, Force Majeure, Suspension & Termination...</p>
                                <p><strong>26-32:</strong> Dispute Resolution, Governing Law, IP, Official Comm, Electronic Acceptance, Severability, Entire Agreement. These Terms and the Privacy Policy form the complete agreement.</p>
                            </div>
                        </div>

                    </div>

                    <!-- TAB 2: PRIVACY -->
                    <div id="content-privacy" class="tab-content hidden space-y-4">
                        <div class="mb-8">
                            <h2 class="text-2xl font-bold font-headline text-white mb-2">Privacy Policy</h2>
                            <p class="text-sm text-gray-500 font-medium">Last updated: April 14, 2026</p>
                            <p class="mt-4 text-sm leading-relaxed">This Privacy Policy explains how GOLDe5 collects, uses, stores, processes, and protects user information...</p>
                        </div>
                        
                        <div class="accordion-item border border-white/10 rounded-xl overflow-hidden bg-white/5">
                            <button class="accordion-header w-full px-6 py-4 flex justify-between items-center font-bold text-lg text-white hover:bg-white/5 transition-colors focus:outline-none">
                                <span>01. Information We Collect</span>
                                <span class="material-symbols-outlined text-[#D4AF37] transform transition-transform duration-300">expand_more</span>
                            </button>
                            <div class="accordion-body px-6 pb-4 hidden text-sm leading-relaxed text-gray-400">
                                <p>We may collect personal and non-personal information including name, mobile number, email address, date of birth, PAN, Aadhaar with consent, bank account details, transaction data, device information, IP address, and usage patterns.</p>
                            </div>
                        </div>
                        
                        <div class="accordion-item border border-white/10 rounded-xl overflow-hidden bg-white/5">
                            <button class="accordion-header w-full px-6 py-4 flex justify-between items-center font-bold text-lg text-white hover:bg-white/5 transition-colors focus:outline-none">
                                <span>02. Purpose of Data Collection</span>
                                <span class="material-symbols-outlined text-[#D4AF37] transform transition-transform duration-300">expand_more</span>
                            </button>
                            <div class="accordion-body px-6 pb-4 hidden text-sm leading-relaxed text-gray-400">
                                <p>Information is collected for purposes including account creation, identity verification, regulatory compliance, transaction processing, customer support, fraud prevention, service improvement, communication, and legal obligations.</p>
                            </div>
                        </div>

                        <div class="accordion-item border border-white/10 rounded-xl overflow-hidden bg-white/5">
                            <button class="accordion-header w-full px-6 py-4 flex justify-between items-center font-bold text-lg text-white hover:bg-white/5 transition-colors focus:outline-none">
                                <span>03. Legal Basis & Details</span>
                                <span class="material-symbols-outlined text-[#D4AF37] transform transition-transform duration-300">expand_more</span>
                            </button>
                            <div class="accordion-body px-6 pb-4 hidden text-sm leading-relaxed text-gray-400 space-y-4">
                                <p><strong>3. Legal Basis for Processing:</strong> We process personal data based on user consent, contractual necessity, legal compliance obligations, and legitimate business interests.</p>
                                <p><strong>4. KYC and Regulatory Compliance:</strong> To comply with applicable laws, including anti-money laundering and financial regulations, users are required to complete KYC verification.</p>
                                <p><strong>5. Data Sharing and Disclosure:</strong> We may share user data with trusted third parties... We do not sell or rent personal data to third parties.</p>
                                <p><strong>6. Data Storage and Security:</strong> User data is stored on secure servers with appropriate technical and organizational safeguards...</p>
                                <p><strong>7-15:</strong> Data Retention, User Rights, Cookies, Cross-Border Data Transfer, Third-Party Links, Children's Privacy, Data Breach Notification, Policy Updates, Contact.</p>
                            </div>
                        </div>
                    </div>

                    <!-- TAB 3: CYBER -->
                    <div id="content-cyber" class="tab-content hidden space-y-4">
                        <div class="mb-8">
                            <h2 class="text-2xl font-bold font-headline text-white mb-2">Cyber Fraud Advisory</h2>
                            <p class="text-sm text-gray-500 font-medium">Last updated: April 14, 2026</p>
                            <p class="mt-4 text-sm leading-relaxed">GOLDe5 is committed to ensuring the safety and security of its users. With the increasing risk of digital fraud, users are advised to remain vigilant and follow safe practices while using financial and digital platforms.</p>
                        </div>

                        <div class="accordion-item border border-white/10 rounded-xl overflow-hidden bg-white/5">
                            <button class="accordion-header w-full px-6 py-4 flex justify-between items-center font-bold text-lg text-white hover:bg-white/5 transition-colors focus:outline-none">
                                <span>01. Official Communication Policy</span>
                                <span class="material-symbols-outlined text-[#D4AF37] transform transition-transform duration-300">expand_more</span>
                            </button>
                            <div class="accordion-body px-6 pb-4 hidden text-sm leading-relaxed text-gray-400">
                                <p>GOLDe5 communicates only through officially registered channels such as the mobile application, verified email addresses, and official customer support. Any communication from unknown or unverified sources should be treated as suspicious.</p>
                            </div>
                        </div>
                        
                        <div class="accordion-item border border-white/10 rounded-xl overflow-hidden bg-white/5">
                            <button class="accordion-header w-full px-6 py-4 flex justify-between items-center font-bold text-lg text-white hover:bg-white/5 transition-colors focus:outline-none">
                                <span>02. We Will Never Ask For</span>
                                <span class="material-symbols-outlined text-[#D4AF37] transform transition-transform duration-300">expand_more</span>
                            </button>
                            <div class="accordion-body px-6 pb-4 hidden text-sm leading-relaxed text-gray-400">
                                <p>GOLDe5 will never request users to share passwords, OTPs, PINs, CVV numbers, or full bank details through calls, messages, emails, or social media. Any such request is fraudulent.</p>
                            </div>
                        </div>
                        
                        <div class="accordion-item border border-white/10 rounded-xl overflow-hidden bg-white/5">
                            <button class="accordion-header w-full px-6 py-4 flex justify-between items-center font-bold text-lg text-white hover:bg-white/5 transition-colors focus:outline-none">
                                <span>03. Fraud Protection Guidelines</span>
                                <span class="material-symbols-outlined text-[#D4AF37] transform transition-transform duration-300">expand_more</span>
                            </button>
                            <div class="accordion-body px-6 pb-4 hidden text-sm leading-relaxed text-gray-400 space-y-4">
                                <p><strong>3. Fake Apps and Websites:</strong> Users should download the GOLDe5 application only from official app stores...</p>
                                <p><strong>4. Payment Safety:</strong> All payments must be made only through official payment gateways...</p>
                                <p><strong>5. Account Security Practices:</strong> Use strong passwords, enable device-level security...</p>
                                <p><strong>6. Social Engineering:</strong> Fraudsters may impersonate company representatives...</p>
                                <p><strong>7. No Guaranteed Returns:</strong> GOLDe5 does not offer fixed, assured, or guaranteed returns...</p>
                                <p><strong>8-10:</strong> Reporting Fraud, Limitation of Liability, User Responsibility to safeguard account credentials.</p>
                            </div>
                        </div>
                    </div>

                    <!-- TAB 4: DISCLAIMER -->
                    <div id="content-disclaimer" class="tab-content hidden space-y-4">
                        <div class="mb-8">
                            <h2 class="text-2xl font-bold font-headline text-white mb-2">Disclaimer</h2>
                            <p class="text-sm text-gray-500 font-medium">Last updated: April 14, 2026</p>
                            <p class="mt-4 text-sm leading-relaxed">The information provided on the GOLDe5 Platform, including its website, mobile application, and associated services, is for general informational and transactional purposes only. By accessing or using the Platform, you acknowledge and agree to the terms set forth in this Disclaimer.</p>
                        </div>
                        
                        <div class="accordion-item border border-white/10 rounded-xl overflow-hidden bg-white/5">
                            <button class="accordion-header w-full px-6 py-4 flex justify-between items-center font-bold text-lg text-white hover:bg-white/5 transition-colors focus:outline-none">
                                <span>01. No Investment Advice</span>
                                <span class="material-symbols-outlined text-[#D4AF37] transform transition-transform duration-300">expand_more</span>
                            </button>
                            <div class="accordion-body px-6 pb-4 hidden text-sm leading-relaxed text-gray-400">
                                <p>GOLDe5 does not provide investment, financial, legal, or tax advice. All content, data, and materials available on the Platform are intended solely for general information and should not be construed as professional advice or recommendations. Users are encouraged to consult qualified professionals before making financial decisions.</p>
                            </div>
                        </div>
                        
                        <div class="accordion-item border border-white/10 rounded-xl overflow-hidden bg-white/5">
                            <button class="accordion-header w-full px-6 py-4 flex justify-between items-center font-bold text-lg text-white hover:bg-white/5 transition-colors focus:outline-none">
                                <span>02. Regulatory Disclosures</span>
                                <span class="material-symbols-outlined text-[#D4AF37] transform transition-transform duration-300">expand_more</span>
                            </button>
                            <div class="accordion-body px-6 pb-4 hidden text-sm leading-relaxed text-gray-400 space-y-4">
                                <p><strong>2. Execution-Only Platform:</strong> GOLDe5 operates as a technology-enabled execution platform facilitating transactions in precious metals...</p>
                                <p><strong>3. No SEBI Registration or Regulation:</strong> GOLDe5 is not registered with the Securities and Exchange Board of India (SEBI)...</p>
                                <p><strong>4. No Guaranteed Returns:</strong> GOLDe5 does not guarantee any returns, profits, or income...</p>
                                <p><strong>5. Market Risk Disclosure:</strong> Investments or holdings in precious metals are subject to market risks...</p>
                                <p><strong>6-14:</strong> Nature of Products, No Collective Investment Scheme, Third-Party Dependencies, Accuracy of Information, Limitation of Liability, User Responsibility, Regulatory and Legal Compliance, Forward-Looking Statements, Consent and Acceptance.</p>
                            </div>
                        </div>
                    </div>

                </div>
                
                <div class="absolute bottom-0 left-0 w-full h-12 bg-gradient-to-t from-[#0B0B0B] to-transparent pointer-events-none rounded-b-[1.5rem]"></div>
            </div>

            <!-- LEGAL AGREEMENT SECTION (CRITICAL) -->
            <div class="mt-8 border border-[#D4AF37]/40 rounded-2xl p-6 bg-[#D4AF37]/5 shadow-[0_0_20px_rgba(212,175,55,0.1)] ux-reveal" style="animation-delay: 0.2s;">
                <label class="flex items-start gap-4 cursor-pointer group">
                    <div class="relative flex items-center justify-center shrink-0 mt-1">
                        <input type="checkbox" id="legal-checkbox" class="w-6 h-6 border-2 border-[#D4AF37]/50 rounded bg-[#0B0B0B] checked:bg-[#D4AF37] checked:border-[#D4AF37] hover:border-[#D4AF37] transition-all cursor-pointer peer appearance-none" disabled onchange="validateAcceptance()">
                        <span class="material-symbols-outlined absolute text-[#0B0B0B] text-[18px] opacity-0 peer-checked:opacity-100 pointer-events-none font-bold">check</span>
                    </div>
                    <span class="text-sm md:text-base text-gray-300 font-medium leading-relaxed">
                        I acknowledge that I have carefully reviewed and fully understood the Terms &amp; Conditions, Privacy Policy, Disclaimer, and Cyber Fraud Advisory, and I agree to be legally bound by them.
                    </span>
                </label>
                <div id="scroll-error" class="ml-10 mt-2 text-xs font-bold text-[#D4AF37] animate-pulse">Required: Please scroll through the documents to read them entirely before accepting.</div>
                <div id="acceptance-error" class="ml-10 mt-2 text-xs font-bold text-red-400 hidden">You must accept the terms to continue.</div>
            </div>

            <!-- CTA BUTTON -->
            <div class="mt-8 text-center sm:text-right ux-reveal" style="animation-delay: 0.3s;">
                <button id="agree-btn" onclick="submitAgreement()" class="w-full sm:w-auto px-12 py-4 rounded-xl font-headline font-extrabold text-lg tracking-widest transition-all duration-300 bg-gray-800 text-gray-500 cursor-not-allowed border border-gray-700" disabled>
                    I AGREE
                </button>
            </div>
            
        </section>

        <!-- TRUST SECTION (RE-USED) -->
        <section class="max-w-7xl mx-auto px-6 md:px-8 py-16 grid grid-cols-1 md:grid-cols-4 gap-6 ux-reveal" style="animation-delay: 0.4s;">
            <div class="glass-card rounded-xl p-6 text-center space-y-4 border border-[#D4AF37]/20">
                <span class="material-symbols-outlined text-[#D4AF37] text-3xl">local_police</span>
                <h4 class="font-bold text-white tracking-wide">Secure Platform</h4>
            </div>
            <div class="glass-card rounded-xl p-6 text-center space-y-4 border border-[#D4AF37]/20">
                <span class="material-symbols-outlined text-[#D4AF37] text-3xl">account_balance</span>
                <h4 class="font-bold text-white tracking-wide">RBI-Compliant Partners</h4>
            </div>
            <div class="glass-card rounded-xl p-6 text-center space-y-4 border border-[#D4AF37]/20">
                <span class="material-symbols-outlined text-[#D4AF37] text-3xl">inventory_2</span>
                <h4 class="font-bold text-white tracking-wide">Insured Vault Storage</h4>
            </div>
            <div class="glass-card rounded-xl p-6 text-center space-y-4 border border-[#D4AF37]/20">
                <span class="material-symbols-outlined text-[#D4AF37] text-3xl">policy</span>
                <h4 class="font-bold text-white tracking-wide">Transparent Policies</h4>
            </div>
        </section>

        <!-- CSS & JS FOR ACCORDIONS & TABS -->
        <style>
            .accordion-body { max-height: 0; opacity: 0; padding-top: 0; padding-bottom: 0; overflow: hidden; transition: all 0.4s cubic-bezier(0.2, 0.8, 0.2, 1); display: block !important; }
            .accordion-open .accordion-body { max-height: 1000px; opacity: 1; padding-top: 1rem; padding-bottom: 1rem; }
            .accordion-open .accordion-header span.material-symbols-outlined { transform: rotate(180deg); }
            
            .tab-btn.active { background: linear-gradient(135deg, #D4AF37 0%, #F2CA50 50%, #E6C65C 100%); color: #111; border-color: transparent; box-shadow: 0 0 15px rgba(212,175,55,0.3); }
            .hide-scrollbar::-webkit-scrollbar { display: none; }
            .hide-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
            
            .custom-scrollbar::-webkit-scrollbar { display: block; width: 6px; }
            .custom-scrollbar::-webkit-scrollbar-track { background: rgba(255,255,255,0.05); border-radius: 10px; }
            .custom-scrollbar::-webkit-scrollbar-thumb { background: rgba(212,175,55,0.5); border-radius: 10px; }
        </style>

        <script>
            // Tab Switching Logic
            function switchTab(tabId) {
                // Remove active from all tabs & contents
                document.querySelectorAll('.tab-btn').forEach(b => {
                    b.classList.remove('active', 'bullion-gradient', 'text-[#111]', 'shadow-[0_0_15px_rgba(212,175,55,0.3)]');
                    b.classList.add('bg-white/5', 'text-gray-400');
                });
                document.querySelectorAll('.tab-content').forEach(c => {
                    c.classList.add('hidden');
                    c.classList.remove('active');
                });
                
                // Add active to selected
                const btn = document.getElementById('tab-' + tabId);
                btn.classList.add('active', 'bullion-gradient', 'text-[#111]', 'shadow-[0_0_15px_rgba(212,175,55,0.3)]');
                btn.classList.remove('bg-white/5', 'text-gray-400');
                
                const content = document.getElementById('content-' + tabId);
                content.classList.remove('hidden');
                content.classList.add('active');
                
                // Reset scroll tracking per tab just to be safe, but global check applies.
                updateScrollProgress();
            }

            // Accordion Logic
            document.querySelectorAll('.accordion-header').forEach(button => {
                button.addEventListener('click', () => {
                    const item = button.parentElement;
                    const isOpen = item.classList.contains('accordion-open');
                    
                    // Close all
                    document.querySelectorAll('.accordion-item').forEach(i => i.classList.remove('accordion-open'));
                    
                    // Open clicked if it wasn't open
                    if(!isOpen) {
                        item.classList.add('accordion-open');
                    }
                    
                    // Open accordion forces container scroll event update
                    setTimeout(updateScrollProgress, 400);
                });
            });

            // Scroll-to-Accept Logic
            let hasScrolledToBottom = false;
            function updateScrollProgress() {
                const container = document.getElementById('scroll-container');
                const progress = document.getElementById('scroll-progress');
                
                // Calculate percentage
                const scrollHeight = container.scrollHeight - container.clientHeight;
                let scrollPercent = 0;
                if (scrollHeight > 0) {
                    scrollPercent = (container.scrollTop / scrollHeight) * 100;
                } else {
                    scrollPercent = 100; // If content is too short to scroll
                }
                
                progress.style.width = scrollPercent + "%";
                
                // Unlock checkbox if reached > 95%
                if (scrollPercent > 95 && !hasScrolledToBottom) {
                    hasScrolledToBottom = true;
                    document.getElementById('legal-checkbox').disabled = false;
                    document.getElementById('scroll-error').style.display = 'none';
                    
                    // Bounce animation to draw attention
                    const checkboxDiv = document.querySelector('#legal-checkbox').parentElement;
                    checkboxDiv.classList.add('animate-bounce');
                    setTimeout(() => checkboxDiv.classList.remove('animate-bounce'), 2000);
                }
            }

            // Validation Logic
            function validateAcceptance() {
                const checkbox = document.getElementById('legal-checkbox');
                const btn = document.getElementById('agree-btn');
                const error = document.getElementById('acceptance-error');
                
                if(checkbox.checked) {
                    btn.disabled = false;
                    btn.classList.remove('bg-gray-800', 'text-gray-500', 'cursor-not-allowed', 'border-gray-700');
                    btn.classList.add('bullion-gradient', 'text-[#111]', 'shadow-[0_0_25px_rgba(212,175,55,0.6)]', 'active:scale-95', 'hover:brightness-110');
                    error.classList.add('hidden');
                } else {
                    btn.disabled = true;
                    btn.classList.add('bg-gray-800', 'text-gray-500', 'cursor-not-allowed', 'border-gray-700');
                    btn.classList.remove('bullion-gradient', 'text-[#111]', 'shadow-[0_0_25px_rgba(212,175,55,0.6)]', 'active:scale-95', 'hover:brightness-110');
                }
            }

            function submitAgreement() {
                const checkbox = document.getElementById('legal-checkbox');
                const error = document.getElementById('acceptance-error');
                
                if(!checkbox.checked) {
                    error.classList.remove('hidden');
                } else {
                    // Redirect logic here
                    window.location.href = 'index.html'; // Or dashboard onboarding
                }
            }

            // Initial calculations
            setTimeout(() => {
                updateScrollProgress();
                // If the container is too tall, forcefully expand the first accordion
                const firstAccordion = document.querySelector('.accordion-item');
                if(firstAccordion) firstAccordion.classList.add('accordion-open');
            }, 100);
        </script>
"""

# Fetch index.html to wrap the content
index_path = r"c:\Users\LENOVO\OneDrive\Desktop\Golde4\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    template = f.read()

# Isolate the <main> block boundaries
header_match = re.search(r'^(.*?)<main[^>]*>', template, re.DOTALL | re.IGNORECASE)
if header_match:
    header = header_match.group(0)
    
    footer_match = re.search(r'</main>(.*)$', template, re.DOTALL | re.IGNORECASE)
    if footer_match:
        footer = footer_match.group(1)
        
        # Build terms page
        terms_html = header + "\n" + TERMS_CONTENT + "\n</main>" + footer
        
        # update title
        terms_html = terms_html.replace("<title>GOLDe5 | Premium Wealth Management</title>", "<title>Terms & Conditions - GOLDe5 Legal</title>")
        
        # save
        out_path = r"c:\Users\LENOVO\OneDrive\Desktop\Golde4\terms.html"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(terms_html)
        print("Successfully created terms.html")
    else:
        print("Could not find </main>")
else:
    print("Could not find <main>")
