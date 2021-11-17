import json

# Create your views here.

from django.http import HttpResponse, JsonResponse

rtmps = []
max_size = 10


def response_success(data=None):
    if data:
        return {"code": 200, "msg": "success", "data": data}
    else:
        return {"code": 200, "msg": "success"}


def response_error(code: int, msg: str):
    return {"code": code, "msg": msg}


def rmtp_api(request):
    print(request)
    if request.method == "POST":
        return add_rtmp(request)

    if request.method == "GET":
        return get_rtmp(request)

    return response_error(10000, f"un_support {request.method}")


def get_rtmp(request):
    print(request.GET)
    size = int(request.GET.get('size', default='0'))
    if size == 0 or len(rtmps) <= size:
        data = rtmps
    else:
        data = rtmps[0:size]
    return JsonResponse(response_success(data))


def add_rtmp(request):
    req = json.loads(request.body)
    print(req)
    url = req['url']
    rtmps.insert(0, url)
    while len(rtmps) > max_size:
        rtmps.pop(max_size)

    return JsonResponse(response_success())
