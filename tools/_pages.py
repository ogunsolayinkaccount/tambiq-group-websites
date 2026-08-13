\
# -*- coding: utf-8 -*-
from _build import write, page, division_hero, status_badge, section_header, DIVISIONS, EMAIL_DOMAIN

P2 = "../../"  # prefix for depth-2 pages (companies/x/)
P1 = "../"     # prefix for depth-1 pages

def simple_section(eyebrow, title, paragraphs, bg="", center=True, extra_id=""):
    ps = "\n          ".join(f'<p class="reveal text-gray-600 dark:text-gray-300 leading-relaxed mb-4 last:mb-0">{p}</p>' for p in paragraphs)
    align = "text-center" if center else ""
    idattr = f' id="{extra_id}"' if extra_id else ""
    return f'''    <section{idattr} class="py-16 sm:py-20{(' ' + bg) if bg else ''}">
      <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 {align}">
        <p class="reveal text-xs font-semibold tracking-[0.25em] uppercase text-gold-600 dark:text-gold-400 mb-4">{eyebrow}</p>
        <h2 class="reveal font-serif text-2xl sm:text-3xl font-bold mb-6">{title}</h2>
        {ps}
      </div>
    </section>'''

def card_grid_section(eyebrow, title, subtitle, cards, cols="sm:grid-cols-2 lg:grid-cols-3", bg="", extra_id=""):
    card_html = []
    for c_title, c_body in cards:
        card_html.append(f'''<div class="rounded-2xl p-6 bg-white dark:bg-ink border border-black/5 dark:border-white/10">
            <h3 class="font-serif font-bold text-lg mb-2">{c_title}</h3>
            <p class="text-sm text-gray-600 dark:text-gray-300 leading-relaxed">{c_body}</p>
          </div>''')
    cards_joined = "\n          ".join(card_html)
    idattr = f' id="{extra_id}"' if extra_id else ""
    sub = f'<p class="reveal text-gray-600 dark:text-gray-300 max-w-2xl mx-auto mt-4">{subtitle}</p>' if subtitle else ""
    return f'''    <section{idattr} class="py-16 sm:py-20{(' ' + bg) if bg else ' bg-gray-50 dark:bg-ink-800'}">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="reveal text-center max-w-2xl mx-auto mb-12">
          <p class="text-xs font-semibold tracking-[0.25em] uppercase text-gold-600 dark:text-gold-400 mb-4">{eyebrow}</p>
          <h2 class="font-serif text-2xl sm:text-3xl font-bold">{title}</h2>
          {sub}
        </div>
        <div class="reveal grid {cols} gap-6">
          {cards_joined}
        </div>
      </div>
    </section>'''

def cta_section(title, body, cta_label, cta_href, dark=True):
    bg = "bg-ink text-white" if dark else "bg-gray-50 dark:bg-ink-800"
    btn = "bg-gold-500 text-ink hover:bg-gold-400" if dark else "bg-ink text-white dark:bg-gold-500 dark:text-ink hover:opacity-90"
    grid = '<div class="absolute inset-0 bg-grid opacity-40"></div>' if dark else ""
    return f'''    <section class="py-16 sm:py-20 {bg} relative overflow-hidden">
      {grid}
      <div class="relative max-w-2xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 class="reveal font-serif text-2xl sm:text-3xl font-bold mb-4">{title}</h2>
        <p class="reveal {'text-gray-300' if dark else 'text-gray-600 dark:text-gray-300'} mb-8">{body}</p>
        <a href="{cta_href}" class="reveal inline-block px-7 py-3.5 rounded-full {btn} font-semibold transition-colors">{cta_label}</a>
      </div>
    </section>'''

# ---------------------------------------------------------------------------
# Companies overview page
# ---------------------------------------------------------------------------
company_cards = []
icons = {
    "construction": '<path d="M3 21h18M5 21V9l7-5 7 5v12M9 21v-6h6v6"/>',
    "properties": '<path d="M3 11l9-7 9 7M5 10v10h5v-6h4v6h5V10"/>',
    "auto": '<path d="M5 11l1.5-5h11L19 11M5 11h14M5 11v7h14v-7"/><circle cx="8.5" cy="18" r="1.6"/><circle cx="15.5" cy="18" r="1.6"/>',
    "logistics": '<path d="M3 17h9V6H3v11zM12 10h5l4 4v3h-9v-7z"/><circle cx="7" cy="19" r="1.6"/><circle cx="17" cy="19" r="1.6"/>',
    "recreation": '<path d="M6.5 6.5a3 3 0 013-3H8v6h-.5a3 3 0 01-3-3zM17.5 6.5a3 3 0 00-3-3H16v6h.5a3 3 0 003-3zM8 6.5h8M12 9.5v5m0 0c-2 0-3.5 1-3.5 3h7c0-2-1.5-3-3.5-3z"/>',
    "fashion": '<path d="M9 4a3 3 0 006 0M5 7l4-3h6l4 3-3 3v11H8V10L5 7z"/>',
    "marketplace": '<path d="M4 8l1.5-4h13L20 8M4 8h16M4 8l1 12h14l1-12M9 12a3 3 0 006 0"/>',
}
statuses = {
    "construction": "development", "properties": "development", "auto": "planning",
    "logistics": "planning", "recreation": "development", "fashion": "planning", "marketplace": "planning",
}
descs = {
    "construction": "Construction, project delivery, project controls, scheduling, development support, and related construction services.",
    "properties": "Real estate acquisition, development, investment analysis, property technology, and property opportunities.",
    "auto": "Automotive sales, dealership operations, vehicle sourcing, and future mobility-related services.",
    "logistics": "Transportation, logistics coordination, commercial delivery, and supply-chain services.",
    "recreation": "Indoor sports, recreation centers, community-focused entertainment, food, and leisure concepts.",
    "fashion": "Fashion, apparel, lifestyle products, sourcing, and retail concepts.",
    "marketplace": "Digital commerce, products, services, and future TambiQ consumer marketplace initiatives.",
}
for slug, name, tag, icon in DIVISIONS:
    span = " sm:col-span-2 lg:col-span-1" if slug == "marketplace" else ""
    company_cards.append(f'''<a href="{slug}/" class="reveal group rounded-2xl bg-white dark:bg-ink border border-black/5 dark:border-white/10 p-7 hover:shadow-xl hover:-translate-y-1 transition-all flex flex-col{span}">
            <div class="flex items-start justify-between mb-5">
              <div class="h-12 w-12 rounded-xl bg-gold-500/10 flex items-center justify-center text-gold-600 dark:text-gold-400"><svg class="h-6 w-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{icons[slug]}</svg></div>
              {status_badge(statuses[slug], "")}
            </div>
            <h3 class="font-serif font-bold text-lg mb-1.5">{name}</h3>
            <p class="text-sm text-gray-600 dark:text-gray-300 mb-5 flex-1">{descs[slug]}</p>
            <span class="inline-flex items-center gap-1.5 text-sm font-semibold text-gold-600 dark:text-gold-400">Explore <svg class="h-4 w-4 transition-transform group-hover:translate-x-1" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span>
          </a>''')

companies_body = f'''    <section class="relative bg-ink text-white overflow-hidden pt-32 pb-20 sm:pt-40 sm:pb-24">
      <div class="absolute inset-0 bg-grid opacity-60"></div>
      <div class="relative max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <p class="reveal text-xs sm:text-sm font-semibold tracking-[0.25em] uppercase text-gold-400 mb-5">Our Portfolio</p>
        <h1 class="reveal font-serif font-bold text-4xl sm:text-5xl leading-[1.1] mb-6">Our Companies</h1>
        <p class="reveal text-base sm:text-lg text-gray-300 max-w-2xl mx-auto">Seven independently operated companies spanning construction, real estate, automotive, logistics, recreation, fashion, and commerce — each built to the same standard of excellence.</p>
      </div>
    </section>
    <section class="py-16 sm:py-20">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {"".join(company_cards)}
        </div>
      </div>
    </section>
{cta_section("Curious How It All Fits Together?", "See how our divisions are designed to support one another across the property, construction, and commerce lifecycle.", "View The TambiQ Ecosystem", P1 + "#ecosystem")}'''

write("companies/index.html", page(
    "Our Companies — TambiQ Group LLC",
    "Explore the seven independently operated companies of TambiQ Group LLC: Construction, Properties, Auto, Logistics, Recreation, Fashion, and Marketplace.",
    "/companies/", P1, "companies", companies_body
))

# ---------------------------------------------------------------------------
# TambiQ Construction
# ---------------------------------------------------------------------------
construction_body = division_hero(
    "TambiQ Construction", "TambiQ Construction",
    "Construction, project delivery, project controls, scheduling, development support, and related construction services.",
    "development"
) + f'''
{simple_section("Overview", "Building With Discipline and Control", [
    "TambiQ Construction is TambiQ Group's construction and project delivery division, focused on bringing discipline, scheduling rigor, and cost control to every phase of a build.",
    "The division is currently in active development, building out its team, processes, and initial project pipeline."
])}
{card_grid_section("Services", "What We Do", "", [
    ("General Contracting", "Coordinating trades, materials, and schedules to deliver projects on time and on budget."),
    ("Design-Build", "Integrated design and construction delivery under a single point of accountability."),
    ("Construction Management", "Owner's-representative oversight of budget, schedule, quality, and risk."),
    ("Development Support", "Pre-development feasibility, constructability review, and planning support for TambiQ Properties and outside owners."),
])}
{card_grid_section("Our Edge", "Project Controls &amp; Scheduling", "We treat project controls and scheduling as a core capability, not an afterthought.", [
    ("Preconstruction", "Estimating, constructability review, and value engineering before ground is broken."),
    ("Project Controls", "Structured cost and schedule tracking designed to catch variance early, not after the fact."),
    ("Scheduling", "Critical-path scheduling to sequence trades and keep projects moving predictably."),
    ("Project Delivery", "Clear delivery milestones and accountability from mobilization to closeout."),
], bg="")}
{simple_section("Projects", "Project Portfolio", [
    'TambiQ Construction does not yet have completed or in-progress projects to publish. As real projects are underway, they will be featured here and on the <a class="text-gold-600 dark:text-gold-400 hover:underline" href="' + P2 + 'projects/">Projects &amp; Investments</a> page.'
])}
{cta_section("Have a Project in Mind?", "Reach out to discuss a construction project or development support need.", "Request a Consultation", P2 + "contact/?division=construction")}'''

write("companies/construction/index.html", page(
    "TambiQ Construction — Project Delivery &amp; Project Controls",
    "TambiQ Construction provides general contracting, design-build, construction management, project controls, and scheduling services.",
    "/companies/construction/", P2, "companies", construction_body
))

# ---------------------------------------------------------------------------
# TambiQ Properties
# ---------------------------------------------------------------------------
properties_body = division_hero(
    "TambiQ Properties", "TambiQ Properties",
    "Real estate acquisition, development, investment analysis, property technology, and property opportunities.",
    "development"
) + f'''
{simple_section("Overview", "Real Estate, Analyzed and Acquired With Discipline", [
    "TambiQ Properties is TambiQ Group's real estate division, focused on acquisition, development, and investment analysis across residential and commercial property.",
    "The division is in active development, building out its acquisition criteria, analysis tools, and initial property pipeline."
])}
{card_grid_section("What We Do", "Acquisition, Development &amp; Investment", "", [
    ("Acquisition", "Sourcing and underwriting residential and commercial property acquisitions."),
    ("Development", "Ground-up and value-add development, coordinated closely with TambiQ Construction."),
    ("Commercial Real Estate", "Acquisition and management of commercial property assets."),
    ("Investment", "Structuring real estate investments for long-term value creation."),
    ("Property Analysis", "Underwriting and market analysis to evaluate opportunities before capital is committed."),
    ("Investor Tools", "Tools and resources to help investors evaluate real estate opportunities, in development."),
])}
{card_grid_section("Opportunity Types", "Tax Lien, Tax Deed &amp; Foreclosure Opportunities", "TambiQ Properties is building out sourcing capability across these opportunity types. None are currently available to the public.", [
    ("Tax Lien Opportunities", "Tax lien sourcing and evaluation — in development."),
    ("Tax Deed Opportunities", "Tax deed sourcing and evaluation — in development."),
    ("Foreclosure Opportunities", "Foreclosure opportunity sourcing and evaluation — in development."),
], cols="sm:grid-cols-3", bg="")}
    <section class="py-16 sm:py-20 bg-ink text-white relative overflow-hidden">
      <div class="absolute inset-0 bg-grid opacity-40"></div>
      <div class="relative max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <p class="reveal text-xs font-semibold tracking-[0.25em] uppercase text-gold-400 mb-4">Property Search</p>
        <h2 class="reveal font-serif text-2xl sm:text-3xl font-bold mb-4">TambiQ Property Search</h2>
        <p class="reveal text-gray-300 leading-relaxed mb-2">
          A dedicated property search and investor-analysis platform is planned as a separate application,
          intended to be available at <span class="font-mono text-gold-400">properties.tambiqgroup.com</span>.
        </p>
        <p class="reveal text-gray-400 text-sm">This platform has not launched yet. A link will be added here once it is live.</p>
      </div>
    </section>
{cta_section("Have a Property or Investment Opportunity?", "Reach out to discuss an acquisition, development, or investment opportunity.", "Contact TambiQ Properties", P2 + "contact/?division=properties")}'''

write("companies/properties/index.html", page(
    "TambiQ Properties — Real Estate Acquisition &amp; Investment",
    "TambiQ Properties provides real estate acquisition, development, investment analysis, and property opportunities including tax lien, tax deed, and foreclosure sourcing.",
    "/companies/properties/", P2, "companies", properties_body
))

# ---------------------------------------------------------------------------
# TambiQ Auto
# ---------------------------------------------------------------------------
auto_body = division_hero(
    "TambiQ Auto", "TambiQ Auto",
    "Automotive sales, dealership operations, vehicle sourcing, and future mobility-related services.",
    "planning"
) + f'''
{simple_section("Overview", "A Planned Automotive Venture", [
    "TambiQ Auto is a planned division of TambiQ Group focused on automotive sales, dealership operations, and vehicle sourcing.",
    "TambiQ Auto is currently in the planning stage. No dealership license, vehicle inventory, or sales operations currently exist. This page describes the division's intended scope."
])}
{card_grid_section("Planned Services", "What TambiQ Auto Will Offer", "", [
    ("Vehicle Sales", "Planned new and used vehicle sales operations."),
    ("Vehicle Sourcing", "Planned sourcing of vehicle inventory through established acquisition channels."),
    ("Dealership", "A planned dealership operation, pending licensing and setup."),
    ("Commercial Vehicles", "Planned sourcing and sales support for commercial vehicle needs."),
    ("Trade-In / Sell Your Vehicle", "A planned trade-in and vehicle purchase program."),
])}
{cta_section("Interested in TambiQ Auto?", "This division is still in planning. Reach out if you'd like to be kept informed as it develops.", "Contact Us", P2 + "contact/?division=auto")}'''

write("companies/auto/index.html", page(
    "TambiQ Auto — Automotive Sales &amp; Dealership (Planned)",
    "TambiQ Auto is a planned division of TambiQ Group focused on automotive sales, dealership operations, vehicle sourcing, and future mobility services.",
    "/companies/auto/", P2, "companies", auto_body
))

# ---------------------------------------------------------------------------
# TambiQ Logistics
# ---------------------------------------------------------------------------
logistics_body = division_hero(
    "TambiQ Logistics", "TambiQ Logistics",
    "Transportation, logistics coordination, commercial delivery, and supply-chain services.",
    "planning"
) + f'''
{simple_section("Overview", "A Planned Logistics Venture", [
    "TambiQ Logistics is a planned division of TambiQ Group focused on transportation, commercial delivery, and supply-chain coordination.",
    "TambiQ Logistics is currently in the planning stage. No fleet, carrier authority, or delivery operations currently exist. This page describes the division's intended scope."
])}
{card_grid_section("Planned Services", "What TambiQ Logistics Will Offer", "", [
    ("Transportation", "Planned freight and transportation coordination services."),
    ("Commercial Delivery", "Planned commercial delivery services for business customers."),
    ("Fleet Services", "Planned fleet coordination and support, pending equipment and authority."),
    ("Supply Chain Support", "Planned supply-chain coordination support for TambiQ divisions and outside clients."),
    ("Logistics Coordination", "Planned dispatch and logistics coordination capability."),
])}
{cta_section("Have a Logistics Need?", "This division is still in planning. Reach out if you'd like to be kept informed as it develops.", "Request Service Info", P2 + "contact/?division=logistics")}'''

write("companies/logistics/index.html", page(
    "TambiQ Logistics — Transportation &amp; Supply Chain (Planned)",
    "TambiQ Logistics is a planned division of TambiQ Group focused on transportation, commercial delivery, fleet services, and supply-chain support.",
    "/companies/logistics/", P2, "companies", logistics_body
))

# ---------------------------------------------------------------------------
# TambiQ Recreation
# ---------------------------------------------------------------------------
recreation_body = division_hero(
    "TambiQ Recreation", "TambiQ Recreation",
    "Indoor sports, recreation centers, community-focused entertainment, food, and leisure concepts.",
    "development"
) + f'''
{simple_section("Overview", "An Upcoming Community Recreation Venture", [
    "TambiQ Recreation is TambiQ Group's recreation and community-entertainment division, planned around indoor sports and family-friendly leisure concepts.",
    "TambiQ Recreation is in active development and is not yet open to the public. Details below describe the concept as currently planned."
])}
{card_grid_section("Planned Concept", "What TambiQ Recreation Will Offer", "", [
    ("Indoor Soccer", "Planned indoor soccer courts for leagues, open play, and events."),
    ("Table Tennis", "Planned table tennis facilities for casual and competitive play."),
    ("Family Recreation", "Planned family-oriented recreation activities and open-play areas."),
    ("Events", "Planned space for private events, tournaments, and community gatherings."),
    ("Food &amp; Lounge", "Planned food and lounge area within the recreation center."),
    ("Membership", "A planned membership program; pricing and details have not been finalized."),
])}
{simple_section("Future Locations", "Where We're Headed", [
    'No TambiQ Recreation locations are open yet. Location plans will be announced here and on the <a class="text-gold-600 dark:text-gold-400 hover:underline" href="' + P2 + 'news/">News &amp; Insights</a> page as they are finalized.'
], bg="bg-gray-50 dark:bg-ink-800")}
{cta_section("Want Updates on TambiQ Recreation?", "Reach out to be notified as this venture develops and locations are announced.", "Contact Us", P2 + "contact/?division=recreation")}'''

write("companies/recreation/index.html", page(
    "TambiQ Recreation — Indoor Sports &amp; Community Recreation",
    "TambiQ Recreation is an upcoming division of TambiQ Group focused on indoor soccer, table tennis, family recreation, events, and community leisure.",
    "/companies/recreation/", P2, "companies", recreation_body
))

# ---------------------------------------------------------------------------
# TambiQ Fashion
# ---------------------------------------------------------------------------
fashion_body = division_hero(
    "TambiQ Fashion", "TambiQ Fashion",
    "Fashion, apparel, lifestyle products, sourcing, and retail concepts.",
    "planning"
) + f'''
{simple_section("Overview", "A Planned Fashion &amp; Lifestyle Venture", [
    "TambiQ Fashion is a planned division of TambiQ Group focused on apparel, lifestyle products, and retail concepts.",
    "TambiQ Fashion is currently in the planning stage. No products, collections, or retail operations currently exist."
])}
{card_grid_section("Planned Concept", "What TambiQ Fashion Will Offer", "", [
    ("Apparel", "Planned apparel offerings across men's and women's categories."),
    ("Lifestyle", "Planned lifestyle products complementing the core apparel line."),
    ("Collections", "Planned seasonal or thematic collections, once launched."),
    ("Retail", "Planned retail distribution, online and potentially in-person."),
])}
{cta_section("Interested in TambiQ Fashion?", "This division is still in planning. Reach out if you'd like to be kept informed ahead of launch.", "Contact Us", P2 + "contact/?division=fashion")}'''

write("companies/fashion/index.html", page(
    "TambiQ Fashion — Apparel &amp; Lifestyle (Planned)",
    "TambiQ Fashion is a planned division of TambiQ Group focused on apparel, lifestyle products, sourcing, and retail concepts.",
    "/companies/fashion/", P2, "companies", fashion_body
))

# ---------------------------------------------------------------------------
# TambiQ Marketplace
# ---------------------------------------------------------------------------
marketplace_body = division_hero(
    "TambiQ Marketplace", "TambiQ Marketplace",
    "Digital commerce, products, services, and future TambiQ consumer marketplace initiatives.",
    "planning"
) + f'''
{simple_section("Overview", "A Planned Digital Marketplace", [
    "TambiQ Marketplace is a planned division of TambiQ Group focused on digital commerce — bringing products and services from across the TambiQ family of companies, and eventually outside sellers, into one platform.",
    "TambiQ Marketplace is currently in the planning stage. No storefront, seller program, or transactions currently exist."
])}
{card_grid_section("Planned Concept", "What TambiQ Marketplace Will Offer", "", [
    ("Shop", "A planned online storefront for TambiQ products and services."),
    ("Categories", "Planned product and service categories spanning TambiQ's divisions."),
    ("Sellers", "A planned seller program allowing outside vendors to list products, modeled after multi-vendor marketplaces."),
    ("TambiQ Brands", "A planned home for products originating from TambiQ Fashion and other divisions."),
])}
{cta_section("Interested in Selling on TambiQ Marketplace?", "This division is still in planning. Reach out if you'd like to be kept informed ahead of launch.", "Contact Us", P2 + "contact/?division=marketplace")}'''

write("companies/marketplace/index.html", page(
    "TambiQ Marketplace — Digital Commerce (Planned)",
    "TambiQ Marketplace is a planned division of TambiQ Group focused on digital commerce, products, services, and a future consumer marketplace.",
    "/companies/marketplace/", P2, "companies", marketplace_body
))

# ---------------------------------------------------------------------------
# Projects & Investments
# ---------------------------------------------------------------------------
projects_body = f'''    <section class="relative bg-ink text-white overflow-hidden pt-32 pb-20 sm:pt-40 sm:pb-24">
      <div class="absolute inset-0 bg-grid opacity-60"></div>
      <div class="relative max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <p class="reveal text-xs sm:text-sm font-semibold tracking-[0.25em] uppercase text-gold-400 mb-5">Portfolio</p>
        <h1 class="reveal font-serif font-bold text-4xl sm:text-5xl leading-[1.1] mb-6">Projects &amp; Investments</h1>
        <p class="reveal text-base sm:text-lg text-gray-300 max-w-2xl mx-auto">Active and upcoming projects across every TambiQ division, published here as they get underway.</p>
      </div>
    </section>
{simple_section("Current Status", "No Projects Published Yet", [
    "TambiQ Group does not currently have projects to publish. As real projects begin across our divisions, they will appear here with their division, location, status, and timeline.",
    "Each project listing will follow a consistent structure — division, location, status, description, investment type, and timeline — so this page can scale as our portfolio grows."
])}
{cta_section("Have a Project or Investment Opportunity?", "If you're bringing a project, land, or investment opportunity to TambiQ Group, we'd like to hear from you.", "Contact Us", P1 + "contact/?division=properties")}'''

write("projects/index.html", page(
    "Projects &amp; Investments — TambiQ Group LLC",
    "Active and upcoming projects and investments across TambiQ Group's divisions.",
    "/projects/", P1, "projects", projects_body
))

# ---------------------------------------------------------------------------
# Careers
# ---------------------------------------------------------------------------
career_division_cards = "\n          ".join(
    f'<a href="../companies/{slug}/" class="rounded-xl p-5 bg-gray-50 dark:bg-ink-700/40 border border-black/5 dark:border-white/10 hover:shadow-md transition-all"><span class="block font-serif font-bold mb-1">{name}</span><span class="block text-xs text-gray-500 dark:text-gray-400">{tag}</span></a>'
    for slug, name, tag, icon in DIVISIONS
)
careers_body = f'''    <section class="relative bg-ink text-white overflow-hidden pt-32 pb-20 sm:pt-40 sm:pb-24">
      <div class="absolute inset-0 bg-grid opacity-60"></div>
      <div class="relative max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <p class="reveal text-xs sm:text-sm font-semibold tracking-[0.25em] uppercase text-gold-400 mb-5">Careers</p>
        <h1 class="reveal font-serif font-bold text-4xl sm:text-5xl leading-[1.1] mb-6">Join Our Family of Companies</h1>
        <p class="reveal text-base sm:text-lg text-gray-300 max-w-2xl mx-auto">We're building teams across every TambiQ division, from construction to commerce.</p>
      </div>
    </section>
{simple_section("Why TambiQ", "Build Something From the Ground Up", [
    "Joining TambiQ Group means joining a company at an early, formative stage — where the systems, standards, and culture of each division are still being defined.",
    "We're looking for people who want ownership over their work and are motivated by building something durable, not just showing up."
])}
    <section class="py-16 sm:py-20 bg-gray-50 dark:bg-ink-800">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="reveal text-center max-w-2xl mx-auto mb-12">
          <p class="text-xs font-semibold tracking-[0.25em] uppercase text-gold-600 dark:text-gold-400 mb-4">Our Companies</p>
          <h2 class="font-serif text-2xl sm:text-3xl font-bold">Where You Could Work</h2>
        </div>
        <div class="reveal grid sm:grid-cols-2 lg:grid-cols-4 gap-4">
          {career_division_cards}
        </div>
      </div>
    </section>
    <section class="py-16 sm:py-20">
      <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <p class="reveal text-xs font-semibold tracking-[0.25em] uppercase text-gold-600 dark:text-gold-400 mb-4">Open Opportunities</p>
        <h2 class="reveal font-serif text-2xl sm:text-3xl font-bold mb-8">Current Openings</h2>
        <div class="reveal rounded-2xl border border-dashed border-black/15 dark:border-white/15 p-10 text-gray-500 dark:text-gray-400">
          There are currently no published openings. You may submit your information for future opportunities.
        </div>
      </div>
    </section>
{cta_section("Join the Future Talent Network", "Send us your resume and area of interest, and we'll reach out when a relevant opportunity opens.", "Submit Your Information", f"mailto:careers@{EMAIL_DOMAIN}?subject=Future Talent Network")}'''

write("careers/index.html", page(
    "Careers — TambiQ Group LLC",
    "Explore career opportunities across TambiQ Group's family of companies, or join our future talent network.",
    "/careers/", P1, "careers", careers_body
))

# ---------------------------------------------------------------------------
# News & Insights
# ---------------------------------------------------------------------------
news_categories = "\n          ".join(
    f'<span class="px-3 py-1.5 rounded-full text-xs font-semibold uppercase tracking-wider bg-gray-100 dark:bg-white/10 text-gray-500 dark:text-gray-400">{c}</span>'
    for c in ["Company News", "Construction", "Real Estate", "Automotive", "Development", "Community", "Investment"]
)
news_body = f'''    <section class="relative bg-ink text-white overflow-hidden pt-32 pb-20 sm:pt-40 sm:pb-24">
      <div class="absolute inset-0 bg-grid opacity-60"></div>
      <div class="relative max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <p class="reveal text-xs sm:text-sm font-semibold tracking-[0.25em] uppercase text-gold-400 mb-5">News &amp; Insights</p>
        <h1 class="reveal font-serif font-bold text-4xl sm:text-5xl leading-[1.1] mb-6">Latest Updates</h1>
        <p class="reveal text-base sm:text-lg text-gray-300 max-w-2xl mx-auto">Company announcements and updates from across the TambiQ family of companies.</p>
      </div>
    </section>
    <section class="py-16 sm:py-20">
      <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <div class="reveal flex flex-wrap justify-center gap-2 mb-10">
          {news_categories}
        </div>
        <div class="reveal rounded-2xl border border-dashed border-black/15 dark:border-white/15 p-10 text-gray-500 dark:text-gray-400">
          There are no published articles yet. Company news and announcements will appear here as they happen.
        </div>
      </div>
    </section>'''

write("news/index.html", page(
    "News &amp; Insights — TambiQ Group LLC",
    "Company announcements and updates from across the TambiQ Group family of companies.",
    "/news/", P1, "news", news_body
))

# ---------------------------------------------------------------------------
# Contact
# ---------------------------------------------------------------------------
contact_body = f'''    <section class="relative bg-ink text-white overflow-hidden pt-32 pb-20 sm:pt-40 sm:pb-24">
      <div class="absolute inset-0 bg-grid opacity-60"></div>
      <div class="relative max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <p class="reveal text-xs sm:text-sm font-semibold tracking-[0.25em] uppercase text-gold-400 mb-5">Contact</p>
        <h1 class="reveal font-serif font-bold text-4xl sm:text-5xl leading-[1.1] mb-6">Let's Talk</h1>
        <p class="reveal text-base sm:text-lg text-gray-300 max-w-2xl mx-auto">Tell us what you're reaching out about and we'll route it to the right team.</p>
      </div>
    </section>
    <section class="py-16 sm:py-20">
      <div class="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8">
        <form id="contact-form" class="reveal rounded-2xl border border-black/5 dark:border-white/10 bg-gray-50 dark:bg-ink-800 p-6 sm:p-8 space-y-5">
          <div>
            <label for="topic" class="block text-sm font-semibold mb-1.5">What is this regarding?</label>
            <select id="topic" name="topic" class="w-full rounded-lg border border-black/10 dark:border-white/15 bg-white dark:bg-ink px-3.5 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-gold-500">
              <option value="general">General Inquiry</option>
              <option value="construction">TambiQ Construction</option>
              <option value="properties">TambiQ Properties</option>
              <option value="auto">TambiQ Auto</option>
              <option value="logistics">TambiQ Logistics</option>
              <option value="recreation">TambiQ Recreation</option>
              <option value="fashion">TambiQ Fashion</option>
              <option value="marketplace">TambiQ Marketplace</option>
              <option value="partnership">Partnerships / Investment</option>
              <option value="careers">Careers</option>
            </select>
          </div>
          <div class="grid sm:grid-cols-2 gap-5">
            <div>
              <label for="name" class="block text-sm font-semibold mb-1.5">Name</label>
              <input id="name" name="name" type="text" class="w-full rounded-lg border border-black/10 dark:border-white/15 bg-white dark:bg-ink px-3.5 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-gold-500" required>
            </div>
            <div>
              <label for="email" class="block text-sm font-semibold mb-1.5">Email</label>
              <input id="email" name="email" type="email" class="w-full rounded-lg border border-black/10 dark:border-white/15 bg-white dark:bg-ink px-3.5 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-gold-500" required>
            </div>
          </div>
          <div>
            <label for="message" class="block text-sm font-semibold mb-1.5">Message</label>
            <textarea id="message" name="message" rows="5" class="w-full rounded-lg border border-black/10 dark:border-white/15 bg-white dark:bg-ink px-3.5 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-gold-500" required></textarea>
          </div>
          <button type="submit" class="w-full px-6 py-3 rounded-full bg-ink text-white dark:bg-gold-500 dark:text-ink font-semibold hover:opacity-90 transition-opacity">Send Message</button>
          <p id="form-note" class="text-xs text-gray-500 dark:text-gray-400 text-center">
            This form is not yet connected to an email service — submitting won't send anything.
            For now, please email us directly at <a href="mailto:info@{EMAIL_DOMAIN}" class="text-gold-600 dark:text-gold-400">info@{EMAIL_DOMAIN}</a>.
          </p>
        </form>
      </div>
    </section>
{card_grid_section("Direct Contact", "Reach a Specific Team", "", [
    ("General Inquiries", f'<a class="text-gold-600 dark:text-gold-400" href="mailto:info@{EMAIL_DOMAIN}">info@{EMAIL_DOMAIN}</a>'),
    ("Careers", f'<a class="text-gold-600 dark:text-gold-400" href="mailto:careers@{EMAIL_DOMAIN}">careers@{EMAIL_DOMAIN}</a>'),
    ("Investor &amp; Partnership Inquiries", f'<a class="text-gold-600 dark:text-gold-400" href="mailto:info@{EMAIL_DOMAIN}">info@{EMAIL_DOMAIN}</a>'),
], cols="sm:grid-cols-3")}
    <script>
      (function () {{
        var params = new URLSearchParams(window.location.search);
        var division = params.get('division');
        if (division) {{
          var select = document.getElementById('topic');
          if (select && select.querySelector('option[value="' + division + '"]')) {{
            select.value = division;
          }}
        }}
        var form = document.getElementById('contact-form');
        var note = document.getElementById('form-note');
        form.addEventListener('submit', function (e) {{
          e.preventDefault();
          note.textContent = "This form isn't connected to an email service yet. Please email us directly at info@{EMAIL_DOMAIN} — we'll get back to you.";
          note.classList.add('text-gold-600', 'dark:text-gold-400', 'font-semibold');
        }});
      }})();
    </script>'''

write("contact/index.html", page(
    "Contact — TambiQ Group LLC",
    "Get in touch with TambiQ Group LLC about a project, partnership, investment, or career opportunity.",
    "/contact/", P1, "contact", contact_body
))

# ---------------------------------------------------------------------------
# Privacy Policy
# ---------------------------------------------------------------------------
privacy_body = f'''    <section class="relative bg-ink text-white overflow-hidden pt-32 pb-16 sm:pt-40 sm:pb-20">
      <div class="absolute inset-0 bg-grid opacity-60"></div>
      <div class="relative max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h1 class="reveal font-serif font-bold text-3xl sm:text-4xl mb-4">Privacy Policy</h1>
      </div>
    </section>
{simple_section("Status", "This Policy Is Being Finalized", [
    "TambiQ Group LLC is committed to protecting the privacy of visitors to this website and future customers of our divisions.",
    "A complete Privacy Policy describing what information we collect, how it is used, and how it is protected is currently being finalized and will be published here.",
    f'In the meantime, if you have questions about our data practices, please contact us at <a class="text-gold-600 dark:text-gold-400" href="mailto:info@{EMAIL_DOMAIN}">info@{EMAIL_DOMAIN}</a>.'
])}'''

write("privacy/index.html", page(
    "Privacy Policy — TambiQ Group LLC",
    "TambiQ Group LLC privacy policy.",
    "/privacy/", P1, "", privacy_body
))

# ---------------------------------------------------------------------------
# Terms of Use
# ---------------------------------------------------------------------------
terms_body = f'''    <section class="relative bg-ink text-white overflow-hidden pt-32 pb-16 sm:pt-40 sm:pb-20">
      <div class="absolute inset-0 bg-grid opacity-60"></div>
      <div class="relative max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h1 class="reveal font-serif font-bold text-3xl sm:text-4xl mb-4">Terms of Use</h1>
      </div>
    </section>
{simple_section("Status", "These Terms Are Being Finalized", [
    "Formal Terms of Use governing the use of this website and TambiQ Group's future digital platforms are currently being finalized and will be published here.",
    f'In the meantime, if you have questions, please contact us at <a class="text-gold-600 dark:text-gold-400" href="mailto:info@{EMAIL_DOMAIN}">info@{EMAIL_DOMAIN}</a>.'
])}'''

write("terms/index.html", page(
    "Terms of Use — TambiQ Group LLC",
    "TambiQ Group LLC terms of use.",
    "/terms/", P1, "", terms_body
))

print("All 7 division pages generated.")
print("Companies overview page generated.")
print("Projects, Careers, News, Contact, Privacy, Terms pages generated.")
