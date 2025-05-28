<template>
  <div class="form-wrapper">
    <h2 class="title">Recepción de Equipos</h2>

    <!-- Paso 1: Buscar cliente por cédula -->
    <div class="form-group">
      <label for="cedula">Cédula del cliente:</label>
      <input id="cedula" v-model="cedula" type="text" placeholder="Cédula del cliente" class="form-input" />
      <button @click="buscarCliente" class="form-button">Buscar</button>
    </div>

    <!-- Si el cliente no existe -->
    <div v-if="!cliente && mensaje">
      <p class="mensaje">{{ mensaje }}</p>
      <!-- Registro nuevo cliente -->
      <div class="form-group">
        <h4>Registrar nuevo cliente</h4>
        <label>Nombre:</label>
        <input v-model="nuevoCliente.nombre" class="form-input" placeholder="Nombre" />
        <label>Apellido:</label>
        <input v-model="nuevoCliente.apellido" class="form-input" placeholder="Apellido" />
        <label>Celular:</label>
        <input v-model="nuevoCliente.celular" class="form-input" placeholder="Celular" />
        <label>Convencional (OPCIONAL):</label>
        <input v-model="nuevoCliente.convencional" class="form-input" placeholder="Teléfono convencional (opcional)" />
        <label>Email:</label>
        <input v-model="nuevoCliente.email" type="email" class="form-input" placeholder="Correo electrónico" />
        <label>Contraseña:</label>
        <input v-model="nuevoCliente.password" type="password" class="form-input" placeholder="Contraseña" />
        <button class="form-button" @click="registrarCliente">Registrar Cliente</button>
      </div>
    </div>

    <!-- Si se encuentra cliente -->
    <div v-if="cliente">
      <p class="cliente-info"><strong>Cliente:</strong> {{ cliente.nombre }} {{ cliente.apellido }}</p>
      <div class="form-group">
        <label for="equipo">Equipo:</label>
        <select id="equipo" v-model="equipoSeleccionado" class="form-input">
          <option disabled value="">-- Selecciona un equipo --</option>
          <option v-for="equipo in equipos" :key="equipo.id" :value="equipo.id">
            {{ equipo.marca || 'Sin marca' }} - {{ equipo.modelo || 'Sin modelo' }}
          </option>
          <option value="nuevo">+ Registrar nuevo equipo</option>
        </select>
      </div>

      <div v-if="equipoSeleccionado === 'nuevo'" class="form-group">
        <h4>Nuevo equipo</h4>
        <label>Marca (OPCIONAL):</label>
        <input v-model="nuevoEquipo.marca" class="form-input" placeholder="Marca" />
        <label>Modelo (OPCIONAL):</label>
        <input v-model="nuevoEquipo.modelo" class="form-input" placeholder="Modelo" />
        <label>Observaciones (OPCIONAL):</label>
        <textarea v-model="nuevoEquipo.observaciones" class="form-input" placeholder="Observaciones"></textarea>
      </div>

      <div class="form-group">
        <h4>Datos de Recepción</h4>
        <label>Diagnóstico:</label>
        <textarea v-model="form.diagnostico" class="form-input" placeholder="Diagnóstico"></textarea>
        <label>Estado:</label>
        <select v-model="form.estado" class="form-input">
          <option disabled value="">-- Selecciona un estado --</option>
          <option v-for="estado in estadosRecepcion" :key="estado.value" :value="estado.value">
            {{ estado.label }}
          </option>
        </select>
        <label>Costo:</label>
        <input v-model.number="form.costo" type="number" class="form-input" placeholder="Costo" />
        <label>Observaciones (OPCIONAL):</label>
        <textarea v-model="form.observaciones" class="form-input" placeholder="Observaciones"></textarea>
        <button @click="registrarRecepcion" class="form-button">Registrar Recepción</button>
      </div>
    </div>

    <p class="mensaje" v-if="mensaje">{{ mensaje }}</p>

    <!-- Diálogo de selección de formato -->
    <SeleccionFormatoDialog
      :visible="mostrarDialogoFormato"
      @update:visible="val => mostrarDialogoFormato = val"
      @seleccionado="formatoSeleccionado"
      @cancelar="volverALista"
    />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import api from '@/services/api'
import SeleccionFormatoDialog from '@/components/SeleccionFormatoDialog.vue'
import { useImpresionRecepcion } from '@/utils/useImpresionRecepcion'

const mostrarDialogoFormato = ref(false)
const datosRecepcion = ref<any>(null)
const cedula = ref('')
const cliente = ref<any>(null)
const equipos = ref<any[]>([])
const equipoSeleccionado = ref('')
const estadosRecepcion = ref<{ value: string; label: string }[]>([])
const mensaje = ref('')
const formato = ref<'a4' | 'ticket' | null>(null)

const nuevoCliente = ref({
  cedula: cedula.value,
  nombre: '',
  apellido: '',
  celular: '',
  convencional: '',
  email: '',
  password: '',
  rol: 'cliente'
})

const nuevoEquipo = ref({
  marca: '',
  modelo: '',
  observaciones: ''
})

const form = ref({
  diagnostico: '',
  estado: 'pendiente',
  costo: 0,
  observaciones: ''
})

const cargarEstadosRecepcion = async () => {
  try {
    const { data } = await api.get('/recepcion/estados/')
    estadosRecepcion.value = data
  } catch (error) {
    console.error('Error al cargar estados de recepción', error)
  }
}

const buscarCliente = async () => {
  try {
    const { data } = await api.get(`/users/buscar/?cedula=${cedula.value}`)
    cliente.value = data
    mensaje.value = ''
    await cargarEquipos()
  } catch (e: any) {
    if (e.response?.status !== 404) console.error('Error al buscar cliente:', e)
    cliente.value = null
    mensaje.value = 'Cliente no encontrado. Regístralo primero.'
    nuevoCliente.value.cedula = cedula.value
  }
}

const cargarEquipos = async () => {
  const resp = await api.get(`/equipos/?cliente_id=${cliente.value.id}`)
  equipos.value = resp.data
  equipoSeleccionado.value = ''
}

const registrarCliente = async () => {
  try {
    const { data } = await api.post('/users/', nuevoCliente.value)
    cliente.value = data
    mensaje.value = 'Cliente registrado exitosamente.'
    await cargarEquipos()
  } catch (err) {
    mensaje.value = 'Error al registrar el cliente.'
    console.error(err)
  }
}

const registrarRecepcion = async () => {
  try {
    let equipoId = equipoSeleccionado.value
    if (equipoId === 'nuevo') {
      console.log('Cliente usado para nuevo equipo:', cliente.value)
      const { data } = await api.post('/equipos/', {
        ...nuevoEquipo.value,
        cliente_id: cliente.value.id
      })
      equipoId = data.id
      console.log('✅ Nuevo equipo registrado:', data)
    }

    const { data } = await api.post('/recepcion/equipos/', {
      ...form.value,
      cliente_id: cliente.value.id,
      equipo_id: equipoId  
    })

    console.log('✅ Recepción registrada:', data)

    datosRecepcion.value = data
    mostrarDialogoFormato.value = true
    console.log('🟢 mostrarDialogoFormato =', mostrarDialogoFormato.value)

    mensaje.value = 'Recepción registrada con éxito'
    form.value = { diagnostico: '', estado: 'pendiente', costo: 0, observaciones: '' }
  } catch (err) {
    mensaje.value = 'Error al registrar la recepción'
    console.error('❌ Error en registrarRecepcion:', err)
  }
}

const formatoSeleccionado = async (seleccion: string) => {
  console.log('📄 Formato seleccionado:', seleccion)
  formato.value = seleccion as 'a4' | 'ticket'
  const { imprimir } = useImpresionRecepcion(datosRecepcion.value, cliente.value)
  imprimir(formato.value)
}

const volverALista = () => {
  window.location.href = '/recepcion'
}

onMounted(() => {
  cargarEstadosRecepcion()
})
</script>

<style scoped>
.form-wrapper {
  max-width: 500px;
  margin: 0 auto;
  padding: 1rem;
}

.title {
  text-align: center;
  margin-bottom: 1.5rem;
  font-size: 1.4rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
  margin-bottom: 1.5rem;
}

.form-input {
  padding: 0.6rem;
  border-radius: 6px;
  background-color: #222;
  border: 1px solid #555;
  color: #fff;
}

.form-button {
  margin-top: 0.5rem;
  padding: 0.6rem;
  background-color: #646cff;
  color: white;
  font-weight: bold;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.form-button:hover {
  background-color: #535bf2;
}

.cliente-info {
  margin: 1rem 0;
  font-weight: bold;
}

.mensaje {
  margin-top: 1rem;
  text-align: center;
}
</style>
