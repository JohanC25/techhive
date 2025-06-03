<template>
  <div class="max-w-xl mx-auto p-6 bg-white rounded-xl shadow">
    <h2 class="text-2xl font-bold mb-6 text-center">Módulo de Reportes</h2>

    <div class="flex flex-col gap-4">
      <Button
        label="📊 Reporte de Ventas"
        icon="pi pi-chart-bar"
        class="p-button-outlined"
        @click="$router.push('/reportes/ventas')"
      />
      <!-- Puedes añadir más reportes aquí -->
    </div>
  </div>
</template>

<script lang="ts" setup>
</script>
