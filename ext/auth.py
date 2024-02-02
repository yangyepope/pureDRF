from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


class MyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get('token')
        if token:
            return "wupeiqi", token

        raise AuthenticationFailed({"code": 2000, "message": "认证失败"})