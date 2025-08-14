
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from . import settings
admin.site.site_header='انجمن علمی دانشگاه گیلان'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('', include('accounts.urls')),
    path('api/articles/', include('articles.urls')),
    path('api/events/', include('events.urls')),
    path('api/news/', include('news.urls')),
    path('api/comments/', include('comments.urls')),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)