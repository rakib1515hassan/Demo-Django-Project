from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from django.contrib.auth import get_user_model
User = get_user_model()

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sessions.models import Session
from django.contrib import messages

from django.utils.decorators import method_decorator
from django.utils import timezone

from django.db.models.functions import Concat
from django.db.models import Q, Count, F, Value as V, CharField
from django.db.models.functions import ExtractMonth, ExtractYear

from django.http import HttpRequest, HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage
from django.core.exceptions import ValidationError

from datetime import datetime, timedelta
from random import randint

from django.views import View
from django.views import generic

## Custom
from backend_setting.permission import is_superuser_or_staff, is_superadmin 
from apps.student.models import Student
from apps.student.forms import StudentForm

"""
    Student Create
"""
# @method_decorator(user_passes_test(is_superuser_or_staff, 
#     login_url=reverse_lazy('auth:login')), name='dispatch')
class StudentCreateView(generic.CreateView, LoginRequiredMixin):
    model = Student
    form_class = StudentForm
    template_name = "Student/create.html"
    # success_url = reverse_lazy('employee:employee_list')

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)

    # def form_invalid(self, form):
    #     field_errors = {field.name: field.errors for field in form}
    #     has_errors = any(field_errors.values())

    #     print("---------------------")
    #     print(f"Field = {field_errors}, HasErrors = {has_errors}")
    #     print(f"HasErrors = {has_errors}")
    #     print("---------------------")

    #     return self.render_to_response(self.get_context_data(
    #             form = form, 
    #             field_errors = field_errors, 
    #             has_errors   = has_errors
    #         ))



"""
    Student List
"""
# @method_decorator(user_passes_test(is_superuser_or_staff, 
#     login_url=reverse_lazy('auth:login')), name='dispatch')
class StudentListView(View, LoginRequiredMixin):
    template_name = "Student/list.html"

    def get_queryset(self):
        queryset = Student.objects.all().order_by('-created_at')
        return queryset
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        context = {
            'students': queryset,
        }

        return render(request, self.template_name, context)