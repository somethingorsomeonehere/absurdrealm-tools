---
id: 171
name: Bulletproof
status: reviewed
character_count: 115
---

# Bulletproof - Ability ID 171

## In-Game Description
"Immune to projectile, ball, or bomb-based moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Provides immunity to ball, bomb, and projectile moves. Includes Acid Spray, Rock Wrecker, Pollen Puff, and Barrage.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Bulletproof provides complete immunity to moves with the `FLAG_BALLISTIC` flag. When a ballistic move targets a Pokemon with Bulletproof, the move fails entirely before any damage calculation or effect application.

### Implementation Details
```cpp
constexpr Ability Bulletproof = {
    .onImmune = +[](ON_IMMUNE) -> int {
        CHECK(gBattleMoves[move].flags & FLAG_BALLISTIC)
        CHECK_NOT(GetBattlerBattleMoveTargetFlags(move, attacker) & MOVE_TARGET_USER)
        *immunityScript = BattleScript_SoundproofProtected;
        return TRUE;
    },
    .breakable = TRUE,
};
```

### Activation Conditions
- Triggers when targeted by any move with `FLAG_BALLISTIC`
- Does NOT block moves that target the user (self-targeting moves)
- Immunity occurs before damage calculation
- Prevents all effects, damage, and secondary effects

### Complete List of Blocked Moves
**Physical Ballistic Moves:**
- Anchor Shot
- Barrage
- Bullet Seed
- Egg Bomb
- Gunk Shot
- Gyro Ball
- Ice Ball
- Magnet Bomb
- Rock Blast
- Rock Wrecker
- Scale Shot
- Seed Bomb
- Spike Cannon

**Special Ballistic Moves:**
- Acid Spray
- Aura Sphere
- Beak Blast
- Electro Ball
- Electro Shot
- Energy Ball
- Flash Cannon
- Focus Blast
- Mist Ball
- Mud Bomb
- Mud Shot
- Octazooka
- Pollen Puff
- Pop Mayhem
- Pyro Ball
- Searing Shot
- Shadow Ball
- Sludge Bomb
- Snipe Shot
- Steel Beam
- Syrup Bomb
- Tar Shot
- Water Gun
- Weather Ball
- Wyrm Wind
- Zap Cannon

### Important Interactions
- **Mold Breaker**: Cannot bypass Bulletproof immunity (works at the move level, not ability level)
- **Gastro Acid**: Can suppress Bulletproof, allowing ballistic moves to hit
- **Self-targeting moves**: Bulletproof does not block moves that target the user
- **Multi-target moves**: Blocks the move entirely for the Bulletproof user, but other targets can still be hit

### Strategic Implications
**Offensive Usage:**
- Provides immunity to many common special attacks (Shadow Ball, Focus Blast)
- Excellent against Bullet Seed and other multi-hit ballistic moves
- Strong counter to many pulse moves (Aura Sphere, Dark Pulse technically isn't ballistic)

**Defensive Considerations:**
- Doesn't block many common physical moves (Earthquake, Close Combat)
- Vulnerable to non-ballistic special moves (Psychic, Flamethrower)
- Can be suppressed by Gastro Acid or similar effects

### Common Users
In Elite Redux, Bulletproof appears as both a regular ability and innate ability on various Pokemon. Common examples include Pokemon with defensive or tanky builds that benefit from selective immunity.

### Competitive Usage
- Excellent in formats with heavy special attack usage
- Pairs well with other defensive abilities as innate
- Strong against specific offensive archetypes
- Less effective against physical sweepers or non-ballistic special attackers

### Counters
- Non-ballistic moves (majority of the movepool)
- Gastro Acid to suppress the ability
- Physical attackers using non-ballistic moves
- Status moves and indirect damage

### Synergies
- Works well with other defensive abilities
- Excellent as an innate ability alongside offensive abilities
- Pairs with recovery moves and defensive stats
- Synergizes with abilities that benefit from taking less damage

### Version History
Bulletproof was introduced in Generation VI and has remained largely unchanged in its core functionality. In Elite Redux, it maintains its original mechanics while being available as both a regular and innate ability on various Pokemon.