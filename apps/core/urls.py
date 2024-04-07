from django.urls import path
from apps.core import apis

app_name = 'core'

urlpatterns = [
    path('division/', apis.DivisionList.as_view(), name='all_division'),

    path('districts/', apis.DistrictList.as_view(), name='all_districts'),
    path('districts/<int:pk>/', apis.DistrictList.as_view(), name='districts'),
    
    path('upazila/',   apis.UpazilaList.as_view(),  name='all_upazila'),
    path('upazila/<int:pk>/',   apis.UpazilaList.as_view(),  name='upazila'),

    path('postcode/',   apis.PostCodeList.as_view(),  name='all_post_code'),
    # path('postcode/<int:division_id>/', apis.PostCodeList.as_view(),  name='upazila_by_division'),
    path('postcode/<int:district_id>/', apis.PostCodeList.as_view(),  name='upazila_by_district'),

    
]