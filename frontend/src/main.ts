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
import InputText from 'primevue/inputtext'
import InputNumber from 'primevue/inputnumber'
import DatePicker from 'primevue/datepicker'
import Checkbox from 'primevue/checkbox'
import CheckboxGroup from 'primevue/checkboxgroup'
import Dialog from 'primevue/dialog'
import ConfirmDialog from 'primevue/confirmdialog'
import ToastService from 'primevue/toastservice'
import ConfirmationService from 'primevue/confirmationservice'
import Toast from 'primevue/toast'

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
app.component('InputText', InputText)
app.component('InputNumber', InputNumber)
app.component('DatePicker', DatePicker)
app.component('Checkbox', Checkbox)
app.component('CheckboxGroup', CheckboxGroup)
app.use(ToastService)
app.use(ConfirmationService)
app.component('ConfirmDialog', ConfirmDialog)
app.component('Toast', Toast)
app.component('Dialog', Dialog)

// Montar app
app.mount('#app')
