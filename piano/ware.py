class PreloadStaticFilesMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # print("Callin to ware to load static data. ")
        from django.contrib.staticfiles import finders
        from django.conf import settings

        for staticfile in settings.STATICFILES_DIRS:
            finders.find(staticfile)

        response = self.get_response(request)
        return response
