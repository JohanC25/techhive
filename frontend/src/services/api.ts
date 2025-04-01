import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:8000/api',
  withCredentials: false,
  headers: {
    'Content-Type': 'application/json',
  },
})

// ✅ Inyectar access token automáticamente
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

// 🔁 Interceptar errores 401 y hacer refresh automáticamente
api.interceptors.response.use(
  response => response,
  async (error) => {
    const originalRequest = error.config

    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true
      const refreshToken = localStorage.getItem('refresh')

      if (refreshToken) {
        try {
          const res = await axios.post('http://localhost:8000/api/auth/refresh/', {
            refresh: refreshToken
          })

          const newAccess = res.data.access
          localStorage.setItem('access', newAccess)

          // Reintenta la petición original con el nuevo token
          originalRequest.headers.Authorization = `Bearer ${newAccess}`
          return api(originalRequest)
        } catch (refreshError) {
          // 🔒 Refresh falló → limpiar sesión y redirigir
          localStorage.removeItem('access')
          localStorage.removeItem('refresh')
          window.location.href = '/login'
        }
      } else {
        // 🚫 No hay refresh token → redirige al login
        localStorage.removeItem('access')
        window.location.href = '/login'
      }
    }

    return Promise.reject(error)
  }
)

export default api
