from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
import socket
import requests

from ..models import Question, Target, Choice


def get_port_status(request, target_id):
    target = get_object_or_404(Target, pk=target_id)

    try :
        endpoint ='http://{0}:8090/evservices/api/router/interactives/ioMargin/uiTestConfiguration'.format(target.name)
        payload = '{"py/object":"evToolsRouter.data.interactive.InteractiveCommandData","commandName":"uiTestConfiguration","settings":""}'
        print endpoint
        print payload
        response = requests.put(endpoint,  payload)
        print response.status_code
        target.ports = response.content
    except :
        target.ports = 'No Response'
    target.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('polls:targetdetail', args=(target.id,)))