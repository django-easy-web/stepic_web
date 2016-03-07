from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from .models import Question, Answer
from .forms import AskForm, AnswerForm

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


@csrf_exempt
def ask_add(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            ask = form.save()
            url = '/question/{0}'.format(ask.id)
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'qa/add_ask.html', {
        'form': form,
    })


@csrf_exempt
def answer_add(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            url = '/question/{0}'.format(answer.question_id)
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm()
    return render(request, 'qa/add_answer.html', {
        'form': form,
    })