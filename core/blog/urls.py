
from django.urls import path
from django.views.generic import TemplateView
from django.views.generic import RedirectView
# from .views import indexView
from . import views

app_name = 'blog'

urlpatterns = [
    # path('fbv-index/',indexView,name='fbv-index'),
    # path('cbv-index/', TemplateView.as_view(template_name="index.html",extra_context={"name":"ali"})),
    path('cbv-index/',views.IndexView.as_view(),name='cbv-index'),
    # path('go-to-maktabkhooneh',RedirectView.as_view(url='https://www.maktabkhooneh.com'),name='go-to-maktabkhooneh')
    # path('go-to-index',RedirectView.as_view(pattern_name='blog:cbv-index'),name='go-to-index')
    path('go-to-maktabkhooneh/<int:pk>',views.RedirectToMaktabkhooneh.as_view(),name='go-to-maktabkhooneh'),
    path('post/',views.PostList.as_view(),name='post-list')
]