#!/usr/bin/env bash
set -euo pipefail

VERSION_LABEL="${1:-}"
BASE_ROM="${2:-/Users/joel/Library/CloudStorage/GoogleDrive-darkyy92@gmail.com/My Drive/Pokemon/ROM Hacks/Pokemon Elite Redux/Elite Redux ROM/Trashman ROM/1986 - Pokemon Emerald (U)(TrashMan).gba}"
BUILT_ROM_INPUT="${3:-}"
OUTPUT_DIR_INPUT="${4:-}"

if [[ -z "$VERSION_LABEL" ]]; then
  echo "usage: $0 \"<version>\" [base_rom] [built_rom] [output_dir]" >&2
  exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
REPO_ROOT="$(cd "$SKILL_DIR/../../../.." && pwd)"

BUILT_ROM="${BUILT_ROM_INPUT:-$REPO_ROOT/pokeemerald_modern.gba}"
OUTPUT_DIR="${OUTPUT_DIR_INPUT:-/Users/joel/Library/CloudStorage/GoogleDrive-darkyy92@gmail.com/My Drive/Pokemon/ROM Hacks/Pokemon Elite Redux/Elite Redux ROM/Dev Versions/Elite Redux v${VERSION_LABEL} Dev}"
OUTPUT_BPS="$OUTPUT_DIR/Elite Redux v${VERSION_LABEL} Dev.bps"
OUTPUT_GBA="$OUTPUT_DIR/Elite Redux v${VERSION_LABEL} Dev.gba"

ensure_flips() {
  if [[ -x "$HOME/.local/bin/flips" ]]; then
    echo "$HOME/.local/bin/flips"
    return
  fi

  mkdir -p "$HOME/.local/src" "$HOME/.local/bin"

  if [[ -d "$HOME/.local/src/Flips/.git" ]]; then
    git -C "$HOME/.local/src/Flips" pull --ff-only >/dev/null
  else
    git clone https://github.com/Alcaro/Flips.git "$HOME/.local/src/Flips" >/dev/null
  fi

  make -C "$HOME/.local/src/Flips" >/dev/null
  cp "$HOME/.local/src/Flips/flips" "$HOME/.local/bin/flips"
  chmod +x "$HOME/.local/bin/flips"
  echo "$HOME/.local/bin/flips"
}

if [[ ! -f "$BASE_ROM" ]]; then
  echo "base ROM not found: $BASE_ROM" >&2
  exit 1
fi

if [[ ! -f "$BUILT_ROM" ]]; then
  echo "built ROM not found: $BUILT_ROM" >&2
  exit 1
fi

mkdir -p "$OUTPUT_DIR"

FLIPS_BIN="$(ensure_flips)"
TMP_ROM="$(mktemp -t eliteredux_patch_verify)"
trap 'rm -f "$TMP_ROM"' EXIT

echo "Creating patch:"
echo "  base:   $BASE_ROM"
echo "  built:  $BUILT_ROM"
echo "  dir:    $OUTPUT_DIR"
echo "  bps:    $OUTPUT_BPS"
echo "  gba:    $OUTPUT_GBA"

"$FLIPS_BIN" --create --bps "$BASE_ROM" "$BUILT_ROM" "$OUTPUT_BPS"
cp "$BUILT_ROM" "$OUTPUT_GBA"
"$FLIPS_BIN" --apply "$OUTPUT_BPS" "$BASE_ROM" "$TMP_ROM" >/dev/null

if ! cmp -s "$TMP_ROM" "$BUILT_ROM"; then
  echo "patch verification failed: recreated ROM does not match built ROM" >&2
  exit 1
fi

echo
echo "Patch and ROM prepared successfully."
echo "BPS: $OUTPUT_BPS"
echo "GBA: $OUTPUT_GBA"
shasum -a 256 "$BUILT_ROM" "$OUTPUT_GBA" "$OUTPUT_BPS"
