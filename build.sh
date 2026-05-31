#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  cat <<EOF
Usage: $0 <tex-file> [latexmk-args...]

Example:
  $0 cv/multi-page/acad-bosch.tex
EOF
  exit 1
fi

texfile="$1"
shift

if [[ ! -f "$texfile" ]]; then
  echo "Error: TeX file not found: $texfile" >&2
  exit 2
fi

base_name="$(basename "$texfile")"
base_no_ext="${base_name%.tex}"
tex_dir="$(cd "$(dirname "$texfile")" && pwd)"
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
build_dir="$script_dir/build"

mkdir -p "$build_dir"

pushd "$tex_dir" >/dev/null
latexmk -pdf -interaction=nonstopmode -file-line-error -outdir="$build_dir" "$base_name" "$@"

mv -f "$build_dir/$base_no_ext.pdf" "$tex_dir/$base_no_ext.pdf"
echo "PDF written to: $tex_dir/$base_no_ext.pdf"
popd >/dev/null
