from django.contrib import admin
from .models import Comment, Follow, Group, Post


class GroupAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'
    list_editable = ('description',)
    list_display = ('pk', 'title', 'slug', 'description')
    search_fields = ('title',)


class PostAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'
    list_editable = ('group',)
    list_display = ('pk', 'text', 'pub_date', 'author', 'group')
    list_filter = ('pub_date',)
    search_fields = ('text',)


class CommentAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'
    list_display = ('pk', 'author', 'post', 'text', 'created')
    list_filter = ('created',)
    search_fields = ('text', 'author__username', 'post__text')


class FollowAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'
    list_display = ('pk', 'user', 'following')
    search_fields = ('user__username', 'following__username')


admin.site.register(Group, GroupAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Follow, FollowAdmin)
