import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ConseilsView from '../views/ConseilsView.vue'
import ConseilsDetailsView  from '../views/ConseilsDetailsView.vue'
import SportCategorie from '../views/SportCategorie.vue'
import SportDetails from '../views/SportDetails.vue'
import ProfileView from '../views/ProfileView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/conseils',
    name: 'conseils',
    component: ConseilsView
  },
  {
    path: '/conseils_details',
    name: 'conseilsdetails',
    component: ConseilsDetailsView
  },
  {
    path: '/sport',
    name: 'sport',
    component: SportCategorie
  },
  {
    path: '/sport_details',
    name: 'sportdetails',
    component: SportDetails
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
