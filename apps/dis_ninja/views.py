from django.shortcuts import render
import re
# Create your views here.
def index(request):

    return render(request, 'dis_ninja/index.html')

def all(request):

    return render(request, 'dis_ninja/all.html')

def ninjas(request, color):
    print color
    match = re.search(r'\b(blue|orange|purple|red)\b', color)

    if not match:
        print 'Not a ninja'
        context = {
            'ninja' : 'img/megan.jpg'
        }
        return render(request, 'dis_ninja/ninja.html', context)
    else:
        print 'Found a ninja'
        url = 'img/' + color + '.jpg'
        print url
        context = {
            'ninja' : url
        }
        return render (request, 'dis_ninja/ninja.html', context)
