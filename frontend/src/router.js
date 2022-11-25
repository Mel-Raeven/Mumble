import {createRouter, createWebHashHistory} from 'vue-router'

import Authenticate from '@/views/AuthenticateView.vue';
import Dashboard from '@/views/DashboardView.vue'
import FriendRequest from '@/views/FriendrequestView.vue';

const routes = [
    {
        path: '/',
        redirect:'/Authenticate'
    },
    {
        path: '/Authenticate',
        component: Authenticate
    },
    {
      path: '/Dashboard',
      component: Dashboard
    },
    {
      path: '/FriendRequest',
      component: FriendRequest
    }
  ]

const router = createRouter({
    history: createWebHashHistory(),
    routes,
  });

  router.beforeEach((to, from, next) => {
    const publicPages = ['/Authenticate'];
    const authRequired = !publicPages.includes(to.path);
    const loggedIn = localStorage.getItem('token');
  
    if (authRequired && !loggedIn) {
      return next('/Authenticate');
    }
  
    next();
  })

export default router;