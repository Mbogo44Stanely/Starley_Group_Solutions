from django.conf import settings


def site_context(request):
    """Expose company details and the primary navigation to every template.

    Keeping this data in settings and injecting it here means adding a new
    page/module only requires editing ``NAV_LINKS`` (or nothing at all) rather
    than touching every template.
    """

    return {
        'company': settings.COMPANY,
        'nav_links': settings.NAV_LINKS,
        'footer_columns': settings.FOOTER_COLUMNS,
    }
