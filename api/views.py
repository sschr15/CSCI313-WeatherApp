from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse


def index(request: WSGIRequest) -> HttpResponse:
    response = HttpResponse(content_type='application/json')
    response['Access-Control-Allow-Origin'] = '*'
    response.content = '{"result": "success"}'
    return response
