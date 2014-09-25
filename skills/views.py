from django.views import generic

from skills.models import Role


class RolesView(generic.ListView):
    model = Role
