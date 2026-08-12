---
id: 748
name: Energy Siphon
status: reviewed
character_count: 135
---

# Energy Siphon - Ability ID 748

## In-Game Description
"Heals the user for 1/4 of the damage they deal."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Heals the user for 25% of all damage they deal to opponents. Healing occurs immediately after damage is dealt. Minimum healing of 1 HP.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Energy Siphon is an offensive ability that provides self-sustaining healing based on damage output. Unlike traditional healing moves, this ability turns aggressive play into defensive value by converting damage dealt into HP recovery.

### Activation Conditions
- **Damage requirement**: Must deal damage to an opponent
- **Timing**: Healing occurs immediately after damage calculation
- **Target requirement**: Must have a target that takes damage
- **Health check**: Will not activate if user is already at maximum HP
- **Healing check**: Must pass CanBattlerHeal() check

### Healing Calculation
```c
// Energy Siphon healing formula
gBattleMoveDamage = -gHpDealt / 4;
if (!gBattleMoveDamage) gBattleMoveDamage = -1;
```

- **Healing amount**: 25% (1/4) of damage dealt
- **Minimum healing**: 1 HP guaranteed even for weak attacks
- **Rounding**: Truncated (rounded down) to nearest integer
- **Maximum healing**: No cap, scales with damage output

### Technical Implementation
Energy Siphon uses the `onAttacker` trigger in the ability system:
- Checks if on-hit effects should apply
- Verifies user isn't at max HP
- Confirms user can be healed
- Calculates healing as negative damage (healing mechanic)
- Uses the same battle script as other drain abilities

### Important Interactions
- **Multi-hit moves**: Heals after each individual hit
- **Critical hits**: Healing scales with critical damage
- **Type effectiveness**: More effective moves = more healing
- **Substitute**: No healing if attacking a Substitute
- **Abilities that boost damage**: Indirectly boost healing amount
- **Life Orb/Choice items**: Damage boost increases healing

### Move Compatibility
**Works with all damaging moves:**
- Physical attacks (Earthquake, Close Combat, etc.)
- Special attacks (Thunderbolt, Ice Beam, etc.)
- Multi-hit moves (Bullet Seed, Rock Blast, etc.)
- Priority moves (Quick Attack, Aqua Jet, etc.)
- Spread moves (Surf, Earthquake in doubles)

**Does NOT work with:**
- Status moves (no damage dealt)
- Self-inflicted damage
- Recoil damage to user
- Fixed damage moves that don't use normal damage calculation

### Strategic Implications
- **Aggressive sustainability**: Rewards offensive play with healing
- **Wallbreaker synergy**: High-damage attackers benefit most
- **Momentum maintenance**: Healing while attacking maintains pressure
- **Anti-chip damage**: Negates passive damage through combat
- **Late-game power**: Becomes stronger as moves get more powerful

### Battle Script Usage
Uses `BattleScript_HydroCircuitAbsorbEffectActivated` - the same script used by other 25% drain abilities like Hydro Circuit and Pure Love, ensuring consistent visual and audio feedback.

### Comparison to Similar Abilities
- **Hydro Circuit**: Same healing rate, but only on Water-type moves
- **Pure Love**: Same healing rate, but only when target is infatuated  
- **Reservoir**: Heals 12.5% (1/8) instead of 25% (1/4)
- **Vampiric**: Heals 10% (1/10) for punching moves only

### Common Users
Energy Siphon is typically found on:
- Offensive Pokemon that lack reliable recovery
- Glass cannon attackers who need sustainability
- Mixed attackers who benefit from any damage type
- Pokemon with high attack stats and diverse movesets

### Competitive Usage Notes
- **Bulky offense**: Excellent on moderately bulky attackers
- **Life Orb synergy**: Recoil can be partially offset by healing
- **Choice item users**: Healing helps offset lack of recovery moves
- **Pivot moves**: U-turn/Volt Switch provide healing while switching
- **Status immunity**: Pairs well with abilities that prevent status

### Counters
- **Non-damaging moves**: Status moves bypass the healing entirely
- **Substitute**: Blocks healing by preventing direct damage
- **Wonder Guard**: Limits which moves can trigger healing
- **Heal Block**: Prevents the healing effect from occurring
- **Magic Bounce**: Reflects moves back without triggering healing

### Synergies
- **Life Orb**: Increased damage = increased healing, helps with recoil
- **Choice items**: Healing compensates for inability to switch moves
- **Type-boosting items**: More damage = more healing
- **Stat-boosting moves**: Setup moves increase future healing
- **Multi-hit moves**: Multiple healing instances per turn

### Team Building Considerations
- **Entry hazard support**: Helps chip opponents for easier KOs
- **Speed control**: Pairs well with Thunder Wave/Sticky Web support
- **Wallbreakers**: Benefits most from high-damage, low-accuracy moves
- **Pivot support**: Works well with VoltTurn cores for chip healing

### Version History
- Elite Redux exclusive ability (ID 748)
- Shares implementation pattern with other 25% drain abilities
- Uses established battle script system for consistent presentation
- Part of the expanded ability roster in Elite Redux