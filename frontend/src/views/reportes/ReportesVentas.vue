<template>
  <div class="max-w-6xl mx-auto p-6 bg-white rounded-xl shadow">
    <h2 class="text-2xl font-bold mb-6 text-center">Reporte de Ventas</h2>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
      <div>
        <label class="font-medium block mb-1">Fecha inicio</label>
        <DatePicker
          v-model="fechaInicio"
          :manual-input="false"
          :format="'yyyy-MM-dd'"
          placeholder="Seleccione una fecha"
          input-class="w-full"
          class="w-full"
        />
      </div>
      <div>
        <label class="font-medium block mb-1">Fecha fin</label>
        <DatePicker
          v-model="fechaFin"
          :manual-input="false"
          :format="'yyyy-MM-dd'"
          placeholder="Seleccione una fecha"
          input-class="w-full"
          class="w-full"
        />
      </div>
    </div>

    <Button
      label="Buscar"
      icon="pi pi-search"
      class="mb-4"
      @click="consultarVentas"
    />

    <DataTable
      :value="ventas"
      class="p-datatable-sm"
      responsive-layout="scroll"
      :show-gridlines="false"
      show-footer
    >
      <Column field="fecha_venta" header="Fecha" />
      <Column field="monto_venta" header="Monto" />
      <Column field="descripcion" header="Descripción" />
      <Column field="pagado_deuna" header="Pagado Deuna">
        <template #body="slotProps">
          <span
            class="font-semibold"
            :class="slotProps.data.pagado_deuna ? 'text-green-600' : 'text-red-500'"
          >
            {{ slotProps.data.pagado_deuna ? '✔ Sí' : '✘ No' }}
          </span>
        </template>
      </Column>

      <template #footer>
        <tr>
          <td class="text-right font-bold pr-2" colspan="1"><b>Total:</b></td>
          <td class="font-bold text-green-700">
            <b>${{ totalVentas.toFixed(2) }}</b>
          </td>
          <td colspan="2"></td>
        </tr>
      </template>
    </DataTable>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue'
import api from '@/services/api'

interface Venta {
  fecha_venta: string
  monto_venta: number
  descripcion: string
  pagado_deuna: boolean
}

const hoy = new Date()
const fechaInicio = ref<Date | null>(hoy)
const fechaFin = ref<Date | null>(hoy)

const ventas = ref<Venta[]>([])
const totalVentas = ref<number>(0)

const consultarVentas = async () => {
  if (!fechaInicio.value || !fechaFin.value) return

  const desde = fechaInicio.value.toISOString().split('T')[0]
  const hasta = fechaFin.value.toISOString().split('T')[0]

  try {
    const response = await api.get('ventas_ai/ventas/', {
      params: { desde, hasta }
    })
    ventas.value = response.data.ventas
    totalVentas.value = response.data.total
  } catch (err) {
    console.error('Error consultando ventas:', err)
  }
}

onMounted(() => {
  consultarVentas()
})
</script>

<style scoped>
.grid > div {
  margin-bottom: 1rem;
}

.mb-4 {
  margin-bottom: 1.5rem;
}

.p-datatable {
  margin-top: 1.5rem;
}
</style>
