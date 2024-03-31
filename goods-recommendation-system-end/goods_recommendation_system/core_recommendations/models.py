from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework import serializers

# Create your models here.

# 用户
class Member(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="编号", help_text="编号")
    username = models.CharField(max_length=255, verbose_name="登录账户 ", null=True, blank=True, help_text="登录账户")
    name = models.CharField(max_length=255, verbose_name="姓名 ", null=True, blank=True, help_text="姓名")
    user_id = models.IntegerField(verbose_name="所属用户", null=True, blank=True, help_text="所属用户")
    phone = models.CharField(max_length=255, verbose_name="联系电话 ", null=True, blank=True, help_text="联系电话")

    @property
    def userId(self):
        return self.user_id

    class Meta:
        db_table = "member"
        verbose_name = "用户"
        verbose_name_plural = verbose_name

class MemberSerializer(serializers.ModelSerializer):
    userId = serializers.SerializerMethodField()

    class Meta:
        model = Member
        fields = '__all__'

    def get_userId(self, obj):
        return obj.user_id


# 商品分类
class Category(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="编号", help_text="编号")
    name = models.CharField(max_length=255, verbose_name="分类名称 ", null=True, blank=True, help_text="分类名称")


    class Meta:
        db_table = "category"
        verbose_name = "商品分类"
        verbose_name_plural = verbose_name

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


# 商品信息
class Goods(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="编号", help_text="编号")
    category_id = models.IntegerField(verbose_name="商品分类", null=True, blank=True, help_text="商品分类")
    name = models.CharField(max_length=255, verbose_name="商品名称 ", null=True, blank=True, help_text="商品名称")
    img = models.CharField(max_length=255, verbose_name="商品图片 ", null=True, blank=True, help_text="商品图片")
    content = models.TextField(verbose_name="商品介绍 ",null=True, blank=True,  help_text="商品介绍")
    price = models.FloatField(verbose_name="价格 ",null=True, blank=True,  help_text="价格")
    business = models.CharField(max_length=255, verbose_name="销售商家 ", null=True, blank=True, help_text="销售商家")
    province = models.CharField(max_length=255, verbose_name="商家省份 ", null=True, blank=True, help_text="商家省份")
    city = models.CharField(max_length=255, verbose_name="商家城市 ", null=True, blank=True, help_text="商家城市")
    sales = models.IntegerField(verbose_name="销售量", null=True, blank=True, help_text="销售量")
    links = models.CharField(max_length=255, verbose_name="数据来源 ", null=True, blank=True, help_text="数据来源")
    views = models.IntegerField(verbose_name="浏览量", null=True, blank=True, help_text="浏览量")

    @property
    def categoryId(self):
        return self.category_id

    class Meta:
        db_table = "goods"
        verbose_name = "商品信息"
        verbose_name_plural = verbose_name

class GoodsSerializer(serializers.ModelSerializer):
    categoryId = serializers.SerializerMethodField()

    class Meta:
        model = Goods
        fields = '__all__'

    def get_categoryId(self, obj):
        return obj.category_id

# 商品评论
class Comments(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="评论编号", help_text="评论编号")
    content = models.TextField(verbose_name="评论内容 ",null=True, blank=True,  help_text="评论内容")
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, help_text="添加时间", verbose_name="添加时间")
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True, help_text="修改时间",verbose_name="修改时间")
    user_id = models.IntegerField(verbose_name="用户", null=True, blank=True, help_text="用户")
    goods_id = models.IntegerField(verbose_name="商品编号", null=True, blank=True, help_text="商品编号")
    pid = models.IntegerField(verbose_name="父评论ID", null=True, blank=True, help_text="父评论ID")
    puser_id = models.IntegerField(verbose_name="父级用户ID", null=True, blank=True, help_text="父级用户ID")
    score = models.IntegerField(verbose_name="评论星级", null=True, blank=True, help_text="评论星级")

    @property
    def createTime(self):
        return self.create_time
    @property
    def updateTime(self):
        return self.update_time
    @property
    def userId(self):
        return self.user_id
    @property
    def goodsId(self):
        return self.goods_id
    @property
    def puserId(self):
        return self.puser_id

    class Meta:
        db_table = "comments"
        verbose_name = "商品评论"
        verbose_name_plural = verbose_name

class CommentsSerializer(serializers.ModelSerializer):
    createTime = serializers.SerializerMethodField()
    updateTime = serializers.SerializerMethodField()
    userId = serializers.SerializerMethodField()
    goodsId = serializers.SerializerMethodField()
    puserId = serializers.SerializerMethodField()

    class Meta:
        model = Comments
        fields = '__all__'

    def get_createTime(self, obj):
        return obj.create_time
    def get_updateTime(self, obj):
        return obj.update_time
    def get_userId(self, obj):
        return obj.user_id
    def get_goodsId(self, obj):
        return obj.goods_id
    def get_puserId(self, obj):
        return obj.puser_id

# 商品收藏
class Collect(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID", help_text="ID")
    user_id = models.IntegerField(verbose_name="用户", null=True, blank=True, help_text="用户")
    goods_id = models.IntegerField(verbose_name="商品", null=True, blank=True, help_text="商品")
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, help_text="创建时间", verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True, help_text="更新时间",verbose_name="更新时间")

    @property
    def userId(self):
        return self.user_id
    @property
    def goodsId(self):
        return self.goods_id
    @property
    def createTime(self):
        return self.create_time
    @property
    def updateTime(self):
        return self.update_time

    class Meta:
        db_table = "collect"
        verbose_name = "商品收藏"
        verbose_name_plural = verbose_name

class CollectSerializer(serializers.ModelSerializer):
    userId = serializers.SerializerMethodField()
    goodsId = serializers.SerializerMethodField()
    createTime = serializers.SerializerMethodField()
    updateTime = serializers.SerializerMethodField()

    class Meta:
        model = Collect
        fields = '__all__'

    def get_userId(self, obj):
        return obj.user_id
    def get_goodsId(self, obj):
        return obj.goods_id
    def get_createTime(self, obj):
        return obj.create_time
    def get_updateTime(self, obj):
        return obj.update_time

# 用户标签
class Membertags(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="编号", help_text="编号")
    user_id = models.IntegerField(verbose_name="用户编号", null=True, blank=True, help_text="用户编号")
    category_id = models.IntegerField(verbose_name="分类编号", null=True, blank=True, help_text="分类编号")

    @property
    def userId(self):
        return self.user_id
    @property
    def categoryId(self):
        return self.category_id

    class Meta:
        db_table = "membertags"
        verbose_name = "用户标签"
        verbose_name_plural = verbose_name

class MembertagsSerializer(serializers.ModelSerializer):
    userId = serializers.SerializerMethodField()
    categoryId = serializers.SerializerMethodField()

    class Meta:
        model = Membertags
        fields = '__all__'

    def get_userId(self, obj):
        return obj.user_id
    def get_categoryId(self, obj):
        return obj.category_id


# 轮播图
class Banner(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="轮播图编号", help_text="轮播图编号")
    img = models.CharField(max_length=255, verbose_name="图片 ", null=True, blank=True, help_text="图片")
    url = models.CharField(max_length=255, verbose_name="链接地址 ", null=True, blank=True, help_text="链接地址")
    index_radio = models.CharField(max_length=255, verbose_name="是否首页 ", null=True, blank=True, help_text="是否首页")

    @property
    def indexRadio(self):
        return self.index_radio

    class Meta:
        db_table = "banner"
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name

class BannerSerializer(serializers.ModelSerializer):
    indexRadio = serializers.SerializerMethodField()

    class Meta:
        model = Banner
        fields = '__all__'

    def get_indexRadio(self, obj):
        return obj.index_radio

