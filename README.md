# CV Build Workflow

This folder contains the CV LaTeX build helper.

## Usage

From `Overleaf/cv`:

```bash
./build.sh multi-page/acad-bosch.tex
./build.sh single-page/single-ComVis.tex
```

To download : 
- https://raw.githubusercontent.com/gawtamcr/cv/main/multi-page/acad-jana.pdf

## Output layout

- `cv/build/` stores LaTeX build artifacts:
  - `.aux`, `.log`, `.fls`, `.out`, `.fdb_latexmk`, etc.
- The generated PDF is moved beside the source `.tex` file:
  - `cv/multi-page/acad-bosch.pdf`
  - `cv/single-page/single-ComVis.pdf`

## Notes

- The helper uses `latexmk` and the `-outdir` option.
- The PDF is intentionally kept next to the `.tex` source, while all intermediate files are centralized in `cv/build/`.
