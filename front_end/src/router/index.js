import { createRouter, createWebHistory } from 'vue-router'
import HelloView from '../views/HelloView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HelloView
    },
    {
      path: '/skillsdomains',
      name: 'skillsdomains',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/SkillsDomainsView.vue')
    },
    {
      path: '/fighters',
      name: 'fighters',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/FightersView.vue')
    },
    {
      path: '/tournaments',
      name: 'tournaments',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/TournamentsView.vue')
    }
  ]
})

export default router
