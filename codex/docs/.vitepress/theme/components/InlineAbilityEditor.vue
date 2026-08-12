<template>
  <div v-if="isAbilityPage" class="inline-editor">
    <!-- Collapsed State -->
    <div v-if="!isExpanded" class="editor-collapsed">
      <div class="editor-header">
        <div class="editor-title">
          <h4>Suggest Improvements</h4>
        </div>
        <p class="editor-subtitle">
          Help improve {{ abilityInfo.name }} (ID: {{ abilityInfo.id }}) - Spot errors or suggest better descriptions
        </p>
        <div class="editor-actions">
          <button 
            v-if="!isReviewed"
            class="editor-button approve"
            @click="approveAbility"
            :disabled="approving"
          >
            {{ approving ? 'Approving...' : 'Approve This Ability' }}
          </button>
          <button 
            class="editor-button primary"
            @click="expandEditor"
            :disabled="loading"
            title="Edit this ability (E)"
          >
            <span>{{ loading ? 'Loading...' : 'Edit This Ability' }}</span>
            <kbd v-if="!loading" class="button-kbd">E</kbd>
          </button>
          <button 
            class="editor-button secondary"
            @click="createSimpleIssue"
          >
            Report Issue
          </button>
        </div>
      </div>
    </div>

    <!-- Expanded State -->
    <div v-if="isExpanded" class="editor-expanded">
      <div class="editor-header-expanded">
        <div class="editor-title-expanded">
          <h4>Editing: {{ abilityInfo.name }} (ID: {{ abilityInfo.id }})</h4>
          <button class="editor-close" @click="collapseEditor">×</button>
        </div>
        
        <div class="editor-warning">
          <strong>Character Limit:</strong> Extended descriptions must be max 300 characters (GBA hardware limit)
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
              <span v-if="!loading && editedContent" :class="['char-count-value', getCharCountClass()]">
                {{ extendedDescCharCount }} / 300 chars
              </span>
              <span v-else class="char-count-value">
                Loading...
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
            :disabled="!hasChanges || !isValidContent || loading"
            :title="hasChanges && isValidContent ? 'Save changes directly (Ctrl+S or Cmd+S)' : 'Make valid changes to save'"
          >
            {{ loading ? 'Saving...' : 'Save Changes' }}
          </button>
          <button 
            class="editor-button secondary"
            @click="resetContent"
            title="Reset all changes"
          >
            Reset Changes
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
          <small><strong>Ctrl+S</strong> (or <strong>Cmd+S</strong>) to save • <strong>Esc</strong> to close</small>
        </div>
      </div>

      <!-- Error State -->
      <div v-if="error" class="editor-error">
        <p><strong>Error:</strong> {{ error }}</p>
        <button class="editor-button secondary" @click="retryLoad">Retry</button>
      </div>
    </div>
    
    <!-- Save Modal -->
    <Modal
      v-model:isOpen="saveModalOpen"
      title="Save Changes"
      :message="saveModalMessage"
      confirmText="Save Changes"
      cancelText="Cancel"
      @confirm="handleSaveConfirm"
      @cancel="saveModalOpen = false"
    />
    
    <!-- Approve Modal -->
    <Modal
      v-model:isOpen="approveModalOpen"
      title="Approve Ability"
      :message="approveModalMessage"
      confirmText="Approve Ability"
      cancelText="Cancel"
      :danger="true"
      @confirm="handleApproveConfirm"
      @cancel="approveModalOpen = false"
    />
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, watch, nextTick } from 'vue'
import { useData } from 'vitepress'
import * as Diff from 'diff'
import Modal from './Modal.vue'
import { useUIState } from '../composables/useUIState'

const { page } = useData()
const { showToast, showConfirm, showSuccess, showError, showUndoableSuccess } = useUIState()

// State
const isExpanded = ref(false)
const loading = ref(false)
const error = ref('')
const activeTab = ref('edit')
const originalContent = ref('')
const editedContent = ref('')
const approving = ref(false)

// Modal states
const saveModalOpen = ref(false)
const approveModalOpen = ref(false)

// Modal messages
const saveModalMessage = computed(() => {
  return `Are you sure you want to save changes to "${abilityInfo.value.name}"?\n\nExtended description: ${extendedDescCharCount.value} characters (max 300)`
})

const approveModalMessage = computed(() => {
  return `Are you sure you want to approve "${abilityInfo.value.name}" (ID: ${abilityInfo.value.id})?\n\nThis will mark the ability as reviewed and include it in the game.\n\nPlease ensure:\n• The extended description is accurate\n• Character count is under 300 (currently: ${extendedDescCharCount.value})\n• No typos or errors exist`
})

// GitHub configuration for direct commits (trusted staff only)
// The token should be set in .env.local as VITE_GITHUB_TOKEN
const GITHUB_TOKEN = import.meta.env.VITE_GITHUB_TOKEN || ''
const REPO_OWNER = 'darkyy92'
const REPO_NAME = 'eliteredux-darky'


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

// Helper function to strip frontmatter from content
function stripFrontmatter(content) {
  // Check if content starts with frontmatter
  if (content.startsWith('---\n')) {
    // Find the closing --- for frontmatter
    const match = content.match(/^---\n(.*?)\n---\n(.*)$/s)
    if (match) {
      // Return only the content after frontmatter
      return match[2]
    }
  }
  return content
}

// Helper function to update status in frontmatter
function updateStatusToReviewed(content) {
  if (!content.startsWith('---\n')) return content
  
  const match = content.match(/^---\n(.*?)\n---\n(.*)$/s)
  if (!match) return content
  
  let frontmatter = match[1]
  const body = match[2]
  
  // Update status to reviewed
  if (frontmatter.includes('status:')) {
    frontmatter = frontmatter.replace(/status:\s*[^\n]+/, 'status: reviewed')
  } else {
    // Add status if it doesn't exist
    frontmatter += '\nstatus: reviewed'
  }
  
  // Update character count
  const charCount = extractExtendedDescription(content).length
  if (frontmatter.includes('character_count:')) {
    frontmatter = frontmatter.replace(/character_count:\s*[^\n]+/, `character_count: ${charCount}`)
  } else {
    // Add character_count if it doesn't exist
    frontmatter += `\ncharacter_count: ${charCount}`
  }
  
  return `---\n${frontmatter}\n---\n${body}`
}

// Improved function to extract extended description
function extractExtendedDescription(content) {
  if (!content) return ''
  
  // Strip frontmatter first
  const contentWithoutFm = stripFrontmatter(content)
  
  // Find the start of Extended In-Game Description section
  const startMatch = contentWithoutFm.match(/## Extended In-Game Description.*?\n/)
  if (!startMatch) return ''
  
  const startIndex = startMatch.index + startMatch[0].length
  let remainingContent = contentWithoutFm.substring(startIndex)
  
  // Skip the instruction line if present (with or without asterisks)
  const instructionMatch = remainingContent.match(/^(?:\*[^\n]*\*|For use in[^\n]*)\n\n/)
  if (instructionMatch) {
    remainingContent = remainingContent.substring(instructionMatch[0].length)
  } else if (remainingContent.startsWith('\n')) {
    // No instruction line, just skip the blank line
    remainingContent = remainingContent.substring(1)
  }
  
  // Find where the description ends
  // Look for: Character count line, next section header, or end of content
  const endPatterns = [
    /\n\*?Character count:/,
    /\n## /,
    /\n### /,
    /\n---/
  ]
  
  let endIndex = remainingContent.length
  for (const pattern of endPatterns) {
    const match = remainingContent.match(pattern)
    if (match && match.index < endIndex) {
      endIndex = match.index
    }
  }
  
  // Extract the description
  let description = remainingContent.substring(0, endIndex).trim()
  
  // Remove any trailing newlines but preserve internal spacing
  description = description.replace(/\n+$/, '')
  
  return description
}

// Computed properties
const hasChanges = computed(() => {
  return originalContent.value !== editedContent.value
})

const isReviewed = computed(() => {
  // Check frontmatter for review status
  if (!originalContent.value) return false
  
  const frontmatterMatch = originalContent.value.match(/^---\n(.*?)\n---/s)
  if (frontmatterMatch) {
    return frontmatterMatch[1].includes('status: reviewed')
  }
  return false
})

const changeCount = computed(() => {
  if (!hasChanges.value) return 0
  // Strip frontmatter before comparing
  const originalWithoutFm = stripFrontmatter(originalContent.value)
  const editedWithoutFm = stripFrontmatter(editedContent.value)
  const diff = Diff.diffLines(originalWithoutFm, editedWithoutFm)
  return diff.filter(part => part.added || part.removed).length
})

const extendedDescCharCount = computed(() => {
  // Don't compute if no content or still loading
  if (!editedContent.value || loading.value) {
    return 0
  }
  
  try {
    const description = extractExtendedDescription(editedContent.value)
    const count = description.length
    
    // Only log if we're in development mode
    if (import.meta.env.DEV) {
      console.log(`Character count for ${abilityInfo.value.name}: ${count} chars`)
      if (count > 1000) {
        console.warn('Suspiciously high character count. Description:', description.substring(0, 100) + '...')
      }
    }
    
    return count
  } catch (error) {
    console.error('Error computing character count:', error)
    return 0
  }
})

const isValidContent = computed(() => {
  const charCount = extendedDescCharCount.value
  return charCount > 0 && charCount <= 300
})

const previewHtml = computed(() => {
  // Simple markdown to HTML conversion for preview
  // Strip frontmatter first
  const contentWithoutFm = stripFrontmatter(editedContent.value)
  return contentWithoutFm
    .replace(/^# (.*$)/gm, '<h1>$1</h1>')
    .replace(/^## (.*$)/gm, '<h2>$1</h2>')
    .replace(/^### (.*$)/gm, '<h3>$1</h3>')
    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
    .replace(/\*(.*?)\*/g, '<em>$1</em>')
    .replace(/\n/g, '<br>')
})

const diffSummary = computed(() => {
  if (!hasChanges.value) return []
  
  // Strip frontmatter before comparing
  const originalWithoutFm = stripFrontmatter(originalContent.value)
  const editedWithoutFm = stripFrontmatter(editedContent.value)
  const diff = Diff.diffLines(originalWithoutFm, editedWithoutFm)
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
  
  // Strip frontmatter before comparing
  const originalWithoutFm = stripFrontmatter(originalContent.value)
  const editedWithoutFm = stripFrontmatter(editedContent.value)
  const diff = Diff.diffLines(originalWithoutFm, editedWithoutFm)
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
  if (count > 300) return 'char-count-high'   // Too long - red/orange  
  return 'char-count-good'                    // Valid range 1-300 - green
}

function getOriginalExtendedDescCharCount() {
  try {
    const description = extractExtendedDescription(originalContent.value)
    return description.length
  } catch (error) {
    return 0
  }
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
  
  // Prevent double-clicks
  if (loading.value) {
    console.log('Save already in progress, ignoring duplicate request')
    return
  }
  
  if (!GITHUB_TOKEN) {
    showError('Direct saving requires GitHub token configuration. Please use "Report Issue" instead.')
    return
  }
  
  // Show save modal
  saveModalOpen.value = true
}

async function handleSaveConfirm() {
  saveModalOpen.value = false
  
  // Create the save action to be executed after delay
  const executeSave = async () => {
    loading.value = true
    error.value = ''
    
    try {
    const filePath = `knowledge/abilities/${abilityInfo.value.filename}.md`
    const apiUrl = `https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}/contents/${filePath}`
    
    const saveTimestamp = new Date().toISOString()
    console.log(`[${saveTimestamp}] Starting save operation`)
    console.log('Saving to repository:', `${REPO_OWNER}/${REPO_NAME}`)
    console.log('File path:', filePath)
    console.log('API URL:', apiUrl)
    console.log('Token present:', GITHUB_TOKEN ? 'Yes' : 'No')
    
    // Get current file info from GitHub
    const response = await fetch(apiUrl, {
      headers: {
        'Authorization': `token ${GITHUB_TOKEN}`,
        'Accept': 'application/vnd.github.v3+json'
      }
    })
    
    console.log('Response status:', response.status)
    
    if (!response.ok) {
      const errorData = await response.json()
      console.error('GitHub API error:', errorData)
      throw new Error(`Failed to get file info: ${response.statusText}`)
    }
    
    const fileData = await response.json()
    
    // Update status to reviewed before saving
    const contentWithReviewedStatus = updateStatusToReviewed(editedContent.value)
    
    // Commit the updated content
    const commitResponse = await fetch(
      `https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}/contents/${filePath}`,
      {
        method: 'PUT',
        headers: {
          'Authorization': `token ${GITHUB_TOKEN}`,
          'Accept': 'application/vnd.github.v3+json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          message: `docs: Update ${abilityInfo.value.name} ability description`,
          content: btoa(unescape(encodeURIComponent(contentWithReviewedStatus))),
          sha: fileData.sha,
          branch: 'main'
        })
      }
    )
    
    if (!commitResponse.ok) {
      const errorData = await commitResponse.json()
      throw new Error(errorData.message || 'Failed to save changes')
    }
    
      // Update original content to reflect saved state (with reviewed status)
      originalContent.value = contentWithReviewedStatus
      editedContent.value = contentWithReviewedStatus
      
      // Hot reload disabled - awaiting full automated approval workflow
      // await updateAbilityStatus(abilityInfo.value.id, {
      //   status: 'reviewed',
      //   reviewed: true,
      //   written: true
      // })
      
      showSuccess(`Successfully saved changes to ${abilityInfo.value.name}!`)
      
    } catch (err) {
      console.error('Save error:', err)
      error.value = err.message || 'Failed to save changes'
      showError(`Failed to save changes: ${err.message}`)
    } finally {
      loading.value = false
    }
  }
  
  // Show undoable success notification and queue the save
  showUndoableSuccess(
    `Saving changes to ${abilityInfo.value.name}...`,
    executeSave,
    { duration: 5000 }
  )
  
  // Close editor immediately
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
  
  // For now, just open directly since it's less critical
  window.open(url, '_blank')
  showSuccess('Opening GitHub to create issue...', { duration: 2000 })
}

function retryLoad() {
  loadOriginalContent()
}

function approveAbility() {
  if (approving.value || isReviewed.value) return
  
  // Show approve modal
  approveModalOpen.value = true
}

async function handleApproveConfirm() {
  approveModalOpen.value = false
  
  // Create the approve action to be executed after delay
  const executeApprove = async () => {
    approving.value = true
    
    try {
    const filePath = `knowledge/abilities/${abilityInfo.value.filename}.md`
    
    // Step 1: Get current file content from GitHub
    const getResponse = await fetch(
      `https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}/contents/${filePath}`,
      {
        headers: {
          'Authorization': `token ${GITHUB_TOKEN}`,
          'Accept': 'application/vnd.github.v3+json'
        }
      }
    )
    
    if (!getResponse.ok) {
      throw new Error(`Failed to fetch file: ${getResponse.statusText}`)
    }
    
    const fileData = await getResponse.json()
    const currentContent = atob(fileData.content)
    
    // Step 2: Update frontmatter status
    const updatedContent = currentContent.replace(
      /status:\s*ai-generated/,
      'status: reviewed'
    )
    
    // Step 3: Commit the change
    const updateResponse = await fetch(
      `https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}/contents/${filePath}`,
      {
        method: 'PUT',
        headers: {
          'Authorization': `token ${GITHUB_TOKEN}`,
          'Accept': 'application/vnd.github.v3+json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          message: `Approved ability ${abilityInfo.value.id} ${abilityInfo.value.name}`,
          content: btoa(unescape(encodeURIComponent(updatedContent))),
          sha: fileData.sha,
          branch: 'main'
        })
      }
    )
    
    if (!updateResponse.ok) {
      throw new Error(`Failed to update file: ${updateResponse.statusText}`)
    }
    
    // Step 4: Update local content to reflect the change
    originalContent.value = updatedContent
    editedContent.value = updatedContent
    
    // Hot reload disabled - awaiting full automated approval workflow
    // await updateAbilityStatus(abilityInfo.value.id, {
    //   status: 'reviewed',
    //   reviewed: true,
    //   written: true
    // })
    
      // Step 5: Show success message
      showSuccess(`Successfully approved ${abilityInfo.value.name}!`)
      
      // Don't auto-reload since changes take up to 3 minutes to propagate
      
    } catch (error) {
      console.error('Error approving ability:', error)
      showError(`Failed to approve ability: ${error.message}`)
    } finally {
      approving.value = false
    }
  }
  
  // Show undoable success notification and queue the approval
  showUndoableSuccess(
    `Approving ${abilityInfo.value.name}...`,
    executeApprove,
    { duration: 5000 }
  )
}

// Keyboard shortcuts
function handleKeydown(event) {
  // Check if user is typing in an input field
  const isTyping = ['INPUT', 'TEXTAREA', 'SELECT'].includes(event.target.tagName)
  
  if (!isExpanded.value && isAbilityPage.value) {
    // 'E' key to open editor
    if (event.key === 'e' || event.key === 'E') {
      // Don't trigger if user is typing or using modifier keys
      if (!isTyping && !event.ctrlKey && !event.metaKey && !event.altKey) {
        event.preventDefault()
        expandEditor()
      }
    }
  } else if (isExpanded.value) {
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

// Function to update ability info from current page
function updateAbilityInfo() {
  const pageTitle = page.value.title || ''
  const pageUrl = page.value.relativePath || ''
  
  // Reset ability info
  abilityInfo.value = {
    id: '',
    name: '',
    filename: '',
    title: ''
  }
  
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
}

// Helper function to load content for review status check
async function loadContentForReviewStatus() {
  if (!isAbilityPage.value || !abilityInfo.value.filename || !GITHUB_TOKEN) return
  
  try {
    const filePath = `knowledge/abilities/${abilityInfo.value.filename}.md`
    const response = await fetch(
      `https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}/contents/${filePath}`,
      {
        headers: {
          'Authorization': `token ${GITHUB_TOKEN}`,
          'Accept': 'application/vnd.github.v3+json'
        }
      }
    )
    
    if (response.ok) {
      const data = await response.json()
      originalContent.value = atob(data.content)
      editedContent.value = originalContent.value
    }
  } catch (error) {
    console.log('Could not check review status:', error)
  }
}

// Watch for page changes with proper cleanup
watch(() => page.value.relativePath, async (newPath, oldPath) => {
  if (isAbilityPage.value && newPath !== oldPath) {
    // Reset ALL state when navigating
    isExpanded.value = false
    activeTab.value = 'edit'
    error.value = ''
    originalContent.value = ''
    editedContent.value = ''
    loading.value = false
    
    // Update ability info for new page
    await nextTick()
    updateAbilityInfo()
    
    // Load content to check review status
    await loadContentForReviewStatus()
    
    if (import.meta.env.DEV) {
      console.log(`Navigated from ${oldPath} to ${newPath}`)
    }
  }
})

// Initialize ability info on mount
onMounted(async () => {
  // Add keyboard event listeners
  document.addEventListener('keydown', handleKeydown)
  updateAbilityInfo()
  
  // Load content to check review status for approve button
  await loadContentForReviewStatus()
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

.char-warning {
  color: #ed8936;
  font-weight: 600;
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
  color: #ed8936; /* Orange/yellow - unused now */
}

.char-count-good {
  color: #48bb78; /* Green for valid range (1-300) */
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

.editor-button.approve {
  background: #48bb78;
  color: white;
  border-color: #48bb78;
}

.editor-button.approve:hover:not(:disabled) {
  background: #38a169;
  border-color: #38a169;
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