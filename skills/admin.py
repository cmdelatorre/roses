from django.contrib import admin
from skills.models import Role, Seniority, Skill

admin.site.register(Role)


class SeniorityAdmin(admin.ModelAdmin):
    fields = ['name', 'role']

admin.site.register(Seniority, SeniorityAdmin)


class SkillAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('name', 'related_seniorities')

admin.site.register(Skill, SkillAdmin)