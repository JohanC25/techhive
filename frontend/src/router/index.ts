import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import Login from '@/views/Login.vue'
import DashboardAdmin from '@/views/DashboardAdmin.vue'
import DashboardTecnico from '@/views/DashboardTecnico.vue'
import DashboardCliente from '@/views/DashboardCliente.vue'

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', name: 'Login', component: Login },

  { path: '/dashboard/admin', name: 'DashboardAdmin', component: DashboardAdmin },
  { path: '/dashboard/tecnico', name: 'DashboardTecnico', component: DashboardTecnico },
  { path: '/dashboard/cliente', name: 'DashboardCliente', component: DashboardCliente },

  { path: '/:pathMatch(.*)*', redirect: '/login' }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  const store = useAuthStore()

  if (!store.token && to.name !== 'Login') {
    return next({ name: 'Login' })
  }

  if (to.name === 'Login' && store.token) {
    if (store.role === 'admin') return next({ name: 'DashboardAdmin' })
    if (store.role === 'tecnico') return next({ name: 'DashboardTecnico' })
    if (store.role === 'cliente') return next({ name: 'DashboardCliente' })
  }

  if (to.name?.toString().startsWith('Dashboard')) {
    if (store.role === 'admin' && to.name !== 'DashboardAdmin') return next({ name: 'DashboardAdmin' })
    if (store.role === 'tecnico' && to.name !== 'DashboardTecnico') return next({ name: 'DashboardTecnico' })
    if (store.role === 'cliente' && to.name !== 'DashboardCliente') return next({ name: 'DashboardCliente' })
  }

  return next()
})

export default router
