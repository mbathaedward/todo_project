class CustomHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        reponse = self.get_response(request)
        reponse['X-Custom-Header'] = 'This is the custom header'
        return reponse