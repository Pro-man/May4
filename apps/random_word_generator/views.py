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
    request.session['word']=keyword_generator(14)
    return redirect('/')

def keyword_generator (length):
    options = string.letters + string.digits
    print options
    new_random_string = ''
    print new_random_string
    for i in range(length):
        new_random_string += random.choice(options)
        print new_random_string
    return  new_random_string
