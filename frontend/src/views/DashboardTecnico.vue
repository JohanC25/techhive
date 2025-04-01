<script setup lang="ts">
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const store = useAuthStore()

const handleLogout = () => {
  store.logout()
  router.push('/login')
}
</script>

<template>
  <div>
    <h1>Dashboard Técnico</h1>
    <button @click="handleLogout">Cerrar sesión</button>
  </div>
</template>
