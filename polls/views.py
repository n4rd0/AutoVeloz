from django.http import HttpResponse
from .models import Question
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

@login_required
def jaja(request):
    return HttpResponse("jajaja")

@login_required
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

@login_required
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

@login_required
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
