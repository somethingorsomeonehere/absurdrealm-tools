import { defineConfig } from 'vitepress'
import { readdirSync, readFileSync, existsSync } from 'fs'
import { join, basename } from 'path'
import { fileURLToPath } from 'url'
import matter from 'gray-matter'

const __dirname = fileURLToPath(new URL('.', import.meta.url))

// Function to load status data from JSON API
function loadStatusData() {
  const statusFile = join(__dirname, 'ability-status.json')
  if (!existsSync(statusFile)) {
    console.warn('Status API file not found, using fallback indicators')
    return null
  }
  
  try {
    const content = readFileSync(statusFile, 'utf-8')
    return JSON.parse(content)
  } catch (e) {
    console.warn('Error loading status data:', e)
    return null
  }
}

// Function to get all ability files with enhanced status indicators
function getAbilityFiles() {
  // Load status data
  const statusData = loadStatusData()
  
  // Try docs/abilities first (copied files)
  let abilitiesDir = join(__dirname, '../abilities')
  let files = []
  
  try {
    files = readdirSync(abilitiesDir)
      .filter(file => {
        // Only include files that match the pattern: number_name.md
        const isAbilityFile = /^\d+_/.test(file) && file.endsWith('.md')
        return isAbilityFile
      })
  } catch {
    // If that fails, try reading from knowledge/abilities
    try {
      abilitiesDir = join(__dirname, '../../../knowledge/abilities')
      files = readdirSync(abilitiesDir)
        .filter(file => {
          // Only include files that match the pattern: number_name.md
          const isAbilityFile = /^\d+_/.test(file) && file.endsWith('.md')
          return isAbilityFile
        })
    } catch {
      console.warn('No ability files found in either location')
      return []
    }
  }
  
  // Sort files numerically by the ID prefix
  files.sort((a, b) => {
    const numA = parseInt(a.split('_')[0])
    const numB = parseInt(b.split('_')[0])
    return numA - numB
  })
  
  return files.map(file => {
    const nameWithoutExt = file.replace('.md', '')
    const [id, ...nameParts] = nameWithoutExt.split('_')
    const abilityId = parseInt(id)
    
    // Title case each word in the ability name
    const formattedName = nameParts
      .join(' ')
      .replace(/\b\w/g, char => char.toUpperCase())
    
    // Get status indicator from API data
    let statusIndicator = ''
    if (statusData && statusData.indicators && statusData.indicators[abilityId]) {
      statusIndicator = statusData.indicators[abilityId].indicator + ' '
    } else {
      // Fallback: check frontmatter for legacy compatibility
      try {
        const filePath = join(abilitiesDir, file)
        const content = readFileSync(filePath, 'utf-8')
        const { data } = matter(content)
        statusIndicator = data.status === 'reviewed' ? '✅ ' : '🟠 '
      } catch (e) {
        statusIndicator = '🟠 '
      }
    }
    
    const displayText = `${statusIndicator}${id} ${formattedName}`
    
    return {
      text: displayText,
      link: `/abilities/${nameWithoutExt}`
    }
  })
}

export default defineConfig({
  title: 'Elite Redux Ability Codex',
  description: 'Comprehensive documentation of all Elite Redux abilities',
  
  // Base URL for custom domain
  base: '/',
  
  // Dark theme by default
  appearance: 'dark',
  
  // Head configuration for favicon and SEO blocking
  head: [
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/favicon.svg' }],
    ['link', { rel: 'icon', type: 'image/png', sizes: '32x32', href: '/favicon-32x32.png' }],
    ['link', { rel: 'icon', type: 'image/png', sizes: '16x16', href: '/favicon-16x16.png' }],
    ['link', { rel: 'apple-touch-icon', sizes: '180x180', href: '/apple-touch-icon.png' }],
    ['meta', { name: 'theme-color', content: '#4f46e5' }],
    
    // Block search engines and crawlers
    ['meta', { name: 'robots', content: 'noindex, nofollow, noarchive, nosnippet, noimageindex, notranslate' }],
    ['meta', { name: 'googlebot', content: 'noindex, nofollow, noarchive, nosnippet, noimageindex, notranslate' }],
    ['meta', { name: 'bingbot', content: 'noindex, nofollow, noarchive, nosnippet, noimageindex, notranslate' }],
    ['meta', { name: 'slurp', content: 'noindex, nofollow, noarchive, nosnippet, noimageindex, notranslate' }],
    ['meta', { 'http-equiv': 'X-Robots-Tag', content: 'noindex, nofollow, noarchive, nosnippet' }],
    
    // Prevent caching and archiving
    ['meta', { 'http-equiv': 'Cache-Control', content: 'no-cache, no-store, must-revalidate' }],
    ['meta', { 'http-equiv': 'Pragma', content: 'no-cache' }],
    ['meta', { 'http-equiv': 'Expires', content: '0' }]
  ],
  
  // Theme configuration
  themeConfig: {
    // Enable search
    search: {
      provider: 'local',
      options: {
        placeholder: 'Search abilities...',
        detailedView: true
      }
    },
    
    // Navigation
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Abilities', link: '/abilities/' },
      { text: 'Contributing', link: '/contributing' },
      { text: 'Discord', link: 'http://discord.elite-redux.com' },
      { text: 'Pokédex', link: 'http://dex.elite-redux.com' },
      { text: 'Wiki', link: 'https://wiki.elite-redux.com' }
    ],
    
    // Sidebar with all abilities
    sidebar: {
      '/abilities/': [
        {
          text: 'All Abilities',
          collapsed: false,
          items: getAbilityFiles()
        }
      ]
    },
    
    // Social links
    socialLinks: [],
    
    // Footer
    footer: {
      message: 'Elite Redux Ability Codex',
      copyright: 'Elite Redux Development Team'
    }
  },
  
  // Markdown configuration
  markdown: {
    theme: {
      light: 'github-light',
      dark: 'github-dark'
    }
  },
  
  // Source directory configuration
  srcDir: '.'
})