---
id: 732
name: Blade Dance
status: reviewed
character_count: 107
---

# Blade Dance - Ability ID 732

## In-Game Description
"Triggers 50 BP Leaf Blade after using a dance move."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Triggers a 50 BP Leaf Blade (Grass-type, Physical) follow-up attack immediately after using any dance move. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Blade Dance is an offensive ability that provides a powerful follow-up attack after using dance moves. When the user successfully executes any move with the dance flag, a 50 BP Leaf Blade attack is automatically triggered against the same target.

### Activation Conditions
- **Move requirement**: Any move with the FLAG_DANCE flag
- **Timing**: Activates immediately after the dance move resolves
- **Target**: Same target as the original dance move (can target self if dance was self-targeting)
- **Power**: Fixed 50 BP for the Leaf Blade follow-up

### Dance Moves That Trigger Blade Dance
- **Swords Dance** - Boosts Attack, then triggers Leaf Blade
- **Dragon Dance** - Boosts Attack/Speed, then triggers Leaf Blade  
- **Quiver Dance** - Boosts SpA/SpD/Speed, then triggers Leaf Blade
- **Petal Dance** - Attacking move, triggers Leaf Blade after
- **Rain Dance** - Sets rain, then triggers Leaf Blade
- **Feather Dance** - Lowers enemy Attack, then triggers Leaf Blade
- **Teeter Dance** - Confuses all others, then triggers Leaf Blade
- **Lunar Dance** - Faints user to heal ally, then triggers Leaf Blade
- **Fiery Dance** - Attacking move, may trigger Leaf Blade after
- **Revelation Dance** - Attacking move, triggers Leaf Blade after

### Technical Implementation
```c
constexpr Ability BladeDance = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(IsDance(battler, move))
        CHECK(AdjustFollowupMoveTarget(battler, &target, move, FOLLOWUP_ALLOW_SELF))

        return UseAttackerFollowUpMove(battler, target, ability, MOVE_LEAF_BLADE, 50);
    },
};
```

### Follow-Up Move Mechanics
- **Base Power**: 50 BP (reduced from Leaf Blade's normal 90 BP)
- **Type**: Grass-type move
- **Critical Hit Ratio**: High critical hit ratio (inherited from Leaf Blade)
- **STAB**: Gains Same Type Attack Bonus if user is Grass-type
- **Accuracy**: 95% accuracy (inherited from Leaf Blade)
- **Contact**: Physical contact move
- **Category**: Physical attack

### Important Interactions
- **Setup synergy**: Works excellently with stat-boosting dances
- **Multi-target**: Can hit different targets if dance was multi-target
- **Self-targeting**: Can target self if original dance was self-targeting
- **Status moves**: Triggers even on non-damaging dance moves
- **Failed moves**: Only triggers if the dance move successfully executes
- **Type effectiveness**: Leaf Blade follow-up affected by type matchups
- **Abilities**: Follow-up Leaf Blade can trigger other abilities

### Strategic Applications
- **Setup sweeper**: Use Dragon Dance, then get free Leaf Blade damage
- **Utility punishment**: Turn defensive dances into offensive opportunities  
- **Coverage option**: Provides Grass-type coverage after setup moves
- **Momentum shift**: Maintain offensive pressure while setting up
- **Multi-hit potential**: Can potentially hit multiple foes with area dances

### Taekkyeon Interaction
The ability also synergizes with the Taekkyeon ability, which makes all non-status moves count as dance moves. This dramatically expands the pool of moves that can trigger Blade Dance.

### STAB Considerations
- **Grass-types**: Get 1.5x damage on the follow-up Leaf Blade
- **Non-Grass types**: Still benefit from the extra 50 BP attack
- **Dual-types**: Grass as either type grants STAB bonus
- **Type changes**: If type changes mid-battle, STAB adjusts accordingly

### Competitive Usage Notes
- Excellent on mixed attackers who use setup moves
- Provides immediate offensive payoff for stat-boosting dances
- Can surprise opponents expecting purely defensive setup
- Grass-type users get maximum benefit from STAB
- Works well with critical hit increasing items/abilities

### Power Calculation Example
- Base 50 BP x 1.5 STAB (if Grass-type) x 2.0 critical hit = 150 effective power
- Without STAB: 50 BP x 2.0 critical hit = 100 effective power
- Regular hit with STAB: 50 BP x 1.5 = 75 effective power

### Synergies
- **Taekkyeon**: Makes all non-status moves trigger Blade Dance
- **Focus Energy**: Increases critical hit ratio for follow-up
- **Scope Lens/Razor Claw**: Boosts critical hit chance
- **Life Orb**: Boosts follow-up damage (with recoil)
- **Choice items**: Don't lock follow-up move selection
- **Stat-boosting dances**: Get setup benefit plus immediate damage

### Counters
- **Grass immunities**: Sap Sipper negates follow-up damage
- **Contact punishment**: Rough Skin, Iron Barbs damage user
- **Defensive abilities**: Filter, Solid Rock reduce damage
- **Type resistance**: Steel, Fire, Poison, Flying resist Grass
- **Ghost types**: Can switch in on predicted setup moves

### Team Building Considerations
- **Grass STAB users**: Maximize follow-up damage potential
- **Setup sweepers**: Turn setup turns into offensive opportunities
- **Mixed attackers**: Benefit from both dance effects and follow-up
- **Critical hit builds**: Stack crit chance for powerful follow-ups
- **Anti-meta**: Punishes opponents who give free setup turns

### Version History
- Elite Redux custom ability (ID 732)
- Designed to reward aggressive setup play
- Provides immediate offensive benefit for dance move usage
- Part of the expanded ability system in Elite Redux