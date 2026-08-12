# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Quick Commands

### Git Sync (Claude Code Slash Command) - RECOMMENDED
```
/project:git-sync
```
This AI-powered slash command will:
- Analyze your actual code changes to understand what was modified
- Create intelligent, contextual commit messages (not just file lists)
- Handle pull, commit, and push operations automatically
- Use conventional commit format (feat:, fix:, docs:, etc.) when appropriate

Example commit messages the AI might generate:
- `feat: Add Wiki tutorial entry to Littleroot NPC after Talk to Nurse Joy`
- `fix: Correct tutorial menu case numbering after Wiki insertion`
- `refactor: Move trainer tools from tools/ to scripts/ directory`

You also have a personal version available across all projects:
```
/user:git-sync
```

### Build ROM (Claude Code Slash Command)
```
/project:build
```
Intelligently builds the ROM, handling common issues like:
- Running `make clean` if needed
- Adjusting CPU core count
- Providing specific error guidance
- Confirming successful builds

### Analyze Ability (Claude Code Slash Command)
```
/project:analyze-ability {ability_name}
```
Deep analysis of ability mechanics with code research:
- Checks if ability is already documented
- Finds implementation in abilities.cc
- Creates extended descriptions (280-300 chars)
- Updates documentation with frontmatter

## Build Commands

### Building the ROM
```bash
# First-time setup: Install agbcc compiler
git clone https://github.com/pret/agbcc
cd agbcc
./build.sh
./install.sh ../eliteredux-source
cd ..

# Build the ROM
# Replace X with number of CPU cores (e.g., -j24 for 24 cores, -j10 for Mac M4 Pro)
# Note: Both 'make' and 'make modern' build with modern GCC - they are equivalent
make -jX
# OR
make modern -jX

# macOS Build Instructions (TESTED AND WORKING!)
# See eliteredux-darky/knowledge/macos_compilation.md for complete guide
# Key commands:
xattr -d com.apple.quarantine tools/poryscript/poryscript  # Remove security warning (one-time)
make mostlyclean  # NEVER use 'make clean' - it removes tools!
make -j4          # Use -j4 to avoid memory issues with poryscript

# If you encounter compilation errors:
# Option 1: Use mostlyclean (preserves tools)
make mostlyclean
make -jX

# Option 2: Use the provided scripts
./eliteredux-darky/scripts/clean_build.sh  # Cleans ROM files, keeps tools
./eliteredux-darky/scripts/smart_build.sh  # Auto-builds tools if needed, then ROM
./eliteredux-darky/scripts/smart_build.sh 10  # Specify core count

# Option 3: Full clean (removes everything including tools)
make clean  # This removes tools too - avoid unless necessary
make tools  # Rebuild tools
make -jX    # Build ROM
# Note: 'make clean' may show errors about missing 'clean' targets in some tool subdirectories
# These errors are harmless - the important ROM files are cleaned successfully
# Alternative: Use 'make mostlyclean' to avoid the tool cleaning errors entirely

# Compare build against original ROM
make compare
```

### Building Tools
```bash
# Build all tools
make tools

# Clean and rebuild tools
make clean-tools  # May show 'No rule to make target' errors - these are harmless
make tools
```

## Working with Large Files

Many data files in this project are extremely large (e.g., `src/data/trainers.h` has 15,000+ lines). When working with these files:

1. **Use Python scripts to modify large files**:
   - Create a Python script to make the necessary changes
   - Run the script and verify the output
   - This approach is more reliable than direct editing
   - **IMPORTANT**: Put python scripts in the `eliteredux-darky/scripts/` directory (not in `tools/`)
   - Example directories: `eliteredux-darky/scripts/trainer_tools/`, `eliteredux-darky/scripts/wiki_tools/`

2. **Read files strategically**:
   - Use grep/search to find specific sections
   - Read only the relevant portions
   - Avoid loading entire large files when possible

Example workflow for editing trainers:
```python
# create edit_trainers.py
# make targeted changes
# run: python edit_trainers.py
# verify changes with diff or targeted reads
```

## Architecture Overview

### Multi-Ability System
The core feature of Elite Redux is the 4-ability system:
- **1 Changeable Ability**: Stored in the regular ability slot, can be changed among up to 3 choices
- **3 Fixed Innate Abilities**: Stored as separate abilities but always active
- Implementation in `src/abilities.cc` and battle engine files

### Data Organization
Game data is primarily edited directly in C header and source files:
- **Pokemon Data**: Base stats, evolutions, learnsets in various `.h` files
- **Trainer Data**: `src/data/trainers.h` and `src/data/trainer_parties.h`
- **Move Data**: Move effects, descriptions, and properties
- **Ability Data**: Ability effects and descriptions
- **Item Data**: Item effects, descriptions, and properties
- **Strings**: Various text strings throughout the codebase

Proto files are a compilation tool that helps generate some of this data, but developers primarily work with the C files directly.

### Map and Script System
- Maps use Pory scripting language (`.pory` files)
- Compiled to `.inc` files via poryscript tool
- Scripts handle trainer battles, events, and interactions

### Graphics Pipeline
- Sprites processed through `tools/gbagfx`
- Pokemon sprites support gender differences and forms
- UI elements for ability pop-ups and battle interface

### Proto-based Codegen System
The project uses a sophisticated proto-based codegen system:
- **Proto definitions**: `proto/*.proto` files define data structures
- **Textproto data**: `proto/*.textproto` files contain actual game data
- **Codegen tool**: `tools/codegen/` (Kotlin-based) generates C headers from proto files
- **Key files**:
  - `AbilityList.textproto` - All ability data
  - `SpeciesList.textproto` - Pokemon species data
  - `MoveList.textproto` - Move data
  - `TrainerList.textproto` - Trainer data
  - `HelpArticles.textproto` - Wiki content

## Development Workflow

### Compilation Workflow
1. **Claude Code should NOT run make commands** - they produce too much output
2. **User runs builds** and provides error logs if needed
3. **Claude Code provides**:
   - Clear instructions on what commands to run
   - Help interpreting error messages
   - Fixes for compilation issues

### Making Game Data Changes
1. Edit the appropriate `.h` or `.c` file directly
2. For large files, use Python scripts to make changes
3. Tell user to run `make clean` if errors are expected
4. Tell user to rebuild with `make -jX` or `make modern -jX` (both are equivalent)

### Common File Locations
- **Trainers**: `src/data/trainers.h`, `src/data/trainer_parties.h`
- **Pokemon**: Various files in `src/data/pokemon/`
- **Moves**: Battle move data files
- **Abilities**: `src/abilities.cc` and related headers
- **Items**: Item data headers
- **Strings**: `src/strings.c` and various other locations

### Script Organization
- **Python Scripts**: All Python scripts go in `eliteredux-darky/scripts/` directory
- **Trainer Scripts**: `eliteredux-darky/scripts/trainer_tools/`
- **Wiki Scripts**: `eliteredux-darky/scripts/wiki_tools/`
- **Ability Scripts**: `eliteredux-darky/scripts/ability_tools/`
- **Never put Python scripts in `tools/`** - that directory is only for C programs that need compilation
- **Clean up temporary scripts**: After completing a task, delete one-off Python scripts that are no longer needed
  - Keep only reusable tools and utilities
  - Document what scripts do if they're worth keeping
  - This prevents clutter and confusion for future work

### Project Planning and Organization
- **Plans Directory**: Complex tasks and projects should have planning documents in `eliteredux-darky/plans/`
- **Format**: Use markdown files (`.md`) for planning documents
- **Organization**: For large multi-file projects, create a subfolder (e.g., `eliteredux-darky/plans/extended_ability_descriptions/`)
- **Master Plan**: Large projects should have a `MASTER_PLAN.md` that links to other documents
- **Content**: Include overview, requirements, implementation steps, and progress tracking
- **When to use**: For any multi-step project that requires coordination or tracking
- **Continuation**: When told to "continue working on X", check `eliteredux-darky/plans/X/` folder first

### Testing Approach
- Python test files in `eliteredux-darky/scripts/ability_tools/` (e.g., `test_generate_progress.py`)
- No formal unit test framework for the C codebase
- Manual testing through ROM builds and gameplay
- Individual validation scripts for specific tools

## Critical Rules

1. **NEVER autocommit or push to GitHub unless explicitly requested by the user**
2. **NEVER take shortcuts or make assumptions** - Always verify file existence:
   - Don't assume a file doesn't exist - use search tools first
   - Don't create new files without checking for existing ones
   - When in doubt, search thoroughly before creating
3. **NEVER hallucinate or make up facts** - When writing game content (ability descriptions, wiki entries, etc.):
   - Look up exact mechanics in the code (abilities.cc, battle scripts, etc.)
   - Verify percentages, damage calculations, and interactions
   - If unsure about an effect, search the codebase first
   - Player-facing text must be 100% accurate
3. **Always use `make mostlyclean` when encountering compilation errors** (NOT `make clean` which removes tools!)
4. **Use Python scripts for editing large files (15k+ lines)**
5. **Test changes thoroughly before committing**
6. **DO NOT run `make`, `make modern`, or other compilation commands** - the output is too large for the context window and wastes tokens. Instead:
   - Tell the user when they need to build and what command to use
   - Let the user run builds and provide error logs if compilation fails
   - For small compilation tasks (single tool builds), consider if output will be manageable first
7. **macOS Build Issues**: If user reports "tools/scaninc/scaninc: No such file or directory":
   - They used `make clean` instead of `make mostlyclean`
   - Solution: `make tools` then `make -j4`
   - Remind them to ALWAYS use `make mostlyclean`
8. **ALWAYS consider text length limits** - GBA UI elements have fixed sizes. Keep text concise to prevent overflow:
   - Start Menu descriptions: ~20 characters per line
   - Dialog boxes: Check line breaks and total length
   - Menu items: Keep names short and clear
   - Extended ability descriptions: 280-300 characters INCLUDING spaces
   - Test in-game or count characters when editing UI text
9. **Character Counting for GBA**: ALWAYS count WITH spaces - GBA hardware renders spaces as tiles

## Important Notes

- Both `make -jX` and `make modern -jX` are equivalent and build with modern GCC (better warnings/errors)
- The `upcoming` branch is the active development branch
- Many files are auto-generated - be careful about which files to edit
- When in doubt about file size, check before attempting to read/edit directly
- The build system attempts to compile all directories under `tools/` - use `eliteredux-darky/scripts/` for Python scripts instead
- GitHub Actions automatically deploys documentation to GitHub Pages when changes are pushed to main

## Knowledge Base

Detailed documentation about specific systems can be found in the `eliteredux-darky/knowledge/` directory:
- **macos_compilation.md** - Complete guide for building on macOS, including troubleshooting
- **difficulty_system.md** - How the 4-tier difficulty system works
- **adding_trainers.md** - Guide for adding new trainers and parties
- **hell_mode_implementation.md** - Process for implementing Hell Mode
- **wiki_system.md** - In-game Wiki system structure and content editing
- **ability-and-innates-learnings.md** - Deep technical documentation about ability system internals
- **abilities/** - Individual ability documentation files (one per ability with frontmatter)
- **extended_ability_descriptions/** - Project documentation for extended ability descriptions

## Memory: Ability and Data Management
- Abilities are now added in `abilities.cc` and `abilitylist.textproto`, not manually via multiple .c and .h files
- `abilities.cc` contains code definitions
- `abilitylist.textproto` currently holds names, descriptions, and ability effects
- `specieslist.textproto` contains Pokemon data
- `battle_util` is still used occasionally
- These files are crucial for project development

## Memory: Data Storage Strategy
- Single file with all data in one location
- Separate files only for sprite/palette files
- Textproto-based codegen and unified abilities file in `abilities.cc` is the main configuration method

## Memory: Learning and Knowledge Management
- When you learn new stuff, especially when you had to search a lot to understand how something works and is connected, don't hesitate to write into CLAUDE.md so next time it will be much faster > like training the AI so it gets better and better!
- **IMPORTANT**: Create detailed documentation in the `eliteredux-darky/knowledge/` directory for complex topics:
  - Platform-specific guides (e.g., `macos_compilation.md`)
  - System implementations (existing: `difficulty_system.md`, `wiki_system.md`, etc.)
  - Problem solutions and workarounds
  - This helps future sessions and other developers
- Update CLAUDE.md with quick references that link to these detailed guides

## In-Game Wiki System

The in-game wiki provides comprehensive help content accessible from the Start Menu or during battles (L button by default).

### Wiki Content Structure
- **Content Source**: `docs/er-wiki-google-docs.md` - Markdown file containing all wiki content
- **Parser Tool**: `eliteredux-darky/scripts/wiki_tools/parse_wiki_markdown.py` - Converts markdown to protobuf format
- **Protobuf Data**: `proto/HelpArticles.textproto` - Generated wiki content in protobuf format
- **Generated Code**: `include/generated/data/text/help_articles.h` - C header with final wiki data

### Adding/Updating Wiki Content
1. Edit `docs/er-wiki-google-docs.md` following the existing format:
   - Categories: `## Category Name`
   - Entries: `### Entry Title`
   - Content lines: `* Content here` (9 lines per page max, 5 pages per entry max)
   - Blank lines: Just `*`

2. Run the parser:
   ```bash
   python3 eliteredux-darky/scripts/wiki_tools/parse_wiki_markdown.py
   ```

3. Rebuild the codegen tools:
   ```bash
   make clean
   make tools/codegen
   ```

4. Build the ROM as usual

### Important Notes
- The GBA font system has limited character support - avoid special characters
- Keep text concise due to display constraints (46 characters per line approx)
- The parser automatically cleans problematic characters (accents, curly quotes, etc.)
- Wiki can be accessed from Start Menu > Wiki or during battles with L button

## Documentation Site (Codex)

Elite Redux has a VitePress-based documentation site for abilities:
- **Location**: `eliteredux-darky/codex/`
- **Local Development**: `npm run dev` in the codex directory
- **Build**: `npm run build`
- **Auto-deployment**: GitHub Actions deploys to GitHub Pages on push to main
- **URL**: Configured in `codex/docs/.vitepress/config.mjs`

## Technical Constraints and Best Practices

### GBA Hardware Limitations
- **Character Counts**: ALWAYS include spaces - GBA renders spaces as tiles
- **UI Text Limits**:
  - Extended ability descriptions: 280-300 chars INCLUDING spaces
  - Dialog: 30 chars/line, 11 usable lines
  - Wiki entries: 46 chars/line, 9 lines/page, 5 pages max
- **Character Encoding**: GBA requires ASCII-compatible characters
  - Fix special characters: "é" → "é", "ö" → "ö", "÷" → "÷"
  - Python scripts need `encoding='utf-8', errors='replace'` when reading files
  - JavaScript needs UTF-8 encoding: `btoa(unescape(encodeURIComponent(content)))`
- **Never assume vanilla Pokemon facts** - Elite Redux has extensive changes

### Auto-Generated File Conflict Resolution
**CRITICAL**: Some files are auto-generated via GitHub Actions and should NEVER be manually edited during conflicts.

#### Auto-Generated Files (DO NOT EDIT)
- `knowledge/extended_ability_descriptions/progress.md` - Generated by `generate_progress.py`
- `codex/docs/.vitepress/ability-status.json` - Generated by `generate_status_api.py`
- Any file with "AUTO-GENERATED" comments at the top

#### Source of Truth Files (SAFE TO EDIT)
- `knowledge/abilities/*.md` - Individual ability documentation files
- All manually-created source files

#### Conflict Resolution Pattern
When encountering conflicts with auto-generated files:

1. **Keep upstream versions of auto-generated files**:
   ```bash
   git checkout --theirs knowledge/extended_ability_descriptions/progress.md
   git checkout --theirs codex/docs/.vitepress/ability-status.json
   ```

2. **Unstage auto-generated files from commit**:
   ```bash
   git restore --staged knowledge/extended_ability_descriptions/progress.md
   git restore --staged codex/docs/.vitepress/ability-status.json
   ```

3. **Only commit source file changes**:
   - Individual ability files with special character fixes
   - Script improvements (generate_progress.py, InlineAbilityEditor.vue)
   - Manual source file edits

4. **Clean up stash after resolution**:
   ```bash
   git stash drop  # Git keeps stash as safety measure during conflicts
   ```

#### Data Flow System
Understanding the data flow prevents future conflicts:
- Individual markdown files → GitHub Actions → auto-generated tracking files
- `generate_progress.py` creates `progress.md` from individual ability files
- `generate_status_api.py` creates `ability-status.json` from `progress.md`
- InlineAbilityEditor.vue enables browser-based editing with GitHub commits
- **Auto-regeneration happens automatically on every push to main branch**
- **No manual script execution needed** - just push source file changes

### Important Technical Details
- Weather/terrain durations are 8 turns base (not 5 like vanilla)
- Fort Knox blocks most offensive abilities except Parental Bond
- Ability IDs are auto-generated from proto files, not manually maintained
- Scripts exist to fix/verify character counts: `recount_ability_descriptions.py`

## Submodule Context

This `eliteredux-darky` directory is a submodule within the main `eliteredux-source` project. The parent directory structure provides:
- Main ROM source code and build system
- Proto files for data generation
- Tools for compilation
- This submodule adds documentation, scripts, and planning tools

## Known Issues and Fixes

### Codex Inline Editor Character Counting
**Issue**: Character count shows 0/300, wrong counts, or even 3030/300 when navigating between abilities
**Root Cause**: Complex regex patterns being too greedy and capturing entire file sections
**Solution**: Use substring-based extraction instead of regex. See `knowledge/extended_ability_descriptions/codex-character-count-fix-v2.md`
**Key Learning**: When dealing with structured markdown, substring operations are often more reliable than complex regex patterns