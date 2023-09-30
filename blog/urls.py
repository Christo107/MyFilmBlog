from . import views
from django.urls import path
from .views import (Add_BlogPost, Delete_Blog_Post, Delete_Blog_Post_Confirm,
                    Edit_Blog_Post, Edit_Comment, Delete_Comment_Confirm,
                    Delete_Comment, PostLike, Add_Actor)

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
     path('edit/<int:post_id>/', views.Edit_Blog_Post, name='edit_blog_post'),
     path('edit_comment/<int:comment_id>/', views.Edit_Comment,
          name='edit_comment'),
     path('<int:comment_id>/delete_confirm/', views.Delete_Comment_Confirm,
          name='delete_comment_confirm'),
     path('delete/<int:comment_id>/', views.Delete_Comment,
          name='delete_comment'),
     path('actor/add/', views.Add_Actor, name='add_actor'),
]
