---
id: 256
name: Neutralizing Gas
status: reviewed
character_count: 250
---

# Neutralizing Gas - Ability ID 256

## In-Game Description
"All abilities are nullified."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Fills the area with gas that completely suppresses all abilities except unsuppressable ones. Effect lasts while user is on field. After the user attempts to switch, all suppressed abilities reactivate their entry effects. Cannot be copied or swapped.

## Detailed Mechanical Explanation
*For Discord/reference use*

**NEUTRALIZING GAS** is an extremely powerful field-wide ability suppression effect that nullifies nearly all other abilities while active.

### Activation Mechanics:
- **Trigger**: Immediately upon entering battle
- **Timing**: Activates before entry hazards
- **Field Effect**: Sets gFieldTimers.neutralizingGas = TRUE
- **Message**: "Neutralizing Gas filled the area!"

### Suppression Rules:
1. **Suppresses ALL abilities EXCEPT**:
   - Unsuppressable abilities (.unsuppressable = TRUE)
   - Persistent abilities (.persistent = TRUE)
   - Abilities on Pokemon with Ability Shield
   
2. **Suppression Method**:
   - Temporarily sets affected abilities to ABILITY_NONE
   - Check occurs through IsSuppressed() function
   - Affects all ability slots in Elite Redux's 4-ability system

3. **Cannot Be Countered By**:
   - Mold Breaker (Neutralizing Gas is unsuppressable)
   - Gastro Acid
   - Worry Seed
   - Simple Beam
   - Any other suppression effect

### Deactivation Mechanics:
**Gas ends when**:
- User switches out
- User faints
- No Pokemon on field has Neutralizing Gas

**When deactivated**:
- gFieldTimers.neutralizingGas = FALSE
- All abilities restored to original state
- Message: "The effects of Neutralizing Gas wore off!"
- ALL Pokemon trigger switch-in abilities again

### Technical Implementation:
```cpp
constexpr Ability NeutralizingGas = {
    .unsuppressable = TRUE,
};
```

### Suppression Check (battle_util.c):
```cpp
int IsSuppressed(int battler, AbilityEnum ability, int checkMoldBreaker) {
    if ((checkMoldBreaker && battler != gBattlerAttacker && 
         gHitMarker & HITMARKER_MOLD_BREAKER && gAbilities[ability].breakable) ||
        ((gFieldTimers.neutralizingGas || gStatuses3[battler] & STATUS3_GASTRO_ACID) && 
         !IsUnsuppressableAbility(ability))) {
        return !DoesBattlerHaveAbilityShield(battler);
    }
    return FALSE;
}
```

### Competitive Impact:
1. **Shuts Down Major Strategies**:
   - Weather teams (no Drizzle/Drought/Sand Stream/Snow Warning)
   - Terrain setters (no Surge abilities)
   - Speed control (no Swift Swim/Chlorophyll/Sand Rush)
   - Setup abilities (no Speed Boost/Beast Boost/Moxie)
   
2. **AI Rating**: 5/5 (highest possible)
   - One of the most valued abilities by AI
   - High priority for AI team building
   - AI will protect Neutralizing Gas users

3. **Team Building**:
   - Best on bulky Pokemon that stay in
   - Anti-synergy with ability-reliant teammates
   - Excellent vs ability-dependent teams
   - Pairs with Pokemon using stats over abilities

### Notable Interactions:
- **Ability Shield**: Only counter - protects holder's abilities
- **Entry Abilities**: All reactivate when gas clears
- **Form Changes**: Affects ability-based forms
- **4-Ability System**: Suppresses ALL ability slots

### Strategic Considerations:
1. **Field Control**:
   - Instant shutdown of field effects
   - Prevents weather/terrain wars
   - Negates speed tiers from abilities
   
2. **Double-Edged**:
   - Also suppresses user's teammates
   - Requires careful team composition
   - Can backfire if not planned properly

3. **Switching Wars**:
   - Opponent may switch to preserve abilities
   - User wants to stay in to maintain effect
   - Pivoting moves become valuable

### Pokemon with Neutralizing Gas:
- Originally from Galarian Weezing
- Check species data for Elite Redux distribution

### Version History:
- Introduced in Gen 8 (Sword/Shield)
- Elite Redux: Affects all 4 ability slots
- Unsuppressable implementation unique to Elite Redux