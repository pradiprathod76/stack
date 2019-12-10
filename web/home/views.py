from django.shortcuts import render,get_object_or_404
from . import models
from .form import FeedbackForm

# Create your views here.
qs_work = models.Works.objects.all()
qs = models.Feature.objects.all()
qs_service = models.Service.objects.all()
qs_team = models.Team.objects.all()
qs_rating = models.Rating.objects.all()
qs_price = models.Price.objects.all()
qs_skill = models.Skill.objects.all()
qs_profile = models.Profile.objects.all()
qs_contect = models.Contect.objects.all()
qs_blog = models.Blog.objects.all()[:3]


def home(request):
    if request.method == 'POST':
        my_form = FeedbackForm(request.POST)
        if my_form.is_valid():
             my_form.save()
    else :
        my_form = FeedbackForm()
    
    




    context = {
        'feature':qs,
        'service':qs_service,
        'team':qs_team,
        'rating':qs_rating,
        'price':qs_price,
        'skill':qs_skill,
        'profile':qs_profile,
        'contect':qs_contect,
        'form' : my_form,
        'blog': qs_blog,
        'all': qs_work,
        
    }
    return render(request,'index.html',context)


def Develop(request):
    if request.method == 'POST':
        my_form = FeedbackForm(request.POST)
        if my_form.is_valid():
             my_form.save()
    else :
        my_form = FeedbackForm()
    #qs_work_de = models.Works.objects.filter(w_type='design')
    #qs_work_pr = models.Works.objects.filter(w_type='print')    
    qs_work_dev = models.Works.objects.filter(w_type='develop')        
    
    context = {
        #'design': qs_work_de,
        #'print': qs_work_pr,
        'develop': qs_work_dev,
        #'all': qs_work,
        'feature':qs,
        'service':qs_service,
        'team':qs_team,
        'rating':qs_rating,
        'price':qs_price,
        'skill':qs_skill,
        'profile':qs_profile,
        'contect':qs_contect,
        'form' : my_form,
        'blog': qs_blog,

    }
    return render(request,'index.html',context)

def Print(request):
    if request.method == 'POST':
        my_form = FeedbackForm(request.POST)
        if my_form.is_valid():
             my_form.save()
    else :
        my_form = FeedbackForm()
    #qs_work_de = models.Works.objects.filter(w_type='design')
    qs_work_pr = models.Works.objects.filter(w_type='print')    
    #qs_work_dev = models.Works.objects.filter(w_type='develop')        
    
    context = {
        #'design': qs_work_de,
        'print': qs_work_pr,
        #'develop': qs_work_dev,
        #'all': qs_work,
        'feature':qs,
        'service':qs_service,
        'team':qs_team,
        'rating':qs_rating,
        'price':qs_price,
        'skill':qs_skill,
        'profile':qs_profile,
        'contect':qs_contect,
        'form' : my_form,
        'blog': qs_blog,

    }
    return render(request,'index.html',context)

def Design(request):
    if request.method == 'POST':
        my_form = FeedbackForm(request.POST)
        if my_form.is_valid():
             my_form.save()
    else :
        my_form = FeedbackForm()
    qs_work_de = models.Works.objects.filter(w_type='design')
    #qs_work_pr = models.Works.objects.filter(w_type='print')    
    #qs_work_dev = models.Works.objects.filter(w_type='develop')        
    
    context = {
        'design': qs_work_de,
        #'print': qs_work_pr,
        #'develop': qs_work_dev,
        #'all': qs_work,
        'feature':qs,
        'service':qs_service,
        'team':qs_team,
        'rating':qs_rating,
        'price':qs_price,
        'skill':qs_skill,
        'profile':qs_profile,
        'contect':qs_contect,
        'form' : my_form,
        'blog': qs_blog,

    }
    return render(request,'index.html',context)

def single_post(request,id):
    blog = get_object_or_404(models.Blog,id=id)
    post = models.Blog.objects.all()[:3]
    contex = {
        'blog':blog,
        'post':post
    }
    return render(request,'single_post.html',contex)