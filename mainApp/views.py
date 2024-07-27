from django.shortcuts import render
from .models import Correct, Incorrect


def index(request):
    correct_words = Correct.objects.all()
    incorrect_words = Incorrect.objects.all()

    correct_word = None

    search = request.GET.get('search').lower()
    if 'x' not in search and 'h' not in search and search != "":
        return render(request, 'index.html', {'hx': True})

    if search is not None:
        correct_words = correct_words.filter(word=search)
        if correct_words.count() == 1:
            correct_word = correct_words[0]
            incorrect_words = Incorrect.objects.filter(correct=correct_word)
        else:
            incorrect_words = Incorrect.objects.filter(word=search)
            if incorrect_words.count() > 0:
                correct_word = incorrect_words[0].correct
                incorrect_words = Incorrect.objects.filter(correct=correct_word)

    if correct_word is None:
        incorrect_words = None
    context = {
        'correct_word': correct_word,
        'incorrect_words': incorrect_words,
        'search': search
    }
    return render(request, 'index.html', context)
