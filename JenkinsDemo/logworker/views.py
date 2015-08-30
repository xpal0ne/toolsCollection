from django.shortcuts import render_to_response

# Create your views here.
from core import log_operation

def show_index(request):
    return render_to_response('index2.html')

def log_check(request):
    tn = log_operation.TestNode('127.0.0.1', 'root', '12345')
    data = tn.get_log('vc.jd.com', 'n400')
    return render_to_response('index2.html', {'data': data})