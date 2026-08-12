---
name: eliteredux-debug-system
description: Work on Elite Redux in-game debug safely and consistently. Use when changing debug access, dev-vs-public debug behavior, Hell-mode debug restrictions, illegal mon/item blocklists, or when you need the exact flag setup for full dev debug, limited public debug, or fully disabled debug.
---

# Elite Redux Debug System

This skill is the quick map for how debug works now.

## Main Idea

There are 3 layers:

- `DEBUG_BUILD` in `include/global.h`
  - Big master switch.
  - If this is off, the in-game debug system should be gone.
- `TX_DEBUG_SYSTEM_ENABLE` in `include/debug.h`
  - Turns the debug menu system on or off inside a debug build.
- `TX_DEBUG_SYSTEM_PUBLIC` in `include/debug.h`
  - Chooses between full dev debug and the limited public debug rules.

Use this simple mental model:

- no debug build = no debug
- debug build + debug menu on + public off = full dev debug
- debug build + debug menu on + public on = limited public debug

## Quick Setup

### Full Dev Debug

Use:

- `#define DEBUG_BUILD`
- `#define TX_DEBUG_SYSTEM_ENABLE TRUE`
- `#define TX_DEBUG_SYSTEM_PUBLIC FALSE`

Result:

- current full-power debug
- dev cheats stay available
- no public restrictions

### Public Debug

Use:

- `#define DEBUG_BUILD`
- `#define TX_DEBUG_SYSTEM_ENABLE TRUE`
- `#define TX_DEBUG_SYSTEM_PUBLIC TRUE`

Result:

- debug still exists for players on allowed difficulties
- Hell and anything at or above Hell cannot open debug
- public-safe menu only
- blocked mons/forms/items stay unavailable

### Debug Fully Disabled

Recommended:

- comment out `#define DEBUG_BUILD`

Optional tighter setup:

- comment out `#define DEBUG_BUILD`
- `#define TX_DEBUG_SYSTEM_ENABLE FALSE`

Result:

- no in-game debug system

## Current Public Rules

Public debug is meant for player use, not dev cheats.

Current public behavior:

- illegal mons stay blocked
- illegal form-enabling items stay blocked
- God Mode is removed
- phasing/collision bypass is removed
- warp/teleport-style debug tools are removed
- complex custom-mon creation is removed
- debug is disabled for `DIFFICULTY_HELL` and above

## How To Explain It Publicly

When describing public debug to players, do not frame it like full debug returning unchanged.

Prefer wording like:

- `limited player-safe debug`
- `keeps useful convenience tools`
- `removes dev/cheat tools`

Explicitly mention when helpful:

- warp/script-skip/dev-travel tools are gone
- God Mode and Autowin are gone
- illegal mons/forms/items stay blocked
- Hell cannot use public debug

## Where The Rules Live

- `include/global.h`
  - `DEBUG_BUILD`
- `include/debug.h`
  - `TX_DEBUG_SYSTEM_ENABLE`
  - `TX_DEBUG_SYSTEM_PUBLIC`
  - shared helper declarations/macros
- `src/debug.c`
  - public restrictions
  - illegal species/item blocklists
  - menu contents
  - Hell gating helper logic
- `src/field_control_avatar.c`
  - overworld hotkey access
- `src/start_menu.c`
  - classic start-menu debug access
  - save-panel debug label behavior
- `src/ui_start_menu.c`
  - UI start-menu debug access
- `docs/illegal-mons.md`
  - source-of-truth document for blocked mons/items and code symbols
- `docs/debug-public-mode-plan.md`
  - implementation plan and reasoning

## Important Helpers

Before changing debug access, search for these first:

- `Debug_IsSystemEnabled()`
- `Debug_IsPublicModeEnabled()`
- `Debug_IsMenuAccessibleForCurrentSave()`

These helpers keep the rules aligned across the hotkey, start menu, and UI menu.

## Current Access Rules

- Dev debug can open anywhere debug is enabled.
- Public debug can open only when difficulty is below `DIFFICULTY_HELL`.
- Hell and future higher challenge modes are blocked by checking `>= DIFFICULTY_HELL`.

## Public Menu Expectations

When `TX_DEBUG_SYSTEM_PUBLIC == TRUE`, the public menu should stay limited.

Do not re-add these without an explicit product decision:

- Scripts
- Flags/Vars editing
- Fill Box
- Fly
- Warp
- Cheat Start
- Debug Map
- God Mode
- collision/phasing tools
- Autowin
- complex custom-mon builder

## Illegal Mons And Items

Blocked content is documented in `docs/illegal-mons.md` and enforced in `src/debug.c`.

Keep the markdown doc and the runtime C blocklists in sync.

When adding a new blocked entry:

1. add the display name and code symbol to `docs/illegal-mons.md`
2. add the species or item symbol to the public runtime blocklist in `src/debug.c`
3. make sure simple give, item give, and bulk/fill paths all stay blocked

## Safe Workflow

1. Search for the three debug flags and the helper functions before editing.
2. Decide whether the change is build-level, menu-level, or public-rules-only.
3. If public legality changes are involved, update both:
   - `docs/illegal-mons.md`
   - `src/debug.c`
4. Build with:

```bash
make -j10
```

5. Smoke-test in-game:
   - allowed difficulty can open public debug
   - Hell cannot open debug
   - forbidden menu entries are absent
   - blocked mons/items cannot be granted

## Quick Search

```bash
rg -n "DEBUG_BUILD|TX_DEBUG_SYSTEM_ENABLE|TX_DEBUG_SYSTEM_PUBLIC|Debug_IsSystemEnabled|Debug_IsPublicModeEnabled|Debug_IsMenuAccessibleForCurrentSave|DIFFICULTY_HELL" include src docs -g '!build/**'
```
