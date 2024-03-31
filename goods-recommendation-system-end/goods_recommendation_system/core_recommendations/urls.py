from django.urls import path
from goods_recommendation_system import settings
from django.conf.urls.static import static
# from .view import *
from core_recommendations.views.member import *
from core_recommendations.views.category import *
from core_recommendations.views.goods import *
from core_recommendations.views.comments import *
from core_recommendations.views.collect import *
from core_recommendations.views.membertags import *
from core_recommendations.views.banner import *
from core_recommendations.views.front import *
from core_recommendations.views.recommend import *
from core_recommendations.views.wordcloud import *

urlpatterns = [
    path('member', MemberView.as_view(), name="member"),
    path('member/<int:pk>', MemberView.as_view(), name='member_detail'),
    path('member/page', MemberPageView.as_view(), name="member_page"),
    path('member/del/batch', MemberBatchDeleteAPIView.as_view(), name="member_batch_delete"),
    path('member/export', MemberExport.as_view(), name="member_export"),
    path('front/member/user/<int:userId>', getMemberByUserId.as_view(), name="getMemberByUserId"),
    path('front/member/update', UpdateMember.as_view(), name="UpdateMember"),

    # 商品分类
    path('category', CategoryView.as_view(), name="category"),
    path('category/<int:pk>', CategoryView.as_view(), name='category_detail'),
    path('category/page', CategoryPageView.as_view(), name="category_page"),
    path('category/del/batch', CategoryBatchDeleteAPIView.as_view(), name="category_batch_delete"),
    path('category/export', CategoryExport.as_view(), name="category_export"),
    path('front/category/update', UpdateCategory.as_view(), name="UpdateCategory"),
    # 商品信息
    path('goods', GoodsView.as_view(), name="goods"),
    path('goods/<int:pk>', GoodsView.as_view(), name='goods_detail'),
    path('goods/page', GoodsPageView.as_view(), name="goods_page"),
    path('goods/del/batch', GoodsBatchDeleteAPIView.as_view(), name="goods_batch_delete"),
    path('goods/export', GoodsExport.as_view(), name="goods_export"),
    path('front/goods/update', UpdateGoods.as_view(), name="UpdateGoods"),
    # 商品评论
    path('comments', CommentsView.as_view(), name="comments"),
    path('comments/<int:pk>', CommentsView.as_view(), name='comments_detail'),
    path('comments/page', CommentsPageView.as_view(), name="comments_page"),
    path('comments/del/batch', CommentsBatchDeleteAPIView.as_view(), name="comments_batch_delete"),
    path('comments/export', CommentsExport.as_view(), name="comments_export"),
    path('front/comments/update', UpdateComments.as_view(), name="UpdateComments"),
    # 商品收藏
    path('collect', CollectView.as_view(), name="collect"),
    path('collect/<int:pk>', CollectView.as_view(), name='collect_detail'),
    path('collect/page', CollectPageView.as_view(), name="collect_page"),
    path('collect/del/batch', CollectBatchDeleteAPIView.as_view(), name="collect_batch_delete"),
    path('collect/export', CollectExport.as_view(), name="collect_export"),
    path('front/collect/update', UpdateCollect.as_view(), name="UpdateCollect"),
    # 用户标签
    path('membertags', MembertagsView.as_view(), name="membertags"),
    path('membertags/<int:pk>', MembertagsView.as_view(), name='membertags_detail'),
    path('membertags/page', MembertagsPageView.as_view(), name="membertags_page"),
    path('membertags/del/batch', MembertagsBatchDeleteAPIView.as_view(), name="membertags_batch_delete"),
    path('membertags/export', MembertagsExport.as_view(), name="membertags_export"),
    path('front/membertags/update', UpdateMembertags.as_view(), name="UpdateMembertags"),

    # 轮播图
    path('banner', BannerView.as_view(), name="banner"),
    path('banner/<int:pk>', BannerView.as_view(), name='banner_detail'),
    path('banner/page', BannerPageView.as_view(), name="banner_page"),
    path('banner/del/batch', BannerBatchDeleteAPIView.as_view(), name="banner_batch_delete"),
    path('banner/export', BannerExport.as_view(), name="banner_export"),

    # 前台-用户
    path('front/user/list', UserListDetail.as_view(), name="front_user_list"),
    path('front/user/<int:pk>', UserListDetail.as_view(), name='front_user_detail'),
    path('front/user/page', UserPage.as_view(), name="front_user_page"),
    # 前台-网站公告
    path('front/notice/list', NoticeListDetail.as_view(), name="front_notice_list"),
    path('front/notice/<int:pk>', NoticeListDetail.as_view(), name='front_notice_detail'),
    path('front/notice/page', NoticePage.as_view(), name="front_notice_page"),
    # 前台-轮播图
    path('front/banner/list', BannerListDetail.as_view(), name="front_banner_list"),
    path('front/banner', BannerListDetail.as_view(), name="front_banner"),
    path('front/banner/<int:pk>', BannerListDetail.as_view(), name='front_banner_detail'),
    path('front/banner/page', BannerPage.as_view(), name='front_banner_page'),
    # 前台-用户
    path('front/member/list', MemberListDetail.as_view(), name="front_member_list"),
    path('front/member', MemberListDetail.as_view(), name="front_member"),
    path('front/member/<int:pk>', MemberListDetail.as_view(), name='front_member_detail'),
    path('front/member/page', MemberPage.as_view(), name='front_member_page'),
    # 前台-产品分类
    path('front/category/list', CategoryListDetail.as_view(), name="front_category_list"),
    path('front/category', CategoryListDetail.as_view(), name="front_category"),
    path('front/category/<int:pk>', CategoryListDetail.as_view(), name='front_category_detail'),
    path('front/category/page', CategoryPage.as_view(), name='front_category_page'),
    # 前台-产品列表
    path('front/goods/list', GoodsListDetail.as_view(), name="front_goods_list"),
    path('front/goods', GoodsListDetail.as_view(), name="front_goods"),
    path('front/goods/<int:pk>', GoodsListDetail.as_view(), name='front_goods_detail'),
    path('front/goods/page', GoodsPage.as_view(), name='front_goods_page'),
    # 前台-产品评论
    path('front/comments/list', CommentsListDetail.as_view(), name="front_comments_list"),
    path('front/comments', CommentsListDetail.as_view(), name="front_comments"),
    path('front/comments/<int:pk>', CommentsListDetail.as_view(), name='front_comments_detail'),
    path('front/comments/page', CommentsPage.as_view(), name='front_comments_page'),
    # 前台-我的产品收藏
    path('front/collect/list', CollectListDetail.as_view(), name="front_collect_list"),
    path('front/collect', CollectListDetail.as_view(), name="front_collect"),
    path('front/collect/<int:pk>', CollectListDetail.as_view(), name='front_collect_detail'),
    path('front/collect/page', CollectPage.as_view(), name='front_collect_page'),
    # 前台-我的产品标签
    path('front/membertags/list', MembertagsListDetail.as_view(), name="front_membertags_list"),
    path('front/membertags', MembertagsListDetail.as_view(), name="front_membertags"),
    path('front/membertags/<int:pk>', MembertagsListDetail.as_view(), name='front_membertags_detail'),
    path('front/membertags/page', MembertagsPage.as_view(), name='front_membertags_page'),

    # 查看产品评论
    path('front/comments/tree', CommentsTree.as_view(), name="front_comments_tree"),
    # 添加/修改产品评论
    path('front/comments/update', UpdateComments.as_view(), name="front_updatecomments"),

    # 统计-不同分类的产品数量
    path('statistics/categoryGoodsStatis', categoryGoodsStatisView.as_view(),
         name="statistics_categoryGoodsStatis"),
    # 统计-不同分类的产品的总销售量
    path('statistics/categorySalesStatis', categorySalesStatisView.as_view(),
         name="statistics_categorySalesStatis"),
    # 统计-不同分类的产品的平均价格
    path('statistics/categoryPriceStatis', categoryPriceStatisView.as_view(),
         name="statistics_categoryPriceStatis"),
    # 统计-各个省份产品数量统计
    path('statistics/provinceCountStatis', provinceCountStatisView.as_view(),
         name="statistics_provinceCountStatis"),
    # 统计-各个省份产品总销售量统计
    path('statistics/provinceSalesStatis', provinceSalesStatisView.as_view(),
         name="statistics_provinceSalesStatis"),
    # 统计-各个省份产品平均价格统计
    path('statistics/provincePriceStatis', provincePriceStatisView.as_view(),
         name="statistics_provincePriceStatis"),
    # 统计-产品销量前10名省份统计
    path('statistics/provinceTopSalesStatis', provinceTopSalesStatisView.as_view(),
         name="statistics_provinceTopSalesStatis"),
    # 统计-产品销量前10名城市统计
    path('statistics/cityTopSalesStatis', cityTopSalesStatisView.as_view(),
         name="statistics_cityTopSalesStatis"),

    # 产品收藏
    path('front/collect/update', UpdateCollect.as_view(), name="front_updateproducecollect"),
    path('front/collect/collect/<int:goodsId>/<int:userId>', CheckCollect.as_view(),
         name="front_checkcollect"),
    path('front/collect/<int:goodsId>/<int:userId>', DeleteCollect.as_view(), name="front_deletecollect"),

    # 修改浏览量
    path('front/goods/views/update/<int:id>', UpdateGoodsViews.as_view(), name="front_goodsupdateviews"),

    # 添加推荐标签
    path('front/membertags/<int:categoryId>/<int:userId>', AddTags.as_view(), name="front_addtags"),
    # 删除推荐标签
    path('front/membertags/del/<int:categoryId>/<int:userId>', DeleteTags.as_view(),
         name="front_deletetags"),

    # 个性化推荐
    path('front/goodsrecommend', UserRecommendView.as_view(), name="front_userrecommend"),

    # 词云分析
    path('front/wordcloud', WordCloudView.as_view(), name="front_wordcloud"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)