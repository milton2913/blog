from django.db.models import Count
from blog.models.category import Category
from blog.models.tag import Tag

class CategoryService:
    @staticmethod
    def get_active_categories():
        return Category.objects.filter(is_active=True).annotate(
            post_count=Count('posts', distinct=True)
        )

class TagService:
    @staticmethod
    def get_active_tags():
        return Tag.objects.filter(is_active=True)
