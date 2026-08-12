---
id: 561
name: Zero To Hero
status: reviewed
character_count: 146
---

# Zero To Hero - Ability ID 561

## In-Game Description
"Changes forms after switching out."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

After switching out, transforms user into Hero Form on entry. Lasts until the end of battle. Cannot be suppressed, swapped, copied, or overridden.

## Detailed Mechanical Explanation
*For Discord/reference use*

**Core Mechanics:**
- Exclusive to Palafin species (ID 964)
- Requires switching out and back in to activate
- Single-use per battle entry (uses GetSingleUseAbilityCounter system)
- Cannot be suppressed (unsuppressable = TRUE)
- Banned from randomizer (randomizerBanned = TRUE)

**Transformation Details:**
- Base Form (Palafin): HP 100, ATK 70, DEF 72, SpATK 53, SpDEF 62, SPE 100
- Hero Form (Palafin-Hero): HP 100, ATK 160, DEF 97, SpATK 106, SpDEF 87, SPE 100
- Stat changes: +90 ATK, +25 DEF, +53 SpATK, +25 SpDEF (no change to HP/Speed)

**Technical Implementation:**
```cpp
constexpr Ability ZeroToHero = {
    .onEntry = +[](ON_ENTRY) -> int {
        CHECK(gBattleMons[battler].species == SPECIES_PALAFIN)
        CHECK_NOT(gBattleMons[battler].status2 & STATUS2_TRANSFORMED)
        CHECK(GetSingleUseAbilityCounter(battler, ability))

        UpdateAbilityStateIndicesForNewSpecies(battler, SPECIES_PALAFIN_HERO);
        gBattleMons[battler].species = SPECIES_PALAFIN_HERO;
        BattleScriptPushCursorAndCallback(BattleScript_AttackerFormChangeEnd3);
        return TRUE;
    },
    .onExit = +[](ON_EXIT) -> int {
        SetSingleUseAbilityCounter(battler, ability, TRUE);
        return FALSE;
    },
    .unsuppressable = TRUE,
    .randomizerBanned = TRUE,
};
```

**Activation Requirements:**
1. Must be Palafin (not already transformed)
2. Must not have the STATUS2_TRANSFORMED flag
3. Must have available single-use counter (first entry after switch)
4. Sets single-use counter on switch out to prevent repeated transformations

**Form Differences:**
- Hero Form has different abilities: Friend Guard, Avenger, Damp
- Hero Form has different innate abilities: Zero To Hero, Justified, Adaptability
- Uses same learnset and movepool
- Different visual sprite and icon

**Competitive Applications:**
- Enables pivot strategy: switch out to reset transformation capability
- Massive Attack boost (70 to 160) makes Hero Form a powerful physical sweeper
- Defensive improvements help survive hits better than base form
- Single-use restriction prevents easy spam but rewards strategic switching
- Works well with U-turn/Volt Switch team compositions

**Strategic Usage:**
- Switch Palafin in early to scout, then switch out
- Bring back later in battle for surprise transformation and sweep attempt
- Consider using with entry hazard support to maximize switch-in value
- Pair with moves like Jet Punch or Wave Crash to utilize the massive Attack boost