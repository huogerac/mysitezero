from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [

    url(r'^index/$',
        TemplateView.as_view(template_name="core/index.html")),

]
