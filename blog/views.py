from django.shortcuts import render
from .models import Post
from django.views import generic

# Create your views here.

class HomeView(generic.TemplateView):
    template_name = "templates/home.html"

class BlogView(generic.DetailView):
    model = Post
    template_name = "templates/blog.html"

class BlogListView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('date_created')
    template_name = "templates/blog-list.html"
    context_object_name = "blog_post_items" #DICT key containing all the blog POSTS in queryset

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BlogListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        # context['some_data'] = 'This is just some data'
        context.update({'some_data1' : 'This is just some data1'})
        return context