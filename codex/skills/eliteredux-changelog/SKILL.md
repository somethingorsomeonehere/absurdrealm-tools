---
name: eliteredux-changelog
description: Generate Elite Redux release changelogs and Discord announcement posts from recent git commits. Use when writing player-facing patch notes, Discord release announcements, changelog summaries since a date/hash, or when you need both a public player version and a more exact internal crew version of what changed.
---

# Elite Redux Changelog

Use this skill when turning commit history into a changelog for Elite Redux players and crew.

This is not a business email skill. Write like a ROM hack release post for Pokemon players on Discord.

## Main Output

Always generate 2 versions from the same commit range:

1. `Player Changelog`
   - short, exciting, easy to scan
   - focused on player benefit
   - suitable for Discord announcements
   - avoid technical implementation details

2. `Crew Changelog`
   - still non-technical and readable
   - more exact about what actually changed
   - call out specific mons, abilities, moves, encounters, UI systems, locations, or mechanics when commits support it
   - still skip pure code cleanup/refactor noise

Always show both in the response.

Always save both to Downloads as:

- `~/Downloads/elite-redux-<version>-changelog-player-YYYY-MM-DD.md`
- `~/Downloads/elite-redux-<version>-changelog-crew-YYYY-MM-DD.md`

## Tone

Write for Elite Redux players, not customers.

Use:

- confident, community-driven release energy
- Pokemon terms naturally
- stronger focus on mons, abilities, moves, fights, randomizer, QoL, UI, sprites, bugfixes
- concise bullets

Do not use:

- corporate or SaaS phrasing
- “I improved your app”
- “users”, “customers”, “business value”, or similar business language

Prefer:

- “players”
- “runs”
- “builds”
- “mons”
- “encounters”
- “route/fight/progression”
- “randomizer”
- “QoL”

## Writing Style

Keep changelogs tight.

Use:

- short bullets
- intent first when it helps explain why the change matters
- player-facing wording
- the names players actually use for menus and systems

Avoid:

- filler
- implementation detail
- vague technical wording
- internal names when player-facing names are better

Good:

- `Lets you skip normal trainer aggro and choose fights manually`
- `New toggle in New Game Options and Options+`
- `DexNav+ now correctly shows when you already caught everything on a route`

Bad:

- `Fixed new-only bulk buy caught-state checks`
- `Debug trainer aggro toggle now uses the same setting`
- `Intro Options`

## Commit Gathering

Use these rules:

- commit hash: `git log <hash>^..HEAD --pretty=format:"%h - %s%n%b%n---"`
- `today`: `git log --since="midnight" --pretty=format:"%h - %s%n%b%n---"`
- `yesterday`: `git log --since="yesterday midnight" --until="midnight" --pretty=format:"%h - %s%n%b%n---"`
- `this week`: `git log --since="last monday" --pretty=format:"%h - %s%n%b%n---"`
- date or datetime: `git log --since="<input>" --pretty=format:"%h - %s%n%b%n---"`

After the first pass, inspect important commits with `git show --stat --summary` or targeted `git show` on touched files when the title is too vague.

Do not trust vague commit subjects alone for the crew changelog if the actual player-visible change needs more precision.

If the superproject commit only bumps the `proto` submodule pointer, inspect the actual `proto` commit before writing release notes.

## What To Include

Include:

- new features players can use
- balance changes with clear player impact
- new or changed mons, abilities, moves, items, encounters, game modes, forms, evolutions, megas
- progression fixes
- QoL changes
- battle UI/info changes
- crash fixes and major bug fixes
- art/sprite/icon/palette polish players will notice

Usually skip:

- merge commits
- formatting
- build-only fixes
- docs-only changes
- refactors/cleanup
- internal tooling/codegen changes

Exception:

- include an internal-looking commit if it clearly changes gameplay, legality, randomizer behavior, save labels, or other player-visible behavior

## How To Read Commits For Crew Notes

The crew version should be more exact, but still not code-speak.

Good crew details:

- exact mons affected
- exact ability names
- exact move names
- exact location/fight names
- exact UI surface changed
- exact mechanic corrected

Bad crew details:

- file names
- function names
- compiler/build details
- “refactored”, “cleaned up”, “reworked backend”, unless tied to a player-visible result

## Discord Announcement Format

The player version should follow Elite Redux announcement style.

Use this structure:

```md
**Thank you to everyone who helped working on this release! :hearts:**

*[release credit line here]*
# **Elite Redux [version or release name if known]**

[optional save compatibility warning only if confirmed]

## Changelog
- bullets

----------------------

**Check out the full changelog:**
https://changelog.elite-redux.com/

**Online Dex:**
http://dex.elite-redux.com

**Patch directly here:**
https://elite-redux.com

Instructions on how to update:
#🚀｜how-to-patch
*Remember to patch on a CLEAN Emerald ROM.*

||@everyone||
```

## Discord Copy Rules

- Always include the footer block above.
- Do not invent a version number, save compatibility warning, contributor callout, or release title if it is not known from the prompt, commits, or repo context.
- If the version is unknown, ask the user for it before writing the final title or saving files.
- If contributor names are not given, use a safe generic line like `*@ER Crew proudly presents:*`
- Keep the player version postable as-is in Discord.

## Recommended Section Style

For the player version, group bullets under a few readable headings when useful:

- `Gameplay & Balance`
- `Pokemon Changes`
- `QoL & UI`
- `Progression`
- `Visual Polish`
- `Bug Fixes`

For the crew version, use similar categories but be more exact.

## Analysis Rules

- Explain the benefit to players, not just the raw change.
- Prefer one clear sentence over two weaker ones.
- Bold the biggest player-facing highlights.
- If a commit touches multiple things, split it into separate bullets if that makes the post clearer.
- Collapse repetitive tiny fixes into one summary bullet unless a specific mon/mechanic is important.
- For large batches of mon or ability changes, summarize cleanly in the player version and list more specifics in the crew version.
- For Adoption Center item changes, prefer precise wording like `lineup updated` unless the whole category was actually added.
- For randomizer QoL, strongly prefer calling out the player value directly.
  Good example: `Wild mons now show randomized abilities/innates before catching.`
- Cut internal wiring details unless players would care about them directly.

## Save Format

Save both outputs to Downloads and then show both in the response for review.

Suggested filenames:

- `elite-redux-<version>-changelog-player-YYYY-MM-DD.md`
- `elite-redux-<version>-changelog-crew-YYYY-MM-DD.md`

If the exact version is not already known from the prompt, commits, or repo context, ask the user for it before saving files.

For internal/dev Elite Redux releases, also save or copy the crew changelog to the versioned release folder:

- `/Users/joel/Library/CloudStorage/GoogleDrive-darkyy92@gmail.com/My Drive/Pokemon/ROM Hacks/Pokemon Elite Redux/Elite Redux ROM/Dev Versions/Elite Redux v<version> Dev/elite-redux-<version>-changelog-crew-YYYY-MM-DD.md`

## Quick Workflow

1. Gather commits from the requested starting point.
2. Remove obvious internal noise.
3. Inspect unclear but potentially player-visible commits with `git show`.
4. Group changes into player-relevant categories.
5. Write the `Player Changelog` in Discord announcement style.
6. Write the `Crew Changelog` with more exact gameplay details.
7. If the version is still unknown, ask the user for it.
8. Save both markdown files to Downloads with the Elite Redux versioned naming pattern.
9. For internal/dev releases, also place the crew changelog in the versioned folder inside `Dev Versions`.
10. Show both outputs in the response.
