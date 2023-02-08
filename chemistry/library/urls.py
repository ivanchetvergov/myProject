from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.library_home, name='library_home'),
    path('add', views.add, name='add'),
    path('<int:pk>', views.LibraryDetailView.as_view(), name='library-detail'),
    path('<int:pk>/update', views.LibraryUpdateView.as_view(), name='library-update'),
    path('tinymce/', include('tinymce.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('tasks', views.tasks, name='tasks')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
