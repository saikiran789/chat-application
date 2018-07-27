import datetime
from django.core.cache import cache
from django.conf import settings

class ActiveUserMiddleware:

    def process_request(self, request):
        current_user = request.username
        if request.username.is_authenticated():
            now = datetime.datetime.now()
            cache.set('seen_%s' % (current_user.username), now, 
                           settings.USER_LASTSEEN_TIMEOUT)
