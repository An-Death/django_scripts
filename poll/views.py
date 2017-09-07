from django.shortcuts import render
from  django.http import HttpResponse


# Create your views here.
htmlformat = '<head><title>BIG NASTY SHIT!</title></head><body><h1>{}</h1></body>'


def index(request):
    text = 'This is fucking shit! Take it and don`t cry like a bitch!'
    return HttpResponse(htmlformat.format(text))

def detail(request, question_id):
    text = htmlformat.format('I have no idea what the shit is it "{}"! Sorry!'.format(question_id))
    return HttpResponse(text)

def results(request, question_id):
    text = htmlformat.format('That second shit "{}" what i`w doesnt`t know  what is it -_-'.format(question_id))
    return HttpResponse(text)

def vote(request, question_id):
    text = htmlformat.format('Just some text, OK? and that shit "{}" Any one can told me what that is it finaly ?!'.
                             format(question_id))
    return HttpResponse(text)