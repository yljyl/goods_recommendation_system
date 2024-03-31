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


  //轮播图
  request.get('/core/front/banner/list').then(res => {
    state.rotationList = res.data
    state.rotationList = state.rotationList.filter((item) => item.indexRadio === '否');
  })

  //加载所有标签
  const getCategory = () =>{
      request.get('/core/front/category/list').then(res => {
          state.tableData = res.data
      })
  }

  //加载用户标签
  state.myList = []
  const getMembertags = () =>{
      request.get('/core/front/membertags/list').then(res => {
          let tagList = res.data
          state.myList = tagList.filter((item) => item.userId === user.id).map(item => item.categoryId);
      })
  }

  //添加标签
  const addTags = (CategoryId) =>{
      request.post('/core/front/membertags/'+CategoryId+'/'+user.id).then(res => {
          load()
      })
  }
  //删除标签
  const deleteTags = (CategoryId) =>{
      request.delete('/core/front/membertags/del/'+CategoryId+'/'+user.id).then(res => {
          load()
      })
  }

  const load = ()=>{
      getCategory()
      getMembertags()
  }
  load()

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
          <span style="font-size: 14px;margin-right: 20px;">当前位置：首页 > 我的商品标签</span>
        </div>

        <div style="padding-bottom: 15px ;border-bottom: 3px solid #4B0082; text-align: left;display: flex;">
          <span style="font-weight: bold; font-size: 24px;float: left;flex: 3;color: #4B0082;">我的商品标签</span>

        </div>

            <div style="padding-bottom: 15px ;margin-top: 100px;text-align: center;line-height: 40px;">
              <span style="font-size: 20px;font-weight: bold;color: #4B0082;">请选择我的商品标签：</span>
              <span v-for="item in state.tableData" :key="item.id" style="margin-right: 10px;" class="navbar" :style="state.myList.includes(item.id)?'background-color:#4B0082;':''">
                <a href="javascript:void(0)" @click="deleteTags(item.id)" v-if="state.myList.includes(item.id)" style="color: #fff;">{{item.name}}</a>
                <a href="javascript:void(0)" @click="addTags(item.id)" v-else>{{item.name}}</a>
              </span>
            </div>

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
    background: #FF9900;
    border: 1px solid #FF9900;
    color: #FFFFFF !important;
  }

  .headerBg {
    background: #FF9933!important;
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
</style> -->

<template>
  <div>
    <!-- 轮播图 -->
    <div class="carousel-container">
      <el-carousel :interval="5000" arrow="always" height="400px">
        <el-carousel-item v-for="item in state.rotationList" :key="item.id">
          <a :href="item.url" target="_blank">
            <img :src="item.img" alt="" class="carousel-image">
          </a>
        </el-carousel-item>
      </el-carousel>
    </div>

    <div class="content-container">
      <div class="section-header">
        <h2 class="section-title">我的商品标签</h2>
      </div>

      <div class="tags-container">
        <span v-for="item in state.tableData" :key="item.id" 
              class="tag-item" 
              :class="{ 'selected': state.myList.includes(item.id) }"
              @click="state.myList.includes(item.id) ? deleteTags(item.id) : addTags(item.id)">
          {{ item.name }}
        </span>
      </div>
    </div>
  </div>
</template>

<style>
/* 轮播图样式调整 */
.carousel-container {
  margin: 30px auto;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  border-radius: 8px;
  overflow: hidden;
}

/* 标签选择器样式调整 */
.tags-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  margin: 20px auto;
  max-width: 85%;
}

.tag-item {
  margin: 5px;
  padding: 5px 15px;
  border: 1px solid #4B0082;
  border-radius: 20px;
  color: #333;
  font-size: 14px;
  cursor: pointer;
  transition: background-color 0.3s, color 0.3s;
}

.tag-item.selected,
.tag-item:hover {
  background-color: #4B0082;
  color: #ffffff;
}

</style>