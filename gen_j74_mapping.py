#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#######################################################################
# ███████████████████████████████████████████████████████████████████ #
# █▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█ #
# █▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓█ #
# █▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓█ #
# █▓░  𝄆𝄡𝄚𝆔𝄚𝄚𝄚𝄚𝅧𝅨𝅩𝅦𝅪𝄚𝄚𝄚𝆖𝄚𝄸𝄚𝄚𝄵𝄚𝄷𝄚𝆱𝄚𝄀𝇜𝄚𝄚𝄴𝄚𝅁𝄚𝄚𝄚𝄀𝄋𝄚𝄚𝄌𝄍𝄎𝄀𝄏𝄬𝄀𝄭𝄮𝄚𝄚𝄀𝄀𝄇     ░▓█ #
# █▓░     𝅫  𝇕𝇖𝇚𝄖𝄗𝄘𝄙𝄚𝄛𝄳𝄀 𝄹 𝄯𝅜 𝅝 𝆖 𝆙𝄚𝄚 𝇛𝄚𝄚𝄚𝄚𝇗𝇘𝄚𝄚𝄮𝄊𝄚𝄚𝄚𝄚𝄚𝄚𝄚𝄚𝄃  ░▓█ #
# █▓░  𝄆𝄠𝄲𝄚𝅘𝅥𝅮𝄚𝅘𝅥𝅰𝅘𝅥𝅯𝅘𝅥𝅰𝄚𝄀𝅘𝅥𝅱𝅘𝅥𝅲𝆔𝆕𝆗𝄀𝆘𝆙𝅥𝅬𝄰𝇝𝇞𝇟𝆰𝆲𝆐𝆑𝆒𝆓𝄜𝄝𝅀𝄚𝄚𝄚𝄚𝄚𝄚𝄚𝄚𝄚𝄚𝄚𝄚𝄚𝄚𝄚𝄚𝄚𝄚𝄚𝄚𝄁𝄁𝄂  ░▓█ #
# █▓░  𝄆𝄣𝄚𝄚𝄚𝅂𝄚𝄚𝄶𝄚𝄱𝄚𝄀𝄮𝅗𝅥𝄚𝄚𝄚𝄬𝄯𝆕𝄚𝄫 𝄭𝄀 𝄫𝄚𝄀𝄐𝄑𝄈𝄉𝄌𝄍𝄎 𝄀𝄏 𝄬𝄀𝄭𝄚𝄚𝄚𝄚𝄐𝄑𝄈𝄉𝄀𝄋𝄚𝄚𝄚𝄇  ░▓█ #
# █▓░  |========================================================  ░▓█ #
# █▓░  |///////////////////////////////////////////////////////|  ░▓█ #
# █▓░  |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|  ░▓█ #
# █▓░  |//////// \\///////// \\/////// \\/// \\/// \/// \\\\\\\|  ░▓█ #
# █▓░  |/// \\/// \/// \\\\\\\/// \\/// \/// \\/// \/// \\\\\\\|  ░▓█ #
# █▓░  |//////// \\/////// \\\///////// \///////// \/// \\\\\\\|  ░▓█ #
# █▓░  |/// \\\\\\\/// \\\\\\\/// \\/// \/// \\/// \/// \\\\\\\|  ░▓█ #
# █▓░  |/// \\\\\\\/// \\\\\\\/// \\/// \/// \\/// \///////// \|  ░▓█ #
# █▓░  |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|  ░▓█ #
# █▓░  |///2025 Rick Pfahl\<pfahlr@gmail.com>//////////////////|  ░▓█ #
# █▓░  |========================================================  ░▓█ #
# █▓░    MUSIC THEORY AND COMPOSITION TOOLS for LIVE:             ░▓█ #
# █▓░      * `gen_j74_mapping.py`:                                ░▓█ #
# █▓░                                                             ░▓█ #
# █▓░    Generate J74 Progressive mapping files from:             ░▓█ #
# █▓░      • a mini progression DSL (--prog)                      ░▓█ #
# █▓░      • a degree sequence preset (--preset)                  ░▓█ #
# █▓░      • a TRUE Markov chain (--markov-preset or --markov)    ░▓█ #
# █▓░      * print genre notes for creative guidance              ░▓█ #
# █▓░                                                             ░▓█ #
# █▓░    2025 Rick Pfahl <pfahlr@gmail.com>                       ░▓█ #
# █▓░    𝄆𝄠𝄚𝄚𝄀𝄚𝄚𝄚𝄀𝄚𝄚𝄚𝄀𝄚𝄚𝄚𝄀𝄚𝄚𝄚𝄀𝄚𝄚𝄚𝄀𝄚𝄚𝄚𝄀𝄚𝄚𝄚𝄀𝄚𝄚𝄚𝄀𝄚𝄚𝄚𝄚𝄚𝄀𝄚𝄚𝄚𝄚𝄚𝄀𝄚𝄚𝄚𝄇 ░▓█ #
# █▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓█ #
# █▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓█ #
# █▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█ #
# ███████████████████████████████████████████████████████████████████ #
#######################################################################

"""
Generate J74 Progressive mapping files from:
  • a mini progression DSL (--prog)
  • a degree sequence preset (--preset)
  • a TRUE Markov chain (--markov-preset or --markov)

New:
  • --allow-borrowed + --borrowed-to-custom {custom1|custom2}
  • Hyperpop A/B presets (sequence + markov)
  • --genre hyperpop → prints a studio one-pager (BPM, modes, meters, voicings)
  • --doc: sidecar Markdown (realized chords via music21 + genre sheet)

Tabs: 2 spaces
"""

import argparse
import os
from typing import Sequence
import random
import re
import sys
from dataclasses import dataclass
from textwrap import dedent
from typing import Dict, List, Sequence, Tuple, Optional

# ──────────────────────────────────────────────────────────────────────────────
# Optional music21 (only used if --doc or --key/--mode provided)
# ──────────────────────────────────────────────────────────────────────────────
try:
  from music21 import key as m21key
  from music21 import roman as m21roman
except Exception:
  m21key = None
  m21roman = None

# ──────────────────────────────────────────────────────────────────────────────
# Modes (validation only; mapping remains row = scale degree 1..7)
# ──────────────────────────────────────────────────────────────────────────────

IONIAN = ["I", "ii", "iii", "IV", "V", "vi", "vii°"]
DORIAN = ["i", "ii", "III", "IV", "v", "vi°", "VII"]
PHRYGIAN = ["i", "II", "III", "iv", "v°", "VI", "vii"]
LYDIAN = ["I", "II", "iii", "iv°", "V", "vi", "vii"]
MIXOLYDIAN = ["I", "ii", "iii°", "IV", "v", "vi", "VII"]
AEOLIAN = ["i", "ii°", "III", "iv", "v", "VI", "VII"]
LOCRIAN = ["i°", "II", "III", "iv", "V", "VI", "vii"]

MODE_TABLE = {
  "ionian": IONIAN,
  "dorian": DORIAN,
  "phrygian": PHRYGIAN,
  "lydian": LYDIAN,
  "mixolydian": MIXOLYDIAN,
  "aeolian": AEOLIAN,
  "locrian": LOCRIAN,
}

# ──────────────────────────────────────────────────────────────────────────────
# Presets — easy to extend
# ──────────────────────────────────────────────────────────────────────────────

PRESET_DEGREES: Dict[str, List[str]] = {
  # Existing
  "pop": ["I", "V", "vi", "IV"],
  "jazz_iiv1": ["ii", "V", "I"],
  "circle5": ["I", "IV", "vii", "iii", "vi", "ii", "V", "I"],
  "andalusian": ["i", "bVII", "bVI", "V"],
  "modal_mix": ["I", "bVII", "IV"],
  "sec_dom": ["iii", "VI", "ii", "V", "I"],
  # New: Hyperpop
  # A: minor-leaning core (1–7–6 with bright pivots)
  "hyperpop_a": ["i", "VII", "VI", "IV", "V", "i", "VII", "VI"],
  # B: major-leaning core (I–V–vi–IV + bVII color)
  "hyperpop_b": ["I", "V", "vi", "IV", "bVII", "I", "V", "vi"],
}

# Markov preset matrices: dict[state][next] = probability (rows sum ~1.0)
MARKOV_PRESETS: Dict[str, Dict[str, Dict[str, float]]] = {
  # Pop flavor
  "pop_basic": {
    "I":  {"V": 0.6, "vi": 0.2, "IV": 0.2},
    "V":  {"vi": 0.6, "IV": 0.25, "I": 0.15},
    "vi": {"IV": 0.7, "ii": 0.2, "V": 0.1},
    "IV": {"I": 0.6, "V": 0.25, "ii": 0.15},
    "ii": {"V": 0.8, "IV": 0.2},
  },
  # Jazz ii–V–I with turnarounds
  "jazz_turn": {
    "I":  {"vi": 0.35, "ii": 0.35, "IV": 0.3},
    "ii": {"V": 0.85, "bII": 0.15},
    "V":  {"I": 0.7, "vi": 0.2, "II": 0.1},
    "vi": {"ii": 0.6, "IV": 0.25, "V": 0.15},
    "IV": {"ii": 0.5, "V": 0.3, "I": 0.2},
    "bII":{"I": 1.0},
    "II": {"V": 1.0},
  },
  # Andalusian minor vibes
  "andalusian_minor": {
    "i":   {"bVII": 0.7, "iv": 0.3},
    "bVII":{"bVI": 0.8, "V": 0.2},
    "bVI": {"V": 0.8, "i": 0.2},
    "V":   {"i": 0.85, "bVII": 0.15},
    "iv":  {"V": 0.7, "i": 0.3},
  },
  # New: Hyperpop A (minor core i→VII→VI, bright hops to IV/V/II)
  "hyperpop_a": {
    "i":   {"VII": 0.55, "VI": 0.25, "IV": 0.1, "V": 0.1},
    "VII": {"VI": 0.7, "V": 0.15, "II": 0.15},
    "VI":  {"IV": 0.45, "V": 0.35, "i": 0.2},
    "IV":  {"V": 0.6, "i": 0.25, "II": 0.15},
    "V":   {"i": 0.6, "VII": 0.25, "IV": 0.15},
    "II":  {"V": 1.0},
  },
  # New: Hyperpop B (major core I→V→vi→IV with bVII color + II lift)
  "hyperpop_b": {
    "I":   {"V": 0.6, "vi": 0.2, "II": 0.2},
    "V":   {"vi": 0.55, "IV": 0.25, "I": 0.2},
    "vi":  {"IV": 0.6, "bVII": 0.25, "V": 0.15},
    "IV":  {"I": 0.55, "V": 0.25, "II": 0.2},
    "bVII":{"I": 0.7, "V": 0.3},
    "II":  {"V": 1.0},
  }
}

# ──────────────────────────────────────────────────────────────────────────────
# Degree syntax + parser (mini-DSL)
# ──────────────────────────────────────────────────────────────────────────────

ROMAN_RE = re.compile(r"^[b#]*[ivIV]+(?:°)?$")

def _strip_accidentals(deg: str) -> str:
  return re.sub(r"^[b#]+", "", deg)

def _roman_to_row(deg: str) -> int:
  core = _strip_accidentals(deg)
  up = core.upper().rstrip("°")
  mapping = {"I":1, "II":2, "III":3, "IV":4, "V":5, "VI":6, "VII":7}
  if up not in mapping:
    raise ValueError(f"Unrecognized degree: {deg}")
  return mapping[up]

def _is_in_mode(deg: str, mode_name: str) -> bool:
  core = _strip_accidentals(deg)
  mode_set = {_strip_accidentals(x) for x in MODE_TABLE[mode_name]}
  return core in mode_set

TOK = re.compile(r"\s*([(),*-])\s*")

def _tokenize(s: str) -> List[str]:
  out, i, buf = [], 0, ""
  while i < len(s):
    m = TOK.match(s, i)
    if m:
      if buf.strip():
        out.append(buf.strip())
        buf = ""
      out.append(m.group(1))
      i = m.end()
    else:
      buf += s[i]
      i += 1
  if buf.strip():
    out.append(buf.strip())
  return [("," if t == "-" else t) for t in out]

@dataclass
class Parser:
  toks: List[str]
  i: int = 0
  def peek(self): return self.toks[self.i] if self.i < len(self.toks) else None
  def eat(self, val=None):
    t = self.peek()
    if t is None: raise ValueError("Unexpected end of input.")
    if val is not None and t != val: raise ValueError(f"Expected '{val}', got '{t}'.")
    self.i += 1
    return t
  def parse_expr(self) -> List[str]:
    cols = []; cols.extend(self.parse_column())
    while self.peek() == ",": self.eat(","); cols.extend(self.parse_column())
    return cols
  def parse_column(self) -> List[str]:
    items = []; items.extend(self.parse_item())
    while self.peek() not in (None, ",", ")"): items.extend(self.parse_item())
    return items
  def parse_item(self) -> List[str]:
    atom = self.parse_atom_or_group()
    if self.peek() == "*":
      self.eat("*"); n = int(self.eat()); atom = atom * n
    return atom
  def parse_atom_or_group(self) -> List[str]:
    t = self.peek()
    if t == "(":
      self.eat("("); inside = self.parse_expr(); self.eat(")"); return inside
    tok = self.eat()
    if not ROMAN_RE.match(tok): raise ValueError(f"Not a degree token: {tok}")
    return [tok]

def parse_progression(spec: str) -> List[str]:
  return Parser(_tokenize(spec)).parse_expr()

# ──────────────────────────────────────────────────────────────────────────────
# Preset helpers + TRUE Markov chain
# ──────────────────────────────────────────────────────────────────────────────

def make_preset(name: str, length: int) -> List[str]:
  name = (name or "").lower()
  if name not in PRESET_DEGREES:
    raise ValueError(f"Unknown preset '{name}'. Try one of: {', '.join(sorted(PRESET_DEGREES))}.")
  base = PRESET_DEGREES[name]
  out: List[str] = []
  while len(out) < length:
    out.extend(base)
  return out[:length]

def normalize_row(row: Dict[str, float]) -> Dict[str, float]:
  s = float(sum(row.values()))
  if s <= 0: raise ValueError("Markov row has non-positive sum.")
  return {k: v/s for k, v in row.items()}

def markov_generate(trans: Dict[str, Dict[str, float]],
                    length: int,
                    start: Optional[str] = None,
                    seed: Optional[int] = None) -> List[str]:
  if seed is not None: random.seed(seed)
  probs = {state: normalize_row(nexts) for state, nexts in trans.items()}
  states = list(probs.keys())
  if start is None:
    start = states[0]
  seq = [start]
  cur = start
  for _ in range(length - 1):
    nexts = probs.get(cur)
    if not nexts:
      cur = states[0]
      nexts = probs[cur]
    choices = list(nexts.keys())
    weights = list(nexts.values())
    cur = random.choices(choices, weights, k=1)[0]
    seq.append(cur)
  return seq

def parse_markov_inline(spec: str) -> Dict[str, Dict[str, float]]:
  """
  Inline syntax:
    "I:ii=0.3,V=0.7; ii:V=1.0; V:I=0.6,vi=0.4"
  """
  graph: Dict[str, Dict[str, float]] = {}
  for clause in [c.strip() for c in spec.split(";") if c.strip()]:
    if ":" not in clause:
      raise ValueError(f"Bad clause '{clause}'. Use STATE:n1=p1,n2=p2 …")
    state, rhs = clause.split(":", 1)
    state = state.strip()
    if not ROMAN_RE.match(state):
      raise ValueError(f"Bad state '{state}'.")
    nxt: Dict[str, float] = {}
    for pair in [p.strip() for p in rhs.split(",") if p.strip()]:
      if "=" not in pair:
        raise ValueError(f"Bad pair '{pair}'. Use NEXT=PROB")
      nxt_state, prob = pair.split("=", 1)
      nxt_state = nxt_state.strip()
      if not ROMAN_RE.match(nxt_state):
        raise ValueError(f"Bad next state '{nxt_state}'.")
      nxt[nxt_state] = float(prob)
    graph[state] = nxt
  return graph

# ──────────────────────────────────────────────────────────────────────────────
# J74 ID math & emit
# ──────────────────────────────────────────────────────────────────────────────

HEADER = """// ******************************************************
// Lines starting with this sign are comments.
// ******************************************************
"""

SECTION_LABELS = {
  'diatonic': ['Diatonic Triads','Diatonic 7th','Diatonic >>9','Diatonic >>11','Diatonic >>13'],
  'custom1':  ['Custom1 Triads','Custom1 7th','Custom1 >>9','Custom1 >>11','Custom1 >>13'],
  'custom2':  ['Custom2 Triads','Custom2 7th','Custom2 >>9','Custom2 >>11','Custom2 >>13'],
}

def slot_id(quality_idx: int, section: str, col0: int, row1: int) -> int:
  tens = {'diatonic':0, 'custom1':1, 'custom2':2}[section]
  ones = col0 + 1   # 1..5
  hundreds = quality_idx  # 1..5
  return hundreds*100 + tens*10 + ones*10 + row1

def _cycle_to_five(seq: List[str]) -> List[str]:
  if not seq:
    return ["I","V","vi","IV","ii"]
  if len(seq) < 5:
    k = (5 + len(seq) - 1) // len(seq)
    return (seq * k)[:5]
  return seq[:5]

def emit_section(section: str,
                 cols: Sequence[str],
                 start_note: int,
                 row_step: int,
                 lane_offsets: Dict[str, int]) -> List[str]:
  lines = []
  for q in range(1, 6):
    lines.append(f"// {SECTION_LABELS[section][q-1]}")
    lane_base = start_note + int(lane_offsets.get(str(q), 0))
    for col0, deg in enumerate(cols[:5]):  # 5 columns per section
      row = _roman_to_row(deg)
      sid = slot_id(q, section, col0, row)
      midi = lane_base + (row - 1) * row_step
      lines.append(f" {sid} {midi}")
  lines.append("// ******************************************************")
  return lines

def emit_mapping_sectioned(section_to_cols: Dict[str, List[str]],
                           start_note: int,
                           row_step: int,
                           lane_offsets: Dict[str, int],
                           sections: Sequence[str]) -> str:
  out = [HEADER]
  for sec in sections:
    cols = _cycle_to_five(section_to_cols.get(sec, []))
    out.extend(emit_section(sec, cols, start_note, row_step, lane_offsets))
  return "\n".join(out).rstrip() + "\n"

# ──────────────────────────────────────────────────────────────────────────────
# Genre one-pager (Hyperpop) + docs
# ──────────────────────────────────────────────────────────────────────────────

GENRE_SHEETS: Dict[str, Dict[str, str | List[str]]] = {
  "hyperpop": {
    "BPM": "140–200 (common), 80–205 (extended)",
    "Rhythm": ("Chaotic/experimental complexity; tempo shifts; polyrhythms; glitchy, "
               "asymmetrical percussion; occasional odd meters (5/4, 7/8)."),
    "Modes": "Phrygian, Lydian, Mixolydian; also Major/Minor, Dorian; pentatonic colors.",
    "Melody": ("Bright synths & vocal chops; heavy FX (autotune/formant/pitch); "
               "catchy repetitive arps; maximalist layering; counter-melodies."),
    "Harmony": ("Melody-driven; layered/pitched vocals imply harmony; frequent borrowed chords; "
                "7ths/9ths for sheen; minor↔major pivots."),
    "Common Progressions": "i–VII–VI; I–V–vi–IV; ascending i→III→IV; add 7ths/9ths.",
    "Voicings": [
      "Drums: transient-forward, staccato/glitch fills, sidechain pump.",
      "Bass: mono or detuned saw; octave jumps; distortion; slides.",
      "Pads: wide, bright (Lydian), shimmer; slow attack or gate-chop.",
      "Leads/Vox: hard-tuned, layered 3rds/6ths; wide detune; OTT/bitcrush."
    ],
    "Meters": "Mostly 4/4; playful switches; feel-based syncopation.",
    "Degrees (melody focus)": "Lean on 1,2,#4(=II),5, bVII; surprise with bVI/bII.",
    "Extensions": "9ths common; 11ths/13ths for extreme brightness.",
    "Tips": [
      "Use Lydian’s #4 (map as II) for lift.",
      "Borrow bVII/bVI/bII for contrast.",
      "Automate formants/pitch; chop vox for motifs."
    ],
    "Refs": [
      "https://www.youtube.com/watch?v=DByOgFWDjBo",
      "https://youtu.be/h3yMkEkqwVU?si=jEvYxRGTrd6eqP-O"
    ]
  }
}

def realize_chords_md(deg_by_col: Sequence[str], key_name: str, mode_name: str) -> str:
  # (same robust version you just fixed: Key(key, mode) not f"{key} {mode}")
  if m21key is None or m21roman is None:
    return ""
  mode_to_quality = {
    "ionian": "major", "aeolian": "minor",
    "dorian": "dorian", "phrygian": "phrygian",
    "lydian": "lydian", "mixolydian": "mixolydian", "locrian": "locrian",
  }
  quality = mode_to_quality.get(mode_name.lower(), "major")
  try:
    ks = m21key.Key(key_name, quality)
  except Exception:
    ks = m21key.Key(key_name, "minor" if quality == "aeolian" else "major")

  lines = []
  lines.append("| Col | Degree | Roman | Root | Pitches |")
  lines.append("|---:|:------:|:-----:|:----:|:--------|")
  for i, deg in enumerate(deg_by_col[:5], 1):
    try:
      rn = m21roman.RomanNumeral(deg, ks)
      pitches = " ".join(p.nameWithOctave for p in rn.pitches[:4])
      lines.append(f"| {i} | {deg} | {rn.figure} | {rn.root().name} | {pitches} |")
    except Exception:
      lines.append(f"| {i} | {deg} | (n/a) | (n/a) | (n/a) |")
  return "\n".join(lines) + "\n"

def load_curated_markdown(path: str) -> str:
  if not os.path.exists(path):
    raise FileNotFoundError(f"Curated genre source not found: {path}")
  with open(path, "r", encoding="utf-8") as f:
    return f.read()

def build_sidecar_from_curated(curated_md: str,
                               degs_for_chords: Sequence[str],
                               key_name: str | None,
                               mode_name: str | None) -> str:
  """
  The curated markdown is the source of truth.
  If it contains the placeholder {{CHORD_TABLE}}, we replace it
  with a realized chord table (if key+mode provided and music21 available).
  If placeholder is absent, we leave the curated doc untouched.
  """
  if "{{CHORD_TABLE}}" not in curated_md:
    return curated_md if curated_md.endswith("\n") else curated_md + "\n"

  # Only generate a chord table when both key and mode are provided
  chord_table = ""
  if key_name and mode_name:
    chord_table = realize_chords_md(degs_for_chords, key_name, mode_name)
    if not chord_table:
      chord_table = "> (music21 not available; chord table omitted)\n"

  return curated_md.replace("{{CHORD_TABLE}}", chord_table)

def genre_sheet_md(genre: str) -> str:
  g = GENRE_SHEETS.get(genre.lower())
  if not g:
    return ""
  lines = [f"# {genre.title()} — Studio One-Pager", ""]
  lines.append("| Topic | Notes |")
  lines.append("|:------|:------|")
  def add(key: str):
    val = g.get(key)
    if isinstance(val, list):
      val_str = "<br>".join(f"• {x}" for x in val)
    else:
      val_str = str(val)
    lines.append(f"| **{key}** | {val_str} |")
  for k in ["BPM","Meters","Modes","Rhythm","Melody","Harmony",
            "Common Progressions","Degrees (melody focus)","Extensions","Voicings","Tips"]:
    add(k)
  # references
  refs = g.get("Refs", [])
  if refs:
    lines.append("")
    lines.append("**References**")
    for r in refs:
      lines.append(f"- {r}")
  # append source file if exists
  src_path = os.path.join("genres", f"{genre.lower()}-source-information.md")
  if os.path.exists(src_path):
    lines.append("\n---\n")
    lines.append(f"_Source notes from `{src_path}`:_\n")
    try:
      with open(src_path, "r", encoding="utf-8") as f:
        lines.append(f.read().strip())
    except Exception as e:
      lines.append(f"> (Could not read source file: {e})")
  return "\n".join(lines).strip() + "\n"

# ──────────────────────────────────────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
  epilog = dedent("""
  EXAMPLES
    # Same 5-degree cycle across all columns/sections
    gen_j74_mapping.py --prog "ii-V-I-iv-III * 15" -o my_map.txt

    # 5-column block: first=ii-V-I-iv-III; next four=IV-V-VI-ii-I; repeat block ×3
    gen_j74_mapping.py --prog "(ii-V-I-iv-III,(IV-V-VI-ii-I*4))*3" -o layered.txt

    # Preset ii–V–I across 10 columns
    gen_j74_mapping.py --preset jazz_iiv1 --repeat 10 -o iiV1.txt

    # TRUE Markov preset with seed
    gen_j74_mapping.py --markov-preset hyperpop_b --length 15 --seed 42 -o hpb_walk.txt

    # Inline Markov transitions
    gen_j74_mapping.py --markov "I:V=0.5,vi=0.5; V:vi=0.6,IV=0.4; vi:IV=1.0" --length 12 -o mwalk.txt

    # Route borrowed degrees to Custom2, keep Diatonic purely in-mode (Mixolydian)
    gen_j74_mapping.py --preset hyperpop_b --repeat 7 --mode mixolydian \\
      --allow-borrowed --borrowed-to-custom custom2 -o hp_map.txt

    # Document realized chords + Hyperpop one-pager
    gen_j74_mapping.py --preset hyperpop_a --repeat 5 --key C --mode aeolian \\
      --genre hyperpop --doc hyperpop.md -o hp.txt
  """).strip("\n")

  p = argparse.ArgumentParser(
    prog="gen_j74_mapping.py",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=dedent("""
      Compile chord-degree progressions into a J74 Progressive keyboard map.

      Sources (pick one):
        • --prog          Mini DSL with () and * repetition
        • --preset        Degree sequence preset (see --help)
        • --markov-*      TRUE Markov chain (preset or inline transitions)

      Options:
        • --allow-borrowed         Allow degrees outside selected mode
        • --borrowed-to-custom     Route borrowed degrees to right grid (custom1/custom2)
        • --genre hyperpop         Add a studio one-pager to --doc
        • --key/--mode --doc       Write a Markdown sidecar (music21 chords + genre sheet)
    """).strip("\n"),
    epilog=epilog
  )

  src = p.add_mutually_exclusive_group(required=True)
  
  src.add_argument('-pg',   "--prog",
                   help="Progression DSL, e.g. \"(ii-V-I-iv-III,(IV-V-VI-ii-I*4))*3\"")
  src.add_argument('-pt',   "--preset",
                   help=f"One of: {', '.join(sorted(PRESET_DEGREES))}")
  src.add_argument('-mp',   "--markov-preset",
                   help=f"One of: {', '.join(sorted(MARKOV_PRESETS))}")
  src.add_argument('-mv',   "--markov",
                   metavar="TRANS",
                   help="Inline Markov: \"I:V=0.6,vi=0.4; V:I=0.7,vi=0.3; vi:IV=1.0\"")
  p.add_argument('-r',  "--repeat", type=int, default=10,
                 help="Columns to generate for --preset (default 10)")
  p.add_argument('-l',  "--length", type=int, default=10,
                 help="Length for --markov sources (default 10)")
  p.add_argument('-s',  "--seed", type=int,
                 help="Seed for Markov RNG")
  p.add_argument('-ab', "--allow-borrowed", action="store_true",
                 help="Permit degrees outside the mode (leading b/# or not present in the mode).")
  p.add_argument('-bc', "--borrowed-to-custom",
                 choices=["custom1","custom2"],
                 help="Route borrowed degrees to this right-hand grid; Diatonic keeps in-mode only.")
  p.add_argument('-k',  "--key",
                help="If provided with --doc, use this tonic with music21 (e.g., C, Eb, A).")
  p.add_argument('-m',  "--mode", choices=list(MODE_TABLE.keys()),
                help="Validate degrees and realize chords for docs (optional).")
  p.add_argument('-d',  "--doc",
                help="Write sidecar Markdown from a curated source file (see --genre/--genre-src).")
  p.add_argument('-g',  "--genre",
                required=False,
                help="Genre key used to find curated doc (e.g., 'hyperpop'). Required when --doc is set.")
  p.add_argument('-gs', "--genre-src",
                help="Path to curated source markdown. Default: ./genres/<genre>-source-information.md")
  p.add_argument('-sn', "--start-note", type=int, default=0,
                 help="Base MIDI note for lane 1 (default 0 = C#-2).")
  p.add_argument('-rs', "--row-step", type=int, default=16,
                 help="Vertical spacing between rows (default 16).")
  p.add_argument('-ln', "--lane", action="append", default=[],
                 help="Lane offsets per quality. Repeatable, e.g.: --lane 1:0 --lane 2:1 --lane 3:2 --lane 4:3 --lane 5:8")
  p.add_argument('-mr', "--mirror", choices=["all","diatonic","custom1","custom2"], default="all",
                 help="Which grid sections to emit (default: all).")
  p.add_argument("-o",  "--outfile", required=True, help="Output mapping file path.")
  p.add_argument("-p",  "--outpath", default="./output", help="path where to generate file output (default:./output/)")
  return p

# ──────────────────────────────────────────────────────────────────────────────

def _split_borrowing(seq: List[str], mode: Optional[str]) -> Tuple[List[str], List[str]]:
  """Return (in_mode, borrowed) based on mode + accidentals."""
  if not seq:
    return [], []
  if not mode:
    # Without a mode, treat explicit accidentals as 'borrowed'
    in_mode = [d for d in seq if not re.match(r"^[b#]+", d)]
    borrowed = [d for d in seq if re.match(r"^[b#]+", d)]
    return in_mode, borrowed
  in_mode, borrowed = [], []
  for d in seq:
    core_ok = _is_in_mode(d, mode)
    acc = bool(re.match(r"^[b#]+", d))
    if core_ok and not acc:
      in_mode.append(d)
    else:
      borrowed.append(d)
  return in_mode, borrowed

def main(argv: Sequence[str] | None = None) -> int:
  parser = build_parser()
  args = parser.parse_args(argv)

  lane_offsets = {"1":0, "2":1, "3":2, "4":3, "5":8}
  for spec in args.lane:
    try:
      k, v = spec.split(":")
      lane_offsets[k.strip()] = int(v.strip())
    except Exception:
      parser.error(f"Bad --lane spec '{spec}'. Use like: --lane 3:2")

  # Build unbounded degree sequence
  if args.prog:
    deg_seq = parse_progression(args.prog)
  elif args.preset:
    deg_seq = make_preset(args.preset, args.repeat)
  elif args.markov_preset:
    trans = MARKOV_PRESETS[args.markov_preset]
    deg_seq = markov_generate(trans, length=args.length, seed=args.seed)
  else:
    trans = parse_markov_inline(args.markov)
    start_state = next(iter(trans.keys()))
    deg_seq = markov_generate(trans, length=args.length, start=start_state, seed=args.seed)

  # Borrowed routing logic
  sections = ["diatonic","custom1","custom2"] if args.mirror == "all" else [args.mirror]
  section_to_cols: Dict[str, List[str]] = {}
  if args.borrowed_to_custom:
    # Split degrees into in-mode vs borrowed
    in_mode, borrowed = _split_borrowing(deg_seq, args.mode)
    if args.mode and not args.allow_borrowed and borrowed:
      parser.error("Borrowed degrees present but --allow-borrowed not set. "
                   "Pass --allow-borrowed or remove borrowed degrees.")
      return 2
    # Fill Diatonic with in-mode, route borrowed to chosen custom grid
    section_to_cols["diatonic"] = _cycle_to_five(in_mode) if "diatonic" in sections else []
    target = args.borrowed_to_custom
    other = "custom1" if target == "custom2" else "custom2"
    if target in sections:
      section_to_cols[target] = _cycle_to_five(borrowed if borrowed else in_mode)
    if other in sections:
      # mirror in-mode on the remaining grid by default
      section_to_cols[other] = _cycle_to_five(in_mode if in_mode else borrowed)
  else:
    # No routing: use the same sequence everywhere (cycled/truncated later)
    for s in sections:
      section_to_cols[s] = list(deg_seq)

  # Emit mapping text
  try:
    text = emit_mapping_sectioned(
      section_to_cols=section_to_cols,
      start_note=args.start_note,
      row_step=args.row_step,
      lane_offsets=lane_offsets,
      sections=sections
    )
  except ValueError as e:
    parser.error(str(e))
    return 2

  with open(args.outpath + '/' +args.outfile, "w", encoding="utf-8") as f:
    f.write(text)
  print(f"Wrote {args.outfile}")

 if args.doc:
  if not args.genre:
    parser.error("--doc requires --genre (so we know which curated file to load).")
    return 2

  genre_src = args.genre_src or os.path.join("genres", f"{args.genre.lower()}-source-information.md")
  try:
    curated_md = load_curated_markdown(genre_src)
  except FileNotFoundError as e:
    parser.error(str(e) + "  (Create this file; the sidecar is curated-only by design.)")
    return 2

  # Pick 5 visible columns for chord table (if placeholder present)
  # Prefer diatonic section if present
  chosen_cols = None
  for choice in ["diatonic"] + [s for s in sections if s != "diatonic"]:
    cols = section_to_cols.get(choice, [])
    if cols:
      chosen_cols = _cycle_to_five(cols)
      break
  if chosen_cols is None:
    chosen_cols = ["I","V","vi","IV","ii"]  # safe fallback

  doc_text = build_sidecar_from_curated(
    curated_md=curated_md,
    degs_for_chords=chosen_cols,
    key_name=args.key,
    mode_name=args.mode
  )
  with open(args.outpath + '/' + args.doc, "w", encoding="utf-8") as f:
    f.write(doc_text)
  print(f"Wrote {args.doc} (from curated: {genre_src})")

if __name__ == "__main__":
  sys.exit(main())
