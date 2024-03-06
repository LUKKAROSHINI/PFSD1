from django.urls import path
from.import views
urlpatterns=[
    path("checkadminlogin",views.checkadminlogin,name="checkadminlogin"),
    path("checkRegistration",views.checkRegistration,name="checkRegistration"),

]

