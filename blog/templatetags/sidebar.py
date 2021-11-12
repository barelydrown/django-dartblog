from django import template
from blog.models import Post, Tag


register = template.Library()


@register.inclusion_tag('blog/pop_posts_tpl.html')
def show_popular(cnt=3):
    posts = Post.objects.order_by('-views')[:cnt]
    context = {'posts': posts}
    return context


@register.inclusion_tag('blog/tags_tpl.html')
def show_tags(cnt=None):
    if not cnt:
        tags = Tag.objects.all()
    else:
        tags = Tag.objects.all()[:cnt]
    context = {'tags': tags}
    return context
