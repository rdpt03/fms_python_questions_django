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

    #create render
    context = {'question': question}
    return render(request, 'question_app/showdetails.html', context)


def frequency(request, question_id):
    #get from db
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choice_set.all()
    #get total votes
    total_votes = sum(c.votes for c in choices) or 1  # evita divisão por 0

    # get percent
    choices_with_percent = []
    for c in choices:
        percent = (c.votes / total_votes) * 100
        choices_with_percent.append((c.choice_text, c.votes, percent))

    #render
    context = {
        'question': question,
        'choices': choices_with_percent,
    }
    return render(request, 'question_app/show_frequency.html', context)
