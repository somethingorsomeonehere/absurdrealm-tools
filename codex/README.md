# Elite Redux Ability Codex

A modern, searchable documentation website for all Elite Redux abilities.

## Features

- 🌑 Beautiful dark theme optimized for readability
- 🔍 Built-in search functionality (Ctrl/Cmd + K)
- 📱 Mobile-first responsive design
- ✅ Direct approval workflow for staff (no GitHub issues)
- 🔄 Automatically updates when new abilities are added
- ⚡ Fast static site with VitePress

## Local Development

1. Install dependencies:
   ```bash
   cd codex
   npm install
   ```

2. Configure GitHub Token (Admin Only):
   ```bash
   cp docs/.env.example docs/.env.local
   # Edit docs/.env.local and add: VITE_GITHUB_TOKEN=ghp_your_token_here
   ```
   **Note**: Only the admin needs this token. Staff can approve without it.

3. Start development server:
   ```bash
   npm run dev
   ```

4. Open http://localhost:5173 in your browser

## Deployment to GitHub Pages

1. **Enable GitHub Pages** in your repository:
   - Go to Settings → Pages
   - Set Source to "GitHub Actions"

2. **Push your changes**:
   ```bash
   git add .
   git commit -m "Add Elite Redux Ability Codex"
   git push
   ```

3. The site will automatically deploy when you push to the main branch. The GitHub Action will:
   - Build the VitePress site
   - Deploy to GitHub Pages
   - Make it available at: https://somethingorsomeonehere.github.io/absurdrealm-tools/

## Adding New Abilities

Simply add new `.md` files to the `knowledge/abilities/` folder. The site will automatically:
- Detect new files
- Add them to the sidebar
- Make them searchable
- Deploy the updates when you push

## File Structure

```
absurdrealm-tools/
├── knowledge/
│   └── abilities/      # Your ability markdown files
└── codex/              # Website code
    ├── docs/           # VitePress content
    │   ├── .vitepress/ # Configuration and theme
    │   ├── index.md    # Homepage
    │   └── abilities/  # Abilities index
    └── package.json    # Dependencies
```

## Customization

- **Theme**: Edit `codex/docs/.vitepress/theme/custom.css`
- **Config**: Edit `codex/docs/.vitepress/config.mjs`
- **Homepage**: Edit `codex/docs/index.md`

## Alternative Deployment Options

If you prefer other platforms:

- **Vercel**: Connect your GitHub repo and set build command to `cd codex && npm run build`
- **Cloudflare Pages**: Same as Vercel, output directory is `codex/docs/.vitepress/dist`
