import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

// Layout
import AdminLayout from '@/layouts/AdminLayout.vue'

// Vistas principales
import Login from '@/views/Login.vue'
import DashboardAdmin from '@/views/DashboardAdmin.vue'
import DashboardTecnico from '@/views/DashboardTecnico.vue'
import DashboardCliente from '@/views/DashboardCliente.vue'

// Recepción
import RecepcionList from '@/views/recepcion/RecepcionList.vue'
import RecepcionForm from '@/views/recepcion/RecepcionForm.vue'

// Usuarios (nuevas vistas)
import UsuarioList from '@/views/usuarios/UsuarioList.vue'
import UsuarioCreate from '@/views/usuarios/UsuarioCreate.vue'
import UsuarioEdit from '@/views/usuarios/UsuarioEdit.vue'


import RegistroVenta from '@/views/ventas_ia/RegistroVenta.vue'


const routes = [
  { path: '/login', name: 'Login', component: Login },

  {
    path: '/',
    component: AdminLayout,
    children: [
      { path: 'dashboard/admin', name: 'DashboardAdmin', component: DashboardAdmin },
      { path: 'dashboard/tecnico', name: 'DashboardTecnico', component: DashboardTecnico },
      { path: 'dashboard/cliente', name: 'DashboardCliente', component: DashboardCliente },

      // Recepción
      { path: 'recepcion', name: 'RecepcionList', component: RecepcionList },
      { path: 'recepcion/nueva', name: 'RecepcionForm', component: RecepcionForm },

      // Usuarios (CRUD)
      { path: 'usuarios', name: 'UsuarioList', component: UsuarioList },
      { path: 'usuarios/nuevo', name: 'UsuarioCreate', component: UsuarioCreate },
      { path: 'usuarios/editar/:id', name: 'UsuarioEdit', component: UsuarioEdit, props: true },

      // Ventas AI
      { path: 'ventas-ai', name: 'VentasAI', component: RegistroVenta },
    ]
  },

  { path: '/', redirect: '/login' },
  { path: '/:pathMatch(.*)*', redirect: '/login' },
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

  if (to.path.startsWith('/dashboard')) {
    if (store.role === 'admin' && to.name !== 'DashboardAdmin') return next({ name: 'DashboardAdmin' })
    if (store.role === 'tecnico' && to.name !== 'DashboardTecnico') return next({ name: 'DashboardTecnico' })
    if (store.role === 'cliente' && to.name !== 'DashboardCliente') return next({ name: 'DashboardCliente' })
  }

  return next()
})

export default router
