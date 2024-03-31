<script setup>
import {onMounted, reactive, ref, watch} from "vue"
import {User, Lock} from '@element-plus/icons-vue'
import request from "@/utils/request";
import {ElMessage} from "element-plus";
import {useUserStore} from "@/stores/user";
import router, {setRoutes} from "@/router";
// import SIdentify from '../components/SIdentify.vue';
import config from "../../config";

// 图形验证码
let identifyCodes = "1234567890"
let identifyCode = ref('')
const failCount = ref(0)
const randomNum = (min, max) => {
  return Math.floor(Math.random() * (max - min) + min)
}
const makeCode = (o, l) => {
  for (let i = 0; i < l; i++) {
    identifyCode.value += o[randomNum(0, o.length)];
  }
}
const refreshCode = () => {
  identifyCode.value = "";
  makeCode(identifyCodes, 4);
}
// 生成验证码
onMounted(() => {
  identifyCode.value = "";
  makeCode(identifyCodes, 4);
})

const loginData = reactive({})
const rules = reactive({
  username: [
    {required: true, message: '请输入账号', trigger: 'blur'},
  ],
  password: [
    {required: true, message: '请输入密码', trigger: 'blur'},
    {min: 3, max: 20, message: '密码长度在3-20位之间', trigger: 'blur'},
  ],
})
const ruleFormRef = ref()
const login = () => {
  ruleFormRef.value.validate(valid => {
    if (valid) {
      // 失败3次触发验证码
      if (failCount.value >= 3 && loginData.code !== identifyCode.value) {
        ElMessage.warning('验证码错误')
        return
      }
      // 发送表单数据给后台
      request.post('/user/login', loginData).then(res => {
        if (res.code === '200') {
          if (res.data.user.role === 'ADMIN') {
            router.push('/') // 后台的首页
          }
          		  else if(res.data.user.role === 'MEMBER'){
            router.push('/front') 
          }
          ElMessage.success('登录成功')
          const userStore = useUserStore()
          userStore.setManagerInfo(res.data)
        } else {
          ElMessage.error(res.msg)
          failCount.value ++  // 失败次数加1
        }
      })
    }
  })
}

</script>

<!-- <template>
  <div class="wrapper">
    <div style="margin: 150px auto; background-color: #F0F8FF; width: 500px; height: 400px; padding: 20px; cursor: pointer; border-radius: 20px;">
      <div style="margin: 20px 0; text-align: center; font-size: 24px;color: #000000;"><b>{{config.projectName}}</b></div>
      <el-form
              ref="ruleFormRef"
              :model="loginData"
              :rules="rules"
              size="large"
              status-icon
      >
        <el-form-item prop="username">
          <span style="color: #000000;">请输入账户：</span>
          <el-input size="medium" prefix-icon="User" v-model="loginData.username" placeholder="请输入账号"></el-input>
        </el-form-item>
        <el-form-item prop="password">
          <span style="color: #000000;">请输入密码：</span>
          <el-input size="medium" prefix-icon="Lock" show-password v-model="loginData.password" placeholder="请输入密码"></el-input>
        </el-form-item>
        <div style="display: flex; margin: 15px 0" v-if="failCount >= 3">
          <div style="flex: 1">
            <el-input v-model="loginData.code" placeholder="验证码"></el-input>
          </div>
          <div>
            <div @click="refreshCode" style="margin-left: 5px">
              <SIdentify :identifyCode="identifyCode" />
            </div>
          </div>
        </div>
        <el-form-item style="margin: 10px 0; text-align: right">
          <el-button class="login-button" type="primary" autocomplete="off" @click="login">登录</el-button>
          <el-button class="register-button" autocomplete="off" @click="router.push('/register-member')">用户注册</el-button>
        </el-form-item>
      </el-form>
        <div style="text-align: center;">
          <a style="text-decoration: none; color: #000000;margin-left: 20px;" href="/front/home">访问前台系统</a>
        </div>
    </div>
  </div>
</template> -->

<!-- <style>
  .wrapper {
    background-image: url("../assets/login-background.jpg");
    background-repeat: no-repeat;
    background-size: cover;
    height: 100vh;
    overflow: hidden;
    /* opacity: 0.6; */
  }

  .el-form-item.is-error .el-input__inner{
    border-color: #ffffff;
  }
  .el-form-item.is-error .el-input__validateIcon{
    color: #ffffff;
  }
  .el-form-item__error{
    color: #ffffff;
  }

  .register-button {
    cursor: pointer;
    border-radius: 20px;
    width: 100px;
  }

  .login-button {
    cursor: pointer;
    border-radius: 20px;
    width: 100px;
    background-color: #87CEEB;
  }
  
</style> -->

<template>
  <div class="wrapper">
    <div class="login-form-container">
      <div class="login-form-header">
        <b>{{ config.projectName }}</b>
      </div>
      <el-form
        ref="ruleFormRef"
        :model="loginData"
        :rules="rules"
        size="large"
        status-icon
        class="login-form"
      >
        <el-form-item prop="username">
          <el-input size="medium" prefix-icon="User" v-model="loginData.username" placeholder="账号"></el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input size="medium" prefix-icon="Lock" show-password v-model="loginData.password" placeholder="密码"></el-input>
        </el-form-item>
        <div class="identify-code-container" v-if="failCount >= 3">
          <el-input v-model="loginData.code" placeholder="验证码" class="identify-code-input"></el-input>
          <div class="identify-code-refresh" @click="refreshCode">
            <!-- SIdentify 组件需要确保样式正确 -->
            <SIdentify :identifyCode="identifyCode" />
          </div>
        </div>
        <el-form-item>
          <el-button class="action-button login-button" type="primary" @click="login">登录</el-button>
          <el-button class="action-button register-button" @click="router.push('/register-member')">注册</el-button>
        </el-form-item>
      </el-form>
      <div class="login-form-footer">
        <a class="action-link" href="/front/home">访问前台系统</a>
      </div>
    </div>
  </div>
</template>


<style>
.wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background: linear-gradient(135deg, #232526 0%, #414345 100%);
}

.login-form-container {
  padding: 40px;
  max-width: 400px;
  background-color: #1c1c1e; /* 略带渐变的暗色 */
  border-radius: 12px; /* 轻微的圆角 */
  box-shadow: 0 2px 8px rgba(255, 255, 255, 0.1); /* 微妙的外阴影 */
}

.login-form-header {
  color: #fff;
  font-size: 24px;
  margin-bottom: 40px; /* 增加了标题和表单之间的距离 */
  text-align: center;
}

.el-form-item {
  margin-bottom: 24px; /* 增加了表单项之间的间隔 */
}

.el-input__inner {
  background-color: rgba(255, 255, 255, 0.5); /* 半透明的白色背景 */
  border: 1px solid #ddd; /* 灰色边框 */
  color: #000; /* 文本颜色为黑色 */
}

.el-input__prefix, .el-input__suffix {
  color: #8e8e93; /* 图标使用更亮的灰色以区分 */
}

.el-button {
  /* 通用样式 */
  border-radius: 8px;
  font-weight: bold;
  padding: 10px 20px;
  text-transform: uppercase; /* 大写文本 */
  letter-spacing: 1px; /* 字母间距 */
  transition: all 0.3s ease;
  border: 1px solid rgba(255, 255, 255, 0.4); /* 透明银色边框 */
  color: #fff; /* 白色文本 */
  background-image: linear-gradient(145deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.2) 100%);
  /* 线性渐变背景 */
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2); /* 细微的阴影 */
}

.el-button:hover {
  border-color: rgba(255, 255, 255, 0.6); /* 鼠标悬浮时边框颜色加深 */
  background-image: linear-gradient(145deg, rgba(255, 255, 255, 0.2) 0%, rgba(255, 255, 255, 0.3) 100%);
  /* 鼠标悬浮时渐变背景加深 */
  transform: translateY(-2px); /* 微妙的向上移动效果 */
}

.el-button:active {
  transform: translateY(1px); /* 点击时微妙的向下移动效果 */
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15); /* 点击时阴影减小 */
}

.login-button {
  background-color: #007aff;
  color: #000;
  margin-right: 10px;
}

.register-button {
  background-color: #f5f5f7; /* 浅灰色按钮与登录按钮形成对比 */
  color: #1c1c1e; /* 深色文字 */
  margin-left: 10px; /* 与登录按钮的间隔 */
  background-color: transparent; /* 透明背景 */
}

.el-button:not(.is-disabled):hover {
  opacity: 0.9;
}

.action-link {
  color: #06c;
  text-decoration: none;
  margin-top: 16px; /* 链接距离表单项的间隔 */
  display: block; /* 链接占据一整行 */
  text-align: center;
}

.action-link:hover {
  text-decoration: underline;
}

.identify-code-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* 根据页面需要，可能还要对验证码组件进行样式调整 */

</style>