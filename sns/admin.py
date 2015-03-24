from django.contrib import admin
from sns.models import *


class ArticleModelAdmin(admin.ModelAdmin):
    search_fields = ('content',)
    list_display = ('datetime', 'student', 'category', 'content')


admin.site.register(Area)
admin.site.register(Student)
admin.site.register(Category)
admin.site.register(Article, ArticleModelAdmin)
admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(Car)
admin.site.register(Store)
admin.site.register(House)
admin.site.register(Trade)
