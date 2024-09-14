from django.urls import path
from . import views

urlpatterns = [
    path('register', views.UserRegistrationView.as_view()),
    path('profile/<int:pk>', views.ManageAccountView.as_view()),
    path('login', views.CustomAuthModel.as_view()),
    path('create-admin', views.CreateHospitalAdmin.as_view()),
    path('change-password', views.ChangePassword.as_view()),
    path('get-hospital-admin/<int:pk>', views.ListHospitalAdmin.as_view()),
    path('delete-admin/<int:pk>', views.DeleteAdmin.as_view())
]
