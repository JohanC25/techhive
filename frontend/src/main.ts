import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'

// ✅ PrimeVue
import PrimeVue from 'primevue/config'
import Aura from '@primeuix/themes/aura'
import 'primeicons/primeicons.css'
import Button from 'primevue/button'
import DataTable from 'primevue/datatable'
import Column from 'primevue/column'

// ✅ Pinia
import { createPinia } from 'pinia'

// Crear app
const app = createApp(App)

// Configurar PrimeVue + Tema
app.use(PrimeVue, {
    theme: {
        preset: Aura
    }
})

// Configurar Pinia y Router
const pinia = createPinia()
app.use(pinia)
app.use(router)
app.component('Button', Button)
app.component('DataTable', DataTable)
app.component('Column', Column)

// Montar app
app.mount('#app')
