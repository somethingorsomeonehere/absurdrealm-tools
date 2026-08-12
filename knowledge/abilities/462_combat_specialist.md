---
id: 462
name: Combat Specialist
status: reviewed
character_count: 72
---

# Combat Specialist - Ability ID 462

## In-Game Description
"Boosts the power of punching and kicking moves by 1.3x."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Combat Specialist boosts the power of punching and kicking moves by 30%. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Combat Specialist is a versatile offensive ability that combines the effects of Iron Fist and Striker abilities, providing a 1.3x (30%) power boost to both punching and kicking moves. This dual-category boost makes it exceptionally valuable for Pokemon with diverse physical movesets.

### Activation Conditions
- **Move requirement**: Must use a move with FLAG_IRON_FIST_BOOST or FLAG_STRIKER_BOOST flags
- **Power multiplier**: 1.3x damage boost applied to base power
- **Timing**: Applied during damage calculation phase
- **Stacking**: Multiplies with other damage modifiers (STAB, type effectiveness, etc.)

### Affected Moves

#### Punching Moves (Iron Fist boosted):
- **Fire Punch**: Fire-type punch with burn chance
- **Ice Punch**: Ice-type punch with freeze chance  
- **Thunder Punch**: Electric-type punch with paralysis chance
- **Dynamic Punch**: Fighting-type punch with confusion
- **Focus Punch**: High-power Fighting-type delayed punch
- **Mach Punch**: Priority Fighting-type punch
- **Mega Punch**: Normal-type high-power punch
- **Comet Punch**: Multi-hit Normal-type punch
- **Dizzy Punch**: Normal-type punch with confusion chance
- **Bullet Punch**: Priority Steel-type punch
- **Drain Punch**: Fighting-type punch with healing
- **Hammer Arm**: Fighting-type punch that lowers Speed
- **Shadow Punch**: Ghost-type punch that never misses
- **Sky Uppercut**: Fighting-type uppercut that hits Fly users

#### Kicking Moves (Striker boosted):
- **Double Kick**: Two-hit Fighting-type kick
- **High Jump Kick**: High-power Fighting-type jumping kick
- **Blaze Kick**: Fire-type kick with critical hit chance
- **Mega Kick**: High-power Normal-type kick
- **Low Kick**: Fighting-type kick with variable power
- **Rolling Kick**: Fighting-type kick with flinch chance
- **Jump Kick**: Fighting-type jumping kick (weaker version)
- **Triple Kick**: Three-hit Fighting-type kick with increasing power
- **Stomp**: Normal-type stomping attack
- **High Horsepower**: Ground-type powerful kick

### Technical Implementation
```c
constexpr Ability CombatSpecialist = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            // Delegate to both Iron Fist and Striker abilities
            IronFist.onOffensiveMultiplier(DELEGATE_OFFENSIVE_MULTIPLIER);
            Striker.onOffensiveMultiplier(DELEGATE_OFFENSIVE_MULTIPLIER);
        },
};

// Move flagging system
int IsIronFistBoosted(int battler, MoveEnum move) {
    if (gBattleMoves[move].flags & FLAG_IRON_FIST_BOOST) return TRUE;
    // Additional conditions for special cases
    return FALSE;
}

int IsStrikerBoosted(int battler, MoveEnum move) {
    if (gBattleMoves[move].flags & FLAG_STRIKER_BOOST) return TRUE;
    // Additional conditions for special cases  
    return FALSE;
}
```

### Important Interactions
- **Power multiplication**: 1.3x boost applies to base power before other calculations
- **STAB stacking**: Combines multiplicatively with Same Type Attack Bonus
- **Type effectiveness**: Multiplies with super-effective/not very effective modifiers
- **Critical hits**: Boost applies before critical hit calculation
- **Item synergy**: Stacks with Life Orb, Choice items, and type-boosting items
- **Weather effects**: Can combine with sun/rain boosts for certain move types
- **Multi-hit moves**: Each hit receives the full 1.3x multiplier

### Strategic Implications
- **Movepool versatility**: Supports both punching and kicking moves equally
- **Type coverage**: Works across multiple types (Normal, Fighting, Fire, Ice, Electric, etc.)
- **Priority moves**: Boosts Mach Punch and Bullet Punch for priority damage
- **Mixed attackers**: Valuable for Pokemon with both punching and kicking moves
- **Physical sweepers**: Excellent for physical attackers with diverse contact moves

### Common Users
Combat Specialist is typically found on:
- Fighting-type Pokemon with diverse physical movesets
- Pokemon with access to elemental punches and kicks
- Physical attackers that learn both move categories
- Martial arts-themed Pokemon
- Pokemon designed for close-quarters combat

### Competitive Usage Notes
- **Movepool requirement**: Only valuable if the Pokemon learns multiple boosted moves
- **Contact dependency**: Most boosted moves make contact, vulnerable to Rough Skin, etc.
- **Physical focus**: Purely beneficial for physical attackers
- **Type diversity**: Allows effective coverage across multiple types
- **Priority utility**: Enhances priority moves like Mach Punch for speed control

### Counters
- **Intimidate**: Reduces Attack stat, diminishing the boosted damage
- **Burn status**: Halves physical attack power, negating much of the boost
- **Defense boosts**: Bulk Up, Cosmic Power, and defensive items reduce impact
- **Contact punishers**: Rough Skin, Iron Barbs, Rocky Helmet damage on contact
- **Ghost immunity**: Normal-type punches and kicks are ineffective
- **Protect/Detect**: Blocks the boosted attacks entirely
- **Will-O-Wisp**: Burns the attacker to reduce damage output

### Synergies
- **Life Orb**: Multiplies damage further at cost of recoil
- **Choice Band**: Another 1.5x multiplier for huge damage output
- **Type-boosting items**: Expert Belt, Fist Plate, etc. for additional boosts
- **Speed control**: Thunder Wave, Trick Room to ensure attack opportunities
- **Entry hazards**: Stealth Rock weakens opponents before powerful attacks
- **Healing moves**: Drain Punch becomes more effective with the boost
- **Setup moves**: Bulk Up, Swords Dance to maximize damage potential

### Damage Calculations
- **Base calculation**: (Base Power x 1.3) x other modifiers
- **Example**: Fire Punch (75 BP) becomes effectively 97.5 BP before other modifiers
- **With STAB**: Fire Punch on Fire-type becomes ~146 effective BP
- **Super effective**: Fire Punch vs Grass becomes ~195 effective BP
- **Maximum boost**: With STAB + super effective + Choice Band = ~292 effective BP

### Version History
- **Elite Redux exclusive**: Custom ability not found in official games
- **Design purpose**: Combines Iron Fist and Striker into single ability
- **Balance consideration**: 30% boost balanced by move type restrictions
- **Movepool dependency**: Effectiveness varies greatly by Pokemon's available moves

### Related Abilities
- **Iron Fist**: Boosts only punching moves by 1.2x (weaker)
- **Striker**: Boosts only kicking moves by 1.3x (single category)
- **Strong Jaw**: Boosts biting moves instead of punches/kicks
- **Mega Launcher**: Boosts pulse/aura moves with similar multiplier
- **Tough Claws**: Boosts all contact moves by 1.3x (broader but includes non-punches/kicks)