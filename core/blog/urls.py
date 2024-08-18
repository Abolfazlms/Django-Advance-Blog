
from django.urls import include, path
from django.views.generic import TemplateView
from django.views.generic import RedirectView
# from .views import indexView

from . import views

app_name = 'blog'

urlpatterns = [
    # path('fbv-index/',indexView,name='fbv-index'),
    # path('cbv-index/', TemplateView.as_view(template_name="index.html",extra_context={"name":"ali"})),    
    # path('go-to-maktabkhooneh',RedirectView.as_view(url='https://www.maktabkhooneh.com'),name='go-to-maktabkhooneh')
    # path('go-to-index',RedirectView.as_view(pattern_name='blog:cbv-index'),name='go-to-index')

    path('cbv-index/',views.IndexView.as_view(),name='cbv-index'),
    path('go-to-maktabkhooneh/<int:pk>',views.RedirectToMaktabkhooneh.as_view(),name='go-to-maktabkhooneh'),
    path('post/',views.PostListView.as_view(),name='post-list'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='post-detail'),
    path('post/create/',views.PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/edit',views.PostEditView.as_view(),name='post-edit'),
    path('post/<int:pk>/delete',views.PostDeleteView.as_view(),name='post-delete'),

    path('api/v1/',include('blog.api.v1.urls'))
]