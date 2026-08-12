---
id: 581
name: Beads Of Ruin
status: reviewed
character_count: 195
---

# Beads Of Ruin - Ability ID 581

## In-Game Description
"Lowers the Special Defense of other Pokemon by 25%."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Reduces the Special Defense stat of every other Pokemon by 25% while the user is out. Multiples of the same Ruin ability do not stack together. Stacks multiplicatively with Special Defense drops.

## Detailed Mechanical Explanation
*For Discord/reference use*

**Core Mechanics:**
- Beads of Ruin is a passive field-affecting ability that reduces the Special Defense stat of all other Pokemon (allies and opponents) by 25%
- Part of the "Treasures of Ruin" quartet alongside Tablets of Ruin (Attack reduction), Sword of Ruin (Defense reduction), and Vessel of Ruin (Special Attack reduction)
- The effect is applied as a stat modifier using the `RuinEffect` function with a 0.75x multiplier

**Activation Conditions:**
- Activates immediately when the Pokemon enters the battlefield
- Remains active as long as the Pokemon stays on the field
- Does not require any specific trigger or condition beyond presence

**Technical Implementation:**
```cpp
constexpr Ability BeadsOfRuin = {
    .onStat = +[](ON_STAT) { RuinEffect(STAT_SPDEF, battler, statId, stat, flags); },
    .onStatFor = APPLY_ON_OTHER,
    .ruinStat = STAT_SPDEF,
};

static void RuinEffect(int ruinStat, int battler, int statId, u32 *stat, NonStackingState *flags) {
    if (statId != ruinStat) return;
    if (*flags & NON_STACKING_RUIN) return;
    ON_ABILITY(battler, FALSE, gAbilities[ability].ruinStat == statId, return) *stat *= .75;
    *flags = static_cast<NonStackingState>(static_cast<int>(*flags) | static_cast<int>(NON_STACKING_RUIN));
}
```

**Note:** There appears to be a bug in the current implementation where the code uses `STAT_DEF` (Defense) instead of `STAT_SPDEF` (Special Defense), which contradicts the ability description.

**Affected Pokemon:**
- Only affects other Pokemon on the field (not the user)
- Affects both allies and opponents in doubles battles
- The reduction is calculated before other stat modifiers

**Interactions with Other Abilities/Mechanics:**
- **Multiple Ruin Abilities:** Each Ruin ability affects different stats and can stack (e.g., having both Beads of Ruin and Tablets of Ruin on the field reduces Special Defense AND Attack)
- **Non-Stacking Protection:** Multiple Pokemon with the same Ruin ability do not stack (NON_STACKING_RUIN flag prevents this)
- **Neutralizing Gas:** Cannot suppress Ruin abilities - they continue to function even under Neutralizing Gas
- **Stat Boosts/Drops:** The 25% reduction applies to the base Special Defense before stage modifiers are calculated
- **Clear Body/White Smoke/etc.:** These abilities do not prevent Ruin effects as they are not traditional stat drops

**Strategic Implications:**
- Excellent for special attackers as it makes all other Pokemon more vulnerable to special attacks
- Chi Yu (the primary user) benefits greatly as it has high Special Attack (145) and can exploit the reduced Special Defense of opponents
- Creates offensive pressure immediately upon switching in
- Forces opponents to account for the permanent field effect when team building

**Example Damage Calculations:**
If a Pokemon normally has 100 Special Defense:
- With Beads of Ruin: 100 x 0.75 = 75 Special Defense (33% more damage taken from special attacks)
- Combined with other effects: If the Pokemon also gets -1 Special Defense stage, the effective Special Defense becomes 75 x 0.67 about 50

**Common Users:**
- **Chi Yu** (National Dex #1004): Dark/Fire type legendary with Beads of Ruin as an innate ability
  - High Special Attack (145) to capitalize on the reduced Special Defense
  - Has access to powerful special moves like Mystical Fire, Inferno, and Pyro Ball
  - Part of the Treasures of Ruin legendary quartet

**Competitive Usage Notes:**
- Extremely powerful in special-attack focused teams
- Creates immediate offensive pressure without requiring setup
- Particularly devastating in doubles battles where it affects multiple targets
- Can turn 2HKOs into OHKOs for special attackers
- Forces defensive teams to run specially bulky Pokemon

**Counters:**
- Physical attackers are unaffected by the Special Defense reduction
- Pokemon with very high HP can still tank special attacks despite the reduction
- Abilities that boost Special Defense (like Download with Special Defense boost) can partially offset the effect
- Priority moves can bypass the need to survive special attacks

**Synergies:**
- Special attackers benefit immensely from having a Beads of Ruin teammate
- Works well with Trick Room teams where slow, powerful special attackers can capitalize
- Psychic Terrain + special attackers for guaranteed powerful hits
- Life Orb/Choice Specs users become even more threatening

**Version History:**
- Introduced in Pokemon Scarlet/Violet as part of the Treasures of Ruin legendary abilities
- Implemented in Elite Redux as part of the comprehensive ability system
- Currently has a bug where the code targets Defense instead of Special Defense (implementation inconsistency)