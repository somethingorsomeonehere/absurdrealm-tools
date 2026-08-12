# Config Update Notes for Review Status Indicators

## Changes Made

1. **config-updated.mjs** - New version of config that reads frontmatter to show review status
   - Added `gray-matter` import to parse YAML frontmatter
   - Modified `getAbilityFiles()` to read each file's frontmatter
   - Added checkmark (✅) prefix for reviewed abilities in sidebar

2. **custom.css** - Added styles for review indicators
   - Styles to display checkmarks properly
   - Green color for the checkmark

## How to Enable

1. Install the gray-matter dependency:
   ```bash
   cd eliteredux-darky/codex
   npm install gray-matter
   ```

2. Replace the current config:
   ```bash
   mv docs/.vitepress/config.mjs docs/.vitepress/config-old.mjs
   mv docs/.vitepress/config-updated.mjs docs/.vitepress/config.mjs
   ```

3. Test locally:
   ```bash
   npm run dev
   ```

## How It Works

- When building the sidebar, the config now reads each ability file
- It checks the frontmatter for `status: reviewed`
- If reviewed, it adds a ✅ prefix to the ability name in the sidebar
- The CSS ensures the checkmark appears in green

## Notes

- Only abilities with `status: reviewed` in frontmatter will show the checkmark
- Abilities with `status: ai-generated` or no frontmatter won't have a checkmark
- The checkmark appears directly in the sidebar text for simplicity