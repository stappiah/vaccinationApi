from django.urls import path
from . import views


urlpatterns = [
    path("hospital", views.CreateListHostpital.as_view()),
    path("hospital/<int:pk>", views.RetrieveUpdateHostpital.as_view()),
    path("child", views.CreateChild.as_view()),
    path("child/<int:pk>", views.RetrieveUpdateDeleteChild.as_view()),
    path("parent", views.RetrieveParentChild.as_view()),
    path("parent-child/<int:pk>", views.ListParentChild.as_view()),
    path("admin-hospital", views.GetAdminHospital.as_view()),
    path("hospital-confirmation", views.ConfirmDiseaseForHospital.as_view()),
    path("create-vaccination", views.CreateVaccination.as_view()),
    path("update-vaccination/<int:pk>", views.RetrieveUpdateVaccination.as_view()),

    path("create-appointment", views.CreateAppointment.as_view()),
    path("update-appointment/<int:pk>", views.UpdateAppointment.as_view()),
    path("parent-appointment", views.RetrieveParentAppointment.as_view()),
    path("hospital-appointment/<int:pk>", views.RetrieveHospitalAppointment.as_view()),
    path("hospital-vaccination/<int:pk>", views.GetHospitalVaccination.as_view()),
    path("hospital-mothers", views.GetHospitalMothers.as_view()),
    path("hospital-users", views.GetHospitalUsers.as_view()),
]
