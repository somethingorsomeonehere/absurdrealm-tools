<template>
  <Teleport to="body">
    <Transition name="modal">
      <div
        v-if="isOpen"
        class="modal-overlay"
        @click="handleOverlayClick"
        @keydown="handleKeydown"
      >
        <div
          ref="modalContainer"
          class="modal-container"
          role="dialog"
          aria-modal="true"
          :aria-labelledby="titleId"
          @click.stop
        >
          <div class="modal-header">
            <h3 :id="titleId" class="modal-title">{{ title }}</h3>
            <button
              ref="closeButton"
              class="modal-close"
              @click="cancel"
              aria-label="Close modal"
            >
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M18 6L6 18M6 6l12 12"/>
              </svg>
            </button>
          </div>
          
          <div class="modal-body">
            <slot>{{ message }}</slot>
          </div>
          
          <div class="modal-footer">
            <div class="modal-keyboard-hint">
              Press <kbd>Enter</kbd> to {{ confirmText || 'confirm' }}, <kbd>Esc</kbd> to cancel
            </div>
            <div class="modal-actions">
              <button
                v-if="showCancel"
                class="modal-button modal-button-cancel"
                @click="cancel"
              >
                {{ cancelText }}
              </button>
              <button
                ref="confirmButton"
                class="modal-button modal-button-confirm"
                @click="confirm"
                :class="{ 'modal-button-danger': danger }"
              >
                {{ confirmText }}
              </button>
            </div>
          </div>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup>
import { ref, watch, nextTick, computed, onBeforeUnmount } from 'vue'

const props = defineProps({
  isOpen: {
    type: Boolean,
    default: false
  },
  title: {
    type: String,
    default: 'Confirmation'
  },
  message: {
    type: String,
    default: ''
  },
  confirmText: {
    type: String,
    default: 'Confirm'
  },
  cancelText: {
    type: String,
    default: 'Cancel'
  },
  showCancel: {
    type: Boolean,
    default: true
  },
  danger: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['confirm', 'cancel', 'update:isOpen'])

const modalContainer = ref(null)
const confirmButton = ref(null)
const closeButton = ref(null)
const previousActiveElement = ref(null)

// Generate unique ID for accessibility
const titleId = computed(() => `modal-title-${Math.random().toString(36).substr(2, 9)}`)

// Focus management
watch(() => props.isOpen, async (newVal) => {
  if (newVal) {
    // Store the previously focused element
    previousActiveElement.value = document.activeElement
    
    // Wait for DOM update
    await nextTick()
    
    // Focus the confirm button by default
    if (confirmButton.value) {
      confirmButton.value.focus()
    }
    
    // Add event listener for focus trap
    document.addEventListener('keydown', trapFocus)
  } else {
    // Remove event listener
    document.removeEventListener('keydown', trapFocus)
    
    // Return focus to previous element
    if (previousActiveElement.value && previousActiveElement.value.focus) {
      previousActiveElement.value.focus()
    }
  }
})

// Cleanup on unmount
onBeforeUnmount(() => {
  document.removeEventListener('keydown', trapFocus)
})

// Get all focusable elements within the modal
function getFocusableElements() {
  if (!modalContainer.value) return []
  
  const focusableSelectors = [
    'button:not([disabled])',
    'input:not([disabled])',
    'textarea:not([disabled])',
    'select:not([disabled])',
    '[tabindex]:not([tabindex="-1"])',
    'a[href]'
  ]
  
  return Array.from(
    modalContainer.value.querySelectorAll(focusableSelectors.join(', '))
  )
}

// Trap focus within modal
function trapFocus(event) {
  if (event.key !== 'Tab') return
  
  const focusableElements = getFocusableElements()
  if (focusableElements.length === 0) return
  
  const firstElement = focusableElements[0]
  const lastElement = focusableElements[focusableElements.length - 1]
  
  if (event.shiftKey) {
    // Shift + Tab
    if (document.activeElement === firstElement) {
      event.preventDefault()
      lastElement.focus()
    }
  } else {
    // Tab
    if (document.activeElement === lastElement) {
      event.preventDefault()
      firstElement.focus()
    }
  }
}

// Handle keyboard events
function handleKeydown(event) {
  if (event.key === 'Escape') {
    event.preventDefault()
    cancel()
  } else if (event.key === 'Enter' && event.target.tagName !== 'TEXTAREA') {
    event.preventDefault()
    confirm()
  }
}

// Handle overlay click
function handleOverlayClick(event) {
  if (event.target === event.currentTarget) {
    cancel()
  }
}

// Actions
function confirm() {
  emit('confirm')
  emit('update:isOpen', false)
}

function cancel() {
  emit('cancel')
  emit('update:isOpen', false)
}
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
  padding: 20px;
}

.modal-container {
  background-color: var(--vp-c-bg);
  border-radius: 8px;
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
  max-width: 500px;
  width: 100%;
  max-height: 90vh;
  display: flex;
  flex-direction: column;
  position: relative;
}

.modal-header {
  padding: 20px 24px;
  border-bottom: 1px solid var(--vp-c-divider);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.modal-title {
  margin: 0;
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--vp-c-text-1);
}

.modal-close {
  background: none;
  border: none;
  padding: 4px;
  cursor: pointer;
  color: var(--vp-c-text-3);
  border-radius: 4px;
  transition: all 0.2s;
}

.modal-close:hover {
  color: var(--vp-c-text-1);
  background-color: var(--vp-c-gray-soft);
}

.modal-close:focus {
  outline: 2px solid var(--vp-c-brand);
  outline-offset: 2px;
}

.modal-body {
  padding: 24px;
  overflow-y: auto;
  flex: 1;
  color: var(--vp-c-text-2);
  line-height: 1.6;
}

.modal-footer {
  padding: 16px 24px;
  border-top: 1px solid var(--vp-c-divider);
}

.modal-keyboard-hint {
  font-size: 0.875rem;
  color: var(--vp-c-text-3);
  margin-bottom: 12px;
  text-align: center;
}

.modal-keyboard-hint kbd {
  background-color: var(--vp-c-gray-soft);
  border: 1px solid var(--vp-c-divider);
  border-radius: 4px;
  padding: 2px 6px;
  font-family: var(--vp-font-family-mono);
  font-size: 0.85em;
}

.modal-actions {
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}

.modal-button {
  padding: 8px 16px;
  border-radius: 4px;
  font-size: 0.875rem;
  font-weight: 500;
  border: none;
  cursor: pointer;
  transition: all 0.2s;
  min-width: 80px;
}

.modal-button:focus {
  outline: 2px solid var(--vp-c-brand);
  outline-offset: 2px;
}

.modal-button-cancel {
  background-color: var(--vp-c-gray-soft);
  color: var(--vp-c-text-2);
}

.modal-button-cancel:hover {
  background-color: var(--vp-c-gray);
}

.modal-button-confirm {
  background-color: var(--vp-c-brand);
  color: white;
}

.modal-button-confirm:hover {
  background-color: var(--vp-c-brand-dark);
}

.modal-button-danger {
  background-color: var(--vp-c-danger);
}

.modal-button-danger:hover {
  background-color: var(--vp-c-danger-dark);
}

/* Transitions */
.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.2s ease;
}

.modal-enter-active .modal-container,
.modal-leave-active .modal-container {
  transition: transform 0.2s ease;
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}

.modal-enter-from .modal-container,
.modal-leave-to .modal-container {
  transform: scale(0.95);
}

/* Mobile responsiveness */
@media (max-width: 640px) {
  .modal-overlay {
    padding: 16px;
  }
  
  .modal-container {
    max-width: 100%;
  }
  
  .modal-keyboard-hint {
    font-size: 0.75rem;
  }
}
</style>