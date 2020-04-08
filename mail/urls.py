from django.urls import path
from . import views

urlpatterns = [
    path('', views.application, name='application'),
    path("applicantlist", views.applicantlist, name="applicant_list"),
    #path("sendmail", views.sendmail, name="sendmail"),
    path('^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate_account, name='activate'),
    path('application', views.application, name='info')
    #path('info', views.info, name='info')
    ]