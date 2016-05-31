from collections import Counter

from .models import Deck, Question, Class, Reply, Alternative


def get_decks(user_id):
    return Deck.objects.filter(created_by__id=user_id)


def get_deck(deck_id):
    return Deck.objects.get(id=deck_id)


def add_deck(user_id, deck_name):
    return Deck.objects.create(created_by_id=int(user_id), name=deck_name)


def delete_deck(deck_id):
    q = Deck.objects.get(id=int(deck_id))
    q.delete()


def create_class(user_id, deck_id):
    return Class.objects.create(created_by_id=int(user_id),
                                deck_id=int(deck_id))

def get_alternatives(class_id, question_id):
    qs = Alternative.objects.filter(question_id=question_id)
    return qs


def get_questions(class_id):
    deck = Class.objects.get(id=int(class_id)).deck
    return Question.objects.filter(deck=deck)


def answer_question(class_id, alternative_id):
    Reply.objects.create(in_class_id=int(class_id),
                         alternative_id=alternative_id)


def get_question(question_id):
    return Question.objects.get(id=question_id)


def get_class(class_id):
    return Class.objects.get(id=int(class_id))


def get_classes(user_id):
    return Class.objects.filter(created_by_id=int(user_id))


def delete_class(class_id):
    q = Class.objects.get(id=int(class_id))
    q.delete()


def start_question(class_id, question_id):
    q = Class.objects.get(id=int(class_id))
    question = Question.objects.get(id=question_id)
    q.active_question = question
    q.save()


def stop_question(class_id, question_id):
    q = Class.objects.get(id=int(class_id))
    q.active_question = None
    q.save()


def get_reply_counts(class_id, question_id):
    alts = get_alternatives(class_id, question_id)
    ids = sorted(list(set([alt.id for alt in alts])))
    id2label = {alt.id: alt.text for alt in alts}
    counter = Counter({alt.id: 0 for alt in alts})
    replies = Reply.objects.filter(in_class_id=class_id,
                                 alternative__question_id=question_id)
    counter.update([reply.alternative.id for reply in replies])
    # Made as list to have same ordering in both returns
    counts = [(id, counter[id]) for id in ids]
    labels = [id2label[id] for id in ids]
    print(class_id, question_id, counts, labels)
    return counts, labels
