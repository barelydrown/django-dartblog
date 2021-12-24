from django.db import models
from django.urls import reverse
from django.db import transaction


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('get_category', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Categories'


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('get_tag', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    views = models.IntegerField(default=0)
    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        related_name='posts'
    )
    tags = models.ManyToManyField('Tag', blank=True, related_name='tags')
    is_pinned = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.is_pinned:
            return super(Post, self).save(*args, **kwargs)
        with transaction.atomic():
            Post.objects.filter(is_pinned=True).update(is_pinned=False)
            return super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('get_post', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-created_at']
