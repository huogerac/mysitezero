from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = [

    url(settings.ADMIN_URL, admin.site.urls, name='django.admin.home'),

    url(r'^core/', include('core.urls')),

    url(r'^$', RedirectView.as_view(url='/core/index'), name='core.index'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
