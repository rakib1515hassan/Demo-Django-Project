from django.urls import path, include
from apps.student import views

app_name = 'student'

urlpatterns = [
    path('create/', views.StudentCreateView.as_view(), name='student_create'),
    path('list/', views.StudentListView.as_view(), name='student_list'),
    # path('delete/<int:s_id>/', views.deleteStudent, name='std_delete'),
]
