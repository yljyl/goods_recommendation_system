<script setup>
import { RouterView } from 'vue-router'
import router from "@/router";
import {useUserStore} from "@/stores/user";
import request from "@/utils/request";
import {ElMessage} from "element-plus";
const userStore = useUserStore()
let user = userStore.getUser
const activePath = router.currentRoute.value.path.replace('/', '')

const logout = () => {
  request.get('/logout/' + user.uid).then(res => {
    if (res.code === '200') {
      userStore.logout()
    } else {
      ElMessage.error(res.msg)
    }
  })
}
const menus = userStore.getMenus

const getAvatarHandler = (avatar) => {
  user.avatar = avatar
}
</script>

<!-- <template>
  <div class="mainBg">
    <div style="height: 60px; line-height: 60px; border-bottom: 1px solid #ccc; background-color: #ffffff;">
      <div style="display: flex">
        <div style="flex:1.2; color: #87CEEB; font-weight: bold;  text-align: right; font-size: 20px">
          用户画像的商品推荐系统
        </div>

        <div style="flex: 1;text-align: right; ">
          <div>
          </div>
          <div style="width: 500px; text-align: right; padding-right: 20px">
            <span style="margin-right: 5px; color: #87CEEB">你好，{{ user.name }}</span>
            <a href="javascript:void(0)" @click="router.push('/front/home')" class="infoCls">前台系统</a>
            <a href="javascript:void(0)" @click="router.push('/person')" class="infoCls">个人信息</a>
            <a href="javascript:void(0)" @click="router.push('/password')" class="infoCls">修改密码</a>
            <a href="javascript:void(0)" @click="logout" class="infoCls">注销</a>
          </div>
        </div>
      </div>
    </div>

    <div style="display: flex;">
      <div style="width: 230px; min-height: calc(100vh - 60px); border-right: 1px solid #ccc;background-color: #ffffff;">
        <el-menu
            :default-active="activePath"
            :default-openeds="menus.map(v => v.id + '')"
            class="el-menu-demo"
            style="border: none"
            router
        >
        <div v-for="item in menus" :key="item.id">
          <div v-if="item.type === 2">
            <el-menu-item :index="item.path" v-if="!item.hide">
              <el-icon v-if="item.icon">
                <component :is="item.icon"></component>
              </el-icon>
              <span>{{ item.name }}</span>
            </el-menu-item>
          </div>
          <div v-else>
            <el-sub-menu :index="item.id + ''" v-if="!item.hide">
              <template #title>
                <el-icon v-if="item.icon">
                  <component :is="item.icon"></component>
                </el-icon>
                <span>{{ item.name }}</span>
              </template>
              <div  v-for="subItem in item.children" :key="subItem.id">
                <el-menu-item :index="subItem.path" v-if="!subItem.hide">
                  <template #title>
                    <el-icon v-if="subItem.icon">
                      <component :is="subItem.icon"></component>
                    </el-icon>
                    <span>{{ subItem.name }}</span>
                  </template>
                </el-menu-item>
              </div>
            </el-sub-menu>
          </div>
        </div>
        </el-menu>
      </div>

      <div style="flex: 1; padding: 10px">
        <router-view v-slot="{ Component }">
          <component @getAvatar="getAvatarHandler" ref="childRef" :is="Component" />
        </router-view>
      </div>
    </div>

  </div>
</template> -->

<!-- <style>
  .infoCls{
    margin-left: 10px;
    text-decoration: none;
    color: #87CEEB;
  }
  .infoCls a {
    text-decoration: none;
    color: #ffffff;
    transition: color 0.3s;
  }

  .infoCls:hover {
    color: #f00;
  }

  .infoCls:visited {
    color: #999;
  }

  .infoCls::after {
    content: '';
    width: 0;
    height: 1px;
    background-color: #f00;
    transition: width 0.3s;
  }

  .infoCls:hover::after {
    width: 100%;
  }

  .mainBg{
    background-color: rgba(255, 255, 255, 0.5);
    background-image: url("../assets/login-background.jpg");
    background-repeat: no-repeat;
    background-size: cover;
    height: 100vh;
  }
</style> -->

<template>
  <div class="mainBg">
    <div class="top-bar">
      <div class="system-title">用户画像的商品推荐系统</div>
      <div class="user-info">
        <span class="user-greeting">你好，{{ user.name }}</span>
        <a @click="router.push('/front/home')" class="infoCls">前台系统</a>
        <a @click="router.push('/person')" class="infoCls">个人信息</a>
        <a @click="router.push('/password')" class="infoCls">修改密码</a>
        <a @click="logout" class="infoCls">注销</a>
      </div>
    </div>

    <div style="display: flex;">
      <div style="width: 230px; min-height: calc(100vh - 60px);">
        <el-menu
            :default-active="activePath"
            :default-openeds="menus.map(v => v.id + '')"
            class="el-menu-demo"
            style="border: none"
            router
        >
        <div v-for="item in menus" :key="item.id">
          <div v-if="item.type === 2">
            <el-menu-item :index="item.path" v-if="!item.hide">
              <el-icon v-if="item.icon">
                <component :is="item.icon"></component>
              </el-icon>
              <span>{{ item.name }}</span>
            </el-menu-item>
          </div>
          <div v-else>
            <el-sub-menu :index="item.id + ''" v-if="!item.hide">
              <template #title>
                <el-icon v-if="item.icon">
                  <component :is="item.icon"></component>
                </el-icon>
                <span>{{ item.name }}</span>
              </template>
              <div  v-for="subItem in item.children" :key="subItem.id">
                <el-menu-item :index="subItem.path" v-if="!subItem.hide">
                  <template #title>
                    <el-icon v-if="subItem.icon">
                      <component :is="subItem.icon"></component>
                    </el-icon>
                    <span>{{ subItem.name }}</span>
                  </template>
                </el-menu-item>
              </div>
            </el-sub-menu>
          </div>
        </div>
        </el-menu>
      </div>

      <div style="flex: 1; padding: 10px">
        <router-view v-slot="{ Component }">
          <component @getAvatar="getAvatarHandler" ref="childRef" :is="Component" />
        </router-view>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* 设置整个页面的背景为黑色 */
body {
  background-color: #000; /* 纯黑色背景 */
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
}

/* 设置透明度的主背景样式 */
.mainBg {
  background-color: rgba(0, 0, 0, 1); /* 黑色背景，80%透明度 */
  color: #fff; /* 白色文本对比黑色背景 */
  min-height: 100vh;
  padding: 20px; /* 页面内容的内边距 */
  padding-top: 60px;
  border: none;
}

/* 顶部栏样式，具有透明度 */
.top-bar {
  background-color: rgba(0, 0, 0, 0.8); /* 80%透明度的黑色背景 */
  color: #fff; /* 白色文本 */
  position: fixed;
  top: 0;
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.8);
  z-index: 1000;
}

.system-title {
  flex-grow: 1;
  font-weight: bold;
  font-size: 20px;
  text-align: left;
}

/* 侧边栏样式，也具有透明度 */
.el-menu-demo {
  background-color: rgba(0, 0, 0, 1); /* 80%透明度的黑色背景 */
  color: #fff; /* 白色文本 */
  min-height: calc(100vh - 60px); /* 减去顶部栏的高度 */
  border: none;
  height: 100vh;
}

/* 侧边栏中的菜单项样式 */
.el-menu-item {
  background-color: transparent; /* 保持背景透明 */
  color: #fff; /* 白色文本 */
}

.el-menu-demo, 
.el-menu-demo .el-menu-item, 
.el-menu-demo .el-sub-menu__content {
  background-color: #000 !important; /* 使用 !important 确保覆盖 */
}

/* 当菜单项被悬浮时，更改背景颜色 */
.el-menu-item:hover, .el-sub-menu__title:hover {
  background-color: rgba(255, 255, 255, 0.8); /* 轻微的白色高亮 */
  color: #555;
}

/* 当子菜单项被展开时，保持透明背景 */
.el-menu-item.is-opened, .el-menu-item.is-opened .el-menu-item__content,
.el-sub-menu__content {
  background-color: rgba(0, 0, 0, 1); /* 80%透明度的黑色背景 */
}


/* 用户信息和操作链接样式 */
.user-info {
  display: flex; /* 此处确保使用flex布局 */
  align-items: center;
  justify-content: flex-end; /* 将内容推向右侧 */
  margin-left: auto; /* 将用户信息推向顶部栏的右侧 */
  padding-right: 20px; /* 根据需要可能要调整右内边距 */
}

.infoCls {
  margin-left: 20px; /* 为链接之间添加间隔 */
  color: #fff; /* 白色文本 */
  cursor: pointer;
  text-decoration: none; /* 移除下划线 */
  transition: color 0.3s;
}


/* 用户信息和操作链接的鼠标悬浮效果 */
.user-info .infoCls:hover {
  color: #555; /* 淡白色 */
}

/* 操作链接的下划线效果 */
.user-info .infoCls::after {
  content: '';
  display: block;
  width: 0;
  height: 2px;
  background-color: #fff; /* 白色下划线 */
  transition: width 0.3s;
}

/* 用户信息和操作链接悬浮时的下划线效果 */
.user-info .infoCls:hover::after {
  width: 100%;
}

/* 其他样式... */
</style>



