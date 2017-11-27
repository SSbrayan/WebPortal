from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
import socket


from ..models import Question, Target, Choice


def update_IP(request, target_id):
    target = get_object_or_404(Target, pk=target_id)

    try :
        target.IP = socket.gethostbyname(target.name)
    except :
        target.IP = 'No Response'
    target.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('polls:targetdetail', args=(target.id,)))