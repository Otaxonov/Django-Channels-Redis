from django.urls import path
from Test.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='test_home')
]