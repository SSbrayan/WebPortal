from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
import socket
import requests
import json

from ..models import Question, Target, Choice, Interface, Port




def get_port_status(request, target_id):
    target = get_object_or_404(Target, pk=target_id)

    portscleanup(target)
    sysinfocleanup(target)

    try :
        endpoint ='http://{0}:8090/evservices/api/router/interactives/ioMargin/uiTestConfiguration'.format(target.name)
        payload = '{"py/object":"evToolsRouter.data.interactive.InteractiveCommandData","commandName":"uiTestConfiguration","settings":""}'
        response = requests.put(endpoint,  payload)
    except:
        target.status ='Not Conected'


        target.system_information_js = json.loads(response.content)
    if  target.system_information_js['status'] == '3':
        target.ports_dic = target.system_information_js['result']['portInformation']
        target.ports_dic.pop()
        target.system_information_dic = json.loads(response.content)['result']['systemInformation']
        target.ports_limits_dic = json.loads(response.content)['result']['uiTestConfiguration']
        portsdecode(target)
        sysinfodecode(target)


    else:
        target.status = 'Deny({})'.format(response['status'])


    target.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('polls:targetdetail', args=(target.id,)))



def portscleanup(target):
    for interface in target.interface_set.all():
        interface.delete()

def portsdecode(target):
    portscleanup(target)
    for interface in target.ports_dic:
        interfaceDB=target.interface_set.create(name=interface['interface'])
        for port in interface['information']:
            interfaceDB.port_set.create(number=str(port['Port']),speed=str(port['Speed']),width=str(port['Width']),state=str(port['Link State']))
          
def sysinfocleanup(target):
    target.CPUplatform='NO DATA'
    target.CPUSKU='NO DATA'
    target.CPUstepping='NO DATA'
    target.CPUid='NO DATA'
    target.PCHplatform='NO DATA'
    target.PCHSKU='NO DATA'
    target.PCHstepping='NO DATA'
    target.PCHid='NO DATA'

def sysinfodecode(target):
    target.CPUplatform=target.system_information_dic['CPUPLATFORM']
    target.CPUSKU=target.system_information_dic['CPUSKU']
    target.CPUstepping=target.system_information_dic['CPU Stepping']
    target.CPUid=target.system_information_dic['CPUID']
    target.PCHplatform=target.system_information_dic['PCHPLATFORM']
    target.PCHSKU=target.system_information_dic['PCHSKU']
    target.PCHstepping=target.system_information_dic['PCH Stepping']
    target.PCHid=target.system_information_dic['PCHID']

















          


def parse_systeminfo(systeminfo_js):
    systeminfo_dic=json.loads(systeminfo_js)
    ports_dict=systeminfo_dic['result']['portInformation']
    ports_dict.pop()
    port_str=portsdecode(ports_dict)




#if __name__ == '__main__':
    
#    jsonobject=open('testfile.txt', 'r').read()
#    parse_systeminfo(jsonobject)
