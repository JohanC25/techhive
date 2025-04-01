import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: localStorage.getItem('access') || null,
    refresh: localStorage.getItem('refresh') || null,
    role: localStorage.getItem('rol') || null,
  }),
  actions: {
    login(data: any) {
      this.token = data.access
      this.refresh = data.refresh
      this.role = data.rol
      localStorage.setItem('access', data.access)
      localStorage.setItem('refresh', data.refresh)
      localStorage.setItem('rol', data.rol)
    },
    logout() {
      this.token = null
      this.refresh = null
      this.role = null
      localStorage.removeItem('access')
      localStorage.removeItem('refresh')
      localStorage.removeItem('rol')
    },
  },
})
