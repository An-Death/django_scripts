from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

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
        return render(request, 'poll/question_detail.html', {'question': question})


    def results(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'poll/results.html', {'question': question})


    def vote(request, question_id):
       question = get_object_or_404(Question, pk=question_id)
       try:
           selected_choice = question.choice_set.get(pk=request.POST['choice'])
       except (KeyError, Choice.DoesNotExist):
           return render(request, 'test:question_detail.html', {
               'question': question,
               'error_message': 'Ну ты и дибил! Ты не выбрали нихера! хВ'
           })
       else:
           selected_choice.votes += 1
           selected_choice.save()
           return  HttpResponseRedirect(reverse('test:results', args=question_id))
