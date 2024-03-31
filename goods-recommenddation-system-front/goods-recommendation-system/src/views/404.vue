<!-- <template>
    <div style="text-align: center">
      <h1 style="font-size: 150px">404</h1>
      <h2>未找到页面</h2>
      <a href="/">返回主页</a>
    </div>
  </template> -->
  
<template>
  <div class="not-found-container">
    <h1 class="error-code">404</h1>
    <h2 class="error-message">未找到页面</h2>
    <a href="/" class="home-link">返回主页</a>
  </div>
</template>

<style scoped>
.not-found-container {
  text-align: center;
  padding-top: 100px;
  padding-bottom: 100px;
  background-color: #f7f7f8; /* 轻灰色背景，增加对比 */
}

.error-code {
  font-size: 150px;
  font-weight: bold;
  color: #a2a2a2; /* 淡灰色，减少视觉冲击 */
}

.error-message {
  font-size: 24px;
  color: #606060; /* 较深的灰色，保持可读性 */
}

.home-link {
  display: inline-block;
  margin-top: 20px;
  font-size: 16px;
  color: #007aff; /* Apple蓝 */
  text-decoration: none;
  padding: 10px 20px;
  border: 1px solid #007aff; /* 边框颜色 */
  border-radius: 20px; /* 圆角边框 */
  transition: background-color 0.3s, color 0.3s;
}

.home-link:hover {
  background-color: #007aff;
  color: #ffffff; /* 鼠标悬浮时的样式变化 */
}
</style>
