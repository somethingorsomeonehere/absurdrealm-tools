import DefaultTheme from 'vitepress/theme'
import { h } from 'vue'
import './custom.css'
import InlineAbilityEditor from './components/InlineAbilityEditor.vue'
import UIProvider from './components/UIProvider.vue'
import Modal from './components/Modal.vue'
import Toast from './components/Toast.vue'
import PasswordGate from './components/PasswordGate.vue'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    // Register global components
    app.component('InlineAbilityEditor', InlineAbilityEditor)
    app.component('Modal', Modal)
    app.component('Toast', Toast)
    app.component('UIProvider', UIProvider)
    app.component('PasswordGate', PasswordGate)
  },
  Layout() {
    return h(UIProvider, null, {
      default: () => [
        h(PasswordGate, null, {
          default: () => h(DefaultTheme.Layout, null, {
            'doc-before': () => h(InlineAbilityEditor)
          })
        })
      ]
    })
  }
}