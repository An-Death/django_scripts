from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import Question, Choice
# Create your views here.
htmlformat = '<head><title>BIG NASTY SHIT!</title></head><body><h1>{}</h1></body>'


class Test():
    def index(request):
        lates_message = Question.objects.order_by('pub_date')[:5]
        context = {
            'latest_shit_was_happened': lates_message
        }
        return render(request, 'poll/index.html', context) # HttpResponse(template.render(context, request))


    def detail(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
            # raise Http404("That shit what you are asking fo is doest not exist!")
        return render(request, 'poll/detail.html', {'question': question})


    def results(request, question_id):
        text = htmlformat.format('That second shit "{}" what i`w doesnt`t know  what is it -_-'.format(question_id))
        return HttpResponse(text)


    def vote(request, question_id):
        text = htmlformat.format('Just some text, OK? and that shit "{}" Any one can told me what that is it finaly ?!'.
                                 format(question_id))
        return HttpResponse(text)
