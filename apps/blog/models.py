from django.db import models

# Create your models here.
import os
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
import datetime


# Create your models here.
def imagePath():
    return os.path.join(settings.STATIC_URL, 'assets/images/blog')
    
class Post_Subjects(models.Model):
    subject = models.CharField(max_length=120) # max_length required
    image = models.ImageField(upload_to = 'subjects',null = True, blank = True)
    class ActiveStatus(models.IntegerChoices):
        INACTIVE = 0
        ACTIVE = 1

    status = models.IntegerField(choices=ActiveStatus.choices)
    created_at = models.DateField(default=datetime.date.today) 
    # It will show the title in admin panel instead of objects(id)
    def __str__(self):
        return  self.subject
    class Meta:
        verbose_name = 'post_subject' 
        verbose_name_plural = 'post_subjects'

class Posts(models.Model):
    post_subject = models.ForeignKey(Post_Subjects, on_delete=models.CASCADE)
    title = models.CharField(max_length=120) # max_length required
    slug = models.SlugField(max_length=120) # max_length required
    summary = RichTextUploadingField(blank=False, null=False)
    image = models.ImageField(upload_to = 'blogs', blank = True)
    banner_image = models.ImageField(upload_to = 'banners', null= True)
    reference_url = models.URLField(max_length = 200, default='https://github.com/tauovir', blank = True)
    comment_count = models.IntegerField(default=0)
    # It will show the title in admin panel instead of objects(id)
    def __str__(self):
        return  self.title

    class IsPublish(models.IntegerChoices):
        NOT_PUBLISH = 0
        PUBLISH = 1

    is_publish = models.IntegerField(choices=IsPublish.choices)
    publish_date = models.DateField(auto_now_add = False) 
    created_at = models.DateField(default=datetime.date.today) 
    updated_at = models.DateField(auto_now_add = True) 

    def get_absolute_url(self):
        return f"post/{self.slug}"

    class Meta:
        verbose_name = 'post' 
        verbose_name_plural = 'posts'
    
    # @property
    # def days_since_creation(self):
    #     diff = timezone.now().date() - self.publish_date
    #     return diff.days 


    """
    When you're using a ModelForm instance to create/edit a model, 
    the model's clean() method is guaranteed to be called. So, 
    if you want to strip whitespace from a field, you just add a clean() method to your model (no need to edit the ModelForm class):
    """
    # def clean(self):
    #    if self.code:
    #        self.code = self.code.strip()

    # It will show the title in admin panel instead of objects(id)
    def __str__(self):
        return  self.title
    
   
class About(models.Model):
    brief_summary = RichTextUploadingField() 
    detail_summary = RichTextUploadingField() 
    skils = RichTextUploadingField(blank=False, null=False)
    blog_summary = RichTextUploadingField(blank=False, null=False)
    image = models.ImageField(upload_to = 'profile')
    # size is "width x height"
    # cropping = ImageRatioField('image', '430x360',size_warning=True)
    blog_image = models.ImageField(upload_to = 'profile')
    created_at = models.DateField(default=datetime.date.today) 
    updated_at = models.DateField(auto_now_add = True) 
    
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    comment = models.CharField(max_length=250) # max_length required
    replied_on= models.IntegerField(default=0)
    created_at = models.DateField(default=datetime.date.today) 
    def __str__(self):
        return  self.comment


class Subscription(models.Model):
    email = models.EmailField(max_length=100)
    created_at = models.DateField(default=datetime.date.today)
    class Meta:
        verbose_name = 'subscription' 
        verbose_name_plural = 'subscriptions' 

    def __str__(self):
        return self.email

        
# Signals is just like a triggers, After inserting comment,we are updating comment_count in post object
from django.db.models import signals
from django.dispatch import receiver

@receiver(signals.post_save, sender=Comment) 
def update_comment_count(sender, instance, created, **kwargs):
    print("================Comment signals Executed===============" )
    postObj = Posts.objects.get(id = instance.post.pk)
    postObj.comment_count += 1 
    postObj.save()
