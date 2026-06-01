from django.middleware.locale import LocaleMiddleware
from django.utils import translation
from django.conf import settings


class ForceDefaultLanguageMiddleware(LocaleMiddleware):
    """
    Custom Locale Middleware that ignores browser Accept-Language headers,
    forcing settings.LANGUAGE_CODE (uz) unless a language prefix is in the URL
    or explicitly chosen by the user (stored in session/cookie).
    """

    def process_request(self, request):
        # 1. First, check if language prefix is in URL path (e.g. /ru/... or /en/...)
        language = translation.get_language_from_path(request.path_info)

        # 2. Check if a language preference is in the session or cookie
        if not language:
            if hasattr(request, 'session'):
                language = request.session.get('_language')
            if not language:
                cookie_name = getattr(settings, 'LANGUAGE_COOKIE_NAME', 'django_language')
                language = request.COOKIES.get(cookie_name)

        # 3. If not resolved, fallback directly to settings.LANGUAGE_CODE
        # This bypasses Django's default browser Accept-Language header detection
        if not language:
            language = settings.LANGUAGE_CODE

        # Activate resolved language
        translation.activate(language)
        request.LANGUAGE_CODE = translation.get_language()
