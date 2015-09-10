from django.shortcuts import render_to_response

# Create your views here.
from core import log_operation

def show_index(request):
    return render_to_response('index_log.html')

def log_check(request):
    host = request.GET['host']
    username = request.GET['user_name']
    passwd = request.GET['passwd']
    tn = log_operation.TestNode(host, username, passwd)
    data = tn.get_log('vc.jd.com', 'n400')
    return render_to_response('index_log.html', {'data': data})