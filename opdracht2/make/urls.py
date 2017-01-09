from django.conf.urls import url
from . import views

app_name = 'make'

urlpatterns = [

    # index pagina
    url(r'^$', views.welcome, name='welcome'),
    #rate pagina
    url(r'^rate$', views.index, name='index'),
    # =create pagina
    url(r'^create$', views.create, name='create'),
    #Tosti opslaan
    url(r'^save/$', views.save, name='save'),

    url(r'^(?P<tosti_id>[0-9]+)/$', views.detail, name='detail' ),

    url(r'^(?P<tosti_id>[0-9]+)/upvote/$', views.upvote, name='upvote')


]
