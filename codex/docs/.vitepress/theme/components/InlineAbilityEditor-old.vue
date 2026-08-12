<template>
  <div v-if="isAbilityPage" class="inline-editor">
    <!-- Collapsed State -->
    <div v-if="!isExpanded" class="editor-collapsed">
      <div class="editor-header">
        <div class="editor-title">
          <span class="editor-icon">✏️</span>
          <h4>Suggest Improvements</h4>
        </div>
        <p class="editor-subtitle">
          Help improve {{ abilityInfo.name }} (ID: {{ abilityInfo.id }}) - Spot errors or suggest better descriptions
        </p>
        <div class="editor-actions">
          <button 
            class="editor-button primary"
            @click="expandEditor"
            :disabled="loading"
          >
            {{ loading ? 'Loading...' : '📝 Edit This Ability' }}
          </button>
          <button 
            class="editor-button secondary"
            @click="createSimpleIssue"
          >
            🐛 Report Issue
          </button>
        </div>
      </div>
    </div>

    <!-- Expanded State -->
    <div v-if="isExpanded" class="editor-expanded">
      <div class="editor-header-expanded">
        <div class="editor-title-expanded">
          <span class="editor-icon">✏️</span>
          <h4>Editing: {{ abilityInfo.name }} (ID: {{ abilityInfo.id }})</h4>
          <button class="editor-close" @click="collapseEditor">×</button>
        </div>
        
        <div class="editor-warning">
          <strong>⚠️ Character Limit:</strong> Extended descriptions must be 280-300 characters (GBA hardware limit)
          <div v-if="extendedDescCharCount > 0" class="char-status">
            Current: <strong :class="getCharCountClass()">{{ extendedDescCharCount }}</strong> characters
            <span v-if="extendedDescCharCount < 280" class="char-advice">
              - Add {{ 280 - extendedDescCharCount }} more characters
            </span>
            <span v-else-if="extendedDescCharCount > 300" class="char-advice">
              - Remove {{ extendedDescCharCount - 300 }} characters
            </span>
            <span v-else class="char-advice">
              ✅ Perfect length!
            </span>
          </div>
        </div>
      </div>

      <!-- Loading State -->
      <div v-if="loading" class="editor-loading">
        <div class="loading-spinner"></div>
        <p>Loading ability content...</p>
      </div>

      <!-- Editor Interface -->
      <div v-if="!loading && originalContent" class="editor-interface">
        <!-- Tabs -->
        <div class="editor-tabs">
          <button 
            :class="['tab', { active: activeTab === 'edit' }]"
            @click="activeTab = 'edit'"
          >
            Edit
          </button>
          <button 
            :class="['tab', { active: activeTab === 'preview' }]"
            @click="activeTab = 'preview'"
          >
            Preview
          </button>
          <button 
            :class="['tab', { active: activeTab === 'diff' }]"
            @click="activeTab = 'diff'"
          >
            Changes ({{ hasChanges ? 'Yes' : 'None' }})
          </button>
        </div>

        <!-- Edit Tab -->
        <div v-if="activeTab === 'edit'" class="editor-content">
          <textarea 
            v-model="editedContent"
            class="editor-textarea"
            placeholder="Edit the ability description..."
            @input="onContentChange"
          ></textarea>
          
          <div class="editor-stats">
            <div class="char-count">
              <span class="stat-label">Extended Description: </span>
              <span :class="['char-count-value', getCharCountClass()]">
                {{ extendedDescCharCount }} / 300 chars
              </span>
            </div>
            <div class="total-changes">
              <span class="stat-label">Total Changes: </span>
              <span class="changes-value">{{ changeCount }} modifications</span>
            </div>
          </div>
        </div>

        <!-- Preview Tab -->
        <div v-if="activeTab === 'preview'" class="editor-preview">
          <div class="preview-content" v-html="previewHtml"></div>
        </div>

        <!-- Diff Tab -->
        <div v-if="activeTab === 'diff'" class="editor-diff">
          <div v-if="!hasChanges" class="no-changes">
            <p>No changes made yet. Edit the content to see differences.</p>
          </div>
          <div v-else class="diff-content">
            <div class="diff-section">
              <h5>Changes Summary:</h5>
              <ul class="diff-summary">
                <li v-for="change in diffSummary" :key="change.type" :class="change.type">
                  {{ change.description }}
                </li>
              </ul>
            </div>
            <div class="diff-visual" v-html="diffHtml"></div>
          </div>
        </div>

        <!-- Actions -->
        <div class="editor-actions-expanded">
          <button 
            class="editor-button primary"
            @click="submitToGitHub"
            :disabled="!hasChanges || !isValidContent"
            :title="hasChanges && isValidContent ? 'Submit to GitHub (Ctrl+S or Cmd+S)' : 'Make valid changes to submit'"
          >
            🚀 Submit to GitHub
          </button>
          <button 
            class="editor-button secondary"
            @click="resetContent"
            title="Reset all changes"
          >
            🔄 Reset Changes
          </button>
          <button 
            class="editor-button tertiary"
            @click="collapseEditor"
            title="Close editor (Esc)"
          >
            Cancel
          </button>
        </div>

        <!-- Keyboard shortcuts hint -->
        <div class="keyboard-hints">
          <small>💡 <strong>Ctrl+S</strong> (or <strong>Cmd+S</strong>) to submit • <strong>Esc</strong> to close</small>
        </div>
      </div>

      <!-- Error State -->
      <div v-if="error" class="editor-error">
        <p><strong>Error:</strong> {{ error }}</p>
        <button class="editor-button secondary" @click="retryLoad">Retry</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, watch } from 'vue'
import { useData } from 'vitepress'
import * as Diff from 'diff'

const { page } = useData()

// State
const isExpanded = ref(false)
const loading = ref(false)
const error = ref('')
const activeTab = ref('edit')
const originalContent = ref('')
const editedContent = ref('')

// Check if this is an ability page
const isAbilityPage = computed(() => {
  const path = page.value.relativePath || ''
  return path.startsWith('abilities/') && path.endsWith('.md') && path !== 'abilities/index.md'
})

// Extract ability information from the current page
const abilityInfo = ref({
  id: '',
  name: '',
  filename: '',
  title: ''
})

// Computed properties
const hasChanges = computed(() => {
  return originalContent.value !== editedContent.value
})

const changeCount = computed(() => {
  if (!hasChanges.value) return 0
  const diff = Diff.diffLines(originalContent.value, editedContent.value)
  return diff.filter(part => part.added || part.removed).length
})

const extendedDescCharCount = computed(() => {
  // Extract the extended description section from the edited content
  // Format: ## Extended In-Game Description\n*instruction line*\n\nActual description\n\n*Character count: X*
  const extendedMatch = editedContent.value.match(/## Extended In-Game Description\s*\n\*.*?\*\s*\n\n(.*?)(?:\n\n|\*Character count:|$)/s)
  if (extendedMatch && extendedMatch[1]) {
    const desc = extendedMatch[1].trim()
    return desc.length
  }
  return 0
})

const isValidContent = computed(() => {
  const charCount = extendedDescCharCount.value
  return charCount >= 280 && charCount <= 300
})

const previewHtml = computed(() => {
  // Simple markdown to HTML conversion for preview
  // This is a basic implementation - in production you might want a proper markdown parser
  return editedContent.value
    .replace(/^# (.*$)/gm, '<h1>$1</h1>')
    .replace(/^## (.*$)/gm, '<h2>$1</h2>')
    .replace(/^### (.*$)/gm, '<h3>$1</h3>')
    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
    .replace(/\*(.*?)\*/g, '<em>$1</em>')
    .replace(/\n/g, '<br>')
})

const diffSummary = computed(() => {
  if (!hasChanges.value) return []
  
  const diff = Diff.diffLines(originalContent.value, editedContent.value)
  const summary = []
  
  let additions = 0
  let deletions = 0
  
  diff.forEach(part => {
    if (part.added) additions += part.count || 1
    if (part.removed) deletions += part.count || 1
  })
  
  if (additions > 0) {
    summary.push({ type: 'addition', description: `${additions} line(s) added` })
  }
  if (deletions > 0) {
    summary.push({ type: 'deletion', description: `${deletions} line(s) removed` })
  }
  
  const charCountChange = extendedDescCharCount.value - getOriginalExtendedDescCharCount()
  if (charCountChange !== 0) {
    const type = charCountChange > 0 ? 'addition' : 'deletion'
    summary.push({ 
      type, 
      description: `Extended description ${charCountChange > 0 ? '+' : ''}${charCountChange} characters` 
    })
  }
  
  return summary
})

const diffHtml = computed(() => {
  if (!hasChanges.value) return ''
  
  const diff = Diff.diffLines(originalContent.value, editedContent.value)
  let html = '<div class="diff-lines">'
  
  diff.forEach(part => {
    const className = part.added ? 'diff-added' : part.removed ? 'diff-removed' : 'diff-unchanged'
    const prefix = part.added ? '+ ' : part.removed ? '- ' : '  '
    const lines = part.value.split('\n').filter(line => line.length > 0)
    
    lines.forEach(line => {
      html += `<div class="${className}">${prefix}${escapeHtml(line)}</div>`
    })
  })
  
  html += '</div>'
  return html
})

// Methods
function getCharCountClass() {
  const count = extendedDescCharCount.value
  if (count < 280) return 'char-count-low'    // Too short - red
  if (count > 300) return 'char-count-high'   // Too long - red/orange  
  return 'char-count-good'                    // Perfect range 280-300 - green
}

function getOriginalExtendedDescCharCount() {
  const extendedMatch = originalContent.value.match(/## Extended In-Game Description\s*\n\*.*?\*\s*\n\n(.*?)(?:\n\n|\*Character count:|$)/s)
  if (extendedMatch && extendedMatch[1]) {
    const desc = extendedMatch[1].trim()
    return desc.length
  }
  return 0
}

function escapeHtml(text) {
  const div = document.createElement('div')
  div.textContent = text
  return div.innerHTML
}

async function expandEditor() {
  isExpanded.value = true
  await loadOriginalContent()
}

function collapseEditor() {
  isExpanded.value = false
  activeTab.value = 'edit'
  error.value = ''
}

async function loadOriginalContent() {
  loading.value = true
  error.value = ''
  
  try {
    // Try multiple methods to get the original content
    let content = ''
    
    // Method 1: Try to fetch from the source repository (GitHub raw)
    const githubRawUrl = `https://raw.githubusercontent.com/darkyy92/eliteredux-darky/main/knowledge/abilities/${abilityInfo.value.filename}.md`
    
    try {
      const response = await fetch(githubRawUrl)
      if (response.ok) {
        content = await response.text()
      }
    } catch (err) {
      console.log('GitHub raw fetch failed, trying alternative method')
    }
    
    // Method 2: If GitHub fails, extract from current DOM content
    if (!content) {
      const mainContent = document.querySelector('.VPDoc .vp-doc')
      if (mainContent) {
        // This is a fallback - extract visible content and reconstruct markdown
        content = reconstructMarkdownFromDOM(mainContent)
      }
    }
    
    if (!content) {
      throw new Error('Could not load content from any source')
    }
    
    originalContent.value = content
    editedContent.value = content
    
  } catch (err) {
    error.value = 'Could not load the original content. You can still report issues using the simple form.'
    console.error('Failed to load content:', err)
  } finally {
    loading.value = false
  }
}

function reconstructMarkdownFromDOM(container) {
  // Basic DOM to markdown reconstruction
  // This is a fallback method when we can't fetch the original
  let markdown = ''
  
  // Get the title
  const title = document.querySelector('h1')
  if (title) {
    markdown += `# ${title.textContent}\n\n`
  }
  
  // Get all headings and content
  const elements = container.querySelectorAll('h2, h3, p, pre, ul, ol')
  
  elements.forEach(el => {
    if (el.tagName === 'H2') {
      markdown += `## ${el.textContent}\n`
    } else if (el.tagName === 'H3') {
      markdown += `### ${el.textContent}\n`
    } else if (el.tagName === 'P') {
      const text = el.textContent
      if (text.startsWith('*') && text.endsWith('*')) {
        markdown += `${text}\n`
      } else {
        markdown += `${text}\n`
      }
    } else if (el.tagName === 'PRE') {
      markdown += `\`\`\`\n${el.textContent}\n\`\`\`\n`
    }
    markdown += '\n'
  })
  
  return markdown.trim()
}

function onContentChange() {
  // Trigger reactivity
}

function resetContent() {
  editedContent.value = originalContent.value
  activeTab.value = 'edit'
}

function submitToGitHub() {
  if (!hasChanges.value || !isValidContent.value) return
  
  const repoUrl = 'https://github.com/darkyy92/eliteredux-darky'
  
  // Create issue body with diff
  const diffText = Diff.createPatch(
    abilityInfo.value.filename + '.md',
    originalContent.value,
    editedContent.value,
    'Original',
    'Proposed Changes'
  )
  
  const issueBody = `## Ability Information
**Ability Name:** ${abilityInfo.value.name}
**Ability ID:** ${abilityInfo.value.id}
**Source File:** \`knowledge/abilities/${abilityInfo.value.filename}.md\`
**Codex URL:** ${window.location.href}

## Proposed Changes
The following changes are suggested for this ability:

**Summary:**
${diffSummary.value.map(s => `- ${s.description}`).join('\n')}

**Extended Description Character Count:** ${extendedDescCharCount.value} characters (${isValidContent.value ? '✅ Valid' : '❌ Invalid'})

## Diff
\`\`\`diff
${diffText}
\`\`\`

## Additional Context
These changes were made using the Elite Redux Ability Codex inline editor.

---
*This issue was created via the Elite Redux Ability Codex smart editing system.*`

  const params = new URLSearchParams({
    title: `[Ability Edit] ${abilityInfo.value.name} (ID: ${abilityInfo.value.id}) - Inline Changes`,
    body: issueBody,
    labels: 'codex-submission'
  })
  
  const url = `${repoUrl}/issues/new?${params.toString()}`
  window.open(url, '_blank')
  
  // Collapse the editor after submission
  collapseEditor()
}

function createSimpleIssue() {
  const repoUrl = 'https://github.com/darkyy92/eliteredux-darky'
  
  const params = new URLSearchParams({
    template: 'ability-review.yml',
    title: `[Ability Review] ${abilityInfo.value.name} (ID: ${abilityInfo.value.id})`,
    'ability-name': abilityInfo.value.name,
    'ability-id': abilityInfo.value.id,
    'source-file': `knowledge/abilities/${abilityInfo.value.filename}.md`,
    'codex-url': window.location.href,
    labels: 'codex-submission'
  })
  
  const url = `${repoUrl}/issues/new?${params.toString()}`
  window.open(url, '_blank')
}

function retryLoad() {
  loadOriginalContent()
}

// Keyboard shortcuts
function handleKeydown(event) {
  if (isExpanded.value) {
    // Ctrl/Cmd + S to submit
    if ((event.ctrlKey || event.metaKey) && event.key === 's') {
      event.preventDefault()
      if (hasChanges.value && isValidContent.value) {
        submitToGitHub()
      }
    }
    // Escape to close
    if (event.key === 'Escape') {
      event.preventDefault()
      collapseEditor()
    }
  }
}

// Initialize ability info on mount
onMounted(() => {
  // Add keyboard event listeners
  document.addEventListener('keydown', handleKeydown)
  const pageTitle = page.value.title || ''
  const pageUrl = page.value.relativePath || ''
  
  // Try to extract from title first (e.g., "Speed Boost - Ability ID 3")
  const titleMatch = pageTitle.match(/^(.+?)\s*-\s*Ability ID\s*(\d+)$/i)
  if (titleMatch) {
    abilityInfo.value.name = titleMatch[1].trim()
    abilityInfo.value.id = titleMatch[2]
    abilityInfo.value.title = pageTitle
  }
  
  // Extract filename from URL (e.g., "abilities/3_speed_boost.md")
  const filenameMatch = pageUrl.match(/abilities\/(.+?)\.md$/)
  if (filenameMatch) {
    abilityInfo.value.filename = filenameMatch[1]
    
    // If we don't have name/ID from title, try to extract from filename
    if (!abilityInfo.value.id || !abilityInfo.value.name) {
      const [id, ...nameParts] = filenameMatch[1].split('_')
      abilityInfo.value.id = id
      abilityInfo.value.name = nameParts.join(' ').replace(/\b\w/g, char => char.toUpperCase())
    }
  }
})

// Cleanup event listeners
onUnmounted(() => {
  document.removeEventListener('keydown', handleKeydown)
})
</script>

<style scoped>
.inline-editor {
  margin: 1rem 0 2rem 0;
  font-family: var(--vp-font-family-base);
}

/* Collapsed State */
.editor-collapsed {
  background: linear-gradient(135deg, var(--vp-c-bg-soft) 0%, var(--vp-c-bg-mute) 100%);
  border: 2px solid var(--vp-c-border);
  border-radius: 12px;
  padding: 1.5rem;
  transition: all 0.3s ease;
}

.editor-collapsed:hover {
  border-color: var(--vp-c-brand);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.editor-header {
  text-align: center;
}

.editor-title {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  margin-bottom: 0.5rem;
}

.editor-icon {
  font-size: 1.2rem;
}

.editor-title h4 {
  margin: 0;
  color: var(--vp-c-text-1);
  font-size: 1.2rem;
  font-weight: 600;
}

.editor-subtitle {
  color: var(--vp-c-text-2);
  margin: 0 0 1rem 0;
  font-size: 0.9rem;
  line-height: 1.4;
}

.editor-actions {
  display: flex;
  gap: 0.75rem;
  justify-content: center;
  flex-wrap: wrap;
}

/* Expanded State */
.editor-expanded {
  background: var(--vp-c-bg);
  border: 2px solid var(--vp-c-brand);
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
}

.editor-header-expanded {
  background: var(--vp-c-brand);
  color: white;
  padding: 1rem;
}

.editor-title-expanded {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 0.5rem;
}

.editor-title-expanded h4 {
  margin: 0;
  font-size: 1.1rem;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.editor-close {
  background: rgba(255, 255, 255, 0.2);
  border: none;
  color: white;
  width: 2rem;
  height: 2rem;
  border-radius: 50%;
  font-size: 1.2rem;
  cursor: pointer;
  transition: background 0.2s;
}

.editor-close:hover {
  background: rgba(255, 255, 255, 0.3);
}

.editor-warning {
  background: rgba(255, 255, 255, 0.1);
  padding: 0.5rem;
  border-radius: 6px;
  font-size: 0.85rem;
}

.char-status {
  margin-top: 0.25rem;
  font-size: 0.8rem;
}

.char-advice {
  margin-left: 0.5rem;
  opacity: 0.9;
}

/* Loading State */
.editor-loading {
  padding: 3rem;
  text-align: center;
  color: var(--vp-c-text-2);
}

.loading-spinner {
  width: 2rem;
  height: 2rem;
  border: 3px solid var(--vp-c-border);
  border-top: 3px solid var(--vp-c-brand);
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 1rem;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* Tabs */
.editor-tabs {
  display: flex;
  background: var(--vp-c-bg-soft);
  border-bottom: 1px solid var(--vp-c-border);
}

.tab {
  flex: 1;
  padding: 0.75rem 1rem;
  background: none;
  border: none;
  cursor: pointer;
  transition: all 0.2s;
  font-weight: 500;
  color: var(--vp-c-text-2);
}

.tab:hover {
  background: var(--vp-c-bg-mute);
  color: var(--vp-c-text-1);
}

.tab.active {
  background: var(--vp-c-bg);
  color: var(--vp-c-brand);
  border-bottom: 2px solid var(--vp-c-brand);
}

/* Editor Content */
.editor-content {
  padding: 1rem;
}

.editor-textarea {
  width: 100%;
  min-height: 400px;
  padding: 1rem;
  border: 1px solid var(--vp-c-border);
  border-radius: 6px;
  font-family: 'JetBrains Mono', 'Fira Code', 'Monaco', monospace;
  font-size: 0.9rem;
  line-height: 1.5;
  resize: vertical;
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-1);
}

.editor-textarea:focus {
  outline: none;
  border-color: var(--vp-c-brand);
  box-shadow: 0 0 0 2px rgba(var(--vp-c-brand-rgb), 0.2);
}

.editor-stats {
  display: flex;
  justify-content: space-between;
  margin-top: 1rem;
  padding: 0.75rem;
  background: var(--vp-c-bg-mute);
  border-radius: 6px;
  font-size: 0.85rem;
}

.stat-label {
  font-weight: 600;
  color: var(--vp-c-text-2);
}

.char-count-value {
  font-weight: 600;
}

.char-count-low {
  color: #ed8936; /* Orange/yellow for too short (< 280) - warning */
}

.char-count-good {
  color: #48bb78; /* Green for perfect range (280-300) */
}

.char-count-high {
  color: #f56565; /* Red for too long (> 300) - error */
}

.changes-value {
  color: var(--vp-c-brand);
  font-weight: 600;
}

/* Preview */
.editor-preview {
  padding: 1rem;
  max-height: 500px;
  overflow-y: auto;
}

.preview-content {
  line-height: 1.6;
  color: var(--vp-c-text-1);
}

/* Diff */
.editor-diff {
  padding: 1rem;
}

.no-changes {
  text-align: center;
  color: var(--vp-c-text-2);
  padding: 2rem;
}

.diff-section {
  margin-bottom: 1rem;
}

.diff-section h5 {
  margin: 0 0 0.5rem 0;
  color: var(--vp-c-text-1);
  font-size: 0.9rem;
  font-weight: 600;
}

.diff-summary {
  list-style: none;
  padding: 0;
  margin: 0;
}

.diff-summary li {
  padding: 0.25rem 0.5rem;
  margin: 0.25rem 0;
  border-radius: 4px;
  font-size: 0.85rem;
}

.diff-summary li.addition {
  background: rgba(72, 187, 120, 0.1);
  color: #48bb78;
}

.diff-summary li.deletion {
  background: rgba(245, 101, 101, 0.1);
  color: #f56565;
}

.diff-visual {
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-border);
  border-radius: 6px;
  padding: 1rem;
  font-family: 'JetBrains Mono', 'Fira Code', monospace;
  font-size: 0.8rem;
  max-height: 400px;
  overflow: auto;
}

.diff-lines {
  line-height: 1.4;
}

.diff-added {
  background: rgba(72, 187, 120, 0.15);
  color: #2d543d;
}

.diff-removed {
  background: rgba(245, 101, 101, 0.15);
  color: #742a2a;
}

.diff-unchanged {
  color: var(--vp-c-text-2);
}

/* Actions */
.editor-actions-expanded {
  padding: 1rem;
  background: var(--vp-c-bg-soft);
  border-top: 1px solid var(--vp-c-border);
  display: flex;
  gap: 0.75rem;
  justify-content: flex-end;
}

.keyboard-hints {
  padding: 0.5rem 1rem;
  background: var(--vp-c-bg-soft);
  border-top: 1px solid var(--vp-c-border);
  text-align: center;
  color: var(--vp-c-text-2);
}

/* Buttons */
.editor-button {
  padding: 0.5rem 1rem;
  border: 1px solid;
  border-radius: 6px;
  font-size: 0.9rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 0.3rem;
}

.editor-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.editor-button.primary {
  background: var(--vp-c-brand);
  color: white;
  border-color: var(--vp-c-brand);
}

.editor-button.primary:hover:not(:disabled) {
  background: var(--vp-c-brand-dark);
  border-color: var(--vp-c-brand-dark);
}

.editor-button.secondary {
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  border-color: var(--vp-c-border);
}

.editor-button.secondary:hover {
  background: var(--vp-c-bg-mute);
  border-color: var(--vp-c-border-hard);
}

.editor-button.tertiary {
  background: transparent;
  color: var(--vp-c-text-2);
  border-color: transparent;
}

.editor-button.tertiary:hover {
  color: var(--vp-c-text-1);
  border-color: var(--vp-c-border);
}

/* Error State */
.editor-error {
  padding: 1rem;
  background: rgba(245, 101, 101, 0.1);
  border: 1px solid rgba(245, 101, 101, 0.3);
  border-radius: 6px;
  margin: 1rem;
  color: #742a2a;
}

/* Mobile Responsiveness */
@media (max-width: 640px) {
  .inline-editor {
    margin: 0.5rem 0 1.5rem 0;
  }
  
  .editor-collapsed {
    padding: 1rem;
  }
  
  .editor-actions {
    flex-direction: column;
  }
  
  .editor-button {
    width: 100%;
    justify-content: center;
  }
  
  .editor-stats {
    flex-direction: column;
    gap: 0.5rem;
  }
  
  .editor-actions-expanded {
    flex-direction: column;
  }
  
  .editor-tabs {
    font-size: 0.85rem;
  }
  
  .tab {
    padding: 0.5rem;
  }
  
  .editor-textarea {
    min-height: 300px;
    font-size: 0.85rem;
  }
}

/* Dark theme adjustments */
html.dark .diff-added {
  background: rgba(72, 187, 120, 0.2);
  color: #68d391;
}

html.dark .diff-removed {
  background: rgba(245, 101, 101, 0.2);
  color: #fc8181;
}

html.dark .editor-error {
  background: rgba(245, 101, 101, 0.15);
  color: #fc8181;
}
</style>