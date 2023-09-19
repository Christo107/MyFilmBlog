from . import views
from django.urls import path
from .views import Add_BlogPost, Delete_Blog_Post, Delete_Blog_Post_Confirm

# based on CI walkthrough blog project
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('actor_list/', views.ActorList.as_view(), name='actor_list'),
    path('actor/<int:id>/', views.ActorDetail.as_view(), name='actor_detail'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('blog/add/', views.Add_BlogPost, name='add_blog_post'),
    path('<int:post_id>/confirm_delete/', views.Delete_Blog_Post_Confirm,
         name='delete_blog_post_confirm'),
    path('<int:post_id>/delete/', views.Delete_Blog_Post,
         name='delete_blog_post'),
]
