from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from  django.views import generic


from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'generic_views/index.html'
    context_object_name = 'latest_shit_was_happened'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:10]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'generic_views/question_detail.html'


class ResultView(generic.DetailView):
    model = Question
    template_name = 'generic_views/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'test1:question_detail.html', {
            'question': question,
            'error_message': 'Ну ты и дибил! Ты не выбрали нихера! хВ'
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('test1:results', args=question_id))
