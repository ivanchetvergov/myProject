from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.library_home, name='library_home'),
    path('<int:pk>', views.LibraryDetailView.as_view(), name='library-detail'),
    path('<int:pk>/update', views.LibraryUpdateView.as_view(), name='library-update'),
    path('tinymce/', include('tinymce.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('tasks', views.tasks, name='tasks'),
    path('tasks1', views.tasks1, name='tasks1'),
    path('tasks2', views.tasks2, name='tasks2'),
    path('tasks3', views.tasks3, name='tasks3'),
    path('tasks4', views.tasks4, name='tasks4'),
    path('tasks5', views.tasks5, name='tasks5'),
    path('tasks6', views.tasks6, name='tasks6'),
    path('tasks7', views.tasks7, name='tasks7'),
    path('about', views.about, name='about-project')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
