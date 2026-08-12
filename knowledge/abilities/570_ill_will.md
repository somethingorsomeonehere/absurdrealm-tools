---
id: 570
name: Ill Will
status: reviewed
character_count: 81
---

# Ill Will - Ability ID 570

## In-Game Description
"Deletes the PP of the move that faints this Pokemon."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Ill Will drains the PP of the move that defeats the user. Has to be a direct hit.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Activation Trigger**: Only when the Pokemon with Ill Will is knocked out (HP reaches 0)
- **Move Requirement**: The finishing move must make contact with the defender
- **PP Effect**: Sets the attacking move's PP to 0 (complete deletion, not reduction)
- **Timing**: Activates immediately after the Pokemon faints from the contact move

### Activation Conditions
```cpp
// From abilities.cc - IllWill implementation
CHECK(ShouldApplyOnHitAffect(attacker))     // Standard hit effect check
CHECK(move != MOVE_STRUGGLE)                // Struggle is exempt
CHECK(IsMoveMakingContact(move, attacker))  // Must be a contact move
CHECK(gBattleMons[attacker].pp[gChosenMovePos])  // Move must have PP remaining
CHECK_NOT(IsBattlerAlive(battler))          // Defender must be defeated
```

### Technical Implementation
- **PP Deletion**: `gBattleMons[attacker].pp[gChosenMovePos] = 0;`
- **Battle Message**: "{ATTACKER}'s {MOVE} lost all of its PP to Ill Will!"
- **Data Update**: Automatically syncs PP change to the battle data
- **No Bypass**: Cannot be prevented by Sheer Force, Magic Guard, or similar abilities

### Comparison with Similar Abilities
| Ability | PP Effect | Trigger | Contact Required |
|---------|-----------|---------|------------------|
| **Ill Will** | Deletes all PP | When fainting | Yes |
| **Spiteful** | Reduces 2-5 PP | When hit | Yes |
| **Cursed Body** | Disables move | When hit (30% chance) | Yes |

### Moves That Bypass Ill Will
- **Struggle**: Explicitly exempt from PP deletion
- **Non-contact moves**: Projectiles, special attacks, etc.
- **Indirect damage**: Poison, burn, entry hazards, weather

### Strategic Implications
- **Revenge Ability**: Punishes physical attackers for delivering the killing blow
- **PP Stalling**: Forces opponents to use non-contact moves for the finish
- **Resource Management**: Creates significant pressure on limited-PP moves
- **Sweeper Counter**: Particularly effective against physical setup sweepers

### Common Users
Based on the species data, Ill Will appears on various Pokemon including:
- Ghost-types (thematically appropriate for vengeful spirits)
- Dark-types (fits the malicious nature)
- Pokemon with low defenses but high offensive potential

### Competitive Usage Notes
- **Suicide Leads**: Particularly effective on Pokemon designed to trade favorably
- **Revenge Killer Deterrent**: Makes opponents think twice about using contact moves
- **Team Support**: Protects teammates by punishing physical attackers
- **Anti-Meta**: Counters physical-heavy metagames

### Counters
- **Special Attackers**: Completely avoid the ability's effect
- **Non-contact Physical Moves**: Earthquake, Rock Slide, etc.
- **Indirect Damage**: Poison, burn, entry hazards
- **Priority Users**: Can finish with non-contact priority moves

### Synergies
- **Rocky Helmet**: Stacks contact punishment with PP deletion
- **Iron Barbs/Rough Skin**: Additional contact damage before PP deletion
- **Destiny Bond**: Ensures mutual KO while still triggering PP deletion
- **Focus Sash/Sturdy**: Provides setup for revenge scenarios

### Version History
- **Elite Redux**: Introduced as a unique revenge ability
- **Implementation**: Uses the onDefender hook to trigger on fainting
- **Battle Integration**: Fully integrated with battle message system