<script setup>
  import router from "@/router";
  import request from "@/utils/request";
  import {ElMessage} from "element-plus";
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

  state.searchKey = ''
  const load = () => {
    if(state.searchKey!=null && state.searchKey!=''){
      name = state.searchKey
    }
    request.get('/core/front/collect/page', {
      params: {
        name: name,
        pageNum: pageNum.value,
        pageSize: pageSize.value,
      }
    }).then(res => {
      // state.tableData = res.data.records
      state.tableData = res.data.records.filter(item => item.user_id === user.id)
      total.value = res.data.total
    })
  }
  load()  // 调用 load方法拿到后台数据

  //轮播图
  request.get('/core/front/banner/list').then(res => {
    state.rotationList = res.data
    state.rotationList = state.rotationList.filter((item) => item.indexRadio === '否');
  })

  state.userOptions = []
  request.get('/core/front/user/list').then(res => state.userOptions = res.data)
  state.goodsOptions = []
  request.get('/core/front/goods/list').then(res => state.goodsOptions = res.data)


  //搜索
  state.searchKey = ''
  const search = () =>{
    load()
  }

  const deleteItem = (id) =>{
      request.delete('/core/front/collect/'+id).then(res => {
          if (res.code === '200') {
              ElMessage.success("删除成功")
              load()
          } else {
              ElMessage.error(res.msg)
          }
      })
  }
</script>

<!-- <template>
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
          <span style="font-size: 14px;margin-right: 20px;">当前位置：首页 > 我的商品收藏</span>
        </div>

        <div style="padding-bottom: 15px ;border-bottom: 3px solid #4B0082; text-align: left;display: flex;">
          <span style="font-weight: bold; font-size: 24px;float: left;flex: 3;color: #4B0082;">我的商品收藏</span>

          <div style="margin-top: 10px;float: right;flex: 1;">
            <el-input style="width: 200px" placeholder="查询我的商品收藏" v-model="state.searchKey" clearable></el-input>
            <el-button style="margin-left: 5px; background-color: #4B0082; color: white;" @click="search" size="large">查询</el-button>
          </div>
        </div>


        <el-table :data="state.tableData" style="width: 100%;margin-top: 20px;" stripe border :header-cell-class-name="'headerBg'">
                <el-table-column prop="id" label="ID"></el-table-column>
      <el-table-column label="用户"><template #default="scope"><span v-if="scope.row.user_id">{{ state.userOptions.find(v => v.id === scope.row.user_id) ? state.userOptions.find(v => v.id === scope.row.user_id).name : '' }}</span></template></el-table-column>
      <el-table-column label="商品"><template #default="scope"><span v-if="scope.row.goods_id" @click="router.push('/front/goods-detail?id=' + scope.row.goods_id)">{{ state.goodsOptions.find(v => v.id === scope.row.goods_id) ? state.goodsOptions.find(v => v.id === scope.row.goods_id).name : '' }}</span></template></el-table-column>

                <el-table-column label="操作">
                        <template #default="scope"><el-button style="background-color: #4B0082;" type="primary" size="small" @click="deleteItem(scope.row.id)">删除</el-button></template>
                </el-table-column>
        </el-table>


      <el-dialog v-model="viewShow" title="浏览内容" width="40%">
        <div  id="editor-content-view" class="editor-content-view" v-html="content" style="padding: 0 20px"></div>
        <template #footer>
      <span class="dialog-footer">
        <el-button @click="viewShow = false">关闭</el-button>
      </span>
        </template>
      </el-dialog>
    </div>
  </div>
</template> -->

<!-- <style>
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
    background: #4B0082;
    border: 1px solid #4B0082;
    color: #FFFFFF !important;
  }

  .headerBg {
    background: #4B0082!important;
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
    background-color: #4B0082;
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
</style> -->

<template>
  <div class="content-wrapper">
    <div class="carousel-wrapper">
      <el-carousel :interval="5000" arrow="always" height="200px">
        <el-carousel-item v-for="item in state.rotationList" :key="item.id">
          <a :href="item.url" target="_blank">
            <img :src="item.img" alt="" class="carousel-img">
          </a>
        </el-carousel-item>
      </el-carousel>
    </div>

    <div class="main-content">
      <div class="breadcrumb">当前位置：首页 > 我的商品收藏</div>
      <div class="collection-header">
        <h2 class="collection-title">我的商品收藏</h2>
        <div class="search-area">
          <el-input placeholder="查询我的商品收藏" v-model="state.searchKey" clearable class="search-input"></el-input>
          <el-button @click="search" class="search-button">查询</el-button>
        </div>
      </div>

      <el-table :data="state.tableData" stripe border class="data-table">
            <el-table-column prop="id" label="ID"></el-table-column>
            <el-table-column label="用户"><template #default="scope"><span v-if="scope.row.user_id">{{ state.userOptions.find(v => v.id === scope.row.user_id) ? state.userOptions.find(v => v.id === scope.row.user_id).name : '' }}</span></template></el-table-column>
            <el-table-column label="商品"><template #default="scope"><span v-if="scope.row.goods_id" @click="router.push('/front/goods-detail?id=' + scope.row.goods_id)">{{ state.goodsOptions.find(v => v.id === scope.row.goods_id) ? state.goodsOptions.find(v => v.id === scope.row.goods_id).name : '' }}</span></template></el-table-column>
            <el-table-column label="操作">
                <template #default="scope"><el-button class="delete-button" @click="deleteItem(scope.row.id)">删除</el-button></template>
            </el-table-column>
      </el-table>

      <el-dialog v-model="viewShow" title="浏览内容" width="40%">
        <div v-html="content" class="dialog-content"></div>
        <template #footer>
          <el-button @click="viewShow = false">关闭</el-button>
        </template>
      </el-dialog>
    </div>
  </div>
</template>

<style>
.content-wrapper {
  padding-top: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  background: #f3f3f3; /* 轻灰色背景适合数据展示 */
  min-height: 100vh;
}

.carousel-wrapper {
  width: 80%;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 轻微的阴影 */
  margin-bottom: 20px; /* 与主内容的间距 */
}

.carousel-img {
  width: 100%;
  height: auto;
  border-radius: 4px; /* 轻微的圆角边框 */
}

.main-content {
  width: 85%;
  margin: 0 auto;
  background: #ffffff; /* 白色背景 */
  padding: 20px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); /* 阴影效果 */
  border-radius: 8px; /* 圆角边框 */
}

.breadcrumb, .collection-title {
  color: #FFFFFF; /* Light text color for breadcrumb and title */
}

.search-area, .data-table, .dialog-content {
  color: #FFFFFF; /* Light text color for search area, table, and dialog content */
}

.collection-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 20px;
}

.collection-title {
  font-size: 24px;
}

.search-area {
  display: flex;
  align-items: center;
}

.search-input {
  width: 200px;
  margin-right: 10px;
  --el-input-fill: #ffffff; /* Assuming Element Plus supports CSS variables for styling */
}

.search-button, .delete-button {
  background-color: #4B0082;
  color: #FFF; /* White text color for buttons */
}

.data-table {
  width: 100%;
  border-collapse: collapse; /* 删除双边框 */
}


.data-table .cell {
  color: #000; 
  padding: 10px; /* 单元格内间距 */
  border-bottom: 1px solid #ebeef5; /* 分隔线 */
}

.headerBg {
  background-color: #4B0082; /* 主题颜色 */
  color: #ffffff;
  font-weight: bold;
  line-height: 1.5; /* 行间距 */
}

/* 鼠标悬停在单元格上时的样式 */
.el-table .cell:hover {
  background-color: #f9f9f9; /* 轻微的背景色变化 */
}

/* 表格操作按钮样式 */
.delete-button {
  background-color: #ff4d4f; /* 删除按钮的颜色 */
  color: white;
  border: none;
  border-radius: 4px; /* 圆角 */
  padding: 5px 10px; /* 内间距 */
  margin: 4px 2px; /* 外间距 */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 阴影 */
}

.delete-button:hover {
  background-color: #ff7875; /* 悬停时变化 */
}

.dialog-content {
  padding: 20px;
}

/* Style for links to ensure they are visible against the background */
.action-link {
  color: #82B1FF; /* Light blue color for links */
  text-decoration: underline; /* Underline to denote clickable links */
}

.action-link:hover {
  color: #FFC107; /* Change color on hover for better visibility */
}

</style>

