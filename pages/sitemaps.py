from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class PagesSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.7
    protocol = 'https'

    # URL names registered in pages/urls.py.
    _names = [
        'about', 'careers',
        'managed-it', 'cybersecurity-risk', 'cloud-consulting', 'digital-transformation',
        'industry-financial', 'industry-healthcare', 'industry-legal',
        'case-studies', 'partners',
        'privacy', 'terms',
    ]

    def items(self):
        return [name for name in self._names]

    def location(self, name):
        return reverse(name)
