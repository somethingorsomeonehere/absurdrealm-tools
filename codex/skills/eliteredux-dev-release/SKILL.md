---
name: eliteredux-dev-release
description: Use when preparing an internal Elite Redux dev release: enabling full dev debug, bumping dev-visible version strings, writing a dev-only changelog, and creating a verified BPS patch from the TrashMan Emerald base ROM.
---

# Elite Redux Dev Release

Use this skill for the full internal dev-release flow.

This is the "make me a dev build" skill.

## What This Covers

- full dev debug instead of public debug
- dev release version text updates
- dev-only changelog writing
- BPS patch creation from the TrashMan Emerald base ROM
- patch verification by applying it back and comparing against the built ROM

## Read These First

Before changing anything, read only the skill files you need:

- `../eliteredux-debug-system/SKILL.md`
- `../eliteredux-versioning/SKILL.md`
- `../eliteredux-changelog/SKILL.md`

Use them in that order.

## Workflow

1. **Debug mode**
   - Follow `eliteredux-debug-system`.
   - For dev releases, use:
     - `DEBUG_BUILD`
     - `TX_DEBUG_SYSTEM_ENABLE TRUE`
     - `TX_DEBUG_SYSTEM_PUBLIC FALSE`

2. **Version text**
   - Follow `eliteredux-versioning`.
   - Update only player-visible version surfaces.
   - Do **not** change `CURRENT_GAME_VERSION` unless save migration actually changed.
   - Usual files:
     - `src/strings.c`
     - `src/start_menu.c`
     - `src/hall_of_fame.c`

3. **Dev changelog**
   - Use `eliteredux-changelog` for commit gathering and release-note style.
   - For this internal flow, write **only the crew/dev version**.
   - Save it to:
     - `/Users/joel/Library/CloudStorage/GoogleDrive-darkyy92@gmail.com/My Drive/Pokemon/ROM Hacks/Pokemon Elite Redux/Elite Redux ROM/Dev Versions/Elite Redux v<version> Dev/elite-redux-<version>-changelog-crew-YYYY-MM-DD.md`
   - Keep it concise.
   - Lead with the headline feature instead of burying it under generic QoL.
   - Prefer intent plus visible behavior.
   - Cut internal implementation details players or devs would not care about.
   - Use player-facing names like `New Game Options`, not internal labels like `Intro Options`.

4. **Build**
   - Run:

   ```bash
   make -j10
   ```

5. **Create the BPS patch**
   - Use the bundled script:

   ```bash
   ./scripts/create_bps_patch.sh "2.65 Beta2.1"
   ```

   - The script:
     - installs Floating IPS locally if needed
     - creates the BPS patch
     - copies the built `.gba` into the dev release folder with the matching versioned name
     - applies the patch back to the clean ROM
     - verifies the recreated ROM matches `pokeemerald_modern.gba`

## Default Paths

The patch script defaults to:

- base ROM:
  `/Users/joel/Library/CloudStorage/GoogleDrive-darkyy92@gmail.com/My Drive/Pokemon/ROM Hacks/Pokemon Elite Redux/Elite Redux ROM/Trashman ROM/1986 - Pokemon Emerald (U)(TrashMan).gba`
- built ROM:
  `<repo-root>/pokeemerald_modern.gba`
- release output dir:
  `/Users/joel/Library/CloudStorage/GoogleDrive-darkyy92@gmail.com/My Drive/Pokemon/ROM Hacks/Pokemon Elite Redux/Elite Redux ROM/Dev Versions/Elite Redux v<version> Dev`
- changelog output:
  `.../Elite Redux v<version> Dev/elite-redux-<version>-changelog-crew-YYYY-MM-DD.md`
- patch output:
  `.../Elite Redux v<version> Dev/Elite Redux v<version> Dev.bps`
- ROM copy output:
  `.../Elite Redux v<version> Dev/Elite Redux v<version> Dev.gba`

## Patch Script Usage

```bash
./scripts/create_bps_patch.sh "<version>" [base_rom] [built_rom] [output_dir]
```

Examples:

```bash
./scripts/create_bps_patch.sh "2.65 Beta2.1"
./scripts/create_bps_patch.sh "2.65 Beta2.1" "/path/to/base.gba" "/path/to/pokeemerald_modern.gba" "/path/to/release-folder"
```

## Verification

Before calling the release ready, verify all of this fresh:

- `make -j10` succeeds
- the dev changelog file exists in the versioned release folder with the `elite-redux-<version>-changelog-crew-YYYY-MM-DD.md` naming pattern
- the `.bps` and copied `.gba` exist where expected
- the patch script reports a verified apply/compare pass

## Notes

- This is for **dev/internal releases**, not public player patch posts.
- Prefer the dev changelog tone from the crew version, not the public Discord version.
- If the user asks for a public build instead, switch back to the public-debug/versioning flow instead of using this skill as-is.
