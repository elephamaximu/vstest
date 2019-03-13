from django.shortcuts import render
from . models import Article
from django.http import HttpResponse

# Create your views here.

def article_list(request):
    qs = Article.objects.all()
    q = request.GET.get('q', '') 
    # request.getParameter('q')
    if q:
        qs = qs.filter(title__contains=q)
    return render(request, 'shop/article_list.html', 
              {'article_list':qs, 'q2':q})

def article_insert(request):
    article = Article(title='목요일', body='날씨가좋아요', status='p')
    article.save()
    Article.objects.create(title='금요일', body='날씨가 더 좋아요', status='p')
    return HttpResponse("입력합니다.")

def article_update(request):
    #aa = Article.objects.get(id=1)
    '''
    aa = Article.objects.first()
    aa.title = "진짜로오금요일입니다."
    aa.save()
    '''
    '''
    qs = Article.objects.filter(title__contains=1)
    print(qs)
    for aa in qs:
        aa.title = '1입니다.'
        aa.save() 
    '''
    
    qs = Article.objects.filter(title__contains='3')
    qs.update(title = '3입니다.')

    return HttpResponse("수정합니다.")

from django.db.models import Q
def article_delete(request):
    qs = Article.objects.filter(Q(title__contains='7') | Q(title__contains='8'))
    qs.delete()
    return HttpResponse("삭제합니다.")