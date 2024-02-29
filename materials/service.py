from django.db.models import Count

from materials.models import Group
from users.models import User


def add_user_to_group(course, user):
    if not Group.objects.filter(material=course).exists():
        group = Group.objects.create(name=f'{course.name}-1', material=course)
        group.students.add(user)
    else:
        groups = Group.objects.filter(material=course).annotate(num_students=Count('students'))
        groups = sorted(groups, key=lambda x: x.num_students)
        if groups[0].students.count() < course.max_students_in_group:
            groups[0].students.add(user)
        else:
            new_group = create_new_group(course)
            new_group.students.add(user)
            while new_group.students.count() < groups[-1].students.count():
                student = groups[-1].students.last()
                new_group.students.add(student)
                groups[-1].students.remove(student)
                groups = sorted(groups, key=lambda x: x.students.count())


def create_new_group(course):
    last_group = Group.objects.filter(material=course).last()
    new_group_number = int(last_group.name.split('-')[-1]) + 1
    return Group.objects.create(name=f'{course.name}-{new_group_number}', material=course)


def get_groups_completeness(course):
    groups_amount = Group.objects.filter(material=course).count()
    students_amount = course.material_users.all().count()
    mean_amount = round(students_amount / groups_amount)
    return round((100 / course.max_students_in_group) * mean_amount)


def get_users_percentage(course):
    all_students = User.objects.count()
    course_students = course.material_users.all().count()
    return round((100 / all_students) * course_students)
