from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('rem.urls', namespace='rem')),
    # path('cart/', include('cart.urls')),
    url('admin/', admin.site.urls),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^', include('rem.urls', namespace='rem')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
