from functools import partial

from django.http import Http404
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .content import PAGES


@require_http_methods(['GET'])
def marketing_page(request, key):
    """Render a content-driven marketing page by its registry key."""

    page = PAGES.get(key)
    if page is None:
        raise Http404('Page not found')

    return render(request, 'html/pages/page.html', {'page': page})


def page_view(key):
    """Return a view bound to a specific page key (used in urls.py)."""

    return partial(marketing_page, key=key)
