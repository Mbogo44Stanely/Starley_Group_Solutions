from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import Service


@require_http_methods(['GET'])
def service_list(request):
    services = Service.objects.published()
    return render(request, 'html/services/service-list.html', {
        'services': services,
    })


@require_http_methods(['GET'])
def service_detail(request, slug):
    try:
        service = Service.objects.published().get(slug=slug)
    except Service.DoesNotExist:
        return render(request, '404.html', status=404)

    related = Service.objects.published().exclude(pk=service.pk)[:3]
    return render(request, 'html/services/service-detail.html', {
        'service': service,
        'related_services': related,
    })
