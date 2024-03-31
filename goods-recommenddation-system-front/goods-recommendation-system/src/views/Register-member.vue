<script setup>
import { reactive, ref} from "vue"
import { User, Lock, Message } from '@element-plus/icons-vue'
import request from "@/utils/request";
import {ElMessage} from "element-plus";
import router from "@/router";
import config from "../../config";

  const loginData = reactive({})
  const rules = reactive({
    username: [
      { required: true, message: '请输入登录账户', trigger: 'blur' },
    ],
    email: [
      { required: true, message: '请输入邮箱', trigger: 'blur' },
    ],
    password: [
      { required: true, message: '请输入密码', trigger: 'blur' },
      { min: 3, max: 20, message: '密码长度在3-20位之间', trigger: 'blur' },
    ],
    confirmPassword: [
      { required: true, message: '请确认密码', trigger: 'blur' },
      { min: 3, max: 20, message: '密码长度在3-20位之间', trigger: 'blur' },
    ],
  })
  const ruleFormRef = ref()
  const register = () => {
    ruleFormRef.value.validate(valid => {
      if (valid) {
        if (loginData.password !== loginData.confirmPassword) {
          ElMessage.warning('两次密码不一致')
        }
		loginData.role = 'MEMBER'
        // 发送表单数据给后台
        request.post('/user/register', loginData).then(res => {
          if (res.code === '200') {
            ElMessage.success('注册成功')
            router.push('/login')
          } else {
            ElMessage.error(res.msg)
          }
        })
      }
    })
  }

</script>

<!-- <template>
  <div class="wrapper">
    <div style="margin: 100px auto; background-color: #F0F8FF; width: 500px; height: 600px; padding: 20px;">
      <div style="margin: 20px 0; text-align: center; font-size: 24px;color: black;"><b>{{config.projectName}} | 用户注册</b></div>
      <el-form
              ref="ruleFormRef"
              :model="loginData"
              :rules="rules"
              size="large"
              status-icon
      >
        <el-form-item prop="username">
          <span style="color: black;">请输入登录账户：</span>
          <el-input v-model="loginData.username" placeholder="请输入登录账户"  />
        </el-form-item>
        <el-form-item prop="email">
          <span style="color: black;">请输入邮箱：</span>
          <el-input v-model="loginData.email" placeholder="请输入邮箱"  />
        </el-form-item>
        <el-form-item prop="password">
          <span style="color: black;">请输入密码：</span>
          <el-input v-model="loginData.password" show-password placeholder="请输入密码" />
        </el-form-item>
        <el-form-item prop="confirmPassword">
          <span style="color: black;">请确认密码：</span>
          <el-input v-model="loginData.confirmPassword" show-password placeholder="请确认密码"/>
        </el-form-item>
        <el-form-item style="margin: 10px 0; text-align: right">
          <el-button class="button" type="primary" autocomplete="off" @click="register">注册</el-button>
          <el-button class="button" autocomplete="off" @click="router.push('/login')">登录</el-button>
        </el-form-item>
      </el-form>
        <div style="text-align: center;">
          <a style="text-decoration: none; color: black;margin-left: 20px;" href="/front/home">访问前台系统</a>
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

  .button {
    cursor: pointer;
    border-radius: 20px;
    width: 100px;
  }
</style> -->

<template>
  <div class="wrapper">
    <div class="form-container">
      <div class="form-header">
        <b>{{ config.projectName }} | 用户注册</b>
      </div>
      <el-form
        ref="ruleFormRef"
        :model="loginData"
        :rules="rules"
        size="large"
        status-icon
        class="form"
      >
        <el-form-item prop="username">
          <el-input v-model="loginData.username" prefix-icon="User" placeholder="登录账户" />
        </el-form-item>
        <el-form-item prop="email">
          <el-input v-model="loginData.email" prefix-icon="Message" placeholder="邮箱" />
        </el-form-item>
        <el-form-item prop="password">
          <el-input v-model="loginData.password" prefix-icon="Lock" show-password placeholder="密码" />
        </el-form-item>
        <el-form-item prop="confirmPassword">
          <el-input v-model="loginData.confirmPassword" prefix-icon="Lock" show-password placeholder="确认密码"/>
        </el-form-item>
        <el-form-item class="form-action">
          <el-button class="action-button register-button" type="primary" @click="register">注册</el-button>
          <el-button class="action-button login-button" @click="router.push('/login')">登录</el-button>
        </el-form-item>
      </el-form>
      <div class="form-footer">
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

.form-container {
  padding: 40px;
  max-width: 500px;
  background-color: #1c1c1e;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(255, 255, 255, 0.1);
}

.form-header {
  color: #fff;
  font-size: 24px;
  margin-bottom: 30px;
  text-align: center;
}

.el-form-item {
  margin-bottom: 24px;
}

.el-input__inner {
  background-color: rgba(255, 255, 255, 0.3);
  border: 1px solid #ddd;
  color: #000;
}

.el-input__prefix, .el-input__suffix {
  color: #8e8e93;
}

.el-button {
  border-radius: 8px;
  font-weight: bold;
  text-transform: uppercase;
  letter-spacing: 1px;
  transition: all 0.3s ease;
  color: #fff;
  margin-top: 10px; /* 按钮顶部的空间 */
  width: 100%; /* 按钮宽度 */
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  background-image: linear-gradient(145deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.2) 100%);
}

.el-button:hover {
  border-color: rgba(255, 255, 255, 0.6);
  background-image: linear-gradient(145deg, rgba(255, 255, 255, 0.2) 0%, rgba(255, 255, 255, 0.3) 100%);
  transform: translateY(-2px);
}

.el-button:active {
  transform: translateY(1px);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
}

.register-button {
  background-color: transparent; /* 透明背景 */
  border: 1px solid rgba(255, 255, 255, 0.4); /* 透明银色边框 */
}

.login-button {
  background-color: #007aff;
  color: #fff; /* 白色文本 */
}

.form-action {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 10px;
}

.action-button {
  flex: 1;
  margin: 0;
}

.form-footer {
  text-align: center;
  margin-top: 20px;
}

.action-link {
  color: #06c;
  text-decoration: none;
}

.action-link:hover {
  text-decoration: underline;
}

/* Styles for error state */
.el-form-item.is-error .el-input__inner {
  border-color: #ff3b30;
}

.el-form-item__error {
  color: #ff3b30;
}

</style>
