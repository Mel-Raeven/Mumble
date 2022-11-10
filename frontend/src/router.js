import {createRouter, createWebHashHistory} from 'vue-router'

import Authenticate from '@/views/AuthenticateView.vue';


const routes = [
    {
        path: '/',
        redirect:'/Authenticate'
    },
    {
        path: '/Authenticate',
        component: Authenticate
    }
  ]

const router = createRouter({
    history: createWebHashHistory(),
    routes,
  });

  router.beforeEach((to, from, next) => {
    // redirect to login page if not logged in and trying to access a restricted page
    const publicPages = ['/Authenticate'];
    const authRequired = !publicPages.includes(to.path);
    const loggedIn = localStorage.getItem('user');
  
    if (authRequired && !loggedIn) {
      return next('/Authenticate');
    }
  
    next();
  })

export default router;