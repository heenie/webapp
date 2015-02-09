import django_filters
from sns.models import Article


class ArticleFilter(django_filters.FilterSet):

    class Meta:
        model = Article
        fields = ['category']