import { ref, reactive, markRaw, nextTick, defineAsyncComponent } from 'vue'

// Global state for managing UI components
const toasts = ref([])
const modals = reactive({})
const pendingAction = ref(null)
const pendingTimeout = ref(null)

// Toast management
export function useToast() {
  const toastIdCounter = ref(0)
  
  /**
   * Show a toast notification
   * @param {Object} options - Toast options
   * @param {string} options.type - Type of toast: 'success', 'error', 'warning', 'info'
   * @param {string} options.message - Toast message
   * @param {string} [options.title] - Optional toast title
   * @param {number} [options.duration=5000] - Duration in ms (0 for no auto-dismiss)
   * @param {Object} [options.action] - Optional action button { text: String, handler: Function }
   * @returns {string} - Toast ID for manual dismissal
   */
  function showToast(options) {
    const id = `toast-${++toastIdCounter.value}`
    const toast = {
      id,
      ...options,
      component: markRaw(defineAsyncComponent(() => import('../components/Toast.vue')))
    }
    
    toasts.value.push(toast)
    
    return id
  }
  
  /**
   * Dismiss a specific toast by ID
   * @param {string} id - Toast ID
   */
  function dismissToast(id) {
    const index = toasts.value.findIndex(t => t.id === id)
    if (index > -1) {
      toasts.value.splice(index, 1)
    }
  }
  
  /**
   * Dismiss all toasts
   */
  function dismissAllToasts() {
    toasts.value = []
  }
  
  return {
    toasts,
    showToast,
    dismissToast,
    dismissAllToasts
  }
}

// Modal management
export function useModal() {
  /**
   * Show a modal dialog
   * @param {string} name - Unique modal name
   * @param {Object} options - Modal options
   * @param {string} [options.title='Confirmation'] - Modal title
   * @param {string} [options.message=''] - Modal message
   * @param {string} [options.confirmText='Confirm'] - Confirm button text
   * @param {string} [options.cancelText='Cancel'] - Cancel button text
   * @param {boolean} [options.showCancel=true] - Show cancel button
   * @param {boolean} [options.danger=false] - Use danger styling
   * @param {Function} [options.onConfirm] - Confirm callback
   * @param {Function} [options.onCancel] - Cancel callback
   * @returns {Promise} - Resolves with true on confirm, false on cancel
   */
  function showModal(name, options = {}) {
    return new Promise((resolve) => {
      modals[name] = {
        isOpen: true,
        ...options,
        onConfirm: () => {
          if (options.onConfirm) {
            options.onConfirm()
          }
          closeModal(name)
          resolve(true)
        },
        onCancel: () => {
          if (options.onCancel) {
            options.onCancel()
          }
          closeModal(name)
          resolve(false)
        }
      }
    })
  }
  
  /**
   * Close a specific modal
   * @param {string} name - Modal name
   */
  function closeModal(name) {
    if (modals[name]) {
      modals[name].isOpen = false
      // Clean up after transition
      setTimeout(() => {
        delete modals[name]
      }, 300)
    }
  }
  
  /**
   * Get modal state
   * @param {string} name - Modal name
   * @returns {Object|null} - Modal state or null
   */
  function getModal(name) {
    return modals[name] || null
  }
  
  /**
   * Check if a modal is open
   * @param {string} name - Modal name
   * @returns {boolean}
   */
  function isModalOpen(name) {
    return modals[name]?.isOpen || false
  }
  
  return {
    showModal,
    closeModal,
    getModal,
    isModalOpen
  }
}

// Combined UI state composable
export function useUIState() {
  const toast = useToast()
  const modal = useModal()
  
  // Convenience methods for common patterns
  
  /**
   * Show a success toast
   * @param {string} message - Success message
   * @param {Object} [options] - Additional options
   */
  function showSuccess(message, options = {}) {
    return toast.showToast({
      type: 'success',
      message,
      duration: 3000,
      ...options
    })
  }
  
  /**
   * Show an error toast
   * @param {string} message - Error message
   * @param {Object} [options] - Additional options
   */
  function showError(message, options = {}) {
    return toast.showToast({
      type: 'error',
      message,
      duration: 0, // Don't auto-dismiss errors
      ...options
    })
  }
  
  /**
   * Show a confirmation modal
   * @param {Object} options - Modal options
   * @returns {Promise<boolean>} - Resolves to true if confirmed
   */
  async function showConfirm(options) {
    return modal.showModal('confirm', {
      title: 'Confirm Action',
      showCancel: true,
      ...options
    })
  }
  
  /**
   * Show an alert modal (no cancel button)
   * @param {Object} options - Modal options
   */
  async function showAlert(options) {
    return modal.showModal('alert', {
      title: 'Alert',
      showCancel: false,
      confirmText: 'OK',
      ...options
    })
  }
  
  /**
   * Show an undoable success toast with delayed action execution
   * @param {string} message - Success message
   * @param {Function} action - Action to execute after timeout
   * @param {Object} [options] - Additional options
   */
  function showUndoableSuccess(message, action, options = {}) {
    const duration = options.duration || 5000
    
    // Cancel any existing pending action
    if (pendingTimeout.value) {
      clearTimeout(pendingTimeout.value)
      pendingTimeout.value = null
      pendingAction.value = null
    }
    
    // Store the action
    pendingAction.value = action
    
    // Set timeout to execute action
    pendingTimeout.value = setTimeout(() => {
      if (pendingAction.value) {
        pendingAction.value()
        pendingAction.value = null
        pendingTimeout.value = null
      }
    }, duration)
    
    // Show toast with undo action
    return toast.showToast({
      type: 'success',
      message,
      duration,
      undoable: true,
      action: {
        text: 'Undo (Z)',
        handler: () => {
          // Cancel the pending action
          if (pendingTimeout.value) {
            clearTimeout(pendingTimeout.value)
            pendingTimeout.value = null
            pendingAction.value = null
            toast.showToast({
              type: 'info',
              message: 'Action cancelled',
              duration: 2000
            })
          }
        }
      },
      ...options
    })
  }
  
  return {
    // Toast methods
    ...toast,
    
    // Modal methods
    ...modal,
    
    // Convenience methods
    showSuccess,
    showError,
    showConfirm,
    showAlert,
    showUndoableSuccess
  }
}