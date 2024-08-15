
from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView, FormView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


from .models import Post
from .forms import PostForms

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
    
class PostListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):

    permission_required='blog.view_post'
    # model = Post
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 2
    ordering = '-id'
    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     # return super().get_queryset()
    #     return posts

class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post

'''
class PostCreateView(FormView):
    template_name = 'blog/contact.html'
    form_class = PostForms
    success_url = '/blog/post/'

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
'''
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # fields = ['author','title','content','status','category','published_date']
    form_class = PostForms
    success_url = '/blog/post/'

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForms
    success_url = '/blog/post/'

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/blog/post/'