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
      <Column header="Acciones">
        <template #body="slotProps">
          <Button icon="pi pi-eye" class="p-button-text p-button-sm" @click="verVenta(slotProps.data)" />
          <Button icon="pi pi-pencil" class="p-button-text p-button-sm text-blue-600" @click="editarVenta(slotProps.data)" />
          <Button icon="pi pi-trash" class="p-button-text p-button-sm text-red-600" @click="confirmarEliminar(slotProps.data)" />
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
    <ConfirmDialog />
    <Toast />
  </div>
  <Dialog v-model:visible="mostrarDialogo" :header="modoEdicion ? 'Editar Venta' : 'Detalles de Venta'" modal class="w-full md:w-1/2">
    <div class="grid grid-cols-1 gap-4">
      <div>
        <label class="font-medium block mb-1">Fecha</label>
        <input type="date" v-model="ventaActual.fecha_venta" class="p-inputtext w-full" :readonly="!modoEdicion" />
      </div>
      <div>
        <label class="font-medium block mb-1">Monto</label>
        <input type="number" v-model="ventaActual.monto_venta" class="p-inputtext w-full" :readonly="!modoEdicion" />
      </div>
      <div>
        <label class="font-medium block mb-1">Descripción</label>
        <textarea v-model="ventaActual.descripcion" class="p-inputtext w-full" :readonly="!modoEdicion"></textarea>
      </div>
      <div>
        <label class="font-medium block mb-1">Pagado Deuna</label>
        <input type="checkbox" v-model="ventaActual.pagado_deuna" :disabled="!modoEdicion" />
      </div>
    </div>

    <template #footer>
      <Button label="Cerrar" icon="pi pi-times" @click="cerrarDialogo" class="p-button-text" />
      <Button v-if="modoEdicion" label="Guardar" icon="pi pi-check" @click="guardarEdicion" />
    </template>
  </Dialog>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue'
import api from '@/services/api'
import { useConfirm } from 'primevue/useconfirm'
import { useToast } from 'primevue/usetoast'

interface Venta {
  id: number
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
const confirm = useConfirm()
const toast = useToast()
const mostrarDialogo = ref(false)
const modoEdicion = ref(false)

const ventaActual = ref<Venta>({
  id: 0,
  fecha_venta: '',
  monto_venta: 0,
  descripcion: '',
  pagado_deuna: false
})

const verVenta = (venta: Venta) => {
  ventaActual.value = { ...venta }
  modoEdicion.value = false
  mostrarDialogo.value = true
}

const editarVenta = (venta: Venta) => {
  ventaActual.value = { ...venta }
  modoEdicion.value = true
  mostrarDialogo.value = true
}

const cerrarDialogo = () => {
  mostrarDialogo.value = false
}

const guardarEdicion = async () => {
  try {
    await api.put(`ventas_ai/ventas/${ventaActual.value.id}/`, ventaActual.value)
    toast.add({ severity: 'success', summary: 'Actualizado', detail: 'Venta actualizada', life: 3000 })
    mostrarDialogo.value = false
    consultarVentas()
  } catch (error) {
    toast.add({ severity: 'error', summary: 'Error', detail: 'No se pudo guardar', life: 3000 })
  }
}

const eliminarVenta = async (venta: Venta) => {
  try {
    await api.delete(`ventas_ai/ventas/${venta.id}/`)
    toast.add({ severity: 'success', summary: 'Eliminado', detail: 'Venta eliminada correctamente', life: 3000 })
    consultarVentas() // refrescar
  } catch (error) {
    toast.add({ severity: 'error', summary: 'Error', detail: 'No se pudo eliminar la venta', life: 3000 })
  }
}

const confirmarEliminar = (venta: Venta) => {
  confirm.require({
    message: '¿Está seguro que desea eliminar esta venta?',
    header: 'Confirmación',
    icon: 'pi pi-exclamation-triangle',
    acceptLabel: 'Sí',
    rejectLabel: 'No',
    accept: () => eliminarVenta(venta)
  })
}

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
