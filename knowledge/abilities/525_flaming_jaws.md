---
id: 525
name: Flaming Jaws
status: reviewed
character_count: 102
---

# Flaming Jaws - Ability ID 525

## In-Game Description
"Biting moves have 50% chance to burn the target."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Biting moves a 50% chance to burn the target on hit. Multihits roll the activation chance on each hit.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Flaming Jaws is an offensive ability that adds a burn chance to all biting moves. The ability triggers whenever the user hits with a move that has the FLAG_STRONG_JAW_BOOST flag.

### Activation Conditions
- **Move requirement**: Attack must have the FLAG_STRONG_JAW_BOOST flag
- **Hit requirement**: Move must successfully hit the target
- **Burn check**: Target must be able to be burned (not Fire-type, not already burned)
- **Chance**: 50% probability on each qualifying hit

### Affected Moves
All moves with FLAG_STRONG_JAW_BOOST that benefit from Strong Jaw also trigger Flaming Jaws:
- **Bite** - Dark-type physical move, 60 power
- **Crunch** - Dark-type physical move, 80 power
- **Fire Fang** - Fire-type physical move, 65 power (already can burn)
- **Thunder Fang** - Electric-type physical move, 65 power
- **Ice Fang** - Ice-type physical move, 65 power
- **Hyper Fang** - Normal-type physical move, 80 power
- **Super Fang** - Normal-type physical move, variable damage
- **Poison Fang** - Poison-type physical move, 50 power
- **Bug Bite** - Bug-type physical move, 60 power
- **Psychic Fangs** - Psychic-type physical move, 85 power
- **Jaw Lock** - Dark-type physical move, 80 power
- **Bolt Beak** - Electric-type physical move, 85 power (double if target hasn't moved)
- **Fishious Rend** - Water-type physical move, 85 power (double if target hasn't moved)
- **Snap Trap** - Grass-type physical move, 35 power (trapping move)
- **Deathroll** - Dark-type physical move, variable power
- **Aqua Fang** - Water-type physical move
- **Iron Fangs** - Steel-type physical move
- **Shadow Fangs** - Ghost-type physical move
- **Leech Life** - Bug-type physical move, 80 power (draining move)
- **Pluck** - Flying-type physical move, 60 power

### Technical Implementation
```c
constexpr Ability FlamingJaws = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(ShouldApplyOnHitAffect(target))
        CHECK(CanBeBurned(target))
        CHECK(gBattleMoves[move].flags & FLAG_STRONG_JAW_BOOST)
        CHECK(Random() % 2)  // 50% chance

        return AbilityStatusEffect(MOVE_EFFECT_BURN);
    },
};
```

### Burn Status Effect
- **Damage**: 1/16 of max HP at the end of each turn
- **Attack reduction**: Halves physical Attack stat
- **Duration**: Until switched out, cured, or fainted
- **Visual**: Fire animation around the Pokemon

### Important Interactions
- **Fire-type immunity**: Fire-type Pokemon cannot be burned
- **Already burned**: Cannot burn a target that's already burned
- **Substitutes**: Cannot burn through Substitute
- **Multi-hit moves**: Each hit has independent burn chance
- **Status immunity**: Water Veil, Comatose prevent burning
- **Synchronize**: Can reflect the burn back to the user

### Strategic Implications
- **Physical wallbreaker**: Burn reduces physical attackers' effectiveness
- **Residual damage**: Provides chip damage over time
- **Strong Jaw synergy**: Many biting moves also get 1.5x power boost
- **Type coverage**: Works with biting moves of various types
- **Status spreading**: Can cripple multiple opponents over time

### Common Users
**Current Implementation**: 
- **Centiskorch** (National Dex #851) - Fire/Bug type with Flaming Jaws as innate ability
  - Base stats: 100/115/90/65/90/65
  - Other abilities: Coil Up, Flash Fire, Molten Down (regular abilities)
  - Other innates: Let's Roll, Hyper Aggressive

### Competitive Usage Notes
- **Wallbreaking support**: Burn helps break through physical walls
- **Residual pressure**: Forces switches or healing
- **Type synergy**: Fire-type users resist burn themselves
- **Move variety**: Many different types of biting moves available
- **Timing importance**: Burn at the right moment can swing games

### Counters
- **Fire-type Pokemon**: Immune to burn status
- **Water Veil**: Ability prevents burn status
- **Substitute**: Blocks status application
- **Aromatherapy/Heal Bell**: Team-wide status healing
- **Natural Cure**: Switches out to cure burn
- **Lum Berry/Pecha Berry**: Immediate burn cure

### Synergies
- **Strong Jaw**: Same moves get power boost and burn chance
- **Sheer Force**: Would remove burn chance but boost power (if combined)
- **Kings Rock/Razor Fang**: Additional flinch chance on same moves
- **Life Orb**: Extra power on already strong biting moves
- **Choice items**: Lock into powerful burning bites

### Related Abilities
- **Strong Jaw**: Boosts same moves by 1.5x power
- **Tough Claws**: Boosts contact moves (many biting moves make contact)
- **Flame Body**: Burns on contact (different trigger condition)
- **Poison Touch**: Poisons on contact moves (similar concept)

### Version History
- Elite Redux custom ability
- Part of the expanded ability roster beyond Generation 8
- Designed to give unique identity to Fire-type physical attackers
- Available as innate ability on select Pokemon

### Hybrid Abilities
**Flaming Maw** (separate ability) combines Flaming Jaws with Strong Jaw for both burn chance and power boost on the same moves, creating a potent offensive combination.