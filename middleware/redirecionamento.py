# middleware/force_http_middleware.py

from django.shortcuts import redirect

class ForceHttpMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.is_secure():
            url = request.build_absolute_uri(request.get_full_path())
            http_url = url.replace('https://', 'http://')
            return redirect(http_url)
        response = self.get_response(request)
        return response