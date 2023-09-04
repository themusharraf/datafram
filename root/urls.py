from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from root.settings import DEBUG, STATIC_ROOT, STATIC_URL
from root.settings import MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path('', admin.site.urls),
]
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
