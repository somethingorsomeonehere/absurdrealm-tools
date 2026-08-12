---
id: 215
name: Innards Out
status: reviewed
character_count: 211
---

# Innards Out - Ability ID 215

## In-Game Description
"If KO'd, deals as much damage as what the fatal attack dealt."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Innards Out activates when the Pokemon is knocked out by an opponent's attack. It inflicts the same amount of damage the fatal attack dealt back to the attacker. Cannot affect attackers protected by Magic Guard.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Innards Out triggers when the user is KO'd by a direct attack from an opponent. When activated, it deals damage equal to the exact amount of damage the fatal attack inflicted.

### Activation Conditions
- The Pokemon must be knocked out (HP reduced to 0) by a direct attack
- The attack must come from an opponent (not self-inflicted or ally damage)
- The ability user must not be alive after the attack (`CHECK_NOT(IsBattlerAlive(battler))`)
- The attacking Pokemon must not be protected by Magic Guard (`CHECK_NOT(IsMagicGuardProtected(attacker))`)

### Technical Implementation
```cpp
constexpr Ability InnardsOut = {
    .onDefender = +[](ON_DEFENDER) -> int {
        CHECK(ShouldApplyOnHitAffect(attacker))
        CHECK_NOT(IsBattlerAlive(battler))
        CHECK_NOT(IsMagicGuardProtected(attacker))

        gBattleMoveDamage = gTurnStructs[battler].dmg;
        BattleScriptCall(BattleScript_AftermathDmg);
        return TRUE;
    },
};
```

### Key Implementation Details
- **Damage Calculation**: `gBattleMoveDamage = gTurnStructs[battler].dmg` - Uses the stored damage value from the fatal attack
- **Battle Script**: Uses `BattleScript_AftermathDmg` (same as Aftermath ability)
- **Trigger Check**: `ShouldApplyOnHitAffect(attacker)` ensures proper activation conditions
- **Magic Guard Protection**: Attackers with Magic Guard are immune to the retaliation damage

### Affected Move Types
- **Works with**: All direct damage-dealing moves (physical, special, contact, non-contact)
- **Does NOT work with**: 
  - Indirect damage (poison, burn, weather, entry hazards)
  - Self-inflicted damage
  - Ally attacks in doubles/triples
  - Moves that don't directly deal damage

### Interactions with Other Abilities/Mechanics
- **Magic Guard**: Completely negates Innards Out damage to the attacker
- **Focus Sash/Sturdy**: If the attacker survives the Innards Out damage due to these abilities, they remain at 1 HP
- **Substitute**: Innards Out can break the attacker's substitute if the damage is sufficient
- **Multi-hit moves**: Only the final hit's damage is stored and reflected (if it causes the KO)

### Strategic Implications
- **Revenge KO**: Excellent for securing mutual KOs against powerful attackers
- **Pivot potential**: Can discourage opponents from using their strongest attackers to finish off the Innards Out user
- **Late-game threat**: Particularly dangerous when the opponent has low-HP sweepers
- **Sash breaking**: Can break Focus Sash/Sturdy on the attacker if they're at full HP

### Example Damage Calculations
- **Scenario 1**: Innards Out user has 50 HP remaining, takes 80 damage to Dies, deals 80 damage back
- **Scenario 2**: Innards Out user has 200 HP remaining, takes 250 damage to Dies, deals 250 damage back
- **Scenario 3**: Multi-hit move deals 30+30+40 damage (final hit KOs) to Deals 40 damage back (only final hit)

### Common Users
In Elite Redux, Innards Out is typically found on:
- Defensive Pokemon that can take hits and guarantee damage on KO
- Pokemon with high HP stats to maximize potential retaliation damage
- Support Pokemon that can threaten revenge KOs

### Competitive Usage Notes
- **Doubles/Triples**: Can punish spread moves by retaliating against the user
- **Priority protection**: No protection against priority moves targeting the Innards Out user
- **Setup counter**: Discourages opponents from using setup sweepers to finish off the user
- **Mind games**: Forces opponents to consider the health of their attacker before going for the KO

### Counters
- **Magic Guard**: Complete immunity to the retaliation damage
- **Indirect damage**: Using poison, burn, weather, or entry hazards to finish off the Innards Out user
- **Substitute**: Can absorb the Innards Out damage (though substitute will likely break)
- **High HP attackers**: Can survive the retaliation damage more easily

### Synergies
- **Focus Sash/Sturdy**: Allows the user to survive an otherwise fatal hit and potentially trigger Innards Out on a follow-up
- **Rocky Helmet**: Stacks contact damage with Innards Out for maximum punishment
- **Life Orb users**: Opponents taking Life Orb recoil + Innards Out damage face severe punishment
- **Entry hazards**: Weakening the opponent beforehand makes Innards Out more likely to secure the KO

### Version History
- **Generation VII**: Original introduction in Sun/Moon
- **Elite Redux**: Implemented with the same mechanics as the official games
- **Battle Engine**: Uses the existing Aftermath damage script for consistency