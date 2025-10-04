from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.order_by('-created_at') # descending order: Fetch all posts, newest first
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)# Fetch post by primary key or show 404
    return render(request, 'post_detail.html', {'post': post})

# render - showing a webpage or template with data

'''
IMPORTANT CONCEPTS

1. ForeignKey vs CharField: Use ForeignKey for relational integrity.
2. auto_now_add vs auto_now: Creation time vs updated time.
3. get_object_or_404: Safer than .get() to avoid 500 errors.
4. Template Tags:
    {{ }} = variable
    {% %} = logic/control
5. URL Namespacing: app_name + name ensures links are dynamic.
6. Admin registration: Without it, model won’t appear in admin.
7. Queryset ordering: .order_by('-created_at') = newest first
'''