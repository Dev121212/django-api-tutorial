import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic import View

from apitutorial.mixins import JsonResponseMixin

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


class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            'count': 1000,
            'content': 'Some new content'
        }
        return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            'count': 1000,
            'content': 'Some new content'
        }
        return self.render_to_json_response(data)
