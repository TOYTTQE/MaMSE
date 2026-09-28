# MaMSE

![version](https://img.shields.io/badge/version-1.0.0--beta-blue)
![python](https://img.shields.io/badge/python-3.x-green)
![license](https://img.shields.io/badge/license-MIT-orange)
![MaMSE mascot](mamse.png)

A LaTeX subset renderer for terminal.

## Features

- 🧮 Fractions — `\frac{a}{b}`
- 📐 Square roots — `\sqrt{x}`
- ➖ Overline — `\overline{x}`
- ➕ Underline — `\underline{x}`
- 🔢 Binomial — `\binom{n}{k}`
- 🔤 Greek letters — 46 commands
- ➗ Math operators — 55 commands
- 🅰️ Letter styles — `\bold`, `\oblbold`, `\mono`, `\calgrph`
- 🔡 Double-struck — `\set`, `\twoline`, `\mathbb`
- ⬆️ Superscripts / subscripts
- 📏 Baseline-aligned horizontal stacking
- ⚠️ HT / ER error system with colors

## Known limitations

- `\sqrt` with multiline argument draws overline only above the first line
- Nested scripts (`x^{a^{b}}`) not supported
- Nested fractions (`\frac{\frac{a}{b}}{\frac{c}{d}}`) render vertically

## Usage

```bash
python3 MaMSE.py
```

## License

MIT
