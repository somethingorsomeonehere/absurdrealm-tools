---
id: 487
name: Super Strain
status: reviewed
character_count: 164
---

# Super Strain - Ability ID 487

## In-Game Description
"KOs lower Attack by 1. Take 25% recoil damage."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

The user's moves deal 25% of the damage done to the user as recoil. When the user knocks out the opponent with a direct attack, user's Attack stat drops by 1 stage.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Super Strain combines recoil modification with a debuffing KO effect, creating a unique risk-reward dynamic where powerful recoil moves become more viable while providing offensive punishment.

### Dual Effect Components

#### Recoil Modification
- **Effect**: All recoil moves deal exactly 25% of damage dealt as recoil
- **Calculation**: max(damage_dealt / 4, 1) HP lost
- **Minimum**: Always at least 1 HP recoil damage
- **Override**: Replaces normal recoil calculations
- **Message**: Uses B_MSG_RECOIL_STRAIN for battle text

#### KO Debuff Effect  
- **Trigger**: When this Pokemon causes an opponent to faint
- **Effect**: Lowers the user's Attack stat by 1 stage
- **Target**: Self-debuff after successful KO
- **Timing**: Occurs immediately after opponent faints
- **Message**: Shows stat reduction battle text

### Technical Implementation
```c
constexpr Ability SuperStrain = {
    .onRecoil = +[](ON_RECOIL) -> int {
        // Modify recoil to 25% of damage dealt
        u32 recoilDamage = max(damage / 4, 1);
        gBattleMoveDamage = recoilDamage;
        BattleScriptCall(B_MSG_RECOIL_STRAIN);
        return TRUE;
    },
    .onBattlerFaints = +[](ON_BATTLER_FAINTS) -> int {
        // Lower Attack by 1 stage after KO
        ChangeStatBuffs(STAT_ATK, -1, MOVE_EFFECT_AFFECTS_USER | 
                       STAT_BUFF_DONT_SET_BUFFERS | MOVE_EFFECT_CERTAIN, 
                       ability);
        BattleScriptCall(BattleScript_LowerStatOnFaintingTarget);
        return TRUE;
    },
    .onBattlerFaintsFor = APPLY_ON_ATTACKER,
};
```

### Recoil Move Interactions
**Common recoil moves affected:**
- Double-Edge: 120 BP, normally 1/3 recoil to 25% recoil
- Head Smash: 150 BP, normally 1/2 recoil to 25% recoil  
- Flare Blitz: 120 BP, normally 1/3 recoil to 25% recoil
- Brave Bird: 120 BP, normally 1/3 recoil to 25% recoil
- Wild Charge: 90 BP, normally 1/4 recoil to 25% recoil

### Damage Calculation Examples
**Head Smash (150 BP, normally 50% recoil):**
- Deals 300 damage to opponent
- Normal recoil: 150 damage to self (50%)
- Super Strain recoil: 75 damage to self (25%)
- **Benefit**: 75 HP saved per use

**Double-Edge (120 BP, normally 33% recoil):**
- Deals 240 damage to opponent  
- Normal recoil: 80 damage to self (33%)
- Super Strain recoil: 60 damage to self (25%)
- **Benefit**: 20 HP saved per use

### Strategic Applications
- **Recoil sweeper**: Makes high-power recoil moves more viable
- **Self-limiting offense**: Attack reduction prevents excessive sweeping
- **Risk mitigation**: Reduces recoil damage for sustainability
- **Balanced aggression**: Powerful moves with built-in balancing
- **KO punishment**: Discourages reckless offensive play

### Recoil Move Synergies
**Optimal move choices:**
- Head Smash: Massive damage with reduced recoil
- Flare Blitz: Reliable Fire STAB with less self-damage
- Brave Bird: Flying coverage with improved sustainability
- Double-Edge: Strong Normal STAB with manageable recoil

### KO Effect Strategy
**Attack reduction implications:**
- **First KO**: -1 Attack stage (67% physical damage)
- **Second KO**: -2 Attack stage (50% physical damage)  
- **Third KO**: -3 Attack stage (40% physical damage)
- **Diminishing returns**: Each KO makes subsequent KOs harder

### Competitive Usage
- **Glass cannon**: High power with built-in limitations
- **Recoil specialist**: Enables recoil move strategies
- **Self-regulating**: Prevents excessive snowballing
- **Risk-reward**: Powerful but with consequences
- **Balanced sweeper**: Strong offense with natural slowdown

### Item Synergies
**Enhanced sustainability:**
- Leftovers: Offset remaining recoil damage
- Life Orb: Stack damage boost (though adds more recoil)
- Choice Band: Maximize initial Attack before reduction
- Sitrus Berry: Emergency healing for recoil damage

### Limitations
- **Self-debuffing**: KOs reduce own offensive power
- **Recoil remains**: Still takes 25% recoil damage
- **Attack dependency**: Physical moves become weaker over time
- **Momentum loss**: Each KO reduces future potential
- **Magic Guard immunity**: Some Pokemon immune to recoil

### Counters
- **Defensive walls**: High HP tanks survive recoil moves
- **Attack boosts**: Items/abilities that offset Attack reduction
- **Special attacks**: Switch to special moves after Attack drops
- **Priority moves**: Quick revenge kills
- **Status moves**: Don't trigger Attack reduction

### Advanced Strategy
**KO management:**
- Plan KO order carefully
- Switch out to reset Attack stages
- Use special moves after Attack drops
- Time KOs for maximum benefit

**Recoil optimization:**
- Choose moves with highest recoil normally
- Head Smash gets maximum benefit
- Avoid low-recoil moves (less improvement)

### Double Battle Applications
- **Spread damage**: Recoil moves hit multiple targets
- **Partner support**: Attack reduction doesn't affect ally
- **Field control**: High-power moves with manageable cost
- **Switching coordination**: Reset Attack stages through switching

### Version History
- Elite Redux custom ability for balanced recoil strategies
- Designed to make recoil moves more viable
- Part of risk-reward ability design philosophy
- Creates unique offensive archetype with built-in limitations