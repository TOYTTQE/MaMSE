import re
import sys

ANSI_RE = re.compile(r"\033\[[0-9;]*m")

def visible_len(row):
	return len(ANSI_RE.sub("", row))

def pad_right(row, width):
	diff = width - visible_len(row)
	return row + " " * max(0, diff)

def center_row(row, width):
	diff = width - visible_len(row)
	left = diff // 2
	right = diff - left
	return " " * left + row + " " * right

gl = {
	r"\alpha": "𝛼", r"\beta": "𝛽", r"\gamma": "𝛾", r"\delta": "𝛿",
	r"\epsilon": "𝜀", r"\zeta": "𝜁", r"\eta": "𝜂", r"\theta": "𝜃",
	r"\iota": "𝜄", r"\kappa": "𝜅", r"\lambda": "𝜆", r"\mu": "𝜇",
	r"\nu": "𝜈", r"\xi": "𝜉", r"\omicron": "𝜊", r"\pi": "𝜋",
	r"\rho": "𝜌", r"\varsigma": "𝜍", r"\sigma": "𝜎", r"\tau": "𝜏",
	r"\upsilon": "𝜐", r"\varphi": "𝜑", r"\chi": "𝜒", r"\psi": "𝜓",
	r"\omega": "𝜔", r"\partial": "𝜕", r"\varepsilon": "𝜀",
	r"\vartheta": "𝜗", r"\varpi": "𝜛", r"\varrho": "𝜚",
	r"\Gamma": "𝛤", r"\Delta": "𝛥", r"\Theta": "𝛩", r"\Lambda": "𝛬",
	r"\Xi": "𝛯", r"\Pi": "𝛱", r"\Sigma": "𝛴", r"\Upsilon": "𝛶",
	r"\Phi": "𝛷", r"\Psi": "𝛹", r"\Omega": "𝛺", r"\digamma": "𝟊",
	r"\varkappa": "𝜘", r"\varTheta": "𝛳", r"\nabla": "𝛻",
}

gl_ops = {
	r"\infty": "∞", r"\pm": "±", r"\mp": "∓",
	r"\times": "×", r"\div": "÷", r"\cdot": "·",
	r"\ast": "∗", r"\star": "⋆", r"\circ": "∘", r"\bullet": "•",
	r"\sum": "∑", r"\prod": "∏", r"\int": "∫", r"\oint": "∮",
	r"\iint": "∬", r"\iiint": "∭", r"\lim": "lim",
	r"\leq": "≤", r"\le": "≤", r"\geq": "≥", r"\ge": "≥",
	r"\neq": "≠", r"\ne": "≠", r"\approx": "≈", r"\equiv": "≡",
	r"\sim": "∼", r"\propto": "∝", r"\ll": "≪", r"\gg": "≫",
	r"\rightarrow": "→", r"\to": "→", r"\leftarrow": "←",
	r"\leftrightarrow": "↔", r"\Rightarrow": "⇒", r"\Leftarrow": "⇐",
	r"\Leftrightarrow": "⇔", r"\uparrow": "↑", r"\downarrow": "↓",
	r"\in": "∈", r"\notin": "∉", r"\subset": "⊂", r"\supset": "⊃",
	r"\subseteq": "⊆", r"\supseteq": "⊇", r"\cup": "∪", r"\cap": "∩",
	r"\emptyset": "∅", r"\forall": "∀", r"\exists": "∃",
	r"\neg": "¬", r"\land": "∧", r"\lor": "∨",
	r"\ldots": "…", r"\cdots": "⋯", r"\dots": "…",
	r"\angle": "∠", r"\perp": "⊥", r"\parallel": "∥", r"\degree": "°",
}

gl_set_upper = {"A": "𝔸", "B": "𝔹", "C": "ℂ", "D": "𝔻", "E": "𝔼", "F": "𝔽", "G": "𝔾", "H": "ℍ", "I": "𝕀", "J": "𝕁", "K": "𝕂", "L": "𝕃", "M": "𝕄", "N": "ℕ", "O": "𝕆", "P": "ℙ", "Q": "ℚ", "R": "ℝ", "S": "𝕊", "T": "𝕋", "U": "𝕌", "V": "𝕍", "W": "𝕎", "X": "𝕏", "Y": "𝕐", "Z": "ℤ"}
gl_set_lower = {"a": "𝕒", "b": "𝕓", "c": "𝕔", "d": "𝕕", "e": "𝕖", "f": "𝕗", "g": "𝕘", "h": "𝕙", "i": "𝕚", "j": "𝕛", "k": "𝕜", "l": "𝕝", "m": "𝕞", "n": "𝕟", "o": "𝕠", "p": "𝕡", "q": "𝕢", "r": "𝕣", "s": "𝕤", "t": "𝕥", "u": "𝕦", "v": "𝕧", "w": "𝕨", "x": "𝕩", "y": "𝕪", "z": "𝕫"}
gl_set_digit = {"0": "𝟘", "1": "𝟙", "2": "𝟚", "3": "𝟛", "4": "𝟜", "5": "𝟝", "6": "𝟞", "7": "𝟟", "8": "𝟠", "9": "𝟡"}
gl_set_greek = {"gamma": "ℾ", "pi": "ℿ"}
gl_set_all = {**gl_set_upper, **gl_set_lower, **gl_set_digit, **gl_set_greek}

gl_bold_upper = {"A": "𝐀", "B": "𝐁", "C": "𝐂", "D": "𝐃", "E": "𝐄", "F": "𝐅", "G": "𝐆", "H": "𝐇", "I": "𝐈", "J": "𝐉", "K": "𝐊", "L": "𝐋", "M": "𝐌", "N": "𝐍", "O": "𝐎", "P": "𝐏", "Q": "𝐐", "R": "𝐑", "S": "𝐒", "T": "𝐓", "U": "𝐔", "V": "𝐕", "W": "𝐖", "X": "𝐗", "Y": "𝐘", "Z": "𝐙"}
gl_bold_lower = {"a": "𝐚", "b": "𝐛", "c": "𝐜", "d": "𝐝", "e": "𝐞", "f": "𝐟", "g": "𝐠", "h": "𝐡", "i": "𝐢", "j": "𝐣", "k": "𝐤", "l": "𝐥", "m": "𝐦", "n": "𝐧", "o": "𝐨", "p": "𝐩", "q": "𝐪", "r": "𝐫", "s": "𝐬", "t": "𝐭", "u": "𝐮", "v": "𝐯", "w": "𝐰", "x": "𝐱", "y": "𝐲", "z": "𝐳"}
gl_bold_digit = {"0": "𝟎", "1": "𝟏", "2": "𝟐", "3": "𝟑", "4": "𝟒", "5": "𝟓", "6": "𝟔", "7": "𝟕", "8": "𝟖", "9": "𝟗"}
gl_bold_all = {**gl_bold_upper, **gl_bold_lower, **gl_bold_digit}

gl_obl_upper = {"A": "𝘼", "B": "𝘽", "C": "𝘾", "D": "𝘿", "E": "𝙀", "F": "𝙁", "G": "𝙂", "H": "𝙃", "I": "𝙄", "J": "𝙅", "K": "𝙆", "L": "𝙇", "M": "𝙈", "N": "𝙉", "O": "𝙊", "P": "𝙋", "Q": "𝙌", "R": "𝙍", "S": "𝙎", "T": "𝙏", "U": "𝙐", "V": "𝙑", "W": "𝙒", "X": "𝙓", "Y": "𝙔", "Z": "𝙕"}
gl_obl_lower = {"a": "𝙖", "b": "𝙗", "c": "𝙘", "d": "𝙙", "e": "𝙚", "f": "𝙛", "g": "𝙜", "h": "𝙝", "i": "𝙞", "j": "𝙟", "k": "𝙠", "l": "𝙡", "m": "𝙢", "n": "𝙣", "o": "𝙤", "p": "𝙥", "q": "𝙦", "r": "𝙧", "s": "𝙨", "t": "𝙩", "u": "𝙪", "v": "𝙫", "w": "𝙬", "x": "𝙭", "y": "𝙮", "z": "𝙯"}
gl_obl_digit = {"0": "𝟬", "1": "𝟭", "2": "𝟮", "3": "𝟯", "4": "𝟰", "5": "𝟱", "6": "𝟲", "7": "𝟳", "8": "𝟴", "9": "𝟵"}
gl_obl_all = {**gl_obl_upper, **gl_obl_lower, **gl_obl_digit}

gl_mono_upper = {"A": "𝙰", "B": "𝙱", "C": "𝙲", "D": "𝙳", "E": "𝙴", "F": "𝙵", "G": "𝙶", "H": "𝙷", "I": "𝙸", "J": "𝙹", "K": "𝙺", "L": "𝙻", "M": "𝙼", "N": "𝙽", "O": "𝙾", "P": "𝙿", "Q": "𝚀", "R": "𝚁", "S": "𝚂", "T": "𝚃", "U": "𝚄", "V": "𝚅", "W": "𝚆", "X": "𝚇", "Y": "𝚈", "Z": "𝚉"}
gl_mono_lower = {"a": "𝚊", "b": "𝚋", "c": "𝚌", "d": "𝚍", "e": "𝚎", "f": "𝚏", "g": "𝚐", "h": "𝚑", "i": "𝚒", "j": "𝚓", "k": "𝚔", "l": "𝚕", "m": "𝚖", "n": "𝚗", "o": "𝚘", "p": "𝚙", "q": "𝚚", "r": "𝚛", "s": "𝚜", "t": "𝚝", "u": "𝚞", "v": "𝚟", "w": "𝚠", "x": "𝚡", "y": "𝚢", "z": "𝚣"}
gl_mono_digit = {"0": "𝟶", "1": "𝟷", "2": "𝟸", "3": "𝟹", "4": "𝟺", "5": "𝟻", "6": "𝟼", "7": "𝟽", "8": "𝟾", "9": "𝟿"}
gl_mono_all = {**gl_mono_upper, **gl_mono_lower, **gl_mono_digit}

gl_cal_upper = {"A": "𝒜", "B": "ℬ", "C": "𝒞", "D": "𝒟", "E": "ℰ", "F": "ℱ", "G": "𝒢", "H": "ℋ", "I": "ℐ", "J": "𝒥", "K": "𝒦", "L": "ℒ", "M": "ℳ", "N": "𝒩", "O": "𝒪", "P": "𝒫", "Q": "𝒬", "R": "ℛ", "S": "𝒮", "T": "𝒯", "U": "𝒰", "V": "𝒱", "W": "𝒲", "X": "𝒳", "Y": "𝒴", "Z": "𝒵"}
gl_cal_lower = {"a": "𝒶", "b": "𝒷", "c": "𝒸", "d": "𝒹", "e": "ℯ", "f": "𝒻", "g": "ℊ", "h": "𝒽", "i": "𝒾", "j": "𝒿", "k": "𝓀", "l": "𝓁", "m": "𝓂", "n": "𝓃", "o": "ℴ", "p": "𝓅", "q": "𝓆", "r": "𝓇", "s": "𝓈", "t": "𝓉", "u": "𝓊", "v": "𝓋", "w": "𝓌", "x": "𝓍", "y": "𝓎", "z": "𝓏"}
gl_cal_all = {**gl_cal_upper, **gl_cal_lower}

gl_set = {}
for ch in gl_set_upper:
	gl_set["\\set" + ch] = gl_set_upper[ch]
	gl_set["\\twoline" + ch] = gl_set_upper[ch]
for ch in gl_set_lower:
	gl_set["\\set" + ch] = gl_set_lower[ch]
	gl_set["\\twoline" + ch] = gl_set_lower[ch]
for ch in gl_set_digit:
	gl_set["\\set" + ch] = gl_set_digit[ch]
	gl_set["\\twoline" + ch] = gl_set_digit[ch]
for name in gl_set_greek:
	gl_set["\\set" + name] = gl_set_greek[name]
	gl_set["\\twoline" + name] = gl_set_greek[name]

gl_bold = {"\\bold" + ch: gl_bold_all[ch] for ch in gl_bold_all}
gl_obl = {"\\oblbold" + ch: gl_obl_all[ch] for ch in gl_obl_all}
gl_mono = {"\\mono" + ch: gl_mono_all[ch] for ch in gl_mono_all}
gl_cal = {"\\calgrph" + ch: gl_cal_all[ch] for ch in gl_cal_all}

gl_styles = {**gl_set, **gl_bold, **gl_obl, **gl_mono, **gl_cal}

ital = {"a": "𝑎", "b": "𝑏", "c": "𝑐", "d": "𝑑", "e": "𝑒", "f": "𝑓", "g": "𝑔", "h": "ℎ", "i": "𝑖", "j": "𝑗", "k": "𝑘", "l": "𝑙", "m": "𝑚", "n": "𝑛", "o": "𝑜", "p": "𝑝", "q": "𝑞", "r": "𝑟", "s": "𝑠", "t": "𝑡", "u": "𝑢", "v": "𝑣", "w": "𝑤", "x": "𝑥", "y": "𝑦", "z": "𝑧", "A": "𝐴", "B": "𝐵", "C": "𝐶", "D": "𝐷", "E": "𝐸", "F": "𝐹", "G": "𝐺", "H": "𝐻", "I": "𝐼", "J": "𝐽", "K": "𝐾", "L": "𝐿", "M": "𝑀", "N": "𝑁", "O": "𝑂", "P": "𝑃", "Q": "𝑄", "R": "𝑅", "S": "𝑆", "T": "𝑇", "U": "𝑈", "V": "𝑉", "W": "𝑊", "X": "𝑋", "Y": "𝑌", "Z": "𝑍"}
bold_digit = {"0": "𝟎", "1": "𝟏", "2": "𝟐", "3": "𝟑", "4": "𝟒", "5": "𝟓", "6": "𝟔", "7": "𝟕", "8": "𝟖", "9": "𝟗"}

sup_digit = {"0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹"}
sup_sign = {"+": "⁺", "-": "⁻", "=": "⁼", "(": "⁽", ")": "⁾", "n": "ⁿ"}
sup_lower = {"a": "ᵃ", "b": "ᵇ", "c": "ᶜ", "d": "ᵈ", "e": "ᵉ", "f": "ᶠ", "g": "ᵍ", "h": "ʰ", "i": "ⁱ", "j": "ʲ", "k": "ᵏ", "l": "ˡ", "m": "ᵐ", "n": "ⁿ", "o": "ᵒ", "p": "ᵖ", "r": "ʳ", "s": "ˢ", "t": "ᵗ", "u": "ᵘ", "v": "ᵛ", "w": "ʷ", "x": "ˣ", "y": "ʸ", "z": "ᶻ"}
sup_upper = {"A": "ᴬ", "B": "ᴮ", "D": "ᴰ", "E": "ᴱ", "G": "ᴳ", "H": "ᴴ", "I": "ᴵ", "J": "ᴶ", "K": "ᴷ", "L": "ᴸ", "M": "ᴹ", "N": "ᴺ", "O": "ᴼ", "P": "ᴾ", "R": "ᴿ", "T": "ᵀ", "U": "ᵁ", "V": "ⱽ", "W": "ᵂ"}
sup_greek = {"α": "ᵅ", "β": "ᵝ", "γ": "ᵞ", "δ": "ᵟ", "ε": "ᵋ", "θ": "ᶿ", "ι": "ᶥ", "φ": "ᵠ", "χ": "ᵡ"}
sup_all = {**sup_digit, **sup_sign, **sup_lower, **sup_upper, **sup_greek}

sub_digit = {"0": "₀", "1": "₁", "2": "₂", "3": "₃", "4": "₄", "5": "₅", "6": "₆", "7": "₇", "8": "₈", "9": "₉"}
sub_sign = {"+": "₊", "-": "₋", "=": "₌", "(": "₍", ")": "₎", "·": ".", "•": "."}
sub_lower = {"a": "ₐ", "e": "ₑ", "h": "ₕ", "i": "ᵢ", "j": "ⱼ", "k": "ₖ", "l": "ₗ", "m": "ₘ", "n": "ₙ", "o": "ₒ", "p": "ₚ", "r": "ᵣ", "s": "ₛ", "t": "ₜ", "u": "ᵤ", "v": "ᵥ", "x": "ₓ"}
sub_greek = {"β": "ᵦ", "γ": "ᵧ", "ρ": "ᵨ", "φ": "ᵩ", "χ": "ᵪ"}
sub_all = {**sub_digit, **sub_sign, **sub_lower, **sub_greek}

def find_matching_brace(s, start):
	depth = 0
	for i in range(start, len(s)):
		if s[i] == "{":
			depth += 1
		elif s[i] == "}":
			depth -= 1
			if depth == 0:
				return i
	return -1

def replace_greek(s):
	for cmd in sorted(gl, key=len, reverse=True):
		s = re.sub(re.escape(cmd) + r"(?![a-zA-Z])", gl[cmd], s)
	return s

def replace_ops(s):
	for cmd in sorted(gl_ops, key=len, reverse=True):
		s = re.sub(re.escape(cmd) + r"(?![a-zA-Z])", gl_ops[cmd], s)
	return s

def replace_styles(s):
	for cmd in sorted(gl_styles, key=len, reverse=True):
		s = re.sub(re.escape(cmd) + r"(?![a-zA-Z0-9])", gl_styles[cmd], s)
	return s

def replace_brace_style(s, cmd_name, table):
	marker = "\\" + cmd_name + "{"
	while True:
		i = s.find(marker)
		if i == -1:
			break
		j = find_matching_brace(s, i + len(marker) - 1)
		if j == -1:
			break
		inner = s[i + len(marker):j]
		replaced = "".join(table.get(ch, ch) for ch in inner)
		s = s[:i] + replaced + s[j+1:]
	return s

def split_into_blocks(s):
	blocks = []
	buf = ""
	i = 0
	while i < len(s):
		if s[i:i+5] == "\\frac" and i + 5 < len(s) and s[i+5] == "{":
			if buf:
				blocks.append(("text", buf))
				buf = ""
			rest = s[i+5:]
			j1 = find_matching_brace(rest, 0)
			if j1 == -1:
				return [("error", "UNCLOSED")]
			rest2 = rest[j1+1:]
			if not rest2.startswith("{"):
				return [("error", "NO-SYMBOL")]
			j2 = find_matching_brace(rest2, 0)
			if j2 == -1:
				return [("error", "UNCLOSED")]
			total_len = 5 + (j1 + 1) + (j2 + 1)
			blocks.append(("frac", s[i:i+total_len]))
			i += total_len
		elif s[i:i+5] == "\\sqrt" and i + 5 < len(s) and s[i+5] == "{":
			if buf:
				blocks.append(("text", buf))
				buf = ""
			rest = s[i+5:]
			j = find_matching_brace(rest, 0)
			if j == -1:
				return [("error", "UNCLOSED")]
			total_len = 5 + (j + 1)
			blocks.append(("sqrt", s[i:i+total_len]))
			i += total_len
		elif s[i:i+9] == "\\overline" and i + 9 < len(s) and s[i+9] == "{":
			if buf:
				blocks.append(("text", buf))
				buf = ""
			rest = s[i+9:]
			j = find_matching_brace(rest, 0)
			if j == -1:
				return [("error", "UNCLOSED")]
			total_len = 9 + (j + 1)
			blocks.append(("overline", s[i:i+total_len]))
			i += total_len
		elif s[i:i+10] == "\\underline" and i + 10 < len(s) and s[i+10] == "{":
			if buf:
				blocks.append(("text", buf))
				buf = ""
			rest = s[i+10:]
			j = find_matching_brace(rest, 0)
			if j == -1:
				return [("error", "UNCLOSED")]
			total_len = 10 + (j + 1)
			blocks.append(("underline", s[i:i+total_len]))
			i += total_len
		elif s[i:i+6] == "\\binom" and i + 6 < len(s) and s[i+6] == "{":
			if buf:
				blocks.append(("text", buf))
				buf = ""
			rest = s[i+6:]
			j1 = find_matching_brace(rest, 0)
			if j1 == -1:
				return [("error", "UNCLOSED")]
			rest2 = rest[j1+1:]
			if not rest2.startswith("{"):
				return [("error", "NO-SYMBOL")]
			j2 = find_matching_brace(rest2, 0)
			if j2 == -1:
				return [("error", "UNCLOSED")]
			total_len = 6 + (j1 + 1) + (j2 + 1)
			blocks.append(("binom", s[i:i+total_len]))
			i += total_len
		else:
			buf += s[i]
			i += 1
	if buf:
		blocks.append(("text", buf))
	return blocks

def parse_scripts(s):
	result = ""
	miss_sup = []
	miss_sub = []
	i = 0
	while i < len(s):
		ch = s[i]
		if ch == "^" or ch == "_":
			table = sup_all if ch == "^" else sub_all
			miss = miss_sup if ch == "^" else miss_sub
			i += 1
			if i < len(s) and s[i] == "{":
				j = find_matching_brace(s, i)
				if j == -1:
					result += ch
					continue
				inner = s[i+1:j]
				for c in inner:
					if c in table:
						result += table[c]
					else:
						result += c
						if c not in miss:
							miss.append(c)
				i = j + 1
			elif i < len(s):
				c = s[i]
				if c in table:
					result += table[c]
				else:
					result += c
					if c not in miss:
						miss.append(c)
				i += 1
		else:
			result += ch
			i += 1
	return result, miss_sup, miss_sub

def to_italic(s):
	result = ""
	for ch in s:
		if ch in ital:
			result += ital[ch]
		elif ch in bold_digit:
			result += bold_digit[ch]
		else:
			result += ch
	return result

def parse_frac(s):
	if not s.startswith("\\frac"):
		return None, None
	rest = s[5:]
	if not rest.startswith("{"):
		return None, None
	i = find_matching_brace(rest, 0)
	if i == -1:
		return "UNCLOSED", None
	num = rest[1:i]
	rest = rest[i+1:]
	if not rest.startswith("{"):
		return None, None
	i = find_matching_brace(rest, 0)
	if i == -1:
		return "UNCLOSED", None
	den = rest[1:i]
	return num, den

def parse_sqrt(s):
	if not s.startswith("\\sqrt"):
		return None
	rest = s[5:]
	if not rest.startswith("{"):
		return None
	i = find_matching_brace(rest, 0)
	if i == -1:
		return "UNCLOSED"
	return rest[1:i]

def parse_overline(s):
	if not s.startswith("\\overline"):
		return None
	rest = s[9:]
	if not rest.startswith("{"):
		return None
	i = find_matching_brace(rest, 0)
	if i == -1:
		return "UNCLOSED"
	return rest[1:i]

def parse_underline(s):
	if not s.startswith("\\underline"):
		return None
	rest = s[10:]
	if not rest.startswith("{"):
		return None
	i = find_matching_brace(rest, 0)
	if i == -1:
		return "UNCLOSED"
	return rest[1:i]

def parse_binom(s):
	if not s.startswith("\\binom"):
		return None, None
	rest = s[6:]
	if not rest.startswith("{"):
		return None, None
	i = find_matching_brace(rest, 0)
	if i == -1:
		return "UNCLOSED", None
	num = rest[1:i]
	rest = rest[i+1:]
	if not rest.startswith("{"):
		return None, None
	i = find_matching_brace(rest, 0)
	if i == -1:
		return "UNCLOSED", None
	den = rest[1:i]
	return num, den

def make_ht(miss_sup, miss_sub):
	parts = []
	if miss_sub:
		parts.append("\033[33;1mNO-SUBSCRIPT;\033[0m\033[36m " + " ".join(f"<{c}>" for c in miss_sub))
	if miss_sup:
		parts.append("\033[33;1mNO-SUPERSCRIPT;\033[0m\033[36m " + " ".join(f"<{c}>" for c in miss_sup))
	return "\033[36mHT: \033[0m" + ", ".join(parts) + "\033[0m"

def render_block(s, lnum):
	if s.startswith("\\frac"):
		num, den = parse_frac(s)
		if num == "UNCLOSED" or den == "UNCLOSED":
			return ["\033[36mHT: \033[33;1mUNCLOSED PARENTHESIS;\033[0m"], []
		if num is None or den is None:
			return ["\033[35mER: \033[33;1mNO-SYMBOL;\033[0m"], []
		nb, w1 = render_block(num, lnum)
		db, w2 = render_block(den, lnum)
		return render_frac_block(nb, db), w1 + w2
	elif s.startswith("\\sqrt"):
		arg = parse_sqrt(s)
		if arg == "UNCLOSED":
			return ["\033[36mHT: \033[33;1mUNCLOSED PARENTHESIS;\033[0m"], []
		if arg is None:
			return ["\033[35mER: \033[33;1mNO-SYMBOL;\033[0m"], []
		ab, w = render_block(arg, lnum)
		return render_sqrt_block(ab), w
	elif s.startswith("\\overline"):
		arg = parse_overline(s)
		if arg == "UNCLOSED":
			return ["\033[36mHT: \033[33;1mUNCLOSED PARENTHESIS;\033[0m"], []
		if arg is None:
			return ["\033[35mER: \033[33;1mNO-SYMBOL;\033[0m"], []
		ab, w = render_block(arg, lnum)
		return render_overline_block(ab), w
	elif s.startswith("\\underline"):
		arg = parse_underline(s)
		if arg == "UNCLOSED":
			return ["\033[36mHT: \033[33;1mUNCLOSED PARENTHESIS;\033[0m"], []
		if arg is None:
			return ["\033[35mER: \033[33;1mNO-SYMBOL;\033[0m"], []
		ab, w = render_block(arg, lnum)
		return render_underline_block(ab), w
	elif s.startswith("\\binom"):
		num, den = parse_binom(s)
		if num == "UNCLOSED" or den == "UNCLOSED":
			return ["\033[36mHT: \033[33;1mUNCLOSED PARENTHESIS;\033[0m"], []
		if num is None or den is None:
			return ["\033[35mER: \033[33;1mNO-SYMBOL;\033[0m"], []
		nb, w1 = render_block(num, lnum)
		db, w2 = render_block(den, lnum)
		return render_binom_block(nb, db), w1 + w2
	else:
		s_parsed, miss_sup, miss_sub = parse_scripts(s)
		line = to_italic(s_parsed)
		warns = []
		if miss_sup or miss_sub:
			warns.append(make_ht(miss_sup, miss_sub))
		return [line], warns

def render_frac_block(num_block, den_block):
	num_w = max(visible_len(row) for row in num_block) if num_block else 0
	den_w = max(visible_len(row) for row in den_block) if den_block else 0
	width = max(num_w, den_w)
	num_rows = [center_row(row, width) for row in num_block]
	den_rows = [center_row(row, width) for row in den_block]
	line = "─" * width
	return num_rows + [line] + den_rows

def render_sqrt_block(arg_block):
	width = max(visible_len(row) for row in arg_block) if arg_block else 0
	top = " " + "_" * (width + 1)
	rows = ["√ " + arg_block[0]]
	for row in arg_block[1:]:
		rows.append("  " + row)
	return [top] + rows

def render_overline_block(arg_block):
	width = max(visible_len(row) for row in arg_block) if arg_block else 0
	top = "_" * (width + 1)
	return [top] + list(arg_block)

def render_underline_block(arg_block):
	width = max(visible_len(row) for row in arg_block) if arg_block else 0
	bottom = "‾" * (width + 1)
	return list(arg_block) + [bottom]

def render_binom_block(num_block, den_block):
	num_w = max(visible_len(row) for row in num_block) if num_block else 0
	den_w = max(visible_len(row) for row in den_block) if den_block else 0
	width = max(num_w, den_w)
	num_rows = [center_row(row, width) for row in num_block]
	den_rows = [center_row(row, width) for row in den_block]
	top = "⎛" + num_rows[0] + "⎞"
	middle_num_rows = []
	for row in num_rows[1:]:
		middle_num_rows.append("⎜" + row + "⎟")
	middle_num_rows.append("⎜" + " " * width + "⎟")
	middle_den_rows = []
	for row in den_rows[:-1]:
		middle_den_rows.append("⎜" + row + "⎟")
	bot = "⎝" + den_rows[-1] + "⎠"
	return [top] + middle_num_rows + middle_den_rows + [bot]

def hstack_baseline(items):
	items = [(b, bl) for b, bl in items if b]
	if not items:
		return [""]
	fixed = []
	for block, bl in items:
		if not (0 <= bl < len(block)):
			print(f"\033[35mER: BASELINE {bl} OUT OF RANGE (len={len(block)});\033[0m", file=sys.stderr)
			bl = 0
		fixed.append((block, bl))
	items = fixed
	B = max(bl for _, bl in items)
	H = max(max(0, B - bl) + len(b) for b, bl in items)
	padded = []
	for block, bl in items:
		top = max(0, B - bl)
		bottom = max(0, H - top - len(block))
		rows = [""] * top + list(block) + [""] * bottom
		padded.append(rows)
	widths = []
	for block in padded:
		w = max(visible_len(r) for r in block) if block else 0
		widths.append(w)
	result = []
	for i in range(H):
		line = ""
		for j, block in enumerate(padded):
			line += pad_right(block[i], widths[j])
		result.append(line.rstrip(" "))
	return result

def render(s, lnum):
	s = replace_greek(s)
	s = replace_ops(s)
	s = replace_brace_style(s, "twoline", gl_set_all)
	s = replace_brace_style(s, "set", gl_set_all)
	s = replace_brace_style(s, "mathbb", gl_set_all)
	s = replace_brace_style(s, "bold", gl_bold_all)
	s = replace_brace_style(s, "oblbold", gl_obl_all)
	s = replace_brace_style(s, "mono", gl_mono_all)
	s = replace_brace_style(s, "calgrph", gl_cal_all)
	s = replace_styles(s)

	blocks = split_into_blocks(s)

	if len(blocks) == 0:
		return [""]

	for kind, content in blocks:
		if kind == "error":
			if content == "UNCLOSED":
				return [f"\033[36mHT: \033[33;1mUNCLOSED PARENTHESIS;\033[0m\033[36m <{s}> (\033[34;1mline {lnum} [LAST]\033[0m\033[36m)\033[0m"]
			else:
				return [f"\033[35mER: \033[33;1mNO-SYMBOL;\033[0m\033[35m <{s}> (\033[34;1mline {lnum} [LAST]\033[0m\033[35m)\033[0m"]

	if len(blocks) == 1:
		block, warns = render_block(s, lnum)
		return block + warns

	items = []
	all_warns = []
	for kind, content in blocks:
		if kind == "text":
			b, w = render_block(content, lnum)
			items.append((b, 0))
			all_warns.extend(w)
		elif kind == "frac":
			num, den = parse_frac(content)
			if num is None or num == "UNCLOSED" or den is None:
				return [f"\033[35mER: \033[33;1mNO-SYMBOL;\033[0m\033[35m <{s}> (\033[34;1mline {lnum} [LAST]\033[0m\033[35m)\033[0m"]
			nb, w1 = render_block(num, lnum)
			db, w2 = render_block(den, lnum)
			b = render_frac_block(nb, db)
			items.append((b, len(nb)))
			all_warns.extend(w1)
			all_warns.extend(w2)
		elif kind == "sqrt":
			arg = parse_sqrt(content)
			if arg is None or arg == "UNCLOSED":
				return [f"\033[35mER: \033[33;1mNO-SYMBOL;\033[0m\033[35m <{s}> (\033[34;1mline {lnum} [LAST]\033[0m\033[35m)\033[0m"]
			ab, w = render_block(arg, lnum)
			b = render_sqrt_block(ab)
			items.append((b, len(ab)))
			all_warns.extend(w)
		elif kind == "overline":
			arg = parse_overline(content)
			if arg is None or arg == "UNCLOSED":
				return [f"\033[35mER: \033[33;1mNO-SYMBOL;\033[0m\033[35m <{s}> (\033[34;1mline {lnum} [LAST]\033[0m\033[35m)\033[0m"]
			ab, w = render_block(arg, lnum)
			b = render_overline_block(ab)
			items.append((b, 1))
			all_warns.extend(w)
		elif kind == "underline":
			arg = parse_underline(content)
			if arg is None or arg == "UNCLOSED":
				return [f"\033[35mER: \033[33;1mNO-SYMBOL;\033[0m\033[35m <{s}> (\033[34;1mline {lnum} [LAST]\033[0m\033[35m)\033[0m"]
			ab, w = render_block(arg, lnum)
			b = render_underline_block(ab)
			items.append((b, len(ab) - 1))
			all_warns.extend(w)
		elif kind == "binom":
			num, den = parse_binom(content)
			if num is None or num == "UNCLOSED" or den is None:
				return [f"\033[35mER: \033[33;1mNO-SYMBOL;\033[0m\033[35m <{s}> (\033[34;1mline {lnum} [LAST]\033[0m\033[35m)\033[0m"]
			nb, w1 = render_block(num, lnum)
			db, w2 = render_block(den, lnum)
			b = render_binom_block(nb, db)
			items.append((b, len(nb)))
			all_warns.extend(w1)
			all_warns.extend(w2)
	result = hstack_baseline(items)
	return result + all_warns

nl = 1

while True:
	try:
		line = input(f"{nl} | ")
	except EOFError:
		break
	if not line:
		print("\033[36mHT: CONTAINS \033[33;1m!WHITESPACE;\033[0m\033[36m <ENTER>\033[0m")
		continue
	first = line[0]
	if first == "\t" or first == "	":
		print("\033[36mHT: CONTAINS \033[33;1m!WHITESPACE;\033[0m\033[36m <TAB>\033[0m")
		continue
	if first == " ":
		print("\033[36mHT: CONTAINS \033[33;1m!WHITESPACE;\033[0m\033[36m <SPACE>\033[0m")
		continue
	if first.isspace():
		print("\033[36mHT: CONTAINS \033[33;1m!WHITESPACE;\033[0m\033[36m <AWS>\033[0m")
		continue
	if line in ("quit", "q", "exit"):
		print("Bye.")
		break
	result = render(line, nl)
	print()
	for row in result:
		print(row)
	print()
	nl += 1
