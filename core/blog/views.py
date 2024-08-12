from typing import Any
from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import ListView
from .models import Post
# Create your views here.

#Function Base View show a template
'''
def indexView(request):
    """
    a function based view to show index page
    """
    name = "ali"
    context={"name":name}
    return render(request,"index.html",context)
'''
class IndexView(TemplateView):
    """
    a class based view to show index page
    """
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['name'] = 'ali'
        context ['post'] = Post.objects.all()
        return context

''' FBV To Redirect
from django.shortcuts import redirect
def RedirectToMaktabkhooneh(request):
    return redirect('https://www.maktabkhooneh.com')
'''
class RedirectToMaktabkhooneh(RedirectView):
    url='https://maktabkhooneh.com'

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args,**kwargs)
    
class PostList(ListView):
    model = Post
    context_object_name = 'posts'