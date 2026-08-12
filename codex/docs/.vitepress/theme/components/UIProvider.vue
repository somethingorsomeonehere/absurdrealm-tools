<template>
  <div>
    <!-- Render all active toasts -->
    <component
      v-for="toast in toasts"
      :key="toast.id"
      :is="ToastComponent"
      v-bind="toast"
      @dismiss="() => dismissToast(toast.id)"
      @action="() => dismissToast(toast.id)"
    />
    
    <!-- Slot for main content -->
    <slot />
  </div>
</template>

<script setup>
import { useToast } from '../composables/useUIState'
import Toast from './Toast.vue'

const { toasts, dismissToast } = useToast()
const ToastComponent = Toast
</script>