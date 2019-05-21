import Vue from 'vue'
import './plugins/vuetify'
import './plugins/base'
import App from './App.vue'
import CKEditor from '@ckeditor/ckeditor5-vue';
import router from './router'
import store from './store'


Vue.config.productionTip = false
Vue.use(CKEditor);

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
