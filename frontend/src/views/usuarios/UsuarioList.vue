<template>
    <div class="p-4">
      <h2 class="text-xl font-bold mb-4">Lista de Usuarios</h2>
      <router-link to="/usuarios/nuevo" class="form-button">+ Crear nuevo</router-link>
  
      <table class="table-auto w-full mt-4">
        <thead>
          <tr>
            <th class="px-4 py-2">Nombre</th>
            <th class="px-4 py-2">Rol</th>
            <th class="px-4 py-2">Email</th>
            <th class="px-4 py-2">Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="user in usuarios" :key="user.id">
            <td class="border px-4 py-2">{{ user.nombre }} {{ user.apellido }}</td>
            <td class="border px-4 py-2">{{ user.rol }}</td>
            <td class="border px-4 py-2">{{ user.email }}</td>
            <td class="border px-4 py-2">
              <router-link :to="`/usuarios/editar/${user.id}`" class="text-blue-500">Editar</router-link>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref, onMounted } from 'vue'
  import api from '@/services/api'
  
  const usuarios = ref<any[]>([])
  
  onMounted(async () => {
    const { data } = await api.get('/users/')
    usuarios.value = data
  })
  </script>