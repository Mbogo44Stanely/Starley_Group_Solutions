from django.db import migrations
from django.template.defaultfilters import slugify


DEFAULT_SERVICES = [
    {
        'title': 'Custom Software Development',
        'icon': 'bi-code-slash',
        'summary': 'Web, mobile and desktop applications built around your business.',
        'description': (
            'We design and build reliable, maintainable software tailored to your '
            'workflows. From discovery and architecture to delivery and support, our '
            'engineers work as an extension of your team to ship products that scale.'
        ),
    },
    {
        'title': 'Cloud & DevOps',
        'icon': 'bi-cloud-fill',
        'summary': 'Migrate, automate and optimise your infrastructure in the cloud.',
        'description': (
            'Move to the cloud with confidence. We handle migrations, CI/CD pipelines, '
            'containerisation and infrastructure-as-code so you can release faster while '
            'keeping costs and downtime under control.'
        ),
    },
    {
        'title': 'Cybersecurity',
        'icon': 'bi-shield-lock-fill',
        'summary': 'Protect your data, users and systems from evolving threats.',
        'description': (
            'Our security specialists assess your risk, harden your systems and put '
            'monitoring in place. We help you meet compliance requirements and respond '
            'quickly when it matters most.'
        ),
    },
    {
        'title': 'IT Consulting & Strategy',
        'icon': 'bi-lightbulb-fill',
        'summary': 'Align technology with your goals through expert guidance.',
        'description': (
            'Not sure where to invest next? We audit your current stack, define a '
            'practical roadmap and help you choose the right technologies to support '
            'growth without overspending.'
        ),
    },
    {
        'title': 'Managed IT Support',
        'icon': 'bi-headset',
        'summary': 'Proactive support that keeps your business running.',
        'description': (
            'Round-the-clock monitoring, help desk and maintenance so your team can '
            'focus on the work that matters. We resolve issues before they become '
            'problems and keep your systems up to date.'
        ),
    },
    {
        'title': 'Data & Analytics',
        'icon': 'bi-bar-chart-fill',
        'summary': 'Turn raw data into decisions with dashboards and pipelines.',
        'description': (
            'We build data pipelines, warehouses and dashboards that give you a clear '
            'view of your business. Make confident, data-driven decisions with insights '
            'delivered where you need them.'
        ),
    },
]


def seed_services(apps, schema_editor):
    Service = apps.get_model('services', 'Service')
    for index, item in enumerate(DEFAULT_SERVICES):
        Service.objects.get_or_create(
            title=item['title'],
            defaults={
                'slug': slugify(item['title']),
                'icon': item['icon'],
                'summary': item['summary'],
                'description': item['description'],
                'is_published': True,
                'is_featured': True,
                'order': index,
            },
        )


def unseed_services(apps, schema_editor):
    Service = apps.get_model('services', 'Service')
    titles = [item['title'] for item in DEFAULT_SERVICES]
    Service.objects.filter(title__in=titles).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_services, unseed_services),
    ]
