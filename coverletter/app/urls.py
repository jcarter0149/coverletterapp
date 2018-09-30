from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = "coverletter"
urlpatterns = [
    url(r'^$', views.PersonFormView, name='personform'),
    url(r'^coverletter$', views.CoverLetterView, name='coverletter')
]

