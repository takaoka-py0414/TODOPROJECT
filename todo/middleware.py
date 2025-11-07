from django.conf import settings
from django.shortcuts import redirect
from urllib.parse import quote as urlquote

class LoginRequiredMiddleware:
    """
    未認証ユーザーを LOGIN_EXEMPT_URLS に含まれるパス以外へリダイレクトするミドルウェア。
    settings.LOGIN_URL に ?next=... を付けてリダイレクトします。
    LOGIN_EXEMPT_URLS は path の先頭一致（先頭の '/' は不要）で指定してください。
    空文字列 '' を含めるとトップ（/）のみ許可されます。
    """
    def __init__(self, get_response):
        self.get_response = get_response
        self.exempt = getattr(settings, 'LOGIN_EXEMPT_URLS', [])

    def __call__(self, request):
        path = request.path_info.lstrip('/')  
        if request.user.is_authenticated:
            return self.get_response(request)
        
        for prefix in self.exempt:
            if prefix == '':
                if path == '':
                    return self.get_response(request)
                continue
            if path.startswith(prefix):
                return self.get_response(request)

        login_url = getattr(settings, 'LOGIN_URL', '/login/')
        next_url = urlquote(request.get_full_path(), safe='')
        return redirect(f'{login_url}?next={next_url}')