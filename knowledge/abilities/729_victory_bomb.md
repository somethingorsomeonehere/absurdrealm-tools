---
id: 729
name: Victory Bomb
status: reviewed
character_count: 147
---

# Victory Bomb - Ability ID 729

## In-Game Description
"Attacks with a 100BP Fire-type Explosion on fainting."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When fainting, retaliate with a 100 BP Fire-type Explosion targeting all adjacent Pokemon. Cannot miss. Works regardless of how the user. was KOed.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Victory Bomb is a revenge ability that activates when the Pokemon faints, automatically retaliating with a powerful Fire-type Explosion attack against the attacker. This makes it a dangerous last-resort ability that punishes opponents for KOing the user.

### Activation Conditions
- **Fainting trigger**: Activates when the Pokemon's HP reaches 0
- **Target**: Always targets the battler that caused the fainting
- **Move used**: MOVE_EXPLOSION with 100 Base Power
- **Type override**: The explosion is always Fire-type regardless of user's typing
- **Cannot miss**: The retaliatory explosion has perfect accuracy

### Technical Implementation
```c
constexpr Ability VictoryBomb = {
    .onDefender = +[](ON_DEFENDER) -> int {
        CHECK_NOT(IsBattlerAlive(battler))

        UseOutOfTurnAttack(battler, attacker, ability, MOVE_EXPLOSION, 100);
        return FALSE;
    },
    .onMoveType = +[](ON_MOVE_TYPE) -> int {
        CHECK(gProcessingExtraAttacks)
        CHECK(gQueuedExtraAttackData[0].ability == ability)
        return TYPE_FIRE + 1;
    },
};
```

### Important Interactions
- **Post-fainting activation**: The explosion occurs after the Pokemon has already fainted
- **Special exception**: Unlike other abilities, Victory Bomb can trigger even when the user is not alive
- **Type modification**: Uses onMoveType callback to force Fire typing on the explosion
- **Power override**: The explosion uses 100 Base Power instead of Explosion's normal 250
- **Contact independence**: Works regardless of whether the killing move made contact
- **Status immunity**: Cannot be prevented by sleep, freeze, or other status conditions

### Explosion Mechanics
- **Base Power**: 100 (reduced from Explosion's normal 250)
- **Type**: Fire (overridden from Normal)
- **Category**: Physical
- **Accuracy**: Cannot miss
- **Self-damage**: No self-damage since user is already fainted
- **Target**: Single target (the attacker)

### Strategic Implications
- **Revenge killing**: Guarantees damage to the opponent after fainting
- **Deterrent effect**: Makes opponents think twice about attacking directly
- **Suicide lead potential**: Can be used on lead Pokemon for guaranteed early damage
- **Fire-type coverage**: Provides Fire-type damage even on non-Fire Pokemon
- **Anti-contact**: Punishes physical attackers who expect safe KOs

### Activation Scenarios
- **Direct damage**: Fainting from any attacking move
- **Indirect damage**: Works even if KOed by status effects, entry hazards, etc.
- **Recoil damage**: Triggers if opponent's recoil move causes the KO
- **Weather damage**: Activates if weather damage causes fainting
- **Ability damage**: Works with damage from abilities like Rocky Helmet

### Common Users
- **Suicide leads**: Pokemon designed to deal early damage and faint
- **Revenge killers**: Pokemon that can threaten mutual KOs
- **Fire-type support**: Non-Fire types that want Fire coverage
- **Glass cannons**: Frail attackers that benefit from posthumous damage

### Competitive Usage Notes
- **Lead utility**: Excellent on suicide leads for guaranteed early pressure
- **Mutual destruction**: Can turn unfavorable trades into even exchanges
- **Fire-type utility**: Gives non-Fire types access to Fire-type attacks
- **Prediction tool**: Forces opponents to consider indirect KO methods
- **Team support**: Can weaken threats for teammates to clean up

### Counters
- **Indirect KOs**: Status damage, entry hazards, weather avoid the retaliation
- **Magic Guard**: Protects the attacker from the explosion damage
- **Ghost-type immunity**: Ghost types are immune to the explosion
- **Protect/Detect**: Can potentially shield from the explosion (needs testing)
- **Substitute**: May absorb the explosion damage

### Synergies
- **Focus Sash**: Guarantees survival to low HP for easy Victory Bomb activation
- **Life Orb**: Can be used to boost the explosion's damage output
- **Fire-type STAB**: Fire-type users get STAB bonus on the explosion
- **Flame Body/Flash Fire**: Can be paired with other Fire abilities
- **Stealth Rock**: Combined with entry hazards for massive chip damage

### Version History
- **Elite Redux exclusive**: Custom ability created for Elite Redux
- **ID 729**: Part of the extended ability roster
- **Fire-type twist**: Unique Fire-type Explosion variant
- **Balanced power**: 100 BP instead of full Explosion power for balance

### Design Philosophy
Victory Bomb embodies the "kamikaze" or "last stand" archetype, ensuring that defeating certain Pokemon comes at a cost. The Fire typing adds an offensive element while the reduced power (100 vs 250) maintains competitive balance. This ability rewards aggressive play while punishing reckless attacks, adding strategic depth to team building and battle decisions.