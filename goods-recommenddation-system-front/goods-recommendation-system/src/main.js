import { createApp } from 'vue'
// import './style.css'
import App from './App.vue'
import {createPinia} from 'pinia'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'

import vue3videoPlay from 'vue3-video-play'
// import 'vue-video-play/dist/style.css'
import router from './router'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

import './assets/main.css'

import './assets/css/main.css'

// createApp(App).mount('#app')
const app = createApp(App)

for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}
const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)
app.use(pinia)
app.use(router)
app.use(ElementPlus)
app.use(vue3videoPlay)
app.mount('#app')