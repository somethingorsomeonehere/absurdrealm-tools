---
id: 258
name: Hunger Switch
status: reviewed
character_count: 142
---

# Hunger Switch - Ability ID 258

## In-Game Description
"Changes between Full and Hangry forms after each turn."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Automatically switches between Full and Hangry forms at the end of each turn. Cannot be overridden, suppressed, swapped, or copied in any way.

## Detailed Mechanical Explanation
*For Discord/reference use*

Hunger Switch is Morpeko's signature ability that causes it to alternate between its Full Belly and Hangry forms at the end of each turn. This form change is automatic and unsuppressable.

### Technical Implementation
- **Trigger**: Activates at the end of each turn (onEndTurn)
- **Form Changes**:
  - SPECIES_MORPEKO ↔ SPECIES_MORPEKO_HANGRY  
  - SPECIES_MORPEKYLL ↔ SPECIES_MORPEKYLL_HANGRY
- **Prevents**: Transform users from triggering the ability
- **Cannot be suppressed**: The ability is marked as unsuppressable
- **Randomizer banned**: Cannot appear on other Pokemon in randomizer modes

### Form Differences
**Morpeko Full Belly Form:**
- Electric/Dark typing
- Abilities: Electric Burst, Nocturnal, Friend Guard
- Innates: Hunger Switch, Gluttony, Lightning Rod

**Morpeko Hangry Form:**  
- Electric/Dark typing (same)
- Abilities: Doom Blast, Electrocytes, Power Spot
- Innates: Hunger Switch, Gluttony, Lightning Rod

### Key Mechanics
1. **Automatic switching**: Form changes every turn without player input
2. **Battle persistence**: Form changes continue throughout the entire battle
3. **Ability access**: Different forms provide access to different main abilities
4. **Visual change**: Each form has distinct sprites and appearance
5. **Signature move interaction**: Aura Wheel's type changes based on the current form

### Strategic Usage
- Provides access to a rotating set of abilities each turn
- Unpredictable for opponents who must adapt to changing ability effects
- Morpeko's diverse ability pool makes it versatile across different turns
- Form prediction becomes crucial for both offensive and defensive play

### Related Pokemon
- **Morpeko**: Original Pokemon with this ability
- **Morpekyll**: Elite Redux variant that also has Hunger Switch

This ability makes Morpeko unique as one of the few Pokemon that changes forms automatically during battle, creating dynamic gameplay where strategy must adapt to the current form's capabilities.