import { createApp } from 'vue'
import VueCryptojs from 'vue-cryptojs'
import App from './App.vue'
import router from './router'

const app = createApp(App);

app.use(router);
app.use(VueCryptojs);
app.mount('#app')