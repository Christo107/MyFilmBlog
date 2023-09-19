from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Actor
from .forms import CommentForm, BlogForm

# based on CI walkthrough blog project


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6

# based on CI walkthrough blog project


class PostDetail(View):

    def get(self, request, slug,  *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )
# based on CI walkthrough blog project

    def post(self, request, slug,  *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

# based on CI walkthrough blog project


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

# custom views for project


class ActorList(generic.ListView):
    model = Actor
    queryset = Actor.objects.all().order_by('name')
    template_name = "actor_list.html"
    paginate_by = 12


class ActorDetail(View):

    def get(self, request, id,  *args, **kwargs):
        queryset = Actor.objects.all()
        actor = get_object_or_404(queryset, id=id)

        return render(
            request,
            "actor_detail.html",
            {
                "actor": actor,
            },
        )

    def post(self, request, id,  *args, **kwargs):
        queryset = Actor.objects.all()
        actor = get_object_or_404(queryset, id=id)

        return render(
            request,
            "actor_detail.html",
            {
                "actor": actor,
            },
        )


def Add_BlogPost(request):
    """ Add a new blog post to the website """
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added blog post!')
            return redirect(reverse('add_blog_post'))
        else:
            messages.error(request, 'Failed to add blog post. Please\
                           ensure the form is valid.')
    else:
        form = BlogForm()

    template = 'add_blog_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def Delete_Blog_Post_Confirm(request, post_id):
    """ View to confirm blog post deletion """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins can do that.')
        return redirect(reverse('home'))

    queryset = Post.objects
    post = get_object_or_404(queryset, pk=post_id)

    template = 'delete_blog_post_confirm.html'
    context = {
        'post': post,
    }

    return render(request, template, context)


def Delete_Blog_Post(request, post_id):
    """ Delete a blog post """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins can do that.')
        return redirect(reverse('home'))

    blog_post = get_object_or_404(Post, pk=post_id)
    blog_post.delete()
    messages.success(request, 'Post deleted!')
    return redirect(reverse('home'))
