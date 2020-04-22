from django.views.generic import View
from django.http import HttpResponse

from updates.models import Update as UpdateModel

import json
from .mixins import CSRFExemptMixin

from apitutorial.mixins import HttpResponseMixin
# Creating,Updating,Deleting,Retrieving (1) - Update Model


class UpdateModelDetailAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    '''
    Retrieve, Update, Delete --> Object
    '''
    is_json = True

    def get(self, request, id, *args, **kwargs):
        obj = UpdateModel.objects.get(id=id)
        json_data = obj.serialize()
        return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):
        return self.render_to_response(data)

    def put(self, request, *args, **kwargs):
        return self.render_to_response(data)

    def delete(self, request, *args, **kwargs):
        return self.render_to_response(data, status=403)


class UpdateModelListAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    '''
    List View
    Create View
    '''
    is_json = True

    def get(self, request, *args, **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):
        data = json.dumps({'message': 'Unknown Data'})
        return self.render_to_response(data, status=400)

    def delete(self, request, *args, **kwargs):
        data = json.dumps({'message': 'You can not delete an entire list.'})
        return self.render_to_response(data, status=403)
