#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

// Paths
const sourceDir = path.join(__dirname, '../../knowledge/abilities');
const targetDir = path.join(__dirname, '../docs/abilities');

// Ensure target directory exists
if (!fs.existsSync(targetDir)) {
  fs.mkdirSync(targetDir, { recursive: true });
}

// Get only ability files (pattern: number_name.md) from source directory
const files = fs.readdirSync(sourceDir).filter(file => {
  return /^\d+_/.test(file) && file.endsWith('.md');
});

console.log(`Copying ${files.length} ability files...`);

// Copy each file
files.forEach(file => {
  
  const sourcePath = path.join(sourceDir, file);
  const targetPath = path.join(targetDir, file);
  
  fs.copyFileSync(sourcePath, targetPath);
  console.log(`  ✓ ${file}`);
});

console.log('Done! All ability files copied successfully.');

// Hot reload system removed - no longer copying ability-status.json