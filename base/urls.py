from django.urls import path
from . import views


urlpatterns = [
    path("hospital", views.CreateListHostpital.as_view()),
    path("child", views.CreateChild.as_view()),
    path("child/<int:pk>", views.RetrieveUpdateDeleteChild.as_view()),
    path("parent", views.RetrieveParentChild.as_view()),
    path("admin-hospital", views.GetAdminHospital.as_view()),
    path("hospital-confirmation", views.ConfirmDiseaseForHospital.as_view()),
]
