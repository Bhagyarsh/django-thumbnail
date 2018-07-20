from django.conf.urls import url, include

from .views import ContentCreateAPIView,ContentUpdateAPIView

urlpatterns = [

    url(r'^$',ContentCreateAPIView.as_view(), name='content-create'),
    url(r'^(?P<pk>\d+)/$',ContentUpdateAPIView.as_view(), name='content-update'),
    ]
