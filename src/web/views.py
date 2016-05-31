import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

import deck.api


def login_view(request):

    login_error = False

    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'),
                            password=request.POST.get('password'))
        if user:
            login(request, user)
            return redirect('frontpage')
        else:
            login_error = True

    return render(request, 'login.html', {'login_error': login_error})


def logout_view(request):
    logout(request)
    return redirect('frontpage')


def user_frontpage(request):
    ctx = {
        'hex': hex,
        'decks': deck.api.get_decks(request.user.id),
        'classes': deck.api.get_classes(request.user.id),
        'logged_in': True,
    }
    return render(request, 'user_frontpage.html', ctx)


def frontpage(request):
    if request.user.is_authenticated():
        return user_frontpage(request)
    else:
        return render(request, 'frontpage.html')


def add_deck(request):
    new_deck_name = request.POST.get('new_deck_name')
    new_deck = deck.api.add_deck(request.user.id, new_deck_name)
    return redirect('frontpage')


def class_view(request):
    class_id = int(request.POST.get('class_id'))
    questions = deck.api.get_questions(int(class_id))
    alternative_dict = {question.id: [alternative for alternative
                                                  in deck.api.get_alternatives(class_id, question.id)]
                        for question in questions}
    ctx = {
        'logged_in': request.user.is_authenticated(),
        'questions': questions,
        'class_id': class_id,
        'alternative_dict': alternative_dict,
    }
    return render(request, 'class.html', ctx)


@login_required
def edit_deck(request, deck_id):
    ctx = {
        'deck': deck.api.get_deck(int(deck_id)),
        'logged_in': True,
    }
    return render(request, 'edit_deck.html', ctx)


def start_class(request, deck_id):
    class_id = deck.api.create_class(request.user.id, deck_id).id
    return redirect('/class_teacher/{}/'.format(class_id))


def class_teacher_view(request, class_id):
    # TODO Add login required, and also only teacher owning can see
    ctx = {
        'class': deck.api.get_class(class_id),
        'questions': deck.api.get_questions(class_id),
        'logged_in': True,
    }
    return render(request, 'class_teacher.html', ctx)


def question_teacher_view(request, class_id, question_id):
    # TODO Add login required, and also only teacher owning can see
    counts, labels = deck.api.get_reply_counts(class_id, question_id)
    ctx = {
        'counts': counts,
        'labels': labels,
        'alternatives': deck.api.get_alternatives(class_id, question_id),
        'class': deck.api.get_class(class_id),
        'question': deck.api.get_question(question_id),
        'logged_in': True,
    }
    return render(request, 'question_teacher.html', ctx)

########
# AJAX #
########

def answer_question(request):
    class_id = int(request.GET.get('class_id'))
    alternative_id = int(request.GET.get('alternative_id'))
    deck.api.answer_question(class_id, alternative_id)
    return HttpResponse()


def delete_deck(request):
    deck_id = request.GET.get('deck_id')
    new_deck = deck.api.delete_deck(deck_id)
    return HttpResponse()


def delete_class(request):
    class_id = request.GET.get('class_id')
    new_deck = deck.api.delete_class(class_id)
    return HttpResponse()


def question_state(request):
    class_id = request.GET.get('class_id')
    question_id = request.GET.get('question_id')
    start_bool = int(request.GET.get('start_bool'))
    start_bool = int(start_bool)
    if start_bool:
        deck.api.start_question(class_id, question_id)
    else:
        deck.api.stop_question(class_id, question_id)
    return HttpResponse()


def poll_question(request):
    class_id = int(request.GET['class_id'])
    question_id = int(request.GET['question_id'])
    counts, labels = deck.api.get_reply_counts(class_id, question_id)
    counts_only = [count for id, count in counts]
    return HttpResponse(json.dumps({'counts': counts_only,
                                    'labels': labels}))


def poll_active_question(request):
    class_id = int(request.GET.get('class_id'))
    active = deck.api.get_class(class_id).active_question
    if active:
        active_id = active.id
    else:
        active_id = -1
    return HttpResponse(str(active_id))
