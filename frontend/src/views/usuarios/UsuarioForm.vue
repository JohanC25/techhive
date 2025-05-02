<template>
    <div class="p-4 max-w-xl mx-auto">
      <h2 class="text-xl font-bold mb-4">{{ modo === 'crear' ? 'Crear Usuario' : 'Editar Usuario' }}</h2>
  
      <form @submit.prevent="handleSubmit">
        <div class="form-group">
          <label>Cédula:</label>
          <input v-model="form.cedula" class="form-input" required />
        </div>
  
        <div class="form-group">
          <label>Nombre:</label>
          <input v-model="form.nombre" class="form-input" required />
        </div>
  
        <div class="form-group">
          <label>Apellido:</label>
          <input v-model="form.apellido" class="form-input" required />
        </div>
  
        <div class="form-group">
          <label>Email:</label>
          <input v-model="form.email" type="email" class="form-input" required />
        </div>
  
        <div class="form-group">
          <label>Celular:</label>
          <input v-model="form.celular" class="form-input" required />
        </div>
  
        <div class="form-group">
          <label>Convencional:</label>
          <input v-model="form.convencional" class="form-input" />
        </div>
  
        <div class="form-group" v-if="modo === 'crear'">
          <label>Contraseña:</label>
          <input v-model="form.password" type="password" class="form-input" required />
        </div>
  
        <div class="form-group" v-if="esAdmin">
          <label>Rol:</label>
          <select v-model="form.rol" class="form-input">
            <option value="cliente">Cliente</option>
            <option value="tecnico">Técnico</option>
          </select>
        </div>
  
        <button type="submit" class="form-button">{{ modo === 'crear' ? 'Crear' : 'Actualizar' }}</button>
      </form>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref, onMounted } from 'vue'
  import { useRoute, useRouter } from 'vue-router'
  import api from '@/services/api'
  import { useAuthStore } from '@/stores/auth'
  
  const props = defineProps({ modo: String })
  const route = useRoute()
  const router = useRouter()
  const auth = useAuthStore()
  const esAdmin = auth.role === 'admin'
  
  const form = ref({
    cedula: '', nombre: '', apellido: '', celular: '', convencional: '', email: '', password: '', rol: 'cliente'
  })
  
  onMounted(async () => {
    if (props.modo === 'editar') {
      const { data } = await api.get(`/users/${route.params.id}/`)
      form.value = data
    }
  })
  
  const handleSubmit = async () => {
    if (props.modo === 'crear') {
      await api.post('/users/', form.value)
    } else {
      await api.put(`/users/${route.params.id}/`, form.value)
    }
    router.push('/usuarios')
  }
  </script>
  
  <style scoped>
  .form-group {
    display: flex;
    flex-direction: column;
    margin-bottom: 1rem;
  }
  .form-input {
    padding: 0.5rem;
    border: 1px solid #555;
    border-radius: 6px;
    background-color: #222;
    color: #fff;
  }
  .form-button {
    margin-top: 1rem;
    background-color: #646cff;
    color: white;
    padding: 0.6rem 1.2rem;
    border: none;
    border-radius: 6px;
    cursor: pointer;
  }
  .form-button:hover {
    background-color: #535bf2;
  }
  </style>