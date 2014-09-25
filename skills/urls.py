from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from skills import views

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='skills/index.html'), name='index'),
    url(r'^roles/$', views.RolesView.as_view(), name='roles'),
    url(r'^seniorities/$', views.RolesView.as_view(), name='seniorities'),
    url(r'^skills/$', views.RolesView.as_view(), name='skills'),
)
