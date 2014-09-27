from django.core.urlresolvers import reverse_lazy
from django.views import generic

from skills.models import Role


class RolesView(generic.ListView):
    model = Role
    fields = ['name', 'description']
    template_name = 'skills/role_list.html'


class RoleCreate(generic.CreateView):
    model = Role
    fields = ['name', 'description']


class RoleUpdate(generic.UpdateView):
    model = Role
    fields = ['name', 'description']


class RoleDelete(generic.DeleteView):
    model = Role
    success_url = reverse_lazy('skills:roles')
