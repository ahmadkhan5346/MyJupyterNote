from django.urls import path
from app.views import StudentApi




urlpatterns = [
    path('student/', StudentApi.as_view(), name='student'),
]