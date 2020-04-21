from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json

# Create your views here.


def update_model_detail_view(request):
    '''
    URI - for a REST API
    GET - Retrieve
    '''
    data = {
        'count': 1000,
        'content': 'Some new content'
    }

    return JsonResponse(data)


def json_example_view(request):
    '''
    URI - for a REST API
    GET - Retrieve
    '''
    data = {
        'count': 1000,
        'content': 'Some new content'
    }
    json_data = json.dumps(data)

    return HttpResponse(json_data, content_type='application/json')
