<script setup>
import { RouterView } from 'vue-router'
import Header from './components/Header.vue'
</script>

<template>
  <div style="font-family: Arial, sans-serif; background-color: #f4f7f6; min-height: 100vh;">
    <Header />
    <main>
      <RouterView />
    </main>
  </div>
</template>

<style>
body { margin: 0; padding: 0; }
</style>