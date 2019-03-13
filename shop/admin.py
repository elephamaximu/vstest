from django.contrib import admin
from . models import Post, Article
# Register your models here.

# 방식1
# admin.site.register(Post)

#방식2

'''
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'content', 'content_size10', 'content_len', 'created_at','updated_at']

    def content_size10(self, Post):
        return '{}'.format(Post.content[:10])
    content_size10.short_description = "일부내용"

    def content_len(self, Post):
        return '{}글자'.format(len(Post.content))
    content_len.short_description = "글자수"

admin.site.register(Post, PostAdmin)
'''
# 방식 3

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'content', 'content_size10', 'content_len', 'created_at','updated_at']
    list_display_links = ['title', 'content','content_size10']
    # fields = ['title', 'content']
    list_filter=['user','title']
    search_fields=['title','content']

    def content_size10(self, Post):
        return '{}'.format(Post.content[:10])
    content_size10.short_description = "일부내용"

    def content_len(self, Post):
        return '{}글자'.format(len(Post.content))
    content_len.short_description = "글자수"

def action1(self, request, queryset):
    queryset.update(status='p')
action1.short_description = '모두 p로 변경하기'

def action2(self, request, queryset):
    queryset.update(status='d')
action2.short_description = '모두 d로 변경하기'

def action3(self, request, queryset):
    queryset.update(status='w')
action3.short_description = '모두 w로 변경하기'

def action4(self, request, queryset):
    queryset.update(title='타이틀변경 했3')
action4.short_description = '선택한 타이틀 변경하기'

def action5(self, request, queryset):
    queryset.update(body='날씨가 좋아져라')
action5.short_description = '선택한 body 변경하기'

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    ordering = ['title']
    actions = [action1, action2, action3, action4, action5]
   
    list_display_links = ['title', 'status']
    list_filter=['status']
    search_fields=['title']


