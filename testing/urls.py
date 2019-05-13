from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [

	path('', get_all_posts, name="post_list_url"),
	path('post/<str:slug>/', post_detail, name="post_detail_url"),
	path('tags/', get_all_tags, name="all_tags_url"),
	path('tags/<str:slug>/', get_posts_by_tag, name="post_by_tag_url"),
	path('author/<str:author_id>', get_posts_by_author, name="post_by_author_url")

]