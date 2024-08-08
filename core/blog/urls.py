
from django.urls import path
from django.views.generic import TemplateView
from .views import indexView
from . import views

urlpatterns = [
    path('fbv-index/',indexView,name='fbv-index'),
    # path('cbv-index/', TemplateView.as_view(template_name="index.html",extra_context={"name":"ali"})),
    path('cbv-index/',views.IndexView.as_view(),name='cbv-index')
]