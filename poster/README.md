# Before the Statin: Citrus Bergamot — 90 × 150 cm poster

| File | What it is |
| --- | --- |
| `Bergamot_Poster_90x150cm.pdf` | **Print file.** 900 × 1500 mm, full bleed background, vector text and charts. |
| `preview.jpg` | Screen preview of the same page. |
| `poster.html` | Source. All layout, type and charts are plain HTML/CSS/SVG in millimetres. |
| `build.js` | Renders `poster.html` → PDF + preview with headless Chromium. |
| `assets/` | Painting, university logo, fruit detail, header photo, reference QR code. |

## Re-rendering after an edit

```bash
cd poster && node build.js
```

The build prints a layout report: `overflow` must stay empty and `contentBottom`
must stay below `posterHeight` (5669 px = 1500 mm), otherwise something is
spilling off the sheet.

## Layout

Everything is on one grid: 34 mm page margins, three 266.67 mm columns, 16 mm
gutters, and four labelled acts (Background → Problem/gap/hypothesis → Evidence
→ How to test it). Band heights are set in millimetres in the CSS at the top of
`poster.html`; if you change one, take the same amount off another so the bands
still sum to 1500 mm.

## Printing

Print at 100% / "actual size" — do not let the shop scale to fit. The page is
exactly 900 × 1500 mm with no crop marks; ask for 3 mm bleed only if their
machine needs it, in which case re-export with a slightly larger `@page` size.
