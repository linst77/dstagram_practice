from django.contrib import admin
from django.urls import path
from django.views.generic.detail import DetailView
from .views import *
from .models import Photo
from django.contrib.auth.mixins import LoginRequiredMixin

# name spac
app_name = "photo"

urlpatterns = [
    path('', photo_list, name='photo_list'),
    path('upload/', PhotoUploadView.as_view(), name="photo_upload"),
    path('delete/<int:pk>/', PhotoDeleteView.as_view(), name="photo_delete"),
    path('update/<int:pk>/', PhotoUpdateView.as_view(), name="photo_update"),
    path('detail/<int:pk>/', DetailView.as_view(model=Photo, template_name='photo/detail.html'), name="photo_detail"),
    # 위와 같이 view에서 특별한 작업이 없을시(generic view만 사용) urls에 바로 generic view를 넣어서 사용할수 있다.
]
