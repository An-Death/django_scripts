from django.shortcuts import render
from  django.http import HttpResponse
from django.template import loader

from .models import Question, Choice
# Create your views here.
htmlformat = '<head><title>BIG NASTY SHIT!</title></head><body><h1>{}</h1></body>'


class Test():
    def index(request):
        lates_message = Question.objects.order_by('pub_date')[:5]
        template = loader.get_template('poll/index.html')
        context = {
            'latest_shit_was_happened': lates_message
        }
        # output = '<br>'.join(q.question_text for q in lates_message)
        return HttpResponse(template.render(context, request))


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
