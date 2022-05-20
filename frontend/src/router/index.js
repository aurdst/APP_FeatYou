import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ConseilsView from '../views/ConseilsView.vue'
import ConseilsDetailsView  from '../views/ConseilsDetailsView.vue'
import SportCategorie from '../views/SportCategorie.vue'
import SportDetails from '../views/SportDetails.vue'
import ProfileView from '../views/ProfileView.vue'
import ConversationView from '../views/ConversationView.vue'
import InfosView from '../views/InfosView.vue'
import ConseilsNutri from '../views/ConseilsNutri.vue'
import ConseilsSport from '../views/ConseilsSport.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'

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
    path: '/sports',
    name: 'sports',
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
  {
    path: '/conversation',
    name: 'conversation',
    component: ConversationView
  },
  {
    path: '/conseils_nutri',
    name: 'conseils_nutri',
    component: ConseilsNutri
  },
  {
    path: '/conseils_sport',
    name: 'conseils_sport',
    component: ConseilsSport
  },
  {
    path: '/infos',
    name: 'infos',
    component: InfosView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/register',
    name: 'register',
    component: RegisterView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
