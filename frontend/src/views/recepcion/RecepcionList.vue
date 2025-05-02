<template>
  <div class="card">
    <h2>Listado de Recepciones</h2>

    <Button label="Nueva Recepción" icon="pi pi-plus" class="mb-3" @click="goToForm" />

    <DataTable :value="equipos" stripedRows responsiveLayout="scroll">
      <Column header="Cliente">
        <template #body="slotProps">
          {{ slotProps.data.cliente.nombre }} {{ slotProps.data.cliente.apellido }}
        </template>
      </Column>

      <Column header="Equipo">
        <template #body="slotProps">
          {{ slotProps.data.equipo.marca }} {{ slotProps.data.equipo.modelo }}
        </template>
      </Column>
      <Column field="diagnostico" header="Diagnóstico" />
      <Column field="estado" header="Estado" />

      <Column header="Precio (USD)">
        <template #body="slotProps">
          ${{ parseFloat(slotProps.data.costo).toFixed(2) }}
        </template>
      </Column>

      <Column header="Opciones">
        <template #body="slotProps">
          <div class="flex gap-2">
            <Button icon="pi pi-eye" severity="info" @click="verRecepcion(slotProps.data.id)" />
            <Button icon="pi pi-pencil" severity="warning" @click="editarRecepcion(slotProps.data.id)" />
            <Button icon="pi pi-trash" severity="danger" @click="borrarRecepcion(slotProps.data.id)" />
            <Button icon="pi pi-print" severity="secondary" @click="abrirDialogoImpresion(slotProps.data.id)" />
          </div>
        </template>
      </Column>
    </DataTable>

    <!-- Diálogo de impresión -->
    <SeleccionFormatoDialog
      v-model:visible="mostrarDialogoFormato"
      @seleccionado="formatoSeleccionado"
      @cancelar="mostrarDialogoFormato = false"
    />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import api from '@/services/api'
import SeleccionFormatoDialog from '@/components/SeleccionFormatoDialog.vue'
import Button from 'primevue/button'
import DataTable from 'primevue/datatable'
import Column from 'primevue/column'
import { useDescargarPDF } from '@/composables/useDescargarPDF'

const store = useAuthStore()
const router = useRouter()

interface Equipo {
  id: number
  cliente_nombre: string
  cliente_apellido: string
  equipo: number
  diagnostico: string
  estado: string
  costo: string | number
}

const equipos = ref<Equipo[]>([])
const mostrarDialogoFormato = ref(false)
const idSeleccionado = ref<number | null>(null)

const getEquipos = async () => {
  try {
    const { data } = await api.get('/recepcion/equipos/')
    //console.log("Equipos:", data.map((e: any) => e.equipo));
    equipos.value = data
  } catch (error) {
    console.error("Error al obtener recepciones:", error)
  }
}

const goToForm = () => router.push('/recepcion/nueva')
const verRecepcion = (id: number) => router.push(`/recepcion/ver/${id}`)
const editarRecepcion = (id: number) => router.push(`/recepcion/editar/${id}`)

const borrarRecepcion = async (id: number) => {
  if (confirm('¿Estás seguro de que deseas borrar esta recepción?')) {
    try {
      await api.delete(`/recepcion/equipos/${id}/`)
      getEquipos()
    } catch (error) {
      console.error("Error al borrar recepción:", error)
    }
  }
}

const abrirDialogoImpresion = (id: number) => {
  idSeleccionado.value = id
  mostrarDialogoFormato.value = true
}

const formatoSeleccionado = async (formato: string) => {
  if (!idSeleccionado.value) return
  try {
    const { data: recepcion } = await api.get(`/recepcion/equipos/${idSeleccionado.value}/`)
    console.log('Recepcion recibida:', recepcion)
    const cliente = recepcion.cliente
    const { descargar } = useDescargarPDF(recepcion, cliente)
    await descargar(formato as 'a4' | 'ticket')
    mostrarDialogoFormato.value = false
  } catch (error) {
    console.error("Error al obtener datos para descargar PDF:", error)
  }
}


onMounted(() => {
  if (!store.token) router.push('/login')
  else getEquipos()
})
</script>
