from template_app import views
from django.urls import path

app_name='template_app'
urlpatterns = [

    path('',views.other,name="other"),
    path('relative/',views.relative,name="relative"),
]
