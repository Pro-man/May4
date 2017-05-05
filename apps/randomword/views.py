from django.shortcuts import render, redirect
import string, random

# Create your views here.
def index(request):
    return render(request, 'random_word_generator/index.html')

def random_word(request):
    if ('attempt' in request.session):
        request.session['attempt'] += 1
    else:
        request.session['attempt'] = 1
    request.session['word']=word_generator(14)
    return redirect('/')

def word_generator (length):
    options = string.letters + string.digits
    random_string = ''
    for i in range(length):
        random_string += options
        print random_string
    return  random_string
