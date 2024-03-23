from django.urls import path
from .views import *
from user_management.base.dict import *
from user_management.base.file import *
from user_management.base.login import *
from user_management.base.notice import *
from user_management.base.permission import *
from user_management.base.register import *
from user_management.base.role import *
from user_management.base.user import *

urlpatterns = [
    path('login', LoginView.as_view()),
    path('register', RegisterView.as_view()),
    path('logout/<str:id>', LogoutView.as_view()),
    path('user', UserView.as_view(), name="user"),
    path('user/<int:pk>', UserView.as_view(), name='user_detail'),
    path('user/page', UserPageView.as_view(), name="user_page"),
    path('user/del/batch', UserBatchDeleteAPIView.as_view(), name="user_batch_delete"),
    path('user/export', UserExport.as_view(), name="user_export"),
    path('updateUser', UserInfoUpdate.as_view(), name="user_info_update"),
    path('password/change', UserUpdatePwd.as_view(), name="user_update_pwd"),
    path('role', RoleView.as_view(), name="role"),
    path('role/<int:pk>', RoleView.as_view(), name='role_detail'),
    path('role/page', RolePageView.as_view(), name="role_page"),
    path('role/del/batch', RoleBatchDeleteAPIView.as_view(), name="role_batch_delete"),
    path('role/export', RoleExport.as_view(), name="role_export"),
    path('permission', PermissionView.as_view(), name="permission"),
    path('permission/<int:pk>', PermissionView.as_view(), name='permission_delete'),
    path('permission/del/batch', PermissionBatchDeleteAPIView.as_view(), name="permission_batch_delete"),
    path('permission/export', PermissionExport.as_view(), name="permission_export"),
    path('dict', DictView.as_view(), name="dict"),
    path('dict/<int:pk>', DictView.as_view(), name='dict_detail'),
    path('dict/page', DictPageView.as_view(), name="dict_page"),
    path('dict/del/batch', DictBatchDeleteAPIView.as_view(), name="dict_batch_delete"),
    path('dict/export', DictExport.as_view(), name="dict_export"),
    path('file/upload', FileUploadView.as_view(), name="file_upload"),
    path('file/uploadImg', FileUploadEditorView.as_view(), name="file_upload_editor"),
    path('notice', NoticeView.as_view(), name="notice"),
    path('notice/<int:pk>', NoticeView.as_view(), name='notice_detail'),
    path('notice/page', NoticePageView.as_view(), name="notice_page"),
    path('notice/del/batch', NoticeBatchDeleteAPIView.as_view(), name="notice_batch_delete"),
    path('notice/export', NoticeExport.as_view(), name="notice_export"),
]