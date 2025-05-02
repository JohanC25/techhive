<template>
    <Dialog
      :visible="visible"
      @update:visible="val => emit('update:visible', val)"
      modal
      header="Seleccione Formato"
      :style="{ width: '100%', maxWidth: '400px' }"
      :closable="false"
    >
      <div class="popup-formato">
        <p>Seleccione el formato de impresión</p>
        <div class="formato-opciones">
          <button class="formato-btn" @click="emitirFormato('a4')">📄 A4</button>
          <button class="formato-btn" @click="emitirFormato('ticket')">🎟️ Ticket</button>
        </div>
        <button class="form-button" @click="$emit('cancelar')">⬅ Volver a la lista</button>
      </div>
    </Dialog>
  </template>
  
  <script setup lang="ts">
  import { defineProps, defineEmits } from 'vue'
  import Dialog from 'primevue/dialog'
  
  defineProps<{
    visible: boolean
  }>()
  
  const emit = defineEmits(['update:visible', 'seleccionado', 'cancelar'])
  
  const emitirFormato = (formato: string) => {
    emit('seleccionado', formato)
  }
  </script>
  
  <style scoped>
  .popup-formato {
    text-align: center;
    padding: 1rem;
  }
  
  .formato-opciones {
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin: 1rem 0;
  }
  
  .formato-btn {
    display: flex;
    flex-direction: column; /* icono arriba, texto abajo */
    align-items: center;
    justify-content: center;
    gap: 4px;

    width: 80px;
    height: 80px;
    font-size: 1rem;
    font-weight: bold;
    border-radius: 10px;
    border: 2px solid #555;
    background-color: #222;
    color: white;
    cursor: pointer;
    transition: 0.3s;
  }
  
  .formato-btn:hover {
    background-color: #646cff;
  }
  
  .form-button {
    margin-top: 1rem;
    padding: 0.6rem;
    background-color: #646cff;
    color: white;
    font-weight: bold;
    border: none;
    border-radius: 6px;
    cursor: pointer;
  }
  </style>
  