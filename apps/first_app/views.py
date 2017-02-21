from django.shortcuts import render, redirect
import random
# # Create your views here.
def index(request):
    if 'attempt' not in request.session:
        request.session['attempt'] = 0
        request.session['word'] = "Click the 'Generate' button to make a random string!"
    return render(request, 'first_app/index.html')
def create(request):
    if request.method == "POST":
        random_word = ""
        vowels = ['a','e','i','o','u','y']
        consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
        for i in range(7):
            cons_index = random.randint(0,len(consonants)-1)
            random_word += consonants[cons_index]
            vow_index = random.randint(0, len(vowels)-1)
            random_word += vowels[vow_index]
        request.session['attempt'] += 1
        request.session['word'] = random_word
        return redirect('/')
    else:
        return redirect('/')
def reset(request):
    if request.method == "POST":
        del request.session['attempt']
        del request.session['word']
        return redirect('/')
    else:
        return redirect('/')
