"""Content definitions for the marketing / corporate pages.

Each page is a plain dictionary describing an ordered list of ``sections``.
A section has a ``type`` (matching a partial in ``templates/html/pages/sections/``)
plus the data that partial needs. Adding or editing a page is therefore a pure
content change -- no new views, models or migrations required.
"""

# Reusable call-to-action shortcuts ---------------------------------------
CTA_CONTACT = {'label': 'Talk to an expert', 'url_name': 'contact-us'}
CTA_SERVICES = {'label': 'Explore all services', 'url_name': 'services'}


def _closing_cta(heading, subheading):
    return {
        'type': 'cta',
        'heading': heading,
        'subheading': subheading,
        'primary_cta': CTA_CONTACT,
        'secondary_cta': CTA_SERVICES,
    }


# -------------------------------------------------------------------------
# About Us
# -------------------------------------------------------------------------
ABOUT = {
    'key': 'about',
    'title': 'About Us',
    'meta_description': (
        'Learn about Starley Group Solutions — our identity, core values, '
        'executive leadership and the milestones that shaped our IT company.'
    ),
    'sections': [
        {
            'type': 'hero',
            'eyebrow': 'About Starley Group Solutions',
            'title': 'A technology partner built for the enterprise',
            'subtitle': (
                'We help ambitious organisations modernise, secure and scale '
                'their technology — combining engineering depth with a '
                'consulting mindset and enterprise-grade delivery.'
            ),
            'primary_cta': CTA_CONTACT,
            'secondary_cta': {'label': 'Our services', 'url_name': 'services'},
        },
        {
            'type': 'intro',
            'eyebrow': 'Who we are',
            'heading': 'Our identity',
            'paragraphs': [
                'Founded in 2018, Starley Group Solutions is a full-service IT '
                'company delivering managed infrastructure, cybersecurity, cloud '
                'and digital transformation to enterprises across regulated and '
                'high-growth industries.',
                'We operate as a long-term partner rather than a vendor. Our teams '
                'embed with yours to understand the business outcomes you need, '
                'then design, build and run the technology that delivers them.',
            ],
        },
        {
            'type': 'stats',
            'items': [
                {'value': '150+', 'label': 'Projects delivered'},
                {'value': '98%', 'label': 'Client retention'},
                {'value': '24/7', 'label': 'Managed operations'},
                {'value': '40+', 'label': 'Certified engineers'},
            ],
        },
        {
            'type': 'features',
            'eyebrow': 'What we stand for',
            'heading': 'Core values',
            'subheading': 'The principles behind every engagement.',
            'items': [
                {'icon': 'bi-shield-check', 'title': 'Security first',
                 'text': 'We design with a zero-trust mindset and treat data protection as non-negotiable.'},
                {'icon': 'bi-people-fill', 'title': 'Partnership',
                 'text': 'Transparent, outcome-driven relationships that compound value over time.'},
                {'icon': 'bi-graph-up-arrow', 'title': 'Excellence',
                 'text': 'Certified engineers, rigorous delivery standards and measurable results.'},
                {'icon': 'bi-lightbulb-fill', 'title': 'Innovation',
                 'text': 'We bring emerging technology to bear on real, practical business problems.'},
            ],
        },
        {
            'type': 'people',
            'eyebrow': 'Executive leadership',
            'heading': 'Meet the leadership team',
            'subheading': 'Experienced operators guiding our strategy and delivery.',
            'items': [
                {'name': 'Alex Morgan', 'role': 'Chief Executive Officer', 'icon': 'bi-person-badge',
                 'bio': 'Two decades scaling technology services businesses across finance and healthcare.'},
                {'name': 'Priya Nair', 'role': 'Chief Technology Officer', 'icon': 'bi-cpu',
                 'bio': 'Cloud and platform engineering leader focused on resilient, secure architecture.'},
                {'name': 'Daniel Okoye', 'role': 'Chief Information Security Officer', 'icon': 'bi-shield-lock',
                 'bio': 'Former enterprise CISO specialising in zero-trust and regulatory compliance.'},
                {'name': 'Sofia Rossi', 'role': 'VP, Client Success', 'icon': 'bi-headset',
                 'bio': 'Leads managed services and support, obsessed with uptime and response times.'},
            ],
        },
        {
            'type': 'timeline',
            'eyebrow': 'Our journey',
            'heading': 'Company timeline',
            'items': [
                {'year': '2018', 'title': 'Founded',
                 'text': 'Starley Group Solutions launches with a focus on managed IT support.'},
                {'year': '2020', 'title': 'Security practice',
                 'text': 'We add a dedicated cybersecurity and risk management practice.'},
                {'year': '2022', 'title': 'Cloud & DevOps',
                 'text': 'Cloud consulting and migration becomes a core service line.'},
                {'year': '2024', 'title': 'AI & transformation',
                 'text': 'Digital transformation and AI integration services go to market.'},
                {'year': 'Today', 'title': 'Enterprise scale',
                 'text': 'Trusted by clients across finance, healthcare and professional services.'},
            ],
        },
        _closing_cta('Ready to work with us?',
                     'Let’s talk about where technology can take your business next.'),
    ],
}


# -------------------------------------------------------------------------
# Service line pages
# -------------------------------------------------------------------------
MANAGED_IT = {
    'key': 'managed-it',
    'title': 'Managed IT Infrastructure',
    'meta_description': (
        'Proactive network monitoring, 24/7 helpdesk support and end-to-end '
        'infrastructure management from Starley Group Solutions.'
    ),
    'sections': [
        {
            'type': 'hero',
            'eyebrow': 'Managed Services',
            'title': 'Managed IT Infrastructure',
            'subtitle': (
                'Keep your business running with proactive monitoring, responsive '
                'helpdesk support and fully managed networks and infrastructure.'
            ),
            'primary_cta': {'label': 'Get managed support', 'url_name': 'contact-us'},
            'secondary_cta': {'label': 'All services', 'url_name': 'services'},
        },
        {
            'type': 'features',
            'eyebrow': 'Capabilities',
            'heading': 'End-to-end infrastructure management',
            'subheading': 'A single partner for the systems your business depends on.',
            'items': [
                {'icon': 'bi-activity', 'title': '24/7 network monitoring',
                 'text': 'Continuous monitoring and alerting to catch issues before they cause downtime.'},
                {'icon': 'bi-headset', 'title': 'Service desk & helpdesk',
                 'text': 'Fast, friendly support with clear SLAs for your users and teams.'},
                {'icon': 'bi-hdd-network', 'title': 'Network management',
                 'text': 'Design, configuration and management of secure, high-availability networks.'},
                {'icon': 'bi-server', 'title': 'Server & endpoint management',
                 'text': 'Patching, backups, updates and hardening across servers and devices.'},
                {'icon': 'bi-cloud-arrow-up', 'title': 'Backup & disaster recovery',
                 'text': 'Tested backup and recovery so you can restore quickly from any incident.'},
                {'icon': 'bi-clipboard-data', 'title': 'Reporting & governance',
                 'text': 'Transparent reporting on performance, tickets and infrastructure health.'},
            ],
        },
        {
            'type': 'steps',
            'eyebrow': 'How we onboard you',
            'heading': 'A smooth transition to managed services',
            'items': [
                {'title': 'Assess', 'text': 'We audit your current environment, risks and priorities.'},
                {'title': 'Stabilise', 'text': 'We resolve urgent issues and put monitoring in place.'},
                {'title': 'Optimise', 'text': 'We harden, document and improve your infrastructure.'},
                {'title': 'Operate', 'text': 'We run and continuously improve your environment 24/7.'},
            ],
        },
        {
            'type': 'stats',
            'items': [
                {'value': '99.9%', 'label': 'Uptime target'},
                {'value': '<15 min', 'label': 'Critical response'},
                {'value': '24/7', 'label': 'Monitoring & support'},
            ],
        },
        _closing_cta('Need dependable IT operations?',
                     'Offload the day-to-day so your team can focus on the business.'),
    ],
}

CYBERSECURITY = {
    'key': 'cybersecurity-risk',
    'title': 'Cybersecurity & Risk Management',
    'meta_description': (
        'Enterprise threat detection, penetration testing, compliance audits and '
        'zero-trust security frameworks from Starley Group Solutions.'
    ),
    'sections': [
        {
            'type': 'hero',
            'eyebrow': 'Security & Risk',
            'title': 'Cybersecurity & Risk Management',
            'subtitle': (
                'Detect threats, prove compliance and build a zero-trust security '
                'posture that protects your data, users and reputation.'
            ),
            'primary_cta': {'label': 'Request a security review', 'url_name': 'contact-us'},
            'secondary_cta': {'label': 'All services', 'url_name': 'services'},
        },
        {
            'type': 'features',
            'eyebrow': 'Capabilities',
            'heading': 'Enterprise-grade protection',
            'subheading': 'A complete security programme, tailored to your risk profile.',
            'items': [
                {'icon': 'bi-radar', 'title': 'Threat detection & response',
                 'text': '24/7 monitoring, SIEM and rapid incident response to contain threats.'},
                {'icon': 'bi-bug', 'title': 'Penetration testing',
                 'text': 'Offensive testing of applications, networks and cloud to find gaps first.'},
                {'icon': 'bi-file-earmark-check', 'title': 'Compliance audits',
                 'text': 'Readiness and audits for ISO 27001, SOC 2, GDPR, HIPAA and PCI DSS.'},
                {'icon': 'bi-shield-lock', 'title': 'Zero-trust frameworks',
                 'text': 'Identity-centric access, segmentation and least-privilege by design.'},
                {'icon': 'bi-key', 'title': 'Identity & access management',
                 'text': 'MFA, SSO and privileged access management across your estate.'},
                {'icon': 'bi-exclamation-triangle', 'title': 'Risk management',
                 'text': 'Risk assessments, policies and governance aligned to your business.'},
            ],
        },
        {
            'type': 'steps',
            'eyebrow': 'Our approach',
            'heading': 'From assessment to assurance',
            'items': [
                {'title': 'Assess', 'text': 'Identify assets, threats and compliance obligations.'},
                {'title': 'Protect', 'text': 'Deploy zero-trust controls and harden your environment.'},
                {'title': 'Detect', 'text': 'Monitor continuously and hunt for emerging threats.'},
                {'title': 'Respond', 'text': 'Contain, remediate and learn from every incident.'},
            ],
        },
        {
            'type': 'stats',
            'items': [
                {'value': '24/7', 'label': 'Threat monitoring'},
                {'value': '100%', 'label': 'Compliance focus'},
                {'value': '0-trust', 'label': 'Security model'},
            ],
        },
        _closing_cta('Is your security posture ready?',
                     'Book a security review and get a clear, prioritised action plan.'),
    ],
}

CLOUD = {
    'key': 'cloud-consulting',
    'title': 'Cloud Consulting & Migration',
    'meta_description': (
        'AWS, Microsoft Azure and Google Cloud strategy, architecture and hybrid '
        'migration expertise from Starley Group Solutions.'
    ),
    'sections': [
        {
            'type': 'hero',
            'eyebrow': 'Cloud',
            'title': 'Cloud Consulting & Migration',
            'subtitle': (
                'Strategy, architecture and migration across AWS, Microsoft Azure '
                'and Google Cloud — including complex hybrid environments.'
            ),
            'primary_cta': {'label': 'Plan your migration', 'url_name': 'contact-us'},
            'secondary_cta': {'label': 'All services', 'url_name': 'services'},
        },
        {
            'type': 'features',
            'eyebrow': 'Capabilities',
            'heading': 'Cloud done right',
            'subheading': 'From first strategy to fully optimised operations.',
            'items': [
                {'icon': 'bi-diagram-3', 'title': 'Cloud strategy',
                 'text': 'Business-aligned cloud roadmaps, TCO analysis and platform selection.'},
                {'icon': 'bi-boxes', 'title': 'Architecture & design',
                 'text': 'Well-architected, secure and scalable designs for your workloads.'},
                {'icon': 'bi-arrow-left-right', 'title': 'Migration & modernisation',
                 'text': 'Lift-and-shift, re-platform or re-architect with minimal disruption.'},
                {'icon': 'bi-clouds', 'title': 'Hybrid & multi-cloud',
                 'text': 'Seamless integration across on-premises and multiple cloud providers.'},
                {'icon': 'bi-cash-coin', 'title': 'Cost optimisation (FinOps)',
                 'text': 'Right-sizing, reserved capacity and governance to control spend.'},
                {'icon': 'bi-gear-wide-connected', 'title': 'DevOps & automation',
                 'text': 'CI/CD, infrastructure-as-code and automated, repeatable delivery.'},
            ],
        },
        {
            'type': 'logos',
            'eyebrow': 'Platforms',
            'heading': 'Certified across the major clouds',
            'items': [
                {'name': 'Amazon Web Services'},
                {'name': 'Microsoft Azure'},
                {'name': 'Google Cloud'},
                {'name': 'Kubernetes'},
                {'name': 'Terraform'},
            ],
        },
        _closing_cta('Thinking about the cloud?',
                     'Let’s build a migration plan that de-risks the journey.'),
    ],
}

DIGITAL = {
    'key': 'digital-transformation',
    'title': 'Digital Transformation & AI',
    'meta_description': (
        'Custom software development, workflow automation and AI integration '
        'services from Starley Group Solutions.'
    ),
    'sections': [
        {
            'type': 'hero',
            'eyebrow': 'Innovation',
            'title': 'Digital Transformation & AI',
            'subtitle': (
                'Custom software, intelligent automation and AI integration that '
                'turn manual processes into competitive advantage.'
            ),
            'primary_cta': {'label': 'Start your project', 'url_name': 'contact-us'},
            'secondary_cta': {'label': 'All services', 'url_name': 'services'},
        },
        {
            'type': 'features',
            'eyebrow': 'Capabilities',
            'heading': 'Build, automate, innovate',
            'subheading': 'Modern software and AI, delivered by experienced teams.',
            'items': [
                {'icon': 'bi-code-slash', 'title': 'Custom software development',
                 'text': 'Web, mobile and enterprise applications built around your business.'},
                {'icon': 'bi-robot', 'title': 'AI integration',
                 'text': 'LLMs, machine learning and intelligent assistants embedded in your workflows.'},
                {'icon': 'bi-arrow-repeat', 'title': 'Workflow automation',
                 'text': 'Automate repetitive processes to cut cost and eliminate errors.'},
                {'icon': 'bi-plug', 'title': 'Systems integration',
                 'text': 'Connect your platforms and data with robust APIs and pipelines.'},
                {'icon': 'bi-bar-chart-line', 'title': 'Data & analytics',
                 'text': 'Turn raw data into dashboards and decisions with modern data platforms.'},
                {'icon': 'bi-columns-gap', 'title': 'Product & UX',
                 'text': 'Discovery, design and delivery that keeps users at the centre.'},
            ],
        },
        {
            'type': 'steps',
            'eyebrow': 'How we deliver',
            'heading': 'A proven delivery model',
            'items': [
                {'title': 'Discover', 'text': 'Align on outcomes, users and success metrics.'},
                {'title': 'Design', 'text': 'Prototype and validate before we build.'},
                {'title': 'Build', 'text': 'Ship iteratively with quality and security built in.'},
                {'title': 'Scale', 'text': 'Measure, optimise and grow what works.'},
            ],
        },
        _closing_cta('Ready to transform how you work?',
                     'Let’s scope a pilot and prove the value quickly.'),
    ],
}


# -------------------------------------------------------------------------
# Industry vertical pages
# -------------------------------------------------------------------------
INDUSTRY_FINANCE = {
    'key': 'industry-financial',
    'title': 'Financial Services & Banking',
    'meta_description': (
        'Banking compliance, high-integrity data platforms and fraud-prevention '
        'technology for financial services from Starley Group Solutions.'
    ),
    'sections': [
        {
            'type': 'hero',
            'eyebrow': 'Industry',
            'title': 'Financial Services & Banking',
            'subtitle': (
                'Secure, compliant and resilient technology for banks, fintechs '
                'and financial institutions — where data integrity is everything.'
            ),
            'primary_cta': CTA_CONTACT,
            'secondary_cta': {'label': 'All industries', 'url_name': 'industry-healthcare'},
        },
        {
            'type': 'features',
            'eyebrow': 'How we help',
            'heading': 'Built for regulated finance',
            'subheading': 'Technology that meets the bar for security and compliance.',
            'items': [
                {'icon': 'bi-bank', 'title': 'Banking compliance',
                 'text': 'PCI DSS, SOX and regulatory reporting supported by design.'},
                {'icon': 'bi-shield-shaded', 'title': 'Fraud prevention',
                 'text': 'Real-time monitoring and anomaly detection to stop fraud early.'},
                {'icon': 'bi-database-check', 'title': 'High-integrity data',
                 'text': 'High-frequency, tamper-evident data platforms you can trust.'},
                {'icon': 'bi-lock', 'title': 'Zero-trust security',
                 'text': 'Strong identity, encryption and segmentation across systems.'},
            ],
        },
        _closing_cta('Modernising financial technology?',
                     'Talk to a team that understands regulated finance.'),
    ],
}

INDUSTRY_HEALTH = {
    'key': 'industry-healthcare',
    'title': 'Healthcare & Life Sciences',
    'meta_description': (
        'Medical data security, HIPAA compliance and telehealth infrastructure '
        'for healthcare and life sciences from Starley Group Solutions.'
    ),
    'sections': [
        {
            'type': 'hero',
            'eyebrow': 'Industry',
            'title': 'Healthcare & Life Sciences',
            'subtitle': (
                'Protect patient data, meet compliance standards and deliver '
                'reliable telehealth and clinical infrastructure.'
            ),
            'primary_cta': CTA_CONTACT,
            'secondary_cta': {'label': 'All industries', 'url_name': 'industry-financial'},
        },
        {
            'type': 'features',
            'eyebrow': 'How we help',
            'heading': 'Care-grade technology',
            'subheading': 'Security and reliability for patient-critical systems.',
            'items': [
                {'icon': 'bi-heart-pulse', 'title': 'Medical data security',
                 'text': 'Protect PHI end to end with encryption and strict access controls.'},
                {'icon': 'bi-clipboard2-pulse', 'title': 'Compliance standards',
                 'text': 'HIPAA and HITECH-aligned controls, audits and documentation.'},
                {'icon': 'bi-camera-video', 'title': 'Telehealth infrastructure',
                 'text': 'Secure, high-availability platforms for remote care.'},
                {'icon': 'bi-hdd-stack', 'title': 'Reliable operations',
                 'text': 'Resilient infrastructure for systems that cannot go down.'},
            ],
        },
        _closing_cta('Securing healthcare technology?',
                     'Let’s protect patient data and keep care running.'),
    ],
}

INDUSTRY_LEGAL = {
    'key': 'industry-legal',
    'title': 'Legal & Professional Services',
    'meta_description': (
        'Secure document management and high-availability systems for law firms '
        'and professional services from Starley Group Solutions.'
    ),
    'sections': [
        {
            'type': 'hero',
            'eyebrow': 'Industry',
            'title': 'Legal & Professional Services',
            'subtitle': (
                'Confidential, always-available systems for law firms and '
                'professional services where trust and uptime are paramount.'
            ),
            'primary_cta': CTA_CONTACT,
            'secondary_cta': {'label': 'All industries', 'url_name': 'industry-financial'},
        },
        {
            'type': 'features',
            'eyebrow': 'How we help',
            'heading': 'Discretion, security, uptime',
            'subheading': 'Technology that protects privileged information.',
            'items': [
                {'icon': 'bi-folder-check', 'title': 'Secure document management',
                 'text': 'Encrypted, access-controlled document and matter management.'},
                {'icon': 'bi-hdd-network', 'title': 'High-availability systems',
                 'text': 'Resilient infrastructure so client work is never interrupted.'},
                {'icon': 'bi-shield-lock', 'title': 'Confidentiality',
                 'text': 'Zero-trust controls to protect privileged and sensitive data.'},
                {'icon': 'bi-search', 'title': 'eDiscovery support',
                 'text': 'Tooling and processes to manage discovery efficiently and safely.'},
            ],
        },
        _closing_cta('Protecting client confidentiality?',
                     'Let’s secure your practice and keep it always-on.'),
    ],
}


# -------------------------------------------------------------------------
# Authority & trust
# -------------------------------------------------------------------------
CASE_STUDIES = {
    'key': 'case-studies',
    'title': 'Case Studies & Client Success',
    'meta_description': (
        'Technical problem-solving narratives, ROI data and client success '
        'stories from Starley Group Solutions.'
    ),
    'sections': [
        {
            'type': 'hero',
            'eyebrow': 'Proven results',
            'title': 'Case Studies & Client Success',
            'subtitle': (
                'Real engagements, measurable outcomes. See how we solve hard '
                'technical problems and deliver return on investment.'
            ),
            'primary_cta': {'label': 'Discuss your project', 'url_name': 'contact-us'},
            'secondary_cta': CTA_SERVICES,
        },
        {
            'type': 'cases',
            'eyebrow': 'Selected work',
            'heading': 'Client success stories',
            'items': [
                {'client': 'Regional Bank', 'industry': 'Financial Services',
                 'title': 'Zero-trust rollout across 40 branches',
                 'result': 'Reduced security incidents and passed audit with zero major findings.',
                 'metrics': [{'value': '-70%', 'label': 'Security incidents'}, {'value': '100%', 'label': 'Audit pass'}]},
                {'client': 'HealthTech Provider', 'industry': 'Healthcare',
                 'title': 'HIPAA-compliant telehealth platform',
                 'result': 'Launched a scalable telehealth platform serving thousands of patients.',
                 'metrics': [{'value': '99.99%', 'label': 'Uptime'}, {'value': '3x', 'label': 'Patient capacity'}]},
                {'client': 'National Law Firm', 'industry': 'Legal',
                 'title': 'Secure document management modernisation',
                 'result': 'Migrated to a secure, high-availability document platform with full audit trails.',
                 'metrics': [{'value': '-50%', 'label': 'Search time'}, {'value': '0', 'label': 'Data incidents'}]},
                {'client': 'Retail Group', 'industry': 'Retail',
                 'title': 'Cloud migration and cost optimisation',
                 'result': 'Migrated core systems to the cloud and cut infrastructure spend.',
                 'metrics': [{'value': '-35%', 'label': 'Cloud spend'}, {'value': '2x', 'label': 'Release speed'}]},
            ],
        },
        _closing_cta('Want results like these?',
                     'Tell us about your challenge and we’ll show you what’s possible.'),
    ],
}

PARTNERS = {
    'key': 'partners',
    'title': 'Partners & Alliances',
    'meta_description': (
        'Vendor certifications, strategic partnerships and industry alliances '
        'that back Starley Group Solutions.'
    ),
    'sections': [
        {
            'type': 'hero',
            'eyebrow': 'Ecosystem',
            'title': 'Partners & Alliances',
            'subtitle': (
                'We partner with the world’s leading technology vendors and hold '
                'the certifications that prove our expertise.'
            ),
            'primary_cta': {'label': 'Become a partner', 'url_name': 'contact-us'},
            'secondary_cta': CTA_SERVICES,
        },
        {
            'type': 'logos',
            'eyebrow': 'Certifications & partnerships',
            'heading': 'Backed by the best',
            'items': [
                {'name': 'Microsoft Gold Partner'},
                {'name': 'AWS Certified'},
                {'name': 'Google Cloud Partner'},
                {'name': 'Cisco Select Partner'},
                {'name': 'ISO 27001 Certified'},
                {'name': 'CrowdStrike Partner'},
                {'name': 'Fortinet Partner'},
                {'name': 'VMware Partner'},
            ],
        },
        {
            'type': 'features',
            'eyebrow': 'Why it matters',
            'heading': 'The value of our alliances',
            'subheading': 'Certifications translate directly into client outcomes.',
            'items': [
                {'icon': 'bi-patch-check', 'title': 'Validated expertise',
                 'text': 'Certifications prove our teams meet vendor engineering standards.'},
                {'icon': 'bi-headset', 'title': 'Priority support',
                 'text': 'Partner status gives you faster escalation paths to vendors.'},
                {'icon': 'bi-tags', 'title': 'Better economics',
                 'text': 'Partner pricing and programmes passed on to your business.'},
            ],
        },
        _closing_cta('Interested in partnering?',
                     'Let’s explore how an alliance can benefit both our clients.'),
    ],
}


# -------------------------------------------------------------------------
# Careers
# -------------------------------------------------------------------------
CAREERS = {
    'key': 'careers',
    'title': 'Careers & Culture',
    'meta_description': (
        'Join Starley Group Solutions — our culture, benefits, commitment to '
        'diversity and CSR, and current technical openings.'
    ),
    'sections': [
        {
            'type': 'hero',
            'eyebrow': 'Join us',
            'title': 'Careers & Culture',
            'subtitle': (
                'Build a career solving meaningful technical problems with a team '
                'that values growth, inclusion and impact.'
            ),
            'primary_cta': {'label': 'Get in touch', 'url_name': 'contact-us'},
            'secondary_cta': {'label': 'About us', 'url_name': 'about'},
        },
        {
            'type': 'features',
            'eyebrow': 'Why Starley',
            'heading': 'Benefits & culture',
            'subheading': 'We invest in our people.',
            'items': [
                {'icon': 'bi-cash-stack', 'title': 'Competitive rewards',
                 'text': 'Strong salaries, bonuses and equity for the people who build our success.'},
                {'icon': 'bi-house-heart', 'title': 'Flexible & remote',
                 'text': 'Remote-friendly working and flexibility to do your best work.'},
                {'icon': 'bi-mortarboard', 'title': 'Learning & certifications',
                 'text': 'Paid training, certifications and conference budgets.'},
                {'icon': 'bi-people', 'title': 'Diversity & inclusion',
                 'text': 'An inclusive workplace where everyone can thrive.'},
                {'icon': 'bi-globe2', 'title': 'CSR & community',
                 'text': 'Volunteering time and initiatives that give back.'},
                {'icon': 'bi-heart-pulse', 'title': 'Health & wellbeing',
                 'text': 'Comprehensive health cover and wellbeing support.'},
            ],
        },
        {
            'type': 'openings',
            'eyebrow': 'Open roles',
            'heading': 'Current technical openings',
            'items': [
                {'title': 'Senior Cloud Engineer', 'location': 'Remote', 'type': 'Full-time'},
                {'title': 'Cybersecurity Analyst', 'location': 'Tech City, HQ', 'type': 'Full-time'},
                {'title': 'Full-Stack Developer', 'location': 'Remote', 'type': 'Full-time'},
                {'title': 'IT Support Engineer', 'location': 'Tech City, HQ', 'type': 'Full-time'},
                {'title': 'DevOps Engineer', 'location': 'Remote', 'type': 'Contract'},
            ],
        },
        _closing_cta('Don’t see your role?',
                     'We’re always keen to meet talented people — reach out.'),
    ],
}


# -------------------------------------------------------------------------
# Legal pages
# -------------------------------------------------------------------------
PRIVACY = {
    'key': 'privacy',
    'title': 'Privacy Policy',
    'meta_description': 'How Starley Group Solutions collects, uses and protects your data.',
    'sections': [
        {
            'type': 'legal',
            'heading': 'Privacy Policy',
            'updated': 'Last updated: January 2025',
            'blocks': [
                {'heading': '1. Introduction',
                 'paragraphs': [
                     'Starley Group Solutions ("we", "us", "our") is committed to protecting '
                     'your privacy. This policy explains how we collect, use, disclose and '
                     'safeguard your information when you visit our website or use our services.']},
                {'heading': '2. Information we collect',
                 'paragraphs': [
                     'We may collect personal information you provide directly, such as your '
                     'name, email address, phone number and any details submitted through our '
                     'contact forms, as well as technical data such as IP address, browser type '
                     'and usage information collected automatically.']},
                {'heading': '3. How we use your information',
                 'paragraphs': [
                     'We use your information to respond to enquiries, provide and improve our '
                     'services, communicate with you, and comply with legal obligations. We do '
                     'not sell your personal information.']},
                {'heading': '4. Data protection',
                 'paragraphs': [
                     'We implement appropriate technical and organisational measures, including '
                     'encryption and access controls, to protect your information against '
                     'unauthorised access, alteration, disclosure or destruction.']},
                {'heading': '5. International transfers & compliance',
                 'paragraphs': [
                     'Where data is transferred internationally, we ensure appropriate safeguards '
                     'are in place in line with applicable privacy laws, including the GDPR where '
                     'relevant.']},
                {'heading': '6. Your rights',
                 'paragraphs': [
                     'Depending on your jurisdiction, you may have rights to access, correct, '
                     'delete or restrict processing of your personal data. Contact us to exercise '
                     'these rights.']},
                {'heading': '7. Contact us',
                 'paragraphs': [
                     'If you have questions about this policy, please contact us using the details '
                     'on our contact page.']},
            ],
        },
    ],
}

TERMS = {
    'key': 'terms',
    'title': 'Terms of Service',
    'meta_description': 'The terms governing use of the Starley Group Solutions website and services.',
    'sections': [
        {
            'type': 'legal',
            'heading': 'Terms of Service',
            'updated': 'Last updated: January 2025',
            'blocks': [
                {'heading': '1. Acceptance of terms',
                 'paragraphs': [
                     'By accessing or using the Starley Group Solutions website, you agree to be '
                     'bound by these Terms of Service and all applicable laws and regulations.']},
                {'heading': '2. Use of the website',
                 'paragraphs': [
                     'You agree to use this website only for lawful purposes and in a manner that '
                     'does not infringe the rights of, or restrict the use of, this website by any '
                     'third party.']},
                {'heading': '3. Intellectual property',
                 'paragraphs': [
                     'All content on this website, including text, graphics, logos and software, is '
                     'the property of Starley Group Solutions or its licensors and is protected by '
                     'copyright and other intellectual property laws.']},
                {'heading': '4. Limitation of liability',
                 'paragraphs': [
                     'This website and its content are provided "as is". To the fullest extent '
                     'permitted by law, we exclude liability for any loss or damage arising from '
                     'your use of, or inability to use, this website.']},
                {'heading': '5. Third-party links',
                 'paragraphs': [
                     'Our website may contain links to third-party websites. We are not responsible '
                     'for the content or practices of those websites.']},
                {'heading': '6. Changes to these terms',
                 'paragraphs': [
                     'We may update these terms from time to time. Continued use of the website '
                     'after changes constitutes acceptance of the revised terms.']},
                {'heading': '7. Governing law',
                 'paragraphs': [
                     'These terms are governed by the laws of the jurisdiction in which Starley '
                     'Group Solutions operates, without regard to conflict of law principles.']},
            ],
        },
    ],
}


# Registry: url slug -> page dict --------------------------------------------
PAGES = {
    page['key']: page
    for page in [
        ABOUT,
        MANAGED_IT,
        CYBERSECURITY,
        CLOUD,
        DIGITAL,
        INDUSTRY_FINANCE,
        INDUSTRY_HEALTH,
        INDUSTRY_LEGAL,
        CASE_STUDIES,
        PARTNERS,
        CAREERS,
        PRIVACY,
        TERMS,
    ]
}
