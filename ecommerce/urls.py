from django.contrib import admin
from django.urls import path, include
from .import views
from django.conf import settings
#from django.conf.urls.static import static, staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import views





urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('products.urls')),
    path('auth/', include('user_auth.urls')),
    path('cart/', include('cart.urls')),
    path('check_out/', include('payments.urls')),
    path('admin_panel/', include('admin_panel.urls')),
    path('', include('product_categories.urls')),
    path('', include('system_setting.urls')),
    path('', include('chat_notification.urls')),
    

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
