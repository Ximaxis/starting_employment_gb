from django.urls import path
import one_app.views as one_app
from django.conf import settings
from django.conf.urls.static import static

app_name = 'one_app'

urlpatterns = [
    path(
        '',
        one_app.Index.as_view(),
        name='index'),
    path(
        'create_item/',
        one_app.CreateItem.as_view(),
        name='create_item'),
    ]