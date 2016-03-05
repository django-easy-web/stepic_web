from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Question, Answer

from django.core.paginator import Paginator


def test(request, *args, **kwargs):
    return HttpResponse("OK")


def index(request):
    quests = Question.objects.order_by('-id')
    limit = 10
    paginator = Paginator(quests, limit)

    page = request.GET.get('page', 1)
    quests = paginator.page(page)
    paginator.baseurl = '/?page='

    return render(request, 'qa/index.html', {
        'quest_list': quests,
        'paginator': paginator,
        'page': page,
    })


def popular_quests(request):
    quests = Question.objects.order_by('-rating')
    limit = 10
    paginator = Paginator(quests, limit)

    page = request.GET.get('page', 1)
    quests = paginator.page(page)
    paginator.baseurl = '/popular/?page='

    return render(request, 'qa/popular.html', {
        'quest_list': quests,
        'paginator': paginator,
        'page': page,
    })


def one_quest(request, id):
    id = int(id)
    try:
        quest = Question.objects.get(pk=id)
    except Question.DoesNotExist:
        raise Http404
    return render(request, 'qa/details.html', {
        'quest': quest,
    })