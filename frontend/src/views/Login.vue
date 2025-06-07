<template>
  <div class="login-page">
    <div class="login-container">
      <h1 class="title">
        Bienvenidos a <span>TechHive</span><br />
        by Magic World Computers
      </h1>
      <img src="@/assets/logoTechHive.png" alt="Logo TechHive" class="logo" />

      <div class="form-wrapper">
        <form @submit.prevent="handleLogin" class="login-form">
          <h2>Iniciar sesión</h2>
          <input v-model="email" type="email" placeholder="Correo electrónico" required />
          <input v-model="password" type="password" placeholder="Contraseña" required />

          <!--<label class="remember">
            <input type="checkbox" v-model="rememberMe" />
            Mantenerme conectado
          </label>-->

          <button type="submit" :disabled="loading">
            <span v-if="loading">🔄 Cargando...</span>
            <span v-else>Entrar</span>
          </button>
          <p v-if="error" class="error">{{ error }}</p>
        </form>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import api from '@/services/api'
import { useAuthStore } from '@/stores/auth'
import Swal from 'sweetalert2'

export default {
  setup() {
    const email = ref('')
    const password = ref('')
    const error = ref('')
    const router = useRouter()
    const rememberMe = ref(false)
    const loading = ref(false)
    const store = useAuthStore()

    const handleLogin = async () => {
      loading.value = true
      try {
        const response = await api.post('/users/login/', {
          email: email.value,
          password: password.value
        })

        store.login(response.data)

        if (!rememberMe.value) {
          localStorage.removeItem('refresh')
        }

        if (store.role === 'admin') router.push('/dashboard/admin')
        else if (store.role === 'tecnico') router.push('/dashboard/tecnico')
        else if (store.role === 'cliente') router.push('/dashboard/cliente')
        else throw new Error('Rol no permitido')

      } catch (err) {
        Swal.fire({
          icon: 'error',
          title: 'Error',
          text: 'Correo o contraseña inválidos',
          confirmButtonColor: '#646cff'
        })
      } finally {
        loading.value = false
      }
    }

    return { email, password, error, router, rememberMe, loading, handleLogin }
  }
}
</script>

<style scoped>
/* Aqui va el mismo style que ya tenías */
.login-page {
  height: 100vh;
  background-color: var(--bg-color);
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 1rem;
}

.login-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.5rem;
  width: 100%;
}

.title {
  text-align: center;
  color: var(--text-color);
  font-size: 1.4rem;
  line-height: 1.6;
  margin: 0;
}

.title span {
  color: #646cff;
  font-weight: bold;
}

.logo {
  width: 120px;
  height: auto;
  margin-bottom: 0.5rem;
}

.form-wrapper {
  background-color: var(--form-bg);
  padding: 2.5rem 3rem;
  border-radius: 24px;
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.25);
  width: 100%;
  max-width: 400px;
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.login-form h2 {
  margin: 0 0 1rem;
  text-align: center;
  color: var(--text-color);
}

input {
  padding: 0.8rem;
  border: 1px solid var(--input-border);
  border-radius: 6px;
  background-color: var(--input-bg);
  color: var(--text-color);
}

input::placeholder {
  color: var(--placeholder-color);
}

button {
  background-color: #646cff;
  color: white;
  border: none;
  padding: 0.8rem;
  border-radius: 6px;
  cursor: pointer;
  font-weight: bold;
  transition: background-color 0.3s ease;
}

button[disabled] {
  opacity: 0.6;
  cursor: not-allowed;
}

button:hover:not([disabled]) {
  background-color: #535bf2;
}

.error {
  color: red;
  font-size: 0.9rem;
  text-align: center;
}

@media (max-width: 480px) {
  .title {
    font-size: 1.1rem;
  }

  .logo {
    width: 80px;
  }

  .form-wrapper {
    padding: 1.5rem;
    border-radius: 16px;
  }

  input, button {
    font-size: 0.95rem;
  }
}
</style>
