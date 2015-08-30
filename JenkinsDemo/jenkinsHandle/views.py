from django.shortcuts import render

from django.shortcuts import render_to_response
from jenkins import Jenkins


jenkins_object = Jenkins('http://127.0.0.1:8080')


def job_list(request):
    # jenkins_object = Jenkins('http://127.0.0.1:8080')
    job_lists = jenkins_object.get_info()['jobs']
    data = []
    for i, j in enumerate(job_lists):
        data.append((i+1, j))
    return render_to_response('index.html', {'jobList' : data})


def node_list(request):
    node_lists = jenkins_object.get_node_info('centos')
    return render_to_response('index.html', {'jobList': node_lists})

if __name__ == '__main__':
    pass
