<template>
  <Menubar :model="items" class="mb-4">
    <template #start>
      <h2>TechHive</h2>
    </template>
  </Menubar>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'
import Menubar from 'primevue/menubar'

const store = useAuthStore()
const router = useRouter()

const items = computed(() => {
  if (!store.role) return []

  switch (store.role) {
    case 'admin':
      return [
        { label: 'Recepción', icon: 'pi pi-inbox', command: () => router.push('/recepcion') },
        { label: 'Usuarios', icon: 'pi pi-users', command: () => router.push('/usuarios') },
        { label: 'Inventario', icon: 'pi pi-box', command: () => router.push('/inventario') },
        { label: 'Reportes', icon: 'pi pi-chart-line', command: () => router.push('/reportes') },
        { label: 'Ventas AI', icon: 'pi pi-dollar', command: () => router.push('/ventas-ai') },
        { label: 'Cerrar Sesión', icon: 'pi pi-sign-out', command: () => logout() },
      ]
    case 'tecnico':
      return [
        { label: 'Recepción', icon: 'pi pi-inbox', command: () => router.push('/recepcion') },
        { label: 'Mis Reparaciones', icon: 'pi pi-wrench', command: () => router.push('/reparaciones') },
        { label: 'Ventas AI', icon: 'pi pi-dollar', command: () => router.push('/ventas-ai') },
        { label: 'Reportes', icon: 'pi pi-chart-line', command: () => router.push('/reportes') },
        { label: 'Perfil', icon: 'pi pi-user', command: () => router.push('/perfil') },
        { label: 'Cerrar Sesión', icon: 'pi pi-sign-out', command: () => logout() },
      ]
    case 'cliente':
      return [
        { label: 'Mis Equipos', icon: 'pi pi-desktop', command: () => router.push('/equipos') },
        { label: 'Perfil', icon: 'pi pi-user', command: () => router.push('/perfil') },
        { label: 'Cerrar Sesión', icon: 'pi pi-sign-out', command: () => logout() },
      ]
    default:
      return []
  }
})

function logout() {
  store.logout()
  router.push('/login')
}
</script>

<style scoped>
h2 {
  margin-left: 1rem;
  color: var(--text-color);
}
</style>
