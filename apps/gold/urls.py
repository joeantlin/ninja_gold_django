from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^user$', views.user),
    url(r'^game$', views.game),
    url(r'^process_gold$', views.process_gold),
    url(r'^end$', views.end),
]