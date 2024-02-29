from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView

from materials.models import Material
from materials.service import add_user_to_group, get_groups_completeness, get_users_percentage


class MaterialsListView(ListView):
    model = Material
    extra_context = {'title': 'materials'}


class MyCoursesListView(LoginRequiredMixin, ListView):
    model = Material
    template_name = 'materials/my_courses.html'
    extra_context = {'title': 'my courses'}

    def get_queryset(self):
        user = self.request.user
        courses = super().get_queryset().filter(material_users=user.pk)
        return courses

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['show_lessons'] = self.request.GET.get('show_lessons')
        if context['show_lessons']:
            context['detailed_course'] = Material.objects.get(pk=self.request.GET.get('course'))
        return context


def course_statistics(request, course_pk):
    course = Material.objects.get(pk=course_pk)
    context = {
        'title': 'course info',
        'course': course,
        'groups_completeness': get_groups_completeness(course),
        'users_percentage': get_users_percentage(course),
    }
    return render(request, 'materials/course_statistics.html', context)


def add_course(request, course_pk):
    course = Material.objects.get(pk=course_pk)
    # тут логика покупки курса
    request.user.material_users.add(course)
    add_user_to_group(course, request.user)
    return render(request, 'materials/material_list.html', {'title': 'materials'})
