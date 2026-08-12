<template>
  <div v-if="isAbilityPage" class="suggest-edit">
    <div class="suggest-edit-container">
      <h4>🤝 Help Improve This Ability</h4>
      <p>Spot an error or have suggestions? Help make the codex better!</p>
      
      <div class="suggest-edit-buttons">
        <button 
          class="suggest-button primary"
          @click="createGitHubIssue"
          title="Report errors or suggest improvements"
        >
          📝 Suggest Edit
        </button>
      </div>
      
      <div class="suggest-edit-note">
        <small>
          Your feedback helps the community! Issues are reviewed by the Elite Redux team and can be converted to pull requests.
        </small>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useData } from 'vitepress'

const { page } = useData()

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

onMounted(() => {
  // Extract ability ID and name from page title or URL
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

function createGitHubIssue() {
  const repoUrl = 'https://github.com/Elite-Redux/eliteredux-source'
  
  // Use the ability review issue template with pre-filled data
  const params = new URLSearchParams({
    template: 'ability-review.yml',
    title: `[Ability Review] ${abilityInfo.value.name} (ID: ${abilityInfo.value.id})`,
    'ability-name': abilityInfo.value.name,
    'ability-id': abilityInfo.value.id,
    'source-file': `knowledge/abilities/${abilityInfo.value.filename}.md`,
    'codex-url': window.location.href
  })
  
  const url = `${repoUrl}/issues/new?${params.toString()}`
  
  // Just open directly
  window.open(url, '_blank')
}

</script>

<style scoped>
.suggest-edit {
  margin: 2rem 0;
  padding: 1.5rem;
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-border);
  border-radius: 8px;
  font-family: var(--vp-font-family-base);
}

.suggest-edit-container h4 {
  margin: 0 0 0.5rem 0;
  color: var(--vp-c-text-1);
  font-size: 1.1rem;
  font-weight: 600;
}

.suggest-edit-container p {
  margin: 0 0 1rem 0;
  color: var(--vp-c-text-2);
  font-size: 0.9rem;
  line-height: 1.4;
}

.suggest-edit-buttons {
  display: flex;
  gap: 0.75rem;
  margin-bottom: 1rem;
  flex-wrap: wrap;
}

.suggest-button {
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

.suggest-button.primary {
  background: var(--vp-c-brand);
  color: var(--vp-c-white);
  border-color: var(--vp-c-brand);
}

.suggest-button.primary:hover {
  background: var(--vp-c-brand-dark);
  border-color: var(--vp-c-brand-dark);
}

.suggest-button.secondary {
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  border-color: var(--vp-c-border);
}

.suggest-button.secondary:hover {
  background: var(--vp-c-bg-mute);
  border-color: var(--vp-c-border-hard);
}

.suggest-edit-note {
  color: var(--vp-c-text-3);
  font-size: 0.8rem;
  line-height: 1.3;
}

.suggest-edit-note small {
  font-size: inherit;
}

/* Dark theme adjustments */
html.dark .suggest-edit {
  background: var(--vp-c-bg-soft);
  border-color: var(--vp-c-border);
}

/* Mobile responsiveness */
@media (max-width: 640px) {
  .suggest-edit {
    margin: 1.5rem 0;
    padding: 1rem;
  }
  
  .suggest-edit-buttons {
    flex-direction: column;
  }
  
  .suggest-button {
    width: 100%;
    justify-content: center;
  }
}
</style>