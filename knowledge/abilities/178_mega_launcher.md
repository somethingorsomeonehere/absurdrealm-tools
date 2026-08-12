---
id: 178
name: Mega Launcher
status: reviewed
character_count: 48
---

# Mega Launcher - Ability ID 178

## In-Game Description
"Boosts Beam/Pump/Cannon/Shot/ Gun/Pulse, etc. moves by 1.3x."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts pulse, beam, ball, and aura moves by 30%.

## Detailed Mechanical Explanation
**Mega Launcher** provides a significant **1.3x damage multiplier** to an extensive range of moves, plus special interactions with healing moves.

### Core Mechanics

#### Damage Boost
- **Multiplier**: 1.3x damage to qualifying moves
- **Implementation**: Applied via `onOffensiveMultiplier` in abilities.cc

#### Move Selection Logic
Mega Launcher boosts moves through multiple criteria:
1. **FLAG_MEGA_LAUNCHER_BOOST moves**: Any move with this specific flag
2. **All Status moves**: Every status move gets boosted regardless of name or type
3. **Gunman ability interaction**: If the user has Gunman ability, all status moves are treated as Mega Launcher moves

### Heal Pulse Special Enhancement
**Heal Pulse** receives unique treatment with Mega Launcher:
- **Normal**: Heals 50% of target's max HP
- **Mega Launcher Boosted**: Heals **75% of target's max HP**
- **Implementation**: Special code in battle_script_commands.c checks for Mega Launcher boost and increases healing

```c
if (megaLauncherBoosted)
    gBattleMoveDamage = -(gBattleMons[gActiveBattler].maxHP * 3 / 4);  // 75%
else
    gBattleMoveDamage = -(gBattleMons[gActiveBattler].maxHP / 2);      // 50%
```

### Comprehensive Move Coverage

#### Classic "Beam/Pulse" Moves
- Aurora Beam, Signal Beam, Hyper Beam, Bubble Beam
- Steel Beam, Moongeist Beam, Prismatic Laser
- Heal Pulse, Dragon Pulse, Dark Pulse

#### Ball/Sphere Moves
- Energy Ball, Focus Blast, Aura Sphere
- Shadow Ball, Electro Ball, Weather Ball

#### Projectile Moves
- Rock Blast, Bullet Seed, Seed Bomb
- Gyro Ball, Acid Spray, Mud Bomb

#### Elite Redux Custom Moves
- Archer Shot, Supersonic Shot, Drake Missile
- Various custom beam and pulse attacks

#### Status Move Enhancement
**ALL status moves** receive the 1.3x boost, making Mega Launcher valuable for:
- Support movesets
- Status-based strategies
- Utility moves

### Notable Pokemon with Mega Launcher

#### Natural Users
- **Blastoise line**: Signature Mega Launcher users
- **Clauncher/Clawitzer**: Original Mega Launcher Pokemon

#### High-Tier Users
- **Kingdra**: Has it as an innate ability
- **Genesect variants**: All forms have Mega Launcher as innate
- **Ultra Necrozma forms**: Legendary-tier users

### AI Rating
The AI rates Mega Launcher as **7/10** in terms of ability strength, placing it in the "strong" tier alongside abilities like Mold Breaker and Moxie.

### Battle Applications

#### Offensive Power
- 1.3x boost to massive movepool including high-BP attacks
- Enhanced projectile and energy-based movesets
- Versatility across physical, special, and status moves

#### Support Utility
- Enhanced Heal Pulse (75% HP healing)
- Boosted status moves for better support
- Team utility through enhanced healing

#### Special Interactions
- **Artillery/Super Scope abilities**: Make Mega Launcher moves always hit
- **Gunman ability**: Expands Mega Launcher to include ALL status moves
- **Heal Pulse bleeding interaction**: Heal Pulse fails if target has bleed status

### Strategic Implications
Mega Launcher transforms Pokemon into versatile attackers capable of:
- High damage output across multiple move types
- Superior support capabilities with enhanced healing
- Effective status move application
- Consistent performance regardless of weather or terrain

The ability's broad coverage and utility make it valuable for both offensive and support roles, with the Heal Pulse enhancement providing unique team support capabilities.
