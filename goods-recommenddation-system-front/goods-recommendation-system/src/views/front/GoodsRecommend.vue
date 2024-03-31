<script setup>
  import router from "@/router";
  import request from "@/utils/request";
  import {onMounted, reactive, ref} from "vue";
  import {useUserStore} from "@/stores/user";
  import '@wangeditor/editor/dist/css/style.css' // 引入 css
  import { Editor, Toolbar } from '@wangeditor/editor-for-vue'

  const userStore = useUserStore()
  const user = userStore.getUser
  const pageNum = ref(1)
  const pageSize = ref(5)
  const total = ref(0)

      //判断用户是否登录
  if(user.id==null){
    router.push('/login')
  }

  const content = ref('')
  const viewShow = ref(false)
  const view = (value) => {
    viewShow.value = true
    content.value = value
  }

  const id = router.currentRoute.value.query.id
  let name = router.currentRoute.value.query.name
  const state = reactive({
    tableData:[],
  })

  state.categoryOptions = []
  request.get('/core/front/category/list').then(res => state.categoryOptions = res.data)

  //轮播图
  request.get('/core/front/banner/list').then(res => {
      state.rotationList = res.data
      state.rotationList = state.rotationList.filter((item) => item.indexRadio === '否');
  })

  //加载所有推荐数据
  const load = () =>{
      request.get('/core/front/goodsrecommend').then(res => {
          state.tableData = res.data
      })
  }
  load()

</script>

<template>
  <div>

      <div>
        <div style="width: 100%">
          <el-carousel :interval="5000" arrow="always" height="200px">
            <el-carousel-item v-for="item in state.rotationList" :key="item">
              <a :href="item.url" target="_blank"><img :src="item.img" alt="" style="width: 100%; height: 100%"></a>
            </el-carousel-item>
          </el-carousel>
        </div>
      </div>


    <div style="width:85%;margin: 0 auto;margin-bottom: 50px;">
        <div style="padding-bottom: 15px ;margin-top: 20px;text-align: left;">
          <span style="font-size: 14px;margin-right: 20px;">当前位置：首页 > 个性化推荐产品</span>
        </div>

        <div style="padding-bottom: 15px ;border-bottom: 3px solid #0047AB; text-align: left;display: flex;">
          <span style="font-weight: bold; font-size: 24px;float: left;flex: 3;color: #0047AB;">个性化推荐产品</span>
        </div>

        <el-table :data="state.tableData" style="width: 100%;margin-top: 20px;" stripe border :header-cell-class-name="'headerBg'">
                  <el-table-column prop="id" label="编号"></el-table-column>
      <el-table-column label="产品分类"><template #default="scope"><span v-if="scope.row.category_id">{{ state.categoryOptions.find(v => v.id === scope.row.category_id) ? state.categoryOptions.find(v => v.id === scope.row.category_id).name : '' }}</span></template></el-table-column>
      <el-table-column prop="name" label="产品名称" width="200">
        <template #default="scope">
              <span v-if="scope.row.id" @click="router.push('/front/goods-detail?id=' + scope.row.id)">{{ scope.row.name }}</span>
            </template>
      </el-table-column>
      <el-table-column label="产品图片"><template #default="scope"><el-image preview-teleported style="width: 80px; height: 80px" :src="scope.row.img" :preview-src-list="[scope.row.img]"></el-image></template></el-table-column>
      <el-table-column prop="price" label="价格"></el-table-column>
      <el-table-column prop="business" label="销售商家"></el-table-column>
      <el-table-column prop="province" label="商家省份"></el-table-column>
      <el-table-column prop="city" label="商家城市"></el-table-column>
      <el-table-column prop="sales" label="销售量"></el-table-column>
      <el-table-column prop="views" label="浏览量"></el-table-column>

        </el-table>


    </div>
  </div>
</template>

<style>
  .navbar {
    background-color: #eeeeee;
    padding: 10px;
    justify-content: center;
  }

  .navbar a {
    font-size: 16px;
    color: #333;
    text-decoration: none;
    margin: 0 15px;
    padding: 5px;
    transition: color 0.3s;
  }

  .navbar a:hover {
    color: #ff6700;
  }

  .page {
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 13px;
    color: #656565;
    margin-top: 20px;
    padding-bottom: 20px;
  }

  .page > div.homePage, .page > div.lastPage {
    height: 34px;
    line-height: 34px;
    width: 60px;
    text-align: center;
    border: 1px solid #EAEAEA;
    box-sizing: border-box;
    cursor: pointer;
  }

  .page > div.homePage {
    border-radius: 2px 0 0 2px;
  }

  .page > div.lastPage {
    border-radius: 0 2px 2px 0;
  }

  .el-pagination {
    text-align: center;
    padding: 0;
  }

  .el-pagination > button {
    padding: 0 !important;
    height: 34px !important;
  }

  .el-pagination > button.btn-prev {
    border-right: none !important;
  }

  .el-pagination span {
    color: #656565;
    width: 50px;
    border: 1px solid #EAEAEA;
    height: 34px !important;
    line-height: 34px !important;
    box-sizing: border-box;
  }

  .el-pagination .el-pager .number, .el-icon.more.el-icon-more {
    color: #656565 !important;
    border: 1px solid #EAEAEA;
    height: 34px !important;
    line-height: 34px !important;
    box-sizing: border-box;
  }

  .el-icon.more.btn-quicknext.el-icon-more {
    border-right: none;
  }

  .el-icon.more.btn-quickprev.el-icon-more {
    border-left: none;
  }

  .el-pagination .el-pager .number:not(:first-child) {
    border-right: none !important;
  }

  .el-pagination .el-pager .number.active {
    background: #FF9900;
    border: 1px solid #FF9900;
    color: #FFFFFF !important;
  }

  .headerBg {
    background: #0047AB!important;
    color: #ffffff!important;
  }


  .el-dialog {
    background-color: #fff;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.15); 
    padding: 20px; 
    box-sizing: border-box; 
  }

  .el-dialog__header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px;
    background-color: #FF9933;
    border-bottom: 1px solid #ccc;
  }

  .el-dialog__header > * {
    margin-right: 10px;
    color: #ffffff;
  }

  .el-dialog__title {
    font-size: 18px;
    font-weight: bold;
  }

  .el-dialog__body {
    padding: 20px;
  }

  .el-dialog__footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px;
    border-top: 1px solid #ccc;
  }

  .el-dialog__footer > * {
    margin-left: 10px;
  }
</style>

