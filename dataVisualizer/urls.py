from django.conf.urls import url
from . import views
from .views import ChartsData,HomeView

app_name = 'dataVisualizer'

urlpatterns = [
    # /dataVisualizer
    url(r'^$', views.index, name='index'),
    url(r'^tableview$', views.table, name='tableview'),
    url(r'^about$', views.about, name='about'),
    url(r'^api/chart/data$', ChartsData.as_view(), name='api-data'),
    url(r'^chart/data$', HomeView.as_view(), name='charts-data'),
    url(r'^api/data$', views.get_data, name='api-data')
]