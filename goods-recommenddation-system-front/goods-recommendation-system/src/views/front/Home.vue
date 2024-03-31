<script setup>
import {reactive, ref} from "vue";
import request from "@/utils/request";
import router from "@/router"


const name = ref('')
const state = reactive({
    noticeList:[],
        rotationList:[],
})


state.userOptions = []
request.get('/user/user').then(res => state.userOptions = res.data)

const pageNum = ref(1)
const pageSize = ref(5)
const total = ref(0)
const load = () => {

  //请求前面10条的公告
  request.get('/user/notice/findTop10').then(res => {
    state.noticeList = res.data
  })
}
load()  // 调用 load方法拿到后台数据

//轮播图
request.get('/core/front/banner/list').then(res => {
  state.rotationList = res.data
  state.rotationList = state.rotationList.filter((item) => item.indexRadio === '是');
})

//加载首页数据列表
request.get('/core/front/goods/page', {
  params: {
    pageNum: 1,
    pageSize: 9,
  }
}).then(res => {
  state.goodsData = res.data.records
})
const truncatedContent = (content) => {
  const maxLength = 100;
  if (content.length > maxLength) {
    return content.substring(0, maxLength) + '...';
  }
  return content;
}

state.recommend = []
request.get('/core/front/recommend/goods').then(res => {
  state.recommend = res.data
})
</script>

<template>
  <div>

    <div>
      <div style="width: 100%">
        <el-carousel :interval="5000" arrow="always" height="400px">
          <el-carousel-item v-for="item in state.rotationList" :key="item" v-show="item.indexRadio=='是'">
            <a :href="item.url" target="_blank"><img :src="item.img" alt="" style="width: 100%; height: 100%"></a>
          </el-carousel-item>
        </el-carousel>
      </div>
    </div>

      <div style="width:85%;margin: 0 auto;margin-bottom: 50px;">
        <div style="padding-bottom: 10px ;padding-top: 5px ;border-bottom: 3px solid #f0f8ff;border-top: 3px solid #f0f8ff; background-color: whitesmoke; margin-top: 20px;text-align: center;">
          <span style="font-weight: bold; font-size: 24px;color:lightblue;">商品列表</span>
        </div>
        <div style="margin-top: 20px;">
          <el-row :gutter="10">
            <el-col :span="8" v-for="item in state.goodsData" :key="item.id" style="margin-top: 20px;">
              <el-card style="color: #666" >
                <div ><img @click="router.push('/front/goods-detail?id=' + item.id)" :src="item.img" alt="" style="width: 100%; height: 280px;cursor: pointer;"></div>
                <div><span style="font-weight: bold">{{ item.name}}</span></div>
                <div style="width: 90%;margin-top: 20px;line-height: 40px;height: 40px;">
                  <el-button type="primary" size="small" @click="router.push('/front/goods-detail?id=' + item.id)" style="float: left;">>>>详情</el-button>
                  <span style="color:red;font-size: 18px;font-weight: bold;float: right;" v-if="item.price">￥{{item.price}}</span>
                </div>
              </el-card>
            </el-col>
          </el-row>
        </div>
    </div>


  </div>
</template>

<style scoped>
.refresh:hover {
  cursor: pointer;
}
:deep(.el-card__body) {
  padding: 10px !important;
}



.title {
  font-size: 18px;
  font-weight: bold;
  color: #333; 
  text-decoration: none;  
  transition: color 0.3s ease;
}

.title:hover {
  color: orangered !important;  
}


.item {
  padding: 20px 0;
  display: flex;
  border-radius: 10px;
}

.item img {
  width: 160px;
  height: 140px;
}

.right-container {
  position: relative;
  margin-left: 20px;
  width: 100%;

}

.right-container div {
  margin-bottom: 7px;
}

.top {
  display: flex;
  color: #101d37;
  font-size: 20px;
  font-weight: bold;
}

.time {
  position: absolute;
  left: 0;
  bottom: 0;
  margin-bottom: 0 !important;
  color: rgba(16, 29, 55, .3);
  font-size: 14px;
}
</style>
