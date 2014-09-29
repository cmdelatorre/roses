from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.views.generic.list import MultipleObjectMixin

from skills.models import Role, Seniority


class RolesView(generic.ListView):
    model = Role
    fields = ['name', 'description']
    template_name = 'skills/role_list.html'


class RoleCreate(generic.CreateView):
    model = Role
    fields = ['name', 'description']


class RoleUpdate(generic.UpdateView, MultipleObjectMixin):
    model = Role
    fields = ['name', 'description']
    paginate_by = 2

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Role.objects.all())
        self.object_list = self.object.seniorities.all()
        return super(RoleUpdate, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(RoleUpdate, self).get_context_data(**kwargs)
        context['role'] = self.object
        return context


class RoleDelete(generic.DeleteView):
    model = Role
    success_url = reverse_lazy('skills:roles')
    template_name = 'skills/confirm_delete.html'


#
# Seniorities
#
class SeniorityCreate(generic.CreateView):
    model = Seniority
    fields = ['name', 'rank', 'role']


class SeniorityUpdate(generic.UpdateView, MultipleObjectMixin):
    model = Seniority
    fields = ['name', 'rank', 'role']
    paginate_by = 2

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Seniority.objects.all())
        self.object_list = self.object.skills.all()
        return super(SeniorityUpdate, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SeniorityUpdate, self).get_context_data(**kwargs)
        context['seniority'] = self.object
        return context


class SeniorityDelete(generic.DeleteView):
    model = Seniority
    success_url = reverse_lazy('skills:roles')
    template_name = 'skills/confirm_delete.html'
