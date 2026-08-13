# Absurd Realm Tools

This repository contains AI-assisted development tools, scripts, and documentation for the EliteRedux project.

## Contents

- **`knowledge/`** - Project knowledge base and documentation
- **`plans/`** - Development plans and specifications
- **`scripts/`** - Utility scripts for various tasks
  - `ability_tools/` - Scripts for ability management
  - `trainer_tools/` - Scripts for trainer management
  - `wiki_tools/` - Scripts for wiki management
- **`codex/`** - Elite Redux Ability Codex website (VitePress documentation site)

**Note**: The `.claude/` folder must remain in the main repository (not this submodule) for slash commands to work properly.

## Usage

This repository is used as a git submodule in the main EliteRedux project. It keeps AI-related development files separate from the main codebase while still allowing the AI tool to access them.

## Elite Redux Ability Codex

The `codex/` directory contains a modern, searchable documentation website for all Elite Redux abilities.

### Features
- 🌑 Beautiful dark theme optimized for readability
- 🔍 Built-in search functionality (press Ctrl/Cmd + K)
- 📱 Mobile-first responsive design
- 🔄 Automatically includes all markdown files from `knowledge/abilities/`
- ⚡ Fast static site powered by VitePress

### Local Development
```bash
cd codex
npm install  # First time only
npm run dev  # Start development server
```
Then open http://localhost:5173/absurdrealm-tools/ in your browser.

### Live Website
The documentation is automatically deployed to GitHub Pages:
https://somethingorsomeonehere.github.io/absurdrealm-tools/

The site automatically rebuilds when:
- New ability files are added to `knowledge/abilities/`
- Any changes are made to the codex configuration
- Changes are pushed to the main branch

## Setup

To use this as a submodule in the main repository:

```bash
git submodule add https://github.com/YOUR_USERNAME/absurdrealm-tools.git absurdrealm-tools
```# absurdrealm-tools
