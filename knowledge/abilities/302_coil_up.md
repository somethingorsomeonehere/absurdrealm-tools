---
id: 302
name: Coil Up
status: reviewed
character_count: 116
---

# Coil Up - Ability ID 302

## In-Game Description
"On entry, gives +1 priority once to the first biting move used."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

On entry, gives +1 priority to the first biting move used. Priority boost is consumed after landing any biting move.

## Detailed Mechanical Explanation
*For Discord/reference use*

**COIL UP** is a unique entry ability that provides a one-time priority boost to biting moves.

### Activation Mechanics:
- **Trigger**: Immediately upon entering battle (onEntry hook)
- **Status Applied**: STATUS4_COILED flag
- **Message**: "{Pokemon} coiled up and is ready to bite!"
- **Duration**: Until first biting move is used

### Effect Details:
1. **Priority Boost**:
   - +1 priority to the first biting move used
   - Biting moves identified by FLAG_STRONG_JAW_BOOST
   - Only affects the FIRST biting move after gaining status
   
2. **Affected Moves**:
   - Bite, Crunch, Fire Fang, Thunder Fang, Ice Fang
   - Poison Fang, Psychic Fangs, Fishious Rend
   - Jaw Lock, Hyper Fang, Super Fang
   - Any move with Strong Jaw boost flag

3. **Status Consumption**:
   - Coiled status removed after using one biting move
   - Non-biting moves preserve the status
   - Status persists through switches if unused

### Technical Implementation:
```cpp
constexpr Ability CoilUp = {
    .onEntry = +[](ON_ENTRY) -> int {
        if (!DoesBattlerHaveStatus(battler, STATUS4_COILED)) {
            gStatuses4[battler] |= STATUS4_COILED;
            PrepareStringBattle(STRINGID_COILEDUP, battler);
            return 1;
        }
        return 0;
    },
};
```

### Priority Calculation (battle_main.c):
```c
if ((gStatuses4[battlerId] & STATUS4_COILED) && 
    (gBattleMoves[move].flags & FLAG_STRONG_JAW_BOOST)) {
    priority++;
}
```

### Interaction with Other Mechanics:
- **Coil Move**: The setup move Coil can grant coiled status if user has Coil Up or Sidewinder
- **Sidewinder Ability**: Related ability that doesn't consume coiled status after use
- **Mold Breaker**: Cannot suppress Coil Up (not breakable)
- **Gastro Acid**: Cannot remove the ability but existing coiled status remains

### Pokemon with Coil Up:
**As Innate Ability**:
- Ekans line (Ekans/Arbok) - Snake Pokemon fitting the theme
- Other serpentine Pokemon in Elite Redux

### Competitive Applications:
1. **Revenge Killing**:
   - Priority Crunch for Dark STAB
   - Priority elemental fangs for coverage
   - Outspeed and KO faster threats

2. **Breaking Speed Tiers**:
   - Overcomes Choice Scarf users
   - Beats priority moves with higher speed
   - Surprises opponents expecting to move first

3. **Synergies**:
   - Strong Jaw: Stack for 1.5x damage on priority bite
   - Choice Band: Maximum damage on priority physical bite
   - Life Orb: Flexible item for boosted priority

### Strategic Considerations:
- Must choose timing carefully - only one use per switch-in
- Opponent can scout with Protect/Detect
- Switching resets the ability for another use
- Best on Pokemon with good biting move coverage

### AI Behavior:
- AI values ability with AI_SCORE_COILED_UP
- Considers coiled status when choosing moves
- May switch in specifically to use priority bite

### Version Notes:
- Elite Redux exclusive ability
- Uses STATUS4 flag system for tracking
- Integrates with Strong Jaw flag for move detection