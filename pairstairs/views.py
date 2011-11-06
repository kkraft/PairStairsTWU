from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from models import Pair
from pairstairs.models import Programmer


def add_programmer(request):
    programmers = Programmer.objects.all()
    if request.method == 'POST':
        name = request.POST['programmer_names']
        Programmer(name=name).save()
        create_pair()
    return render_to_response('add_programmer.html', RequestContext(request, {'programmers' : programmers}))

def create_pair():
    programmers = Programmer.objects.all()
    count = len(programmers)
    i = 0
    while i<count:
        j = i+1
        while j<count:
            pairs = Pair.objects.filter(pair1=programmers[i], pair2 = programmers[j])
            if not len(pairs):
                pair = Pair(pair1 = programmers[i], pair2 = programmers[j], count = 0)
                pair.save()
            j +=1
        i +=1

def pairstairs(request):
    programmers = Programmer.objects.all()
    pairs = Pair.objects.all()
    return render_to_response('pairstairs.html', {'programmers' : programmers, 'pairs' : pairs} )

def add_count(request,pair1_id, pair2_id):
    first = Programmer.objects.get(id = pair1_id)
    second = Programmer.objects.get(id = pair2_id)
    pair = Pair.objects.get(pair1 = first, pair2 = second)
    pair.count+=1
    pair.save()
    return pairstairs(request)
