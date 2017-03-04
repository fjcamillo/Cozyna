from django.conf.urls import url, include
from .views import index, sitCounter

urlpatterns = [
    url(r'^sit/', sitCounter.as_view()),
]
