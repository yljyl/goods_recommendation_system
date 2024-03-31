<script setup>
import { RouterView } from 'vue-router'
import router from "@/router";
import {useUserStore} from "@/stores/user";
import request from "@/utils/request";
import {ElMessage} from "element-plus";
import {nextTick, ref} from "vue";
import config from "../../config";

const userStore = useUserStore()
let user = userStore.getUser
const activePath = router.currentRoute.value.path
const name = ref('')  
name.value = router.currentRoute.value.query.name || ''
const childRef = ref()
const menus = ref([])


const logout = () => {
  request.get('user/logout/' + user.uid).then(res => {
    if (res.code === '200') {
      userStore.logout()
	  window.location.href="/front"
    } else {
      ElMessage.error(res.msg)
    }
  })
}

const getAvatarHandler = (avatar) => {
  user.avatar = avatar
}

const search = () => {
  router.push('/front/goods?name=' + name.value)
}
</script>

<!-- <template>
  <div>
    <div style="height: 60px; line-height: 60px; border-bottom: 1px solid #eee;text-align: right;">
      <div style="font-size: 16px; color: #4B0082;" v-if="user.id">
        <el-avatar :size="30" :src="user.avatar" style="margin-top: 10px;" />
        你好，{{ user.name }}
        <a href="javascript:void(0)" @click="router.push('/person')" class="loginCls">修改个人资料</a>
        <a href="javascript:void(0)" @click="router.push('/password')" class="loginCls">重置密码</a>
        <a href="javascript:void(0)" @click="logout" class="loginCls">退出登录</a>
      </div>
      <div style="flex: 3; font-size: 16px; color: #4B0082; margin-left: 180px;" v-else>
        <a href="javascript:void(0)" @click="router.push('/login')" class="loginCls">登录</a>
        <a href="javascript:void(0)" @click="router.push('/register-member')" class="loginCls">用户注册</a>
      </div>
    </div>

    <div style="display: flex; height: 60px; line-height: 60px; border-bottom: 1px solid #eee;background-color: #6A5ACD;">
      <div style="flex: 1;width: 220px; padding-left: 30px">
        <div style="font-size: 20px; color: #FFFFFF; font-weight: bold">{{config.projectName}}</div>
      </div>
      <div style="flex: 3; display: flex">
        <el-menu :default-active="activePath" mode="horizontal" router style="border: none; height: 100%; width: 100%;background-color: #6A5ACD;">
          <el-menu-item index="/front/home">首页</el-menu-item>
          <el-menu-item index="/front/notice">网站公告</el-menu-item>
          <el-menu-item index="/front/goods">商品列表</el-menu-item>
          <el-menu-item index="/statisticscategory" v-if="user.id!=null && user.role=='MEMBER'">商品数据分析</el-menu-item>
          <el-menu-item index="/wordcloud" v-if="user.id!=null && user.role=='MEMBER'">词云分析</el-menu-item>
          <el-dropdown>
            <el-menu-item>个人中心</el-menu-item>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item><div @click="router.push('/front/collect')">我的商品收藏</div></el-dropdown-item>
                <el-dropdown-item><div @click="router.push('/front/membertags')">我的商品标签</div></el-dropdown-item>
                <el-dropdown-item><div @click="router.push('/front/goodsrecommend')">个性化推荐商品</div></el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
          <el-menu-item index="/home" v-if="user.id!=null && user.role=='ADMIN'">后台管理</el-menu-item>
        </el-menu>
      </div>
      <div style="flex: 2;">
          <el-input style="width: 250px" placeholder="在这里搜索商品" v-model="name" clearable size="large"></el-input>
          <el-button style="margin-left: 5px;background-color: #FFFFFF;color: #6A5ACD;" @click="search" size="large">搜索</el-button>
      </div>
    </div>

    <div style="width: 100%; margin: 0 auto;min-height: 600px;">
      <router-view v-slot="{ Component }">
        <component @getAvatar="getAvatarHandler" @getUnread="getUnRead" ref="childRef" :is="Component" />
      </router-view>
    </div>


    <div style="height: 100px; line-height: 100px; border-top: 1px solid rgba(208,208,208,0.08);text-align: center;background-color: #6A5ACD;color: #FFFFFF;">
      <span>{{config.projectName}}</span>
    </div>
  </div>
</template> -->

<!-- <style scoped>
  .badge {
    margin-top: 10px;
    margin-right: 40px;
  }
  :deep(.el-badge__content.is-fixed) {
    top: 10px !important;
  }

  .content {
    text-align: center;
  }

  .el-menu-item{
    background-color: #6A5ACD;
    color: #FFFFFF;
  }

  .el-menu--horizontal>.el-menu-item.is-active{
    color: #ffffff !important;
    border-bottom: 2px solid #ffffff !important;
  }

  .loginCls{
    margin-left: 25px;
    text-decoration: none;
    color: #4B0082;
  }
  .loginCls a {
    text-decoration: none;
    color: #333;
    transition: color 0.3s;
  }

  .loginCls:hover {
    color: #f00;
  }

  .loginCls:visited {
    color: #999;
  }

  .loginCls::after {
    content: '';
    width: 0;
    height: 1px;
    background-color: #f00;
    transition: width 0.3s;
  }

  .loginCls:hover::after {
    width: 100%;
  }
  
</style> -->

<template>
  <div class="app-container">
    <div class="top-bar">
      <div v-if="user.id" class="user-info">
        <el-avatar :size="30" :src="user.avatar" class="user-avatar" />
        你好，{{ user.name }}
        <a href="javascript:void(0)" @click="router.push('/person')" class="action-link">修改个人资料</a>
        <a href="javascript:void(0)" @click="router.push('/password')" class="action-link">重置密码</a>
        <a href="javascript:void(0)" @click="logout" class="action-link">退出登录</a>
      </div>
      <div v-else class="login-register">
        <a href="javascript:void(0)" @click="router.push('/login')" class="action-link">登录</a>
        <a href="javascript:void(0)" @click="router.push('/register-member')" class="action-link">用户注册</a>
      </div>
    </div>

    <div class="navigation-bar">
      <el-menu :default-active="activePath" mode="horizontal" router class="menu">
        <el-menu-item index="/front/home">首页</el-menu-item>
        <el-menu-item index="/front/notice">网站公告</el-menu-item>
        <el-menu-item index="/front/goods">商品列表</el-menu-item>
        <el-menu-item index="/statisticscategory" v-if="user.id!=null && user.role=='MEMBER'">商品数据分析</el-menu-item>
        <el-menu-item index="/wordcloud" v-if="user.id!=null && user.role=='MEMBER'">词云分析</el-menu-item>
        <el-dropdown>
          <el-menu-item>个人中心</el-menu-item>
          <template #dropdown>
            <el-dropdown-menu>
              <el-dropdown-item><div @click="router.push('/front/collect')">我的商品收藏</div></el-dropdown-item>
              <el-dropdown-item><div @click="router.push('/front/membertags')">我的商品标签</div></el-dropdown-item>
              <el-dropdown-item><div @click="router.push('/front/goodsrecommend')">个性化推荐商品</div></el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>
        <el-menu-item index="/home" v-if="user.id!=null && user.role=='ADMIN'">后台管理</el-menu-item>
      </el-menu>
      <div class="search-bar">
        <el-input placeholder="在这里搜索商品" v-model="name" clearable size="large" class="search-input"></el-input>
        <el-button @click="search" size="large" class="search-button">搜索</el-button>
      </div>
    </div>

    <div class="content-container">
      <router-view v-slot="{ Component }">
        <component @getAvatar="getAvatarHandler" @getUnread="getUnRead" ref="childRef" :is="Component" />
      </router-view>
    </div>

    <div class="footer">
      <span>{{config.projectName}}</span>
    </div>
  </div>
</template>

<style scoped>
.app-container {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  color: #fff; /* 白色文本 */
  background-color: #000; /* 黑色背景 */
  min-height: 100vh;
}

.top-bar, .footer {
  background-color: #000; /* 黑色背景 */
  color: #fff; /* 白色文本 */
  padding: 0 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 1px 4px rgba(255, 255, 255, 0.1); /* 浅色阴影效果 */
  border-radius: 0; /* 移除圆角 */
}

.user-info .action-link, .login-register .action-link {
  margin-left: 15px;
  padding: 5px 10px;
  color: #fff; /* 保证链接为白色文本 */
}

.top-bar:hover, .footer:hover {
  box-shadow: 0 4px 8px rgba(255, 255, 255, 0.2); /* 悬停时浅色阴影效果 */
}

.navigation-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 20px;
  background-color: #000; /* 黑色背景 */
}

.menu {
  flex-grow: 1;
  background-color: transparent; /* 透明背景，以符合顶部和底部栏 */
}

.search-bar {
  display: flex;
  align-items: center;
}

.menu .el-menu-item, .el-dropdown-link, .search-button {
  transition: background-color 0.3s ease, transform 0.2s ease;
  border-radius: 0; /* 移除圆角 */
}

.menu .el-menu-item:hover, .el-dropdown-link:hover, .search-button:hover {
  transform: translateY(-2px); /* 悬停时轻微上升效果 */
  background-color: #111; /* 悬停时背景色变暗 */
}

.search-input .el-input__inner {
  border-radius: 0; /* 移除圆角 */
  margin-right: 10px;
  background-color: #fff; /* 白色背景 */
  color: #000; /* 黑色文本 */
}

.search-input .el-input__inner:focus {
  box-shadow: 0 0 8px rgba(255,255,255,0.1); /* 聚焦时浅色阴影效果 */
}

.search-button {
  border-radius: 0; /* 移除圆角 */
  margin-left: 10px;
  background-color: #fff; /* 白色背景 */
  color: #000; /* 黑色文本 */
  border: 1px solid #fff; /* 白色边框 */
}

</style>



