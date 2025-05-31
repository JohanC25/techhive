<template>
  <div class="max-w-md mx-auto bg-white p-6 rounded-xl shadow-md">
    <h2 class="text-2xl font-bold text-center mb-6">Registrar Venta</h2>

    <!-- Formulario -->
    <form @submit.prevent="registrarVenta">
      <div class="mb-4">
        <label class="block font-medium mb-1">Fecha de venta: </label>
        <DatePicker
          v-model="form.fecha_venta"
          :format="'yyyy-MM-dd'"
          :manual-input="false"
          class="w-full"
          input-class="w-full"
          required
        />
      </div>

      <div class="mb-4">
        <label class="block font-medium mb-1">Monto vendido: </label>
        <InputNumber
          v-model="form.monto_venta"
          mode="currency"
          currency="USD"
          locale="en-US"
          class="w-full"
          input-class="w-full"
          required
        />
      </div>

      <div class="mb-4">
        <label class="block font-medium mb-1">Descripción: </label>
        <InputText
          v-model="form.descripcion"
          class="w-full"
          required
        />
      </div>

      <Button label="Guardar Venta" icon="pi pi-save" class="w-full mb-2" type="submit" />
      <p v-if="mensaje" class="text-green-600 text-center">{{ mensaje }}</p>
    </form>

    <!-- Tabla -->
    <div class="mt-8">
      <h3 class="text-xl font-semibold mb-3 text-center">Ventas registradas</h3>

      <p v-if="ventas.length === 0" class="text-gray-600 italic text-center">
        No existen registros para hoy.
      </p>

      <DataTable
        v-else
        :value="ventas"
        responsive-layout="scroll"
        class="p-datatable-sm"
      >
        <Column field="fecha_venta" header="Fecha" />
        <Column field="monto_venta" header="Monto" :body="montoBodyTemplate" />
        <Column field="descripcion" header="Descripción" />
      </DataTable>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue'
import api from '@/services/api'

interface Venta {
  id: number
  fecha_venta: string
  monto_venta: number
  descripcion: string
}

const form = ref({
  fecha_venta: new Date(),
  monto_venta: 0,
  descripcion: '',
})

const mensaje = ref('')
const ventas = ref<Venta[]>([])

const obtenerVentas = async () => {
  try {
    const now = new Date();
    const hoy =
      now.getFullYear() +
      '-' +
      String(now.getMonth() + 1).padStart(2, '0') +
      '-' +
      String(now.getDate()).padStart(2, '0');
    const response = await api.get('ventas_ai/ventas/', { params: { fecha: hoy } })
    console.log('Fecha enviada:', hoy)
    console.log('Ventas recibidas:', response.data)
    ventas.value = response.data
  } catch (error) {
    console.error('Error al cargar las ventas:', error)
  }
}

const registrarVenta = async () => {
  try {
    const payload = {
      ...form.value,
      fecha_venta: form.value.fecha_venta.toISOString().split('T')[0],
    }
    await api.post('ventas_ai/ventas/', payload)
    mensaje.value = 'Venta registrada correctamente'
    form.value = { fecha_venta: new Date(), monto_venta: 0, descripcion: '' }
    await obtenerVentas()
  } catch (error) {
    console.error('Error al registrar la venta:', error)
    mensaje.value = 'Hubo un error al registrar la venta'
  }
}

const montoBodyTemplate = (row: Venta) => {
  return `$${row.monto_venta.toFixed(2)}`
}

onMounted(() => {
  obtenerVentas()
})
</script>
<style scoped>
form > div {
  margin-bottom: 1.25rem; /* equivalente a mb-5 */
}

form .p-inputtext,
form .p-inputnumber,
form .p-datepicker {
  width: 30%;
}

.p-button {
  margin-bottom: 0.75rem;
}
</style>
