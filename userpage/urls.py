from django.urls import path,include
from . import views

app_name="userpage"

urlpatterns = [
    path('',views.index,name="index"),
    path('upload/',views.UploadImg.as_view(),name="upload")

]