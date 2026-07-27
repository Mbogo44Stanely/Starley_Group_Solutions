
from django.conf import settings

from django.shortcuts import redirect
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from django.views.generic import TemplateView

from django.contrib import admin
from django.urls import path

from django.urls import path, include, re_path

from .views import (rate_limiter_view, view_404, 
                        handler_403, home_view) #subscribe_view

from .sitemaps import StaticSitemap
from blog.sitemaps import BlogSitemap
from services.sitemaps import ServiceSitemap
from pages.sitemaps import PagesSitemap

handler404 = view_404

handler403 = handler_403

admin.site.site_header = 'Starley Group Solutions Admin'
admin.site.index_title = 'Site administration'
admin.site.site_title = 'Starley Group Solutions'
admin.site.site_url = "/"


sitemap_dict = {'sitemaps': {'static': StaticSitemap, 'blog': BlogSitemap, 'services': ServiceSitemap, 'pages': PagesSitemap}}


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('user/', include('user.urls')),
    path('blog/', include('blog.urls')),
    path('services/', include('services.urls')),
    path('contact-us/', include('inquiry.urls')),
    path('', include('pages.urls')),
    

    path('sitemap.xml', sitemap, sitemap_dict, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),
    path('ratelimit-error/', rate_limiter_view, name='ratelimit-error'),

    # add new path here

    path('', home_view, name='home'),

    path("__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG:
   urlpatterns +=  []

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   
urlpatterns += [ re_path(r'^.*/$', view_404, name='page_not_found'),]