from django.urls import path

from .views import page_view


urlpatterns = [
    # Company
    path('about/', page_view('about'), name='about'),
    path('careers/', page_view('careers'), name='careers'),

    # Service lines
    path('managed-it-infrastructure/', page_view('managed-it'), name='managed-it'),
    path('cybersecurity-risk-management/', page_view('cybersecurity-risk'), name='cybersecurity-risk'),
    path('cloud-consulting-migration/', page_view('cloud-consulting'), name='cloud-consulting'),
    path('digital-transformation-ai/', page_view('digital-transformation'), name='digital-transformation'),

    # Industries
    path('industries/financial-services/', page_view('industry-financial'), name='industry-financial'),
    path('industries/healthcare/', page_view('industry-healthcare'), name='industry-healthcare'),
    path('industries/legal/', page_view('industry-legal'), name='industry-legal'),

    # Authority & trust
    path('case-studies/', page_view('case-studies'), name='case-studies'),
    path('partners/', page_view('partners'), name='partners'),

    # Legal
    path('privacy-policy/', page_view('privacy'), name='privacy'),
    path('terms-of-service/', page_view('terms'), name='terms'),
]
