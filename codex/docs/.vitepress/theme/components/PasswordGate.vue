<template>
  <!-- Show password gate when not authenticated -->
  <div v-if="!isAuthenticated" class="password-gate-overlay">
    <div class="password-gate-container">
      <div class="password-gate-card">
        <!-- Logo/Title -->
        <div class="logo-section">
          <div class="logo-icon">🔒</div>
          <h1 class="site-title">Elite Redux<br>Ability Codex</h1>
          <p class="site-subtitle">Access Restricted</p>
        </div>

        <!-- Password Form -->
        <form @submit.prevent="attemptLogin" class="password-form">
          <div class="input-group">
            <label for="password" class="password-label">Enter Password</label>
            <input
              id="password"
              ref="passwordInputRef"
              v-model="passwordInput"
              type="password"
              class="password-input"
              placeholder="Enter password to continue"
              :disabled="isLoading"
              autocomplete="current-password"
            />
          </div>
          
          <button
            type="submit"
            class="login-button"
            :disabled="isLoading || !passwordInput.trim()"
          >
            <span v-if="isLoading" class="loading-spinner"></span>
            <span v-else>{{ error ? 'Try Again' : 'Access Codex' }}</span>
          </button>
        </form>

        <!-- Error Message -->
        <div v-if="error" class="error-message">
          {{ error }}
        </div>

        <!-- Footer -->
        <div class="footer-text">
          This documentation contains sensitive information and requires authorization.
        </div>
      </div>
    </div>
  </div>
  
  <!-- Show actual content when authenticated -->
  <div v-else>
    <slot></slot>
  </div>
</template>

<script setup>
import { ref, onMounted, nextTick } from 'vue'

// Reactive state
const isAuthenticated = ref(false)
const passwordInput = ref('')
const isLoading = ref(false)
const error = ref('')
const passwordInputRef = ref(null)

// Password configuration (from environment variable)
const CORRECT_PASSWORD = import.meta.env.VITE_SITE_PASSWORD || 'dev-fallback'
const AUTH_KEY = 'codex_auth_token'
const AUTH_EXPIRY_KEY = 'codex_auth_expiry'
const SESSION_DURATION = 30 * 24 * 60 * 60 * 1000 // 1 month (30 days) in milliseconds

// Simple hash function for password verification
function hashPassword(password) {
  let hash = 0
  for (let i = 0; i < password.length; i++) {
    const char = password.charCodeAt(i)
    hash = ((hash << 5) - hash) + char
    hash = hash & hash // Convert to 32bit integer
  }
  return hash.toString()
}

// Check if user is already authenticated
function checkExistingAuth() {
  const token = localStorage.getItem(AUTH_KEY)
  const expiry = localStorage.getItem(AUTH_EXPIRY_KEY)
  
  if (token && expiry) {
    const expiryTime = parseInt(expiry)
    const currentTime = Date.now()
    
    if (currentTime < expiryTime) {
      // Valid session exists
      isAuthenticated.value = true
      return true
    } else {
      // Session expired, clear it
      clearAuth()
    }
  }
  
  return false
}

// Set authentication
function setAuth() {
  const token = hashPassword(CORRECT_PASSWORD + Date.now())
  const expiryTime = Date.now() + SESSION_DURATION
  
  localStorage.setItem(AUTH_KEY, token)
  localStorage.setItem(AUTH_EXPIRY_KEY, expiryTime.toString())
  isAuthenticated.value = true
}

// Clear authentication
function clearAuth() {
  localStorage.removeItem(AUTH_KEY)
  localStorage.removeItem(AUTH_EXPIRY_KEY)
  isAuthenticated.value = false
}

// Attempt to login
async function attemptLogin() {
  if (isLoading.value) return
  
  isLoading.value = true
  error.value = ''
  
  // Simulate a small delay for better UX
  await new Promise(resolve => setTimeout(resolve, 800))
  
  if (passwordInput.value.trim() === CORRECT_PASSWORD) {
    setAuth()
    passwordInput.value = ''
  } else {
    error.value = 'Incorrect password. Please try again.'
    passwordInput.value = ''
    
    // Focus back to input after error
    await nextTick()
    passwordInputRef.value?.focus()
  }
  
  isLoading.value = false
}

// Component lifecycle
onMounted(async () => {
  // Check for existing authentication
  if (!checkExistingAuth()) {
    // Focus on password input if not authenticated
    await nextTick()
    passwordInputRef.value?.focus()
  }
  
  // Add keyboard shortcut for logout (Ctrl+Shift+L) for testing
  const handleLogout = (e) => {
    if (e.ctrlKey && e.shiftKey && e.key === 'L') {
      e.preventDefault()
      clearAuth()
      console.log('Logged out via keyboard shortcut')
    }
  }
  
  document.addEventListener('keydown', handleLogout)
  
  // Cleanup listener
  return () => {
    document.removeEventListener('keydown', handleLogout)
  }
})

// Expose authentication state to parent
defineExpose({
  isAuthenticated,
  logout: clearAuth
})
</script>

<style scoped>
.password-gate-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10000;
}

.password-gate-container {
  width: 100%;
  max-width: 420px;
  padding: 2rem;
}

.password-gate-card {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 24px;
  padding: 3rem 2.5rem;
  text-align: center;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
}

.logo-section {
  margin-bottom: 2.5rem;
}

.logo-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
  opacity: 0.9;
}

.site-title {
  font-size: 1.75rem;
  font-weight: 700;
  color: #ffffff;
  margin: 0 0 0.5rem 0;
  letter-spacing: -0.02em;
}

.site-subtitle {
  font-size: 1rem;
  color: rgba(255, 255, 255, 0.7);
  margin: 0;
  font-weight: 500;
}

.password-form {
  margin-bottom: 2rem;
}

.input-group {
  margin-bottom: 1.5rem;
}

.password-label {
  display: block;
  font-size: 0.875rem;
  font-weight: 600;
  color: rgba(255, 255, 255, 0.9);
  margin-bottom: 0.75rem;
  text-align: left;
}

.password-input {
  width: 100%;
  padding: 1rem 1.25rem;
  font-size: 1rem;
  background: rgba(255, 255, 255, 0.08);
  border: 2px solid rgba(255, 255, 255, 0.1);
  border-radius: 16px;
  color: #ffffff;
  transition: all 0.2s ease;
  outline: none;
}

.password-input::placeholder {
  color: rgba(255, 255, 255, 0.5);
}

.password-input:focus {
  border-color: #4f46e5;
  background: rgba(255, 255, 255, 0.1);
  box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.2);
}

.password-input:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.login-button {
  width: 100%;
  padding: 1rem 1.5rem;
  font-size: 1rem;
  font-weight: 600;
  background: linear-gradient(135deg, #4f46e5 0%, #6366f1 100%);
  border: none;
  border-radius: 16px;
  color: #ffffff;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}

.login-button:hover:not(:disabled) {
  background: linear-gradient(135deg, #4338ca 0%, #5b21b6 100%);
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(79, 70, 229, 0.4);
}

.login-button:active:not(:disabled) {
  transform: translateY(0);
}

.login-button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
}

.loading-spinner {
  width: 20px;
  height: 20px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-top: 2px solid #ffffff;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.error-message {
  background: rgba(239, 68, 68, 0.1);
  border: 1px solid rgba(239, 68, 68, 0.3);
  border-radius: 12px;
  padding: 0.75rem 1rem;
  color: #fca5a5;
  font-size: 0.875rem;
  font-weight: 500;
  margin-bottom: 1.5rem;
}

.footer-text {
  font-size: 0.75rem;
  color: rgba(255, 255, 255, 0.5);
  line-height: 1.4;
}

/* Responsive design */
@media (max-width: 480px) {
  .password-gate-container {
    padding: 1rem;
  }
  
  .password-gate-card {
    padding: 2rem 1.5rem;
  }
  
  .site-title {
    font-size: 1.5rem;
  }
  
  .password-input,
  .login-button {
    padding: 0.875rem 1rem;
  }
}

/* Dark theme integration */
@media (prefers-color-scheme: light) {
  .password-gate-overlay {
    background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 50%, #cbd5e1 100%);
  }
  
  .password-gate-card {
    background: rgba(255, 255, 255, 0.9);
    border-color: rgba(0, 0, 0, 0.1);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
  }
  
  .site-title {
    color: #1e293b;
  }
  
  .site-subtitle {
    color: rgba(0, 0, 0, 0.7);
  }
  
  .password-label {
    color: rgba(0, 0, 0, 0.9);
  }
  
  .password-input {
    background: rgba(0, 0, 0, 0.05);
    border-color: rgba(0, 0, 0, 0.1);
    color: #1e293b;
  }
  
  .password-input::placeholder {
    color: rgba(0, 0, 0, 0.5);
  }
  
  .footer-text {
    color: rgba(0, 0, 0, 0.5);
  }
}
</style>