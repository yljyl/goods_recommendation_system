from rest_framework.views import APIView
from core_recommendations.models import *
from user_management.models import *
from django.db import connection
from user_management.utils.json_response import *
from rest_framework import status
from django.core.paginator import Paginator
from user_management.utils.user import UserToken


# 用户
class UserListDetail(APIView):
    # 列表和查询一个
    def get(self, request, pk=None):
        if pk is None:
            list = User.objects.all()
            serializerList = UserSerializer(list, many=True)
            return SuccessResponse(data=serializerList.data)
        else:
            model = User.objects.get(id=pk)
            serializer = UserSerializer(model)
            return SuccessResponse(data=serializer.data)


class UserPage(APIView):

    # 分页
    def get(self, request):
        name = request.query_params.get('name')
        pageNum = int(request.query_params.get('pageNum', 1))
        pageSize = int(request.query_params.get('pageSize', 5))

        # 构建查询
        list = User.objects.all().order_by('-id')
        if name:
            list = list.filter(name__icontains=name)

        # 进行分页
        paginator = Paginator(list, pageSize)
        pageList = paginator.page(pageNum)
        serializerList = UserSerializer(pageList, many=True)
        return PageResponse(page=pageNum,
                            limit=pageSize,
                            total=paginator.count,
                            pages=paginator.num_pages,
                            data=serializerList.data
                            )


# 网站公告
class NoticeListDetail(APIView):
    # 列表和查询一个
    def get(self, request, pk=None):
        if pk is None:
            list = Notice.objects.all()
            serializerList = NoticeSerializer(list, many=True)
            return SuccessResponse(data=serializerList.data)
        else:
            model = Notice.objects.get(id=pk)
            serializer = NoticeSerializer(model)
            return SuccessResponse(data=serializer.data)


class NoticePage(APIView):

    # 分页
    def get(self, request):
        name = request.query_params.get('name')
        pageNum = int(request.query_params.get('pageNum', 1))
        pageSize = int(request.query_params.get('pageSize', 5))

        # 构建查询
        list = Notice.objects.all().order_by('-id')
        if name:
            list = list.filter(name__icontains=name)

        # 进行分页
        paginator = Paginator(list, pageSize)
        pageList = paginator.page(pageNum)
        serializerList = NoticeSerializer(pageList, many=True)
        return PageResponse(page=pageNum,
                            limit=pageSize,
                            total=paginator.count,
                            pages=paginator.num_pages,
                            data=serializerList.data
                            )


# 根据userId查询用户
class getMemberByUserId(APIView):
    def get(self, request, userId):
        model = Member.objects.filter(user_id=userId).first()
        serializer = MemberSerializer(model)
        return SuccessResponse(data=serializer.data)


class UpdateMember(APIView):
    # 新增/修改
    def put(self, request):
        if 'id' not in request.data:
            # 新增
            serializer = MemberSerializer(data=request.data)
            if (serializer.is_valid()):
                serializer.save()
                return SuccessResponse(msg="添加成功")
            else:
                return ErrorResponse(msg="数据验证失败")

        try:
            model = Member.objects.get(pk=request.data['id'])
        except Member.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = MemberSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.update(model, serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")


# 轮播图
class BannerListDetail(APIView):
    # 列表和查询一个
    def get(self, request, pk=None):
        if pk is None:
            list = Banner.objects.all()
            serializerList = BannerSerializer(list, many=True)
            return SuccessResponse(data=serializerList.data)
        else:
            model = Banner.objects.get(id=pk)
            serializer = BannerSerializer(model)
            return SuccessResponse(data=serializer.data)

    # 新增
    def post(self, request):
        serializer = BannerSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return SuccessResponse(msg="添加成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 修改
    def put(self, request):
        try:
            model = Banner.objects.get(pk=request.data['id'])
        except Banner.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BannerSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.update(model, serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 删除
    def delete(self, request, pk):
        model = Banner.objects.filter(id=pk)
        model.delete()
        return SuccessResponse(msg="删除成功")


class BannerPage(APIView):

    # 分页
    def get(self, request):
        name = request.query_params.get('name')
        pageNum = int(request.query_params.get('pageNum', 1))
        pageSize = int(request.query_params.get('pageSize', 5))

        # 构建查询
        list = Banner.objects.all().order_by('-id')
        if name:
            list = list.filter(name__icontains=name)

        # 进行分页
        paginator = Paginator(list, pageSize)
        pageList = paginator.page(pageNum)
        serializerList = BannerSerializer(pageList, many=True)
        return PageResponse(page=pageNum,
                            limit=pageSize,
                            total=paginator.count,
                            pages=paginator.num_pages,
                            data=serializerList.data
                            )


class UpdateBanner(APIView):
    # 修改
    def put(self, request):
        if 'id' not in request.data:
            # 新增
            serializer = BannerSerializer(data=request.data)
            if (serializer.is_valid()):
                serializer.save()
                return SuccessResponse(msg="添加成功")
            else:
                return ErrorResponse(msg="数据验证失败")
        try:
            model = Banner.objects.get(pk=request.data['id'])
        except Banner.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BannerSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.update(model, serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")


# 用户
class MemberListDetail(APIView):
    # 列表和查询一个
    def get(self, request, pk=None):
        if pk is None:
            list = Member.objects.all()
            serializerList = MemberSerializer(list, many=True)
            return SuccessResponse(data=serializerList.data)
        else:
            model = Member.objects.get(id=pk)
            serializer = MemberSerializer(model)
            return SuccessResponse(data=serializer.data)

    # 新增
    def post(self, request):
        serializer = MemberSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return SuccessResponse(msg="添加成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 修改
    def put(self, request):
        try:
            model = Member.objects.get(pk=request.data['id'])
        except Member.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = MemberSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.update(model, serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 删除
    def delete(self, request, pk):
        model = Member.objects.filter(id=pk)
        model.delete()
        return SuccessResponse(msg="删除成功")


class MemberPage(APIView):

    # 分页
    def get(self, request):
        name = request.query_params.get('name')
        pageNum = int(request.query_params.get('pageNum', 1))
        pageSize = int(request.query_params.get('pageSize', 5))

        # 构建查询
        list = Member.objects.all().order_by('-id')
        if name:
            list = list.filter(name__icontains=name)

        # 进行分页
        paginator = Paginator(list, pageSize)
        pageList = paginator.page(pageNum)
        serializerList = MemberSerializer(pageList, many=True)
        return PageResponse(page=pageNum,
                            limit=pageSize,
                            total=paginator.count,
                            pages=paginator.num_pages,
                            data=serializerList.data
                            )


class UpdateMember(APIView):
    # 修改
    def put(self, request):
        if 'id' not in request.data:
            # 新增
            serializer = MemberSerializer(data=request.data)
            if (serializer.is_valid()):
                serializer.save()
                return SuccessResponse(msg="添加成功")
            else:
                return ErrorResponse(msg="数据验证失败")
        try:
            model = Member.objects.get(pk=request.data['id'])
        except Member.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = MemberSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.update(model, serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")


# 产品分类
class CategoryListDetail(APIView):
    # 列表和查询一个
    def get(self, request, pk=None):
        if pk is None:
            list = Category.objects.all()
            serializerList = CategorySerializer(list, many=True)
            return SuccessResponse(data=serializerList.data)
        else:
            model = Category.objects.get(id=pk)
            serializer = CategorySerializer(model)
            return SuccessResponse(data=serializer.data)

    # 新增
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return SuccessResponse(msg="添加成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 修改
    def put(self, request):
        try:
            model = Category.objects.get(pk=request.data['id'])
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.update(model, serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 删除
    def delete(self, request, pk):
        model = Category.objects.filter(id=pk)
        model.delete()
        return SuccessResponse(msg="删除成功")


class CategoryPage(APIView):

    # 分页
    def get(self, request):
        name = request.query_params.get('name')
        pageNum = int(request.query_params.get('pageNum', 1))
        pageSize = int(request.query_params.get('pageSize', 5))

        # 构建查询
        list = Category.objects.all().order_by('-id')
        if name:
            list = list.filter(name__icontains=name)

        # 进行分页
        paginator = Paginator(list, pageSize)
        pageList = paginator.page(pageNum)
        serializerList = CategorySerializer(pageList, many=True)
        return PageResponse(page=pageNum,
                            limit=pageSize,
                            total=paginator.count,
                            pages=paginator.num_pages,
                            data=serializerList.data
                            )


class UpdateCategory(APIView):
    # 修改
    def put(self, request):
        if 'id' not in request.data:
            # 新增
            serializer = CategorySerializer(data=request.data)
            if (serializer.is_valid()):
                serializer.save()
                return SuccessResponse(msg="添加成功")
            else:
                return ErrorResponse(msg="数据验证失败")
        try:
            model = Category.objects.get(pk=request.data['id'])
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.update(model, serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")


# 产品列表
class GoodsListDetail(APIView):
    # 列表和查询一个
    def get(self, request, pk=None):
        if pk is None:
            list = Goods.objects.all()
            serializerList = GoodsSerializer(list, many=True)
            return SuccessResponse(data=serializerList.data)
        else:
            model = Goods.objects.get(id=pk)
            serializer = GoodsSerializer(model)
            return SuccessResponse(data=serializer.data)

    # 新增
    def post(self, request):
        serializer = GoodsSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return SuccessResponse(msg="添加成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 修改
    def put(self, request):
        try:
            model = Goods.objects.get(pk=request.data['id'])
        except Goods.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = GoodsSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.update(model, serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 删除
    def delete(self, request, pk):
        model = Goods.objects.filter(id=pk)
        model.delete()
        return SuccessResponse(msg="删除成功")


class GoodsPage(APIView):

    # 分页
    def get(self, request):
        name = request.query_params.get('name')
        pageNum = int(request.query_params.get('pageNum', 1))
        pageSize = int(request.query_params.get('pageSize', 5))
        category_id = request.query_params.get('category_id')

        # 构建查询
        list = Goods.objects.all().order_by('-id')
        if name:
            list = list.filter(name__icontains=name)
        if category_id:
            list = list.filter(category_id=category_id)

        # 进行分页
        paginator = Paginator(list, pageSize)
        pageList = paginator.page(pageNum)
        serializerList = GoodsSerializer(pageList, many=True)
        return PageResponse(page=pageNum,
                            limit=pageSize,
                            total=paginator.count,
                            pages=paginator.num_pages,
                            data=serializerList.data
                            )


class UpdateGoods(APIView):
    # 修改
    def put(self, request):
        if 'id' not in request.data:
            # 新增
            serializer = GoodsSerializer(data=request.data)
            if (serializer.is_valid()):
                serializer.save()
                return SuccessResponse(msg="添加成功")
            else:
                return ErrorResponse(msg="数据验证失败")
        try:
            model = Goods.objects.get(pk=request.data['id'])
        except Goods.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = GoodsSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.update(model, serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")


# 产品评论
class CommentsListDetail(APIView):
    # 列表和查询一个
    def get(self, request, pk=None):
        if pk is None:
            list = Comments.objects.all()
            serializerList = CommentsSerializer(list, many=True)
            return SuccessResponse(data=serializerList.data)
        else:
            model = Comments.objects.get(id=pk)
            serializer = CommentsSerializer(model)
            return SuccessResponse(data=serializer.data)

    # 新增
    def post(self, request):
        serializer = CommentsSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return SuccessResponse(msg="添加成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 修改
    def put(self, request):
        try:
            model = Comments.objects.get(pk=request.data['id'])
        except Comments.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CommentsSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.update(model, serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 删除
    def delete(self, request, pk):
        model = Comments.objects.filter(id=pk)
        model.delete()
        return SuccessResponse(msg="删除成功")


class CommentsPage(APIView):

    # 分页
    def get(self, request):
        name = request.query_params.get('name')
        pageNum = int(request.query_params.get('pageNum', 1))
        pageSize = int(request.query_params.get('pageSize', 5))

        # 构建查询
        list = Comments.objects.all().order_by('-id')
        if name:
            list = list.filter(name__icontains=name)

        # 进行分页
        paginator = Paginator(list, pageSize)
        pageList = paginator.page(pageNum)
        serializerList = CommentsSerializer(pageList, many=True)
        return PageResponse(page=pageNum,
                            limit=pageSize,
                            total=paginator.count,
                            pages=paginator.num_pages,
                            data=serializerList.data
                            )


class UpdateComments(APIView):
    # 修改
    def put(self, request):
        if 'id' not in request.data:
            # 新增
            serializer = CommentsSerializer(data=request.data)
            if (serializer.is_valid()):
                serializer.save()
                return SuccessResponse(msg="添加成功")
            else:
                return ErrorResponse(msg="数据验证失败")
        try:
            model = Comments.objects.get(pk=request.data['id'])
        except Comments.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CommentsSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.update(model, serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")


# 我的产品收藏
class CollectListDetail(APIView):
    # 列表和查询一个
    def get(self, request, pk=None):
        if pk is None:
            list = Collect.objects.all()
            serializerList = CollectSerializer(list, many=True)
            return SuccessResponse(data=serializerList.data)
        else:
            model = Collect.objects.get(id=pk)
            serializer = CollectSerializer(model)
            return SuccessResponse(data=serializer.data)

    # 新增
    def post(self, request):
        serializer = CollectSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return SuccessResponse(msg="添加成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 修改
    def put(self, request):
        try:
            model = Collect.objects.get(pk=request.data['id'])
        except Collect.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CollectSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.update(model, serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 删除
    def delete(self, request, pk):
        model = Collect.objects.filter(id=pk)
        model.delete()
        return SuccessResponse(msg="删除成功")


class CollectPage(APIView):

    # 分页
    def get(self, request):
        name = request.query_params.get('name')
        pageNum = int(request.query_params.get('pageNum', 1))
        pageSize = int(request.query_params.get('pageSize', 5))

        # 构建查询
        list = Collect.objects.all().order_by('-id')
        if name:
            list = list.filter(name__icontains=name)

        # 进行分页
        paginator = Paginator(list, pageSize)
        pageList = paginator.page(pageNum)
        serializerList = CollectSerializer(pageList, many=True)
        return PageResponse(page=pageNum,
                            limit=pageSize,
                            total=paginator.count,
                            pages=paginator.num_pages,
                            data=serializerList.data
                            )


class UpdateCollect(APIView):
    # 修改
    def put(self, request):
        if 'id' not in request.data:
            # 新增
            serializer = CollectSerializer(data=request.data)
            if (serializer.is_valid()):
                serializer.save()
                return SuccessResponse(msg="添加成功")
            else:
                return ErrorResponse(msg="数据验证失败")
        try:
            model = Collect.objects.get(pk=request.data['id'])
        except Collect.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CollectSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.update(model, serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")


# 我的产品标签
class MembertagsListDetail(APIView):
    # 列表和查询一个
    def get(self, request, pk=None):
        if pk is None:
            list = Membertags.objects.all()
            serializerList = MembertagsSerializer(list, many=True)
            return SuccessResponse(data=serializerList.data)
        else:
            model = Membertags.objects.get(id=pk)
            serializer = MembertagsSerializer(model)
            return SuccessResponse(data=serializer.data)

    # 新增
    def post(self, request):
        serializer = MembertagsSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return SuccessResponse(msg="添加成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 修改
    def put(self, request):
        try:
            model = Membertags.objects.get(pk=request.data['id'])
        except Membertags.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = MembertagsSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.update(model, serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 删除
    def delete(self, request, pk):
        model = Membertags.objects.filter(id=pk)
        model.delete()
        return SuccessResponse(msg="删除成功")


class MembertagsPage(APIView):

    # 分页
    def get(self, request):
        name = request.query_params.get('name')
        pageNum = int(request.query_params.get('pageNum', 1))
        pageSize = int(request.query_params.get('pageSize', 5))

        # 构建查询
        list = Membertags.objects.all().order_by('-id')
        if name:
            list = list.filter(name__icontains=name)

        # 进行分页
        paginator = Paginator(list, pageSize)
        pageList = paginator.page(pageNum)
        serializerList = MembertagsSerializer(pageList, many=True)
        return PageResponse(page=pageNum,
                            limit=pageSize,
                            total=paginator.count,
                            pages=paginator.num_pages,
                            data=serializerList.data
                            )


class UpdateMembertags(APIView):
    # 修改
    def put(self, request):
        if 'id' not in request.data:
            # 新增
            serializer = MembertagsSerializer(data=request.data)
            if (serializer.is_valid()):
                serializer.save()
                return SuccessResponse(msg="添加成功")
            else:
                return ErrorResponse(msg="数据验证失败")
        try:
            model = Membertags.objects.get(pk=request.data['id'])
        except Membertags.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = MembertagsSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.update(model, serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")


# 查看产品评论
class CommentsTree(APIView):
    def get(self, request):
        goodsId = request.query_params.get('goodsId')
        user_list = User.objects.all()
        all_user = list(user_list.values())
        comments_all = Comments.objects.filter(goods_id=goodsId)
        comments_all_list = list(comments_all.values())

        # 一级评论
        first_comments = Comments.objects.filter(goods_id=goodsId, pid=None)
        first_comments_list = list(first_comments.values())

        # 给每个评论设置用户
        for comment in first_comments_list:
            user = next((user for user in all_user if user['id'] == comment['user_id']), None)
            comment['user'] = user

        # 二级评论
        for comment in first_comments_list:
            pid = comment['id']
            second_comments = [comment1 for comment1 in comments_all_list if comment1['pid'] == pid]  # 二级评论

            # 二级评论设置用户
            for comment1 in second_comments:
                user = next((user for user in all_user if user['id'] == comment1['user_id']), None)
                puser = next((user for user in all_user if user['id'] == comment1['puser_id']), None)
                comment1['user'] = user
                comment1['puser'] = puser

            comment['children'] = second_comments  # 一级评论设置二级评论

        # 驼峰转换
        for comment in first_comments_list:
            convert_props_to_camel_case(comment)

        return SuccessResponse(data=first_comments_list)


# 添加/修改产品评论
class UpdateComments(APIView):
    def post(self, request):
        content = None
        if 'content' in request.data:
            content = request.data['content']
        score = None
        if 'score' in request.data:
            score = request.data['score']
        userId = None
        if 'userId' in request.data:
            userId = request.data['userId']
        goodsId = None
        if 'goodsId' in request.data:
            goodsId = request.data['goodsId']
        pid = None
        if 'pid' in request.data:
            pid = request.data['pid']
        puserId = None
        if 'puserId' in request.data:
            puserId = request.data['puserId']

        Comments.objects.create(
            content=content,
            score=score,
            user_id=userId,
            goods_id=goodsId,
            pid=pid,
            puser_id=puserId,
        )

        return SuccessResponse(msg="操作成功")


# 统计-不同分类的产品数量
class categoryGoodsStatisView(APIView):
    def get(self, request):
        '''
        sql = "SELECT * FROM my_table WHERE id = %s AND name = %s"
        params = (0, 1)
        params = (1, "John")
        '''

        sql = "SELECT c.name AS `name`, COUNT(g.id) AS `value` FROM category c LEFT JOIN goods g ON c.id = g.category_id GROUP BY c.name"
        params = None
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()
            result = []
            for row in rows:
                data = dict(zip(columns, row))
                result.append(data)
        return SuccessResponse(data=result)


# 统计-不同分类的产品的总销售量
class categorySalesStatisView(APIView):
    def get(self, request):
        '''
        sql = "SELECT * FROM my_table WHERE id = %s AND name = %s"
        params = (0, 1)
        params = (1, "John")
        '''

        sql = "SELECT c.name `name`, SUM(g.sales) AS `value` FROM category c LEFT JOIN goods g ON c.id = g.category_id GROUP BY c.name"
        params = None
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()
            result = []
            for row in rows:
                data = dict(zip(columns, row))
                result.append(data)
        return SuccessResponse(data=result)


# 统计-不同分类的产品的平均价格
class categoryPriceStatisView(APIView):
    def get(self, request):
        '''
        sql = "SELECT * FROM my_table WHERE id = %s AND name = %s"
        params = (0, 1)
        params = (1, "John")
        '''

        sql = "SELECT c.name `name`, AVG(g.price) AS `value` FROM category c LEFT JOIN goods g ON c.id = g.category_id GROUP BY c.name;"
        params = None
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()
            result = []
            for row in rows:
                data = dict(zip(columns, row))
                result.append(data)
        return SuccessResponse(data=result)


# 统计-各个省份产品数量统计
class provinceCountStatisView(APIView):
    def get(self, request):
        '''
        sql = "SELECT * FROM my_table WHERE id = %s AND name = %s"
        params = (0, 1)
        params = (1, "John")
        '''

        sql = "SELECT province AS `name`, COUNT(id) AS `value` FROM goods GROUP BY province"
        params = None
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()
            result = []
            for row in rows:
                data = dict(zip(columns, row))
                result.append(data)
        return SuccessResponse(data=result)


# 统计-各个省份产品总销售量统计
class provinceSalesStatisView(APIView):
    def get(self, request):
        '''
        sql = "SELECT * FROM my_table WHERE id = %s AND name = %s"
        params = (0, 1)
        params = (1, "John")
        '''

        sql = "SELECT province AS `name`, SUM(sales) AS `value` FROM goods GROUP BY province"
        params = None
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()
            result = []
            for row in rows:
                data = dict(zip(columns, row))
                result.append(data)
        return SuccessResponse(data=result)


# 统计-各个省份产品平均价格统计
class provincePriceStatisView(APIView):
    def get(self, request):
        '''
        sql = "SELECT * FROM my_table WHERE id = %s AND name = %s"
        params = (0, 1)
        params = (1, "John")
        '''

        sql = "SELECT province AS `name`, AVG(price) AS `value` FROM goods GROUP BY province"
        params = None
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()
            result = []
            for row in rows:
                data = dict(zip(columns, row))
                result.append(data)
        return SuccessResponse(data=result)


# 统计-产品销量前10名省份统计
class provinceTopSalesStatisView(APIView):
    def get(self, request):
        '''
        sql = "SELECT * FROM my_table WHERE id = %s AND name = %s"
        params = (0, 1)
        params = (1, "John")
        '''

        sql = "SELECT province AS `name`, SUM(sales) AS `value` FROM goods GROUP BY province ORDER BY SUM(sales) DESC LIMIT 10"
        params = None
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()
            result = []
            for row in rows:
                data = dict(zip(columns, row))
                result.append(data)
        return SuccessResponse(data=result)


# 统计-产品销量前10名城市统计
class cityTopSalesStatisView(APIView):
    def get(self, request):
        '''
        sql = "SELECT * FROM my_table WHERE id = %s AND name = %s"
        params = (0, 1)
        params = (1, "John")
        '''

        sql = "SELECT city AS `name`, SUM(sales) AS `value` FROM goods GROUP BY city ORDER BY SUM(sales) DESC LIMIT 10"
        params = None
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()
            result = []
            for row in rows:
                data = dict(zip(columns, row))
                result.append(data)
        return SuccessResponse(data=result)


# 修改产品收藏
class UpdateCollect(APIView):
    # 修改
    def post(self, request):
        id = None
        if 'id' in request.data:
            id = request.data['id']
        userId = None
        if 'userId' in request.data:
            userId = request.data['userId']
        goodsId = None
        if 'goodsId' in request.data:
            goodsId = request.data['goodsId']

        if id:
            dbOne = Collect.objects.filter(id=id).first()
            if dbOne:
                dbOne.user_id = userId
                dbOne.goods_id = goodsId
                dbOne.save()
        else:
            Collect.objects.create(
                user_id=userId,
                goods_id=goodsId
            )
        return SuccessResponse(msg="操作成功")


# 查询产品收藏
class CheckCollect(APIView):
    def get(self, request, goodsId, userId):
        dbOne = Collect.objects.filter(goods_id=goodsId, user_id=userId).first()
        flag = False
        if dbOne:
            flag = True
        return SuccessResponse(flag)


# 删除产品收藏
class DeleteCollect(APIView):
    def delete(self, request, goodsId, userId):
        dbOne = Collect.objects.filter(goods_id=goodsId, user_id=userId).first()
        if dbOne:
            dbOne.delete()
        return SuccessResponse(msg="操作成功")


# 修改浏览量
class UpdateGoodsViews(APIView):
    # 修改
    def post(self, request, id):
        dbOne = Goods.objects.filter(id=id).first()
        if dbOne.views:
            dbOne.views = dbOne.views + 1
        else:
            dbOne.views = 1
        dbOne.save()
        return SuccessResponse(msg="操作成功")


# 添加推荐标签
class AddTags(APIView):
    # 修改
    def post(self, request, categoryId, userId):
        Membertags.objects.create(
            user_id=userId,
            category_id=categoryId,
        )
        return SuccessResponse(msg="操作成功")


# 删除推荐标签
class DeleteTags(APIView):
    # 修改
    def delete(self, request, categoryId, userId):
        Membertags.objects.filter(
            user_id=userId,
            category_id=categoryId,
        ).delete()
        return SuccessResponse(msg="操作成功")


def to_camel_case(s):
    parts = s.split('_')
    return parts[0] + ''.join(part.title() for part in parts[1:])


def convert_props_to_camel_case(data):
    for key, value in list(data.items()):
        if isinstance(value, dict):
            convert_props_to_camel_case(value)
        elif isinstance(value, list):
            for item in value:
                convert_props_to_camel_case(item)
        camel_case_key = to_camel_case(key)
        data[camel_case_key] = data.pop(key)
