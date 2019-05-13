from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Tag
#from settings import BASE_DIR
# Create your views here.




def get_all_posts(request):
	"""
	Get all available posts with shor info

	"""
	posts = Post.objects.all()
	page_title = "Последние публикации"


	return render(request, 'testing/index.html', context={'posts': posts, 
				'title': page_title, "content_name": "Последние новости"})




def post_detail(request, slug):
    """ Showing full post
    
    Args:
        request (TYPE): request obj
        slug (TYPE): slug of post
    """

    post = Post.objects.get(slug__iexact=slug)


    return render(request, "testing/post_detail.html", context={'post': post})


def get_all_tags(request):
    """ 
    Display all available tags

    """

    tags = Tag.objects.all()

    return render(request, "testing/tag_list.html", context={"tags": tags})

def get_posts_by_tag(request, slug):
	"""Displaying all posts with exact tab
	
	Args:
	    request (TYPE): request obj
	    slug (TYPE): slug of the tag
	
	Returns:
	    rendered page
	"""

	posts = Post.objects.filter(tags__slug=slug)
	tag = Tag.objects.get(slug=slug)
	return render(request, 'testing/index.html', context={'posts': posts, 
				'title': tag, 'content_name':"Посты по тегу " + str(tag)})
	

def get_posts_by_author(request, author_id):
    """Render posts by certaion author
    
    Args:
        request, author_id 
    """

    posts = Post.objects.filter(author__id=author_id)
    
    return render (request, 'testing/index.html', context={'posts': posts,
    				'content_name':"Посты по заданому пользователю"})
