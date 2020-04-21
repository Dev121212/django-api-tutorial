from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def update_model_detail_view(request):
    '''
    URI - for a REST API
    '''
    data = {
        'count': 1000,
        'content': 'Some new content'
    }

    return JsonResponse(data)
