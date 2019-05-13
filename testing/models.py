from django.db import models
from django.shortcuts import reverse
# Create your models here.


        



class Author(models.Model):

	"""Model that describes user
	
	"""

	name = models.CharField(max_length=100, db_index=True)
	surname = models.CharField(max_length=100, db_index=True)

	def __str__(self):
		return str(self.name + " " + self.surname)



class Tag(models.Model):
	title = models.CharField(max_length=50)
	slug = models.SlugField(max_length=50, unique=True)

	def __str__(self):
		return str(self.title)


class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    body = models.TextField(db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')

    def get_absolute_url(self):
    	"""
    	full path to current page

    	"""
    	return reverse('post_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return str(self.title)

