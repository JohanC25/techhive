import { defineStore } from 'pinia'
import { jwtDecode } from 'jwt-decode'

interface TokenPayload {
  user_id: number
  role: string
}

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: localStorage.getItem('access') || null,
    refresh: localStorage.getItem('refresh') || null,
    role: localStorage.getItem('rol') || null,
    user_id: localStorage.getItem('user_id') ? parseInt(localStorage.getItem('user_id')!) : null,
  }),
  actions: {
    login(data: any) {
      this.token = data.access
      this.refresh = data.refresh
      this.role = data.rol

      // ⚡️ Decodificamos el token para obtener user_id directamente
      const decoded = jwtDecode<TokenPayload>(data.access)
      this.user_id = decoded.user_id

      // Guardamos todo en localStorage
      localStorage.setItem('access', data.access)
      localStorage.setItem('refresh', data.refresh)
      localStorage.setItem('rol', data.rol)
      localStorage.setItem('user_id', decoded.user_id.toString())
    },
    logout() {
      this.token = null
      this.refresh = null
      this.role = null
      this.user_id = null

      // Limpiar storage
      localStorage.removeItem('access')
      localStorage.removeItem('refresh')
      localStorage.removeItem('rol')
      localStorage.removeItem('user_id')
    },
  },
})
