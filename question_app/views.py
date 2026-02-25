from django.shortcuts import render, get_object_or_404
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]  # last 5 questions
    context = {'latest_question_list': latest_question_list}
    return render(request, 'question_app/index.html', context)

def showall(request):
    question_list = Question.objects.all()  # last 5 questions
    context = {'question_list': question_list}
    return render(request, 'question_app/showall.html', context)

def showone(request, question_id):
    question = get_object_or_404(Question, pk=question_id) # get question

    #get choices

    #create render
    context = {'question': question}
    return render(request, 'question_app/showdetails.html', context)