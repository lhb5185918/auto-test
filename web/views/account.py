from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.decorators.csrf import csrf_exempt
from web.models import User  # 确保导入你的用户模型


class LoginView(APIView):
    @csrf_exempt
    def post(self, request):
        username = request.data.get('username')  # 使用 request.data 获取 JSON 数据
        password = request.data.get('password')

        # 直接查询用户
        try:
            user = User.objects.get(username=username)  # 获取用户对象
        except User.DoesNotExist:
            return Response({'message': '用户名或密码错误'}, status=status.HTTP_401_UNAUTHORIZED)

        # 验证密码
        if user.check_password(password):  # 使用 check_password 方法验证密码
            # 生成 token
            refresh = RefreshToken.for_user(user)  # 使用认证成功的用户对象
            return Response({
                'message': '登录成功',
                'redirect_url': '/',
                'access': str(refresh.access_token),  # 返回 access token
                'refresh': str(refresh),  # 返回 refresh token
            }, status=status.HTTP_200_OK)
        else:
            return Response({'message': '用户名或密码错误'}, status=status.HTTP_401_UNAUTHORIZED)


class RegisterView(APIView):

    @csrf_exempt
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        phone = request.data.get('phone')
        if User.objects.filter(username=username).exists():
            return Response({'message': '用户名已存在'}, status=status.HTTP_200_OK)
        user = User.objects.create_user(username=username, password=password, email=email, phone=phone)
        return Response({'message': '注册成功', 'redirect_url': '/login'}, status=status.HTTP_200_OK)
