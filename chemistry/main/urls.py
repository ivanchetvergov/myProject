from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='home'),
    path('task', views.task, name ='task'),
    path('home_page', views.home, name='home_page'),
    path('tinymce/', include('tinymce.urls')),
    path('theory', views.theory, name='theory'),
    path('links', views.links, name='links'),
    path('summernote/', include('django_summernote.urls')),
    path('<int:pk>', views.TheoryDetailView.as_view(), name='theory-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
