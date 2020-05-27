from django.contrib import admin

# Register your models here.
from django.utils import timezone
# Register your models here.
from apps.blog.models import (
    Posts,PostDetail,About,Post_Subjects,
    Comment,Subscription
)

class PostsAdmin(admin.ModelAdmin):
    list_display = ('title','slug','reference_url','is_publish','days_since_creation','created_at') # Show these element in admin
    list_filter = ('is_publish',)
    search_fields = ('title','slug')
    prepopulated_fields = {'slug':('title',)} # It will auatomatically prefilled slug when we type title
    ## Arrange fields
    #fields = (('title','slug'))
    def days_since_creation(self,Posts):
        diff = timezone.now().date() - Posts.publish_date
        return diff.days 
    days_since_creation.short_description = 'Days Active' # Rename new prperty

class PostDetailAdmin(admin.ModelAdmin):
    list_display = ('post_id','title','is_publish','created_at')
    search_fields = (['title'])

admin.site.register(Post_Subjects)
admin.site.register(Posts,PostsAdmin)
admin.site.register(PostDetail,PostDetailAdmin)
admin.site.register(About)
admin.site.register(Comment)
admin.site.register(Subscription)
