from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from skills import views

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='skills/index.html'), name='index'),
    #
    url(r'^roles/$', views.RolesList.as_view(), name='roles'),
    url(r'^role/add/$', views.RoleCreate.as_view(), name='role_add'),
    url(r'^role/(?P<pk>\d+)/$', views.RoleUpdate.as_view(), name='role_update'),
    url(r'^role/(?P<pk>\d+)/delete/$', views.RoleDelete.as_view(), name='role_delete'),
    #
    url(r'^seniority/add/$', views.SeniorityCreate.as_view(), name='seniority_add'),
    url(r'^seniority/(?P<pk>\d+)/$', views.SeniorityUpdate.as_view(), name='seniority_update'),
    url(r'^seniority/(?P<pk>\d+)/delete/$', views.SeniorityDelete.as_view(), name='seniority_delete'),
    #
    url(r'^skills/$', views.SkillsList.as_view(), name='skills'),
    url(r'^skill/add/$', views.SkillCreate.as_view(), name='skill_add'),
    url(r'^skill/(?P<pk>\d+)/$', views.SkillUpdate.as_view(), name='skill_update'),
    url(r'^skill/(?P<pk>\d+)/delete/$', views.SkillDelete.as_view(), name='skill_delete'),
)
