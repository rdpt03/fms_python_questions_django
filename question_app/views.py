from django import forms
from django.db.models import Sum, Max
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Question, Choice


NB_MAX_CHOIX = 5


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


def statistics(request):
    total_questions = Question.objects.count()
    total_choices = Choice.objects.count()

    total_votes = Choice.objects.aggregate(total=Sum('votes'))['total'] or 0

    if total_questions > 0:
        avg_votes = total_votes / total_questions
    else:
        avg_votes = 0

    last_question = Question.objects.aggregate(last=Max('pub_date'))['last']

    context = {
        'total_questions': total_questions,
        'total_choices': total_choices,
        'total_votes': total_votes,
        'avg_votes': avg_votes,
        'last_question': last_question,
    }

    return render(request, 'question_app/statistics.html', context)


def add(request):
    return render(request, 'question_app/create_question/add.html', {'liste_no_choix': range(NB_MAX_CHOIX)})


def confirm_add(request):
    # récupération du libellé de la question,
    # sans les éventuels espaces avant et après
    question_text = request.POST['question_text'].strip()
    if question_text:
        # ajout de la question si elle n'est pas vide
        question = Question(question_text=question_text,
        pub_date=timezone.now())
        question.save()
        # on traite à présent les champs de choix remplis
        # (on s'arrête au premier vide)
        for no_choix in range(NB_MAX_CHOIX):
            nom_champ = 'choix_{}'.format(no_choix)
            choice_text = request.POST[nom_champ].strip()
            if choice_text:
                choice = Choice(question=question,
                choice_text=choice_text)
                choice.save()
            else:
                break
        return render(request, 'question_app/create_question/confirm_add.html')
    else:
        # réaffichage du formulaire de saisie de la question
        # avec le message d'erreur
        return render(request, 'question_app/create_question/add.html', {'error_message': "You didn't enter a question text",})
