import { createApp } from 'vue'
import './assets/css/style.css'
import App from './App.vue'

import { createRouter, createWebHistory } from 'vue-router'
import routes from './router/routes.js'

const router = createRouter(
    {
        history: createWebHistory(),
        routes,
    }

)

const app = createApp(App)

app.use(router)
app.mount('#app')