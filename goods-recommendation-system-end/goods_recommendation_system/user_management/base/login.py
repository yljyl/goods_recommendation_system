# Create your views here.
import hashlib

from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken
from user_management.utils.permission import PermissionUtil
from user_management.models import *
from user_management.utils.json_response import SuccessResponse,ErrorResponse
import bcrypt

class PermissionSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Permission
        fields = '__all__'

# 用户登录
class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        # 判断用户名
        users = User.objects.filter(username=username)

        if users.exists():
            user = users.first()
            # 判断密码

            md5 = hashlib.md5()
            md5.update(password.encode('utf-8'))
            hashpwd = md5.hexdigest()

            if hashpwd!=user.password:
                return ErrorResponse(msg="用户名或密码错误")

            userSerializer = UserSerializer(user)
            token = AccessToken.for_user(user)
            # 获取角色的权限
            role = Role.objects.get(flag=user.role)
            permissions = role.permission.all()
            all_permissions = list(permissions.values())
            menus = PermissionUtil.get_tree_permissions(all_permissions)
            auths = [permission for permission in all_permissions if permission['type'] == 3]
            data = {
                "user": userSerializer.data,
                "token":str(token),
                "menus":menus,
                "auths":auths
            }

            #保存会话数据
            request.session['user'] = user

            return SuccessResponse(msg="登录成功",data=data)
        else:
            return ErrorResponse(msg="未知用户")


# 用户注销
class LogoutView(APIView):
    def get(self, request, id):

        return SuccessResponse(msg="注销成功")
