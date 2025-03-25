<script setup lang="ts">
import { onMounted, ref } from 'vue'
import api from '@/services/api'

const mensaje = ref('Cargando...')

onMounted(async () => {
  try {
    const res = await api.get('/core/hello/')  // endpoint de prueba en Django
    mensaje.value = res.data.message
  } catch (error) {
    mensaje.value = 'Error al conectar con Django 😢'
    console.error(error)
  }
})
</script>

<template>
  <div>
    <h1>{{ mensaje }}</h1>
  </div>
</template>
