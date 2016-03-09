from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

from .models import Question, Answer
from .forms import AskForm, AnswerForm

from django.core.paginator import Paginator


def test(request, *args, **kwargs):
    return HttpResponse("OK")


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username, email, password)

        user_auth = authenticate(username=username, password=password)
        login(request, user_auth)
        return HttpResponseRedirect('/')
    else:
        return render(request, 'qa/signup.html')


def login_user(request):
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            error = 'Invalid username/password'
            return HttpResponseRedirect('/login/', {'error': error,})
    else:
        return render(request, 'qa/login.html')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


def index(request):
    quests = Question.objects.order_by('-id')
    limit = 10
    paginator = Paginator(quests, limit)

    page = request.GET.get('page', 1)
    quests = paginator.page(page)
    paginator.baseurl = '/?page='

    user = request.user

    return render(request, 'qa/index.html', {
        'quest_list': quests,
        'paginator': paginator,
        'page': page,
        'user': user,
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


def ask_add(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        form._user = request.user
        if form.is_valid():
            ask = form.save()
            url = '/question/{0}'.format(ask.id)
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'qa/add_ask.html', {
        'form': form,
    })


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