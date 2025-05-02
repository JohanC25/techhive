<template>
    <div class="ticket">
      <h3 class="titulo">MAGIC WORLD COMPUTERS</h3>
      <p class="info">Tomás de Berlanga E8-31 y Av. Shyris</p>
      <p class="info">Telf.: 6008553 / 0997717507</p>
      <p class="info">Email: vero_meneses@hotmail.com</p>
      <hr />
  
      <p><strong>Orden #:</strong> {{ recepcion.id }}</p>
      <p><strong>Cliente:</strong> {{ cliente?.nombre }} {{ cliente?.apellido }}</p>
      <p><strong>Cédula:</strong> {{ cliente?.cedula }}</p>
      <p><strong>Fecha:</strong> {{ formatFecha(recepcion.fecha_ingreso) }}</p>
  
      <p><strong>Equipo:</strong> {{ recepcion?.equipo?.marca }} {{ recepcion?.equipo?.modelo }}</p>
      <p><strong>Diagnóstico:</strong> {{ recepcion?.diagnostico }}</p>
      <p><strong>Costo:</strong> ${{ recepcion?.costo }}</p>
      <p><strong>Estado:</strong> {{ recepcion?.estado }}</p>
  
      <hr />
      <p class="importante">* No nos responsabilizamos por equipos no retirados en 30 días.</p>
      <p class="importante">* Garantía de 48h para cartuchos/toners.</p>
  
      <div class="firma">
        <p>______________________</p>
        <p>Firma del Cliente</p>
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  defineProps<{
    recepcion: any,
    cliente: any
  }>()
  
  function formatFecha(fecha: string): string {
    return new Date(fecha).toLocaleDateString()
  }
  </script>
  
  <style scoped>
  .ticket {
    width: 280px;
    font-family: 'Courier New', monospace;
    font-size: 12px;
    color: #000;
    background-color: #fff;
    padding: 10px;
    border: 1px dashed #333;
  }
  
  .titulo {
    text-align: center;
    font-weight: bold;
    font-size: 14px;
  }
  
  .info {
    text-align: center;
    margin: 0;
  }
  
  .importante {
    font-style: italic;
    font-size: 11px;
  }
  
  .firma {
    text-align: center;
    margin-top: 20px;
  }
  </style>
  