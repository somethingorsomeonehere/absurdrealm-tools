<template>
  <Teleport to="body">
    <Transition name="toast">
      <div
        v-if="isVisible"
        ref="toastElement"
        class="toast"
        :class="`toast-${type}`"
        role="alert"
        :aria-live="type === 'error' ? 'assertive' : 'polite'"
        @keydown="handleKeydown"
        tabindex="-1"
      >
        <div class="toast-icon">
          <svg v-if="type === 'success'" width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
          </svg>
          <svg v-else-if="type === 'error'" width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd"/>
          </svg>
          <svg v-else-if="type === 'warning'" width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd"/>
          </svg>
          <svg v-else width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd"/>
          </svg>
        </div>
        
        <div class="toast-content">
          <div v-if="title" class="toast-title">{{ title }}</div>
          <div class="toast-message">
            <slot>{{ message }}</slot>
          </div>
        </div>
        
        <button
          v-if="action"
          class="toast-action"
          @click="handleAction"
        >
          {{ action.text }}
        </button>
        
        <button
          class="toast-close"
          @click="dismiss"
          aria-label="Dismiss notification"
        >
          <svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor">
            <path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z"/>
          </svg>
        </button>
        
        <div v-if="duration > 0" class="toast-progress">
          <div 
            class="toast-progress-bar" 
            :style="{ animationDuration: `${duration}ms` }"
          />
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup>
import { ref, watch, onMounted, onBeforeUnmount, nextTick } from 'vue'

const props = defineProps({
  type: {
    type: String,
    default: 'info',
    validator: (value) => ['success', 'error', 'warning', 'info'].includes(value)
  },
  title: {
    type: String,
    default: ''
  },
  message: {
    type: String,
    required: true
  },
  duration: {
    type: Number,
    default: 5000 // 5 seconds
  },
  action: {
    type: Object,
    default: null
    // Expected shape: { text: String, handler: Function }
  },
  undoable: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['dismiss', 'action'])

const isVisible = ref(false)
const toastElement = ref(null)
const dismissTimer = ref(null)

// Show toast on mount
onMounted(async () => {
  isVisible.value = true
  
  // Focus the toast for keyboard accessibility
  await nextTick()
  if (toastElement.value) {
    toastElement.value.focus()
  }
  
  // Set up auto-dismiss
  if (props.duration > 0) {
    dismissTimer.value = setTimeout(() => {
      dismiss()
    }, props.duration)
  }
  
  // Add global keyboard listener
  document.addEventListener('keydown', handleGlobalKeydown)
})

// Cleanup
onBeforeUnmount(() => {
  if (dismissTimer.value) {
    clearTimeout(dismissTimer.value)
  }
  document.removeEventListener('keydown', handleGlobalKeydown)
})

// Handle keyboard events on the toast element
function handleKeydown(event) {
  if (event.key === 'Escape') {
    event.preventDefault()
    dismiss()
  } else if ((event.key === 'z' || event.key === 'Z') && props.undoable && props.action) {
    event.preventDefault()
    handleAction()
  }
}

// Handle global keyboard events (when toast is focused or undoable)
function handleGlobalKeydown(event) {
  if (event.key === 'Escape' && document.activeElement === toastElement.value) {
    event.preventDefault()
    dismiss()
  } else if ((event.key === 'z' || event.key === 'Z') && props.undoable && props.action && isVisible.value) {
    // Check if user is not typing in an input
    const isTyping = ['INPUT', 'TEXTAREA', 'SELECT'].includes(event.target.tagName)
    if (!isTyping && !event.ctrlKey && !event.metaKey) {
      event.preventDefault()
      handleAction()
    }
  }
}

// Dismiss the toast
function dismiss() {
  if (dismissTimer.value) {
    clearTimeout(dismissTimer.value)
  }
  isVisible.value = false
  setTimeout(() => {
    emit('dismiss')
  }, 300) // Wait for transition to complete
}

// Handle action button click
function handleAction() {
  if (props.action && props.action.handler) {
    props.action.handler()
  }
  emit('action')
  dismiss()
}
</script>

<style scoped>
.toast {
  position: fixed;
  bottom: 24px;
  right: 24px;
  background-color: var(--vp-c-bg);
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 16px;
  min-width: 300px;
  max-width: 500px;
  z-index: 10000;
  overflow: hidden;
}

.toast:focus {
  outline: 2px solid var(--vp-c-brand);
  outline-offset: 2px;
}

/* Type-specific colors */
.toast-success {
  border-color: var(--vp-c-green-dimm);
}

.toast-success .toast-icon {
  color: var(--vp-c-green);
}

.toast-error {
  border-color: var(--vp-c-danger-dimm);
}

.toast-error .toast-icon {
  color: var(--vp-c-danger);
}

.toast-warning {
  border-color: var(--vp-c-warning-dimm);
}

.toast-warning .toast-icon {
  color: var(--vp-c-warning);
}

.toast-info {
  border-color: var(--vp-c-brand-dimm);
}

.toast-info .toast-icon {
  color: var(--vp-c-brand);
}

/* Icon */
.toast-icon {
  flex-shrink: 0;
  margin-top: 2px;
}

/* Content */
.toast-content {
  flex: 1;
  min-width: 0;
}

.toast-title {
  font-weight: 600;
  margin-bottom: 4px;
  color: var(--vp-c-text-1);
}

.toast-message {
  color: var(--vp-c-text-2);
  font-size: 0.875rem;
  line-height: 1.5;
}

/* Action button */
.toast-action {
  flex-shrink: 0;
  padding: 4px 12px;
  background-color: var(--vp-c-brand);
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: background-color 0.2s;
}

.toast-action:hover {
  background-color: var(--vp-c-brand-dark);
}

.toast-action:focus {
  outline: 2px solid var(--vp-c-brand);
  outline-offset: 2px;
}

/* Close button */
.toast-close {
  flex-shrink: 0;
  background: none;
  border: none;
  padding: 4px;
  cursor: pointer;
  color: var(--vp-c-text-3);
  border-radius: 4px;
  transition: all 0.2s;
  margin-left: 8px;
}

.toast-close:hover {
  color: var(--vp-c-text-1);
  background-color: var(--vp-c-gray-soft);
}

.toast-close:focus {
  outline: 2px solid var(--vp-c-brand);
  outline-offset: 2px;
}

/* Progress bar */
.toast-progress {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 3px;
  background-color: var(--vp-c-gray-soft);
  overflow: hidden;
}

.toast-progress-bar {
  height: 100%;
  background-color: currentColor;
  opacity: 0.3;
  animation: progress linear forwards;
}

@keyframes progress {
  from {
    transform: translateX(-100%);
  }
  to {
    transform: translateX(0);
  }
}

/* Transitions */
.toast-enter-active,
.toast-leave-active {
  transition: all 0.3s ease;
}

.toast-enter-from {
  transform: translateX(100%);
  opacity: 0;
}

.toast-leave-to {
  transform: translateX(100%);
  opacity: 0;
}

/* Mobile responsiveness */
@media (max-width: 640px) {
  .toast {
    bottom: 16px;
    right: 16px;
    left: 16px;
    min-width: auto;
    max-width: none;
  }
}

/* Keyboard hint */
.toast::after {
  content: "Press Esc to dismiss";
  position: absolute;
  bottom: -20px;
  right: 0;
  font-size: 0.75rem;
  color: var(--vp-c-text-3);
  opacity: 0;
  transition: opacity 0.2s;
}

.toast:focus::after {
  opacity: 1;
}
</style>