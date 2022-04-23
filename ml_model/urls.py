from django.urls import path
from . import views

urlpatterns = [
    path('model/', views.MlModelView.as_view(), name='model'),
    path('usermodel/', views.UserModelView.as_view(), name='usermodel')
]
