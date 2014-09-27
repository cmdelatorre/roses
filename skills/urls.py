from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from skills import views

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='skills/index.html'), name='index'),
    url(r'^seniorities/$', views.RolesView.as_view(), name='seniorities'),
    url(r'^skills/$', views.RolesView.as_view(), name='skills'),

    url(r'^roles/$', views.RolesView.as_view(), name='roles'),
    url(r'^role/add/$', views.RoleCreate.as_view(), name='role_add'),
    url(r'^role/(?P<pk>\d+)/$', views.RoleUpdate.as_view(), name='role_update'),
    url(r'^role/(?P<pk>\d+)/delete/$', views.RoleDelete.as_view(), name='role_delete'),
)
