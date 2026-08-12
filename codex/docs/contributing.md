# Contributing to the Elite Redux Ability Codex

Thank you for your interest in helping improve the Elite Redux Ability Codex! Community feedback and contributions are essential for maintaining accurate and comprehensive ability documentation.

## How to Contribute

### 🔍 Reviewing Abilities

The easiest way to contribute is by reviewing ability pages and reporting issues:

1. **Browse the abilities** using the sidebar or search
2. **Read the descriptions carefully** and check for:
   - Factual errors in game mechanics
   - Unclear or confusing explanations
   - Missing important information
   - Grammar and spelling errors
   - Character count issues in extended descriptions (should be 280-300 characters)

3. **Report issues** using the "📝 Suggest Edit" button at the bottom of each ability page

## ⚠️ Important: Character Limits

**CRITICAL CONSTRAINT**: Extended ability descriptions have a **strict 280-300 character limit** due to Game Boy Advance hardware limitations. This is not a suggestion - it's a technical requirement enforced by the game engine.

- **Too short** (under 280): May look incomplete in-game
- **Too long** (over 300): Will be cut off or cause display errors
- **Character counting**: Includes all text, spaces, and punctuation
- **No exceptions**: The GBA UI cannot display longer text

When suggesting changes, always check the character count!

### 📝 Reporting Issues

When you click "Suggest Edit" on an ability page, you'll be taken to GitHub with a pre-filled issue template. The template includes:

- **Ability Information**: Name, ID, and source file (automatically filled)
- **Issue Type**: Checkboxes for common issue categories
- **Description**: Space to describe the problem in detail
- **Suggested Changes**: Your specific text recommendations
- **Additional Context**: References, links, or other helpful information

### 🔄 From Issues to Pull Requests

The Elite Redux team reviews all ability feedback issues and can convert them into pull requests for implementation. Here's the typical workflow:

1. **You submit an issue** using the ability codex feedback system
2. **Team reviews the issue** for accuracy and completeness
3. **Issue is converted to a PR** with the necessary file changes
4. **Changes are implemented** in both:
   - Individual ability markdown files (`knowledge/abilities/`)
   - Central data file (`extended_descriptions.txt`)
5. **VitePress site is updated** automatically on the next build

## What Gets Updated

When ability descriptions are improved, several files are updated:

### Source Files
- **Individual ability files**: `knowledge/abilities/[id]_[name].md`
- **Central data file**: `knowledge/extended_ability_descriptions/extended_descriptions.txt`
- **Progress tracking**: `progress.md` with human review status

### Generated Files
- **VitePress docs**: Automatically copied from source files
- **In-game descriptions**: Generated from the central data file

## Quality Standards

To maintain high-quality documentation, ability descriptions should:

### ✅ Content Requirements
- **Accurate mechanics**: Reflect actual in-game behavior
- **Complete information**: Include all relevant details about the ability
- **Clear explanations**: Easy to understand for players of all levels
- **Proper terminology**: Use consistent game terms and formatting

### ✅ Technical Requirements
- **⚠️ CRITICAL: Extended descriptions MUST be 280-300 characters** for in-game UI display
- **GBA Hardware Limits**: The Game Boy Advance has strict UI constraints that cannot be exceeded
- **Proper formatting**: Follow established markdown structure
- **No exceptions**: Character count is enforced by the game engine

### ✅ Style Guidelines
- **Concise writing**: Clear and direct explanations
- **Consistent tone**: Professional but accessible
- **No redundancy**: Avoid repeating information unnecessarily
- **Proper grammar**: Correct spelling, punctuation, and syntax

## Types of Contributions Welcome

### 🎯 High Priority
- **Factual corrections**: Fixing mechanical inaccuracies
- **Clarity improvements**: Making confusing descriptions clearer
- **Missing information**: Adding important details that were omitted

### 📝 Medium Priority
- **Grammar fixes**: Correcting spelling and syntax errors
- **Formatting improvements**: Better markdown structure
- **Consistency updates**: Aligning terminology across abilities

### 🎨 Low Priority
- **Style improvements**: Minor wording enhancements
- **Optimization**: Reducing character count while maintaining clarity

## Advanced Contributions

### Direct Pull Requests

Experienced contributors can create pull requests directly:

1. **Fork the repository**: `https://github.com/darkyy92/eliteredux-darky`
2. **Edit the source files**:
   - `knowledge/abilities/[id]_[name].md`
   - `knowledge/extended_ability_descriptions/extended_descriptions.txt`
3. **Update progress tracking**: Mark abilities as reviewed in `progress.md`
4. **Submit a pull request** with clear description of changes

### File Locations

```
eliteredux-source/
├── eliteredux-darky/
│   ├── knowledge/
│   │   ├── abilities/           # Individual ability files
│   │   └── extended_ability_descriptions/
│   │       ├── extended_descriptions.txt  # Central data file
│   │       └── progress.md               # Progress tracking
│   └── codex/                   # VitePress documentation site
└── .github/
    └── ISSUE_TEMPLATE/
        └── ability-review.yml   # Issue template for feedback
```

## Community Guidelines

### 🤝 Be Respectful
- Provide constructive feedback
- Acknowledge the work of previous contributors
- Focus on improving documentation quality

### 🎯 Be Specific
- Reference exact text when reporting issues
- Provide clear examples of problems
- Suggest specific improvements when possible

### 📚 Research First
- Check existing issues before creating duplicates
- Verify information against the actual game code
- Test mechanics in-game when possible

## Getting Help

If you need assistance with contributing:

- **Discord**: Join our community at [discord.elite-redux.com](http://discord.elite-redux.com)
- **Wiki**: Check the main wiki at [wiki.elite-redux.com](https://wiki.elite-redux.com)
- **Issues**: Create a general issue on GitHub for questions

## Recognition

Contributors who help improve the ability codex will be:

- **Acknowledged** in the project's contributor list
- **Credited** in relevant commit messages
- **Appreciated** by the entire Elite Redux community!

---

*Ready to help? Start by browsing the [abilities](/abilities/) and clicking "Suggest Edit" when you spot something that could be improved!*