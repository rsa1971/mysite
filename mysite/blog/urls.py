from django.urls import path, include
from django.contrib import admin
from . import views


app_name = 'blog'

urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         name='post_detail'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
]
