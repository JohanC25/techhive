<template>
    <div class="orden-a4">
      <div class="hoja">
        <div class="encabezado">
          <h2>MAGIC WORLD COMPUTERS</h2>
          <p>Dirección: Tomás de Berlanga E8-31 y Av. Shyris</p>
          <p>Telf.: 6008553 / 0997717507</p>
          <p>Email: vero_meneses@hotmail.com</p>
          <hr />
        </div>
  
        <h3>ORDEN DE TRABAJO #{{ recepcion?.id }}</h3>
        <p><strong>Cliente:</strong> {{ cliente?.nombre }} {{ cliente?.apellido }}</p>
        <p><strong>Cédula/RUC:</strong> {{ cliente?.cedula }}</p>
        <p><strong>Teléfono:</strong> {{ cliente?.celular }}</p>
        <p><strong>Fecha Recepción:</strong> {{ formatFecha(recepcion?.fecha_ingreso) }}</p>
  
        <p><strong>Equipo:</strong> {{ recepcion?.equipo?.marca || 'Sin marca' }} - {{ recepcion?.equipo?.modelo || 'Sin modelo' }}</p>
        <p><strong>Daño:</strong> {{ recepcion?.diagnostico }}</p>
        <p><strong>Observaciones:</strong> {{ recepcion?.observaciones || 'Ninguna' }}</p>
  
        <div class="importante">
          <h4>IMPORTANTE</h4>
          <ul>
            <li>No nos responsabilizamos por cartuchos y equipos no retirados en un plazo máximo de 30 días</li>
            <li>Todo equipo reparado y no retirado será rematado</li>
            <li>Vigencia de la garantía de recargas de toners y cartuchos es de 48 horas</li>
            <li>Todo diagnóstico del equipo tiene un valor de $18.00</li>
          </ul>
        </div>
  
        <div class="firmas">
          <div>
            <div class="linea"></div>
            <p>Recibido por:<br />Ing. Verónica Meneses</p>
          </div>
          <div>
            <div class="linea"></div>
            <p>Entregado por:<br />{{ cliente?.nombre }} {{ cliente?.apellido }}</p>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  defineProps<{
    recepcion: any
    cliente: any
  }>()
  
  function formatFecha(fecha: string): string {
    return new Date(fecha).toLocaleDateString()
  }
  </script>
  
  <style scoped>
  .orden-a4 {
    font-family: Arial, sans-serif;
    background-color: white;
    color: black;
    width: 100%;
    max-width: 800px;
    padding: 20px;
  }
  
  .hoja {
    border: 1px dashed #333;
    padding: 20px;
    height: 100%;
  }
  
  .encabezado {
    text-align: center;
    margin-bottom: 10px;
  }
  
  .encabezado h2 {
    color: #0000FF;
    margin-bottom: 5px;
  }
  
  .importante {
    margin-top: 20px;
  }
  
  .importante h4 {
    margin-bottom: 5px;
  }
  
  .firmas {
    display: flex;
    justify-content: space-between;
    margin-top: 40px;
  }
  
  .linea {
    border-top: 1px solid black;
    width: 200px;
    margin-bottom: 5px;
  }
  </style>
  