from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
    print('*'*80)
    print('I am Home')
    request.session.clear()
    return render(request, "gold/index.html")

def user(request):
    if request.method == "POST":
        print('*'*80)
        print('User Created')
        request.session['user'] = request.POST['username']
        return redirect('/game')

def game(request):
    print('*'*80)
    print(f"{request.session['user']}'s game")
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['tries'] = 0
        request.session['log'] = "<p class='blue'>Your search for Gold has begun</p>"
    print(f"My gold: {request.session['gold']}")
    print(f"My tries: {request.session['tries']}")
    context = {
        "left": 15 - int(request.session['tries'])
    }
    return render(request, "gold/game.html", context)

def process_gold(request):
    if request.method == "POST":
        counter = request.POST['property']
        request.session['tries'] += 1
        if counter == 'farm':
            farm = random.randint(0, 30)
            request.session['gold'] += farm
            print(f"You've found {farm} more Gold!")
            request.session['log'] = f"<p>Working on the farm has earned you {farm} more Gold!</p>" + request.session['log']
        elif counter == 'cave':
            cave = random.randint(10, 20)
            request.session['gold'] += cave
            print(f"You've found {cave} more Gold!")
            request.session['log'] = f"<p>Exploring through the cave, you found {cave} more Gold!</p>" + request.session['log']
        elif counter == 'house':
            house = 15
            request.session['gold'] += house
            print(f"You've found {house} more Gold!")
            request.session['log'] = f"<p>While scavenging through the house, you found {house} more Gold!<p/>" + request.session['log']
        elif counter == 'casino':
            casino = random.randint(0, 50)
            gamble = random.randint(0, 1)
            if gamble > 0:
                request.session['gold'] += casino
                print(f"You've Won {casino} more Gold!")
                request.session['log'] = f"<p>You placed your bets and Won {casino} more Gold!</p>" + request.session['log']
            else:
                request.session['gold'] -= casino
                print(f"You've Lost {casino} more Gold!")
                request.session['log'] = f"<p class='red'>You placed your bets and Lost {casino} Gold!</p>" + request.session['log']
        if request.session['tries'] >= 15 and request.session['gold'] < 500:
            request.session['log'] = f"<h4 class='red'><b>You have only earned {request.session['gold']} gold, you Lose!</b></h4>" + request.session['log']
            request.session['gold'] = 0
            request.session['tries'] = 0
            request.session['log'] = f"<p class='blue'>{request.session['user']}'s search for gold begins again!</p>" + request.session['log']
        if request.session['gold'] >= 500:
            request.session['log'] = f"<h4 class='yellow'><b>You earned {request.session['gold']} gold, you Win!</b></h4>" + request.session['log']
            request.session['gold'] = 0
            request.session['tries'] = 0
            request.session['log'] = f"<p class='blue'>{request.session['user']}'s search for gold begins again!</p>" + request.session['log']
        return redirect('/game')

def end(request):
    request.session.clear() 
    return redirect('/')