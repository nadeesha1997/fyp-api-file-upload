from django.urls import path
from . import views

urlpatterns = [
    path('text/',views.UploadStringView.as_view(),name='upload_string'),
    path('file/',views.UploadFileView.as_view(),name='file_upload')
]
