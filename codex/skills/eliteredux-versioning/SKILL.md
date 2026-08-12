---
name: eliteredux-versioning
description: Update Elite Redux version text safely and consistently across player-visible UI while keeping save migration versioning separate. Use when changing the in-game version name, release suffixes, debug/non-debug labels, Hall of Fame naming, or any screen that shows the current ROM version.
---

# Elite Redux Versioning

Update player-facing version text carefully. This repo has multiple visible version surfaces, and they do not all share one source of truth.

## What To Change

- Shared menu version text lives in `src/strings.c` as `gText_SavingVersionNum`.
  - It is used by the main Continue screen, the in-game UI start menu top bar, and other shared UI surfaces.
- The cramped save panel in `src/start_menu.c` may need its own debug-only short string.
  - Use this when the full debug label overflows.
- Hall of Fame uses its own hardcoded text in `src/hall_of_fame.c`.
  - Treat it as a separate naming surface.

## What Not To Confuse

- `CURRENT_GAME_VERSION` in `include/global.h` is the internal save/update compatibility version.
- Do not change `CURRENT_GAME_VERSION` just because the release name changes.
- Only bump `CURRENT_GAME_VERSION` when the save migration/update logic actually needs a new internal version.

## Current Learnings

- `gText_SavingVersionNum` is shared. A global string change affects multiple screens.
- The save panel has tighter width limits than the Continue screen.
- Hall of Fame may intentionally use a different release label than the rest of the UI.
- The title screen does not use the same version text path; do not assume a string edit changes title graphics.
- When `DEBUG_BUILD` is enabled, debug labels should be explicit but still respect GBA text limits.

## Current Naming Convention

Verify the code before editing, but the latest known convention is:

- Normal shared UI: `v2.65 Beta2`
- Debug shared UI: `v2.65 Beta2 Debug`
- Debug save panel only: `v2.65 Beta2 D.`
- Hall of Fame normal: `v2.65-B1`
- Hall of Fame debug: `v2.65-B1d`

## Workflow

1. Search for the current version literals and `gText_SavingVersionNum` before editing.
2. Decide which surfaces should share one label and which should stay separate.
3. Update:
   - `src/strings.c` for shared UI text
   - `src/start_menu.c` for save-panel-only shortening
   - `src/hall_of_fame.c` for Hall of Fame branding
4. Leave `include/global.h` alone unless an internal save-version bump is required.
5. Re-search for old literals to catch missed hardcodes.
6. Build the ROM and confirm it compiles.

## Verification

Use targeted searches first:

```bash
rg -n "gText_SavingVersionNum|v2\\.65|Beta2|B1d|CURRENT_GAME_VERSION" src include -g '!build/**'
```

Then build:

```bash
make -j10
```

If UI text was shortened for overflow, visually verify the affected screen in-game as well.
