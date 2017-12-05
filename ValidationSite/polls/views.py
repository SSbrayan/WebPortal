from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic


from scripts.updateip import update_IP
from scripts.updateports import info_update


from .models import Question, Target, Choice


#def index(request):
#    latest_target_list = Target.objects.order_by('-pub_date')[:5]
#    output = ', '.join([q.target_text for q in latest_target_list])
#    return HttpResponse(output)



class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


class TargetIndexView(generic.ListView):
    template_name = 'polls/targetindex.html'
    context_object_name = 'latest_target_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Target.objects.order_by('-pub_date')


class TargetDetailView(generic.DetailView):
    model = Target
    template_name = 'polls/targetdetail.html'







#def update_IP(request, target_id):
#    target = get_object_or_404(Target, pk=target_id)

#    target.IP = 'hola mundo'
#    target.save()
#    # Always return an HttpResponseRedirect after successfully dealing
#    # with POST data. This prevents data from being posted twice if a
#    # user hits the Back button.
#    return HttpResponseRedirect(reverse('polls:targetdetail', args=(target.id,)))
