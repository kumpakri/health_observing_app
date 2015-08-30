from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^edit/$', views.entry_list, name='entry_list'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.edit_page, name='edit_page'),
    url(r'^(?P<var_category>\w{0,4})/(?P<days>[0-9]+)/$', views.category_view, name='category_view'),
    url(r'^(?P<var_category>\w{0,4})/$', views.category_view, name='category_view'),
    url(r'^(?P<var_category>\w{0,4})/(?P<var_value>\w+)/$', views.value_view, name='value_view'),
    url(r'^(?P<var_category>\w{0,4})/(?P<var_value>\w+)/(?P<days>[0-9]+)/$', views.value_view, name='value_view'),
]