from django.shortcuts import render

from django.shortcuts import render_to_response
from jenkins import Jenkins


jenkins_object = Jenkins('http://127.0.0.1:8080')

def job_list(request):
    jenkins_object = Jenkins('http://127.0.0.1:8080')
    jobList = jenkins_object.get_info()['jobs']
    return render_to_response('index.html', {'jobList' : jobList})


def node_list(request):
    jobList = jenkins_object.get_node_info('centos')
    return render_to_response('index.html', {'jobList': jobList})

