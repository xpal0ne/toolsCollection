from django.shortcuts import render_to_response

# Create your views here.


def show_index(request):
    return render_to_response('index_interface.html')