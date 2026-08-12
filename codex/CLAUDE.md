# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

The Elite Redux Ability Codex is a VitePress-based documentation site that provides a searchable database of all game abilities with extended descriptions. It includes an inline editing system for community contributions.

## Commands

### Development
```bash
# Install dependencies (first time setup)
npm install

# Start development server (runs on port 5173)
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Sync abilities from knowledge/abilities/ directory
npm run copy-abilities
```

## Architecture

### Key Components

1. **VitePress Site Structure**
   - `docs/` - Content directory with all markdown files
   - `docs/.vitepress/` - VitePress configuration and theme
   - `docs/abilities/` - Auto-synced ability documentation (DO NOT EDIT DIRECTLY)
   - `scripts/copy-abilities.js` - Syncs abilities from `../knowledge/abilities/`

2. **Custom Vue Components**
   - `InlineAbilityEditor.vue` - In-browser markdown editor with character counting
   - `SuggestEdit.vue` - GitHub issue creation for community contributions

3. **Ability Sync System**
   - Abilities are maintained in `../knowledge/abilities/` (source of truth)
   - `copy-abilities.js` copies them to `docs/abilities/` before dev/build
   - Also runs `fix_ability_caps.py` to normalize title capitalization

### Character Count Requirements

Extended ability descriptions MUST be 280-300 characters INCLUDING spaces due to GBA hardware limitations. The inline editor enforces this with real-time character counting.

### Frontmatter Structure

Each ability file uses frontmatter for metadata:
```yaml
---
name: "Ability Name"
id: 123
description: "Short description"
extendedDescription: "280-300 character extended description..."
reviewed: true  # Shows ✅ in sidebar when true
---
```

## Common Tasks

### Updating Ability Documentation
1. Edit the source file in `../knowledge/abilities/`
2. Run `npm run dev` (automatically syncs)
3. Verify changes in the local site

### Testing Character Count Editor
The inline editor component calculates character count for the extended description. When testing:
- Ensure count shows correctly (e.g., "295/300")
- Verify the count updates as you type
- Check that it only counts the extendedDescription value

### Deployment
The site auto-deploys to GitHub Pages when changes are pushed to main branch. Custom domain: `codex.elite-redux.com`

## Keyboard Shortcuts

### Current Shortcuts
- **E** - Open the ability editor (when on an ability page)
- **Ctrl+S / Cmd+S** - Save changes (when editor is open)
- **Escape** - Close editor, modals, or dismiss toasts
- **Enter** - Confirm modal actions
- **Tab** - Navigate within modals (focus trapped)
- **Z** - Undo pending save/approve actions (when toast is visible)

### Implementation Learnings

When implementing keyboard shortcuts in Vue/VitePress:

1. **Check for Input Context**
   ```javascript
   const isTyping = ['INPUT', 'TEXTAREA', 'SELECT'].includes(event.target.tagName)
   ```
   Always check if the user is typing in a form field to avoid triggering shortcuts accidentally.

2. **Modifier Key Awareness**
   - Check for `event.ctrlKey`, `event.metaKey`, `event.altKey` to avoid conflicts
   - Use both `event.key === 'e'` and `event.key === 'E'` for case-insensitive matching

3. **State-Based Shortcuts**
   - Different shortcuts should be active in different states (collapsed vs expanded editor)
   - Use conditional logic: `if (!isExpanded.value && isAbilityPage.value)`

4. **Visual Hints**
   - Add `title` attributes to buttons: `title="Edit this ability (E)"`
   - Include visible keyboard hints: `<kbd>E</kbd>` styled elements
   - Show hints near relevant UI elements for better discoverability

5. **Event Handling Best Practices**
   - Always `event.preventDefault()` for handled shortcuts
   - Register/unregister listeners in `onMounted`/`onUnmounted` lifecycle hooks
   - Use document-level listeners for global shortcuts

### UI Component Integration

The codex now uses inline UI components instead of browser popups:
- **Modal.vue** - Replaces `confirm()` dialogs
- **Toast.vue** - Replaces `alert()` messages
- **UIProvider.vue** - Manages global UI state
- **useUIState.js** - Composable for UI interactions

This solves Firefox popup blocking issues and provides better UX with full keyboard support.

### UNDO Feature Implementation

The codex now includes an UNDO feature for save/approve actions:

1. **Delayed Execution**: GitHub API calls are delayed by 5 seconds
2. **Undo Toast**: Shows "Undo (Z)" button during the delay
3. **Keyboard Support**: Press 'Z' to cancel the pending action
4. **Simple Implementation**:
   - `showUndoableSuccess()` in useUIState.js handles the delay
   - Single pending action at a time (new actions cancel previous)
   - Toast progress bar shows remaining time
5. **User Benefits**:
   - Prevents accidental saves/approvals
   - No immediate commits to GitHub
   - Time to reconsider actions

## Password Protection

The codex is now protected with a password gate system:
- **Authentication**: Client-side verification with 1-month session persistence
- **Modern UI**: Clean, rounded design with glassmorphism effects
- **Bot Blocking**: Comprehensive robots.txt and meta tags to prevent search engine indexing
- **Testing Logout**: Press `Ctrl+Shift+L` to logout for testing purposes
- **Password**: Contact the project maintainer for access credentials

## Important Notes

- Never edit files in `docs/abilities/` directly - they are auto-generated
- The inline editor uses regex to parse frontmatter - be careful with complex markdown
- Character counts ALWAYS include spaces (GBA renders spaces as tiles)
- The site uses dark theme by default but supports theme switching
- **Site is password protected** - contact maintainer for access credentials

## Auto-Generated File System & Conflict Resolution

### Critical Files and Data Flow
The ability documentation system uses a specific data flow that MUST be understood to avoid data loss:

#### Source of Truth (SAFE TO EDIT)
- `../knowledge/abilities/*.md` - Individual ability documentation files
- These files contain frontmatter with metadata and full documentation
- All manual edits should ONLY be made to these files

#### Auto-Generated Files (NEVER EDIT MANUALLY)
- `../knowledge/extended_ability_descriptions/progress.md` - Progress tracking table
- `docs/.vitepress/ability-status.json` - API data for inline editor
- Generated via GitHub Actions on every push to main

#### Data Flow Chain
1. **Individual ability files** (`../knowledge/abilities/*.md`) 
2. **GitHub Actions triggers** on push to main
3. **`generate_progress.py`** creates progress.md from ability files
4. **`generate_status_api.py`** creates ability-status.json from progress.md
5. **Codex site** uses ability-status.json for inline editor functionality

### Git Conflict Resolution Protocol

When encountering stash/merge conflicts with auto-generated files:

1. **ALWAYS keep upstream versions** of auto-generated files:
   ```bash
   git checkout --theirs ../knowledge/extended_ability_descriptions/progress.md
   git checkout --theirs docs/.vitepress/ability-status.json
   ```

2. **Only commit source file changes**:
   - Individual ability files with special character fixes
   - Manual script improvements (generate_progress.py, InlineAbilityEditor.vue)
   - Direct documentation edits

3. **Character encoding fixes for GBA compatibility**:
   - Replace special characters: "é" → "é", "ö" → "ö", "÷" → "÷"
   - Update generate_progress.py with `encoding='utf-8', errors='replace'`
   - Fix InlineAbilityEditor.vue UTF-8 encoding: `btoa(unescape(encodeURIComponent(content)))`

### Common Conflict Scenarios

#### Scenario 1: Stashed Changes After Extended Period
- **Problem**: Others committed new ability progress while your changes were stashed
- **Solution**: Restore stash, resolve conflicts by keeping upstream auto-generated files
- **Key**: Your special character fixes in source files are preserved, others' progress is not lost

#### Scenario 2: Character Encoding Issues
- **Problem**: Special characters causing display/compilation issues
- **Solution**: Fix in source files only, let automation regenerate tracking files
- **Never**: Manually edit progress.md or ability-status.json

### UTF-8 Encoding Best Practices

#### Python Scripts
```python
with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()
```

#### JavaScript (InlineAbilityEditor.vue)
```javascript
content: btoa(unescape(encodeURIComponent(updatedContent)))
```

### Normal Workflow
1. Edit individual ability files in `../knowledge/abilities/*.md`
2. Push changes to main branch
3. GitHub Actions automatically regenerates tracking files
4. **No manual script execution needed**

### Debugging Automation Issues (Optional)

If auto-generated files seem incorrect after GitHub Actions runs:
1. Check GitHub Actions logs for the latest main branch push
2. Verify individual ability files have correct frontmatter
3. **Optional**: Run `generate_progress.py` locally for debugging only
4. Never manually fix the output - fix the source files and push again

## Future Enhancement: Real-Time Updates

Real-time updates are currently disabled. The planned automated approval workflow (see `/plans/automated_approval_workflow/`) will provide instant updates without the polling issues.