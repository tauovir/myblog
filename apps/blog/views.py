from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from apps.blog.models import Posts,About,Comment
from django.core.paginator import Paginator
from apps.blog import forms

from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template
import json
from apps.blog.errorMessage import getApiMsg
import re 
from apps.blog.utility import utils
from django.contrib.auth import login, authenticate,logout
from django.views import View
from django.contrib import messages
# Create your views here.

def post(request,num = 1):
    #logout(request)
    #obj =Posts.objects.all()[:5]
    limit = 7
    posts = Posts.objects.filter(is_publish=1).order_by('-publish_date')
    aboutData = About.objects.first()
    paginator = Paginator(posts, limit)

    if 'page' in request.GET:
        page = request.GET.get('page')
    else :
         page = num
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    
    subcsribeForm = forms.SubscribeForm()
    
    context = {
        'posts': queryset,
        'subcsribeForm' : subcsribeForm,
        'aboutData' : aboutData
    }
    # print("***********************")
    return render(request, 'blog/index.html', context)
    #return HttpResponse("<h1> khan </h1>")


def post_detail_view(request,slug):
    try:
        post = Posts.objects.get(slug=slug)
        commetQuerySet = Comment.objects.filter(post = post).order_by('-created_at')
        comments = utils.setCommentFormat(commetQuerySet)
        aboutData = About.objects.first()
        context = {
            'posts': post,
            'comments' : comments,
            'aboutData' : aboutData,
        }
    except Posts.DoesNotExist:
        raise Http404("Page Not exist")
    utils.writeTempFile(slug)
    return render(request, 'blog/blog-post.html', context)
    #return render(request, 'std.html', context)


# def about(request):
#     aboutData = About.objects.first()
#     context = {
#         'aboutData' : aboutData
#     }
#     return render(request, 'blog/about.html', context)


# Class Based view for Aboutus
class AboutView(View):
    template_name = 'blog/about.html'

    def get(self, request):
        aboutData = About.objects.first()
        subcsribeForm = forms.SubscribeForm()
        context = {
        'aboutData' : aboutData,
        'subcsribeForm': subcsribeForm
     }
        return render(request, 'blog/about.html', context)

    
#     return render(request, 'portfolio.html', {})

# def subscribe(request):
#     if request.method == 'POST':
#         #form = forms.Subscribe(request.POST)
#         from_email = request.POST['emial']
#         regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
#         if re.search(regex,from_email) == None:
#             response = {'message' : 'Please enter valid email!','code': 201, 'data': {}}
#             return HttpResponse(json.dumps(response), content_type="application/json")
#         sendSubscriptionEmail(from_email)
#         response = {'message' : getApiMsg(200),'code': 200, 'data': {}}
#         return HttpResponse(json.dumps(response), content_type="application/json")
#     else:
#         response = {'message' : getApiMsg(201),'code': 201, 'data': {}}
#         return HttpResponse(json.dumps({'email': 'null'}), content_type="application/json")


class SubscribeView(View):

  def post(self, request):
     # create a form instance and populate it with data from the request:
        print("========================")
        subcsribeForm = forms.SubscribeForm(request.POST)
         # check whether it's valid:
        if subcsribeForm.is_valid():
            # process the data in form.cleaned_data as required
            cleanedData = subcsribeForm.cleaned_data
            subcsribeForm.save()
            messages.add_message(request, messages.SUCCESS, 'Thank you for subscription')
            # redirect to a new URL:
            return redirect('post')
        else:
            context = {
            'subcsribeForm' : subcsribeForm,
            }
            # render(request, 'my_template.html', {'form': form})
            return render(request, 'blog/index.html', context)




def sendSubscriptionEmail(fromEmail):
    subject = "Subscription"
    to_email = settings.DEFAULT_TO_EMAIL
    message = "Sub Scription Request"
    name = 'Anonymous'
    emailData = {
        'name' :name,
        'message' : message,
        'email' : fromEmail,
    }

    messageTemplate = get_template('emails/contactus.html').render(emailData)
    response = send_mail(
        subject,
        messageTemplate,
        fromEmail,
        [to_email],
        fail_silently=True
    )
    return response


# Since Allauth not staying on same page ,We have redicred on that page using slug
def commentRedirect(request):
    slug =  utils.writeTempFile()
    return redirect('post_detail/'+slug)


# def getSession(request):
#     if request.session.has_key('slug'):
#         slug = request.session['slug']
#         return redirect('post_detail/'+slug)
#     else:
#         print("Session not found")
#         return redirect('post')
    