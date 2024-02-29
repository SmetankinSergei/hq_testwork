from django.urls import path

from materials import views


app_name = 'materials'

urlpatterns = [
    path('', views.MaterialsListView.as_view(), name='materials'),
    path('my_courses/', views.MyCoursesListView.as_view(), name='my_courses'),
    path('add_course/<int:course_pk>/', views.add_course, name='add_course'),
    path('course_statistics/<int:course_pk>/', views.course_statistics, name='course_statistics'),
]
