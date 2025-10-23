from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('<int:pk>/', views.article_detail, name='article_detail'),
    path('upload/', views.upload_article, name='upload_article'),
    path('mood_tips/', views.mood_tips, name='mood_tips'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
