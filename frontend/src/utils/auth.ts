export function isAuthenticated(): boolean {
  const token = localStorage.getItem('access')
  if (!token) return false
  try {
      const payload = JSON.parse(atob(token.split('.')[1]))
      const exp = payload.exp
      const now = Math.floor(Date.now() / 1000)
      return exp && exp > now
  } catch {
      return false
  }
}

export function getUserRole(): string | null {
  const token = localStorage.getItem('access')
  if (!token) return null
  try {
      const payload = JSON.parse(atob(token.split('.')[1]))
      return payload.rol || null
  } catch {
      return null
  }
}

export function logout(): void {
  localStorage.removeItem('access')
  localStorage.removeItem('refresh')
}
