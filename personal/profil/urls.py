from django.urls import path
from . import views
from personal.settings import DEBUG, STATIC_URL, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),
]
if DEBUG:
    # urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)