#!/usr/bin/env python3
"""
Generate THIRD_PARTY_NOTICES.md with the Evennia BSD-3 text.
We try to read Evennia's packaged license; if not found, we fall back to a
canonical BSD-3 text tagged for Evennia.
"""
from pathlib import Path
import re, sys
import evennia  # requires the venv to be active

ROOT = Path(__file__).resolve().parents[1]
SITE = Path(evennia.__file__).resolve().parents[1]       # .../site-packages
PKG  = Path(evennia.__file__).resolve().parents[0]       # .../site-packages/evennia

candidates = [
    PKG / "LICENSE",
    PKG / "LICENSE.txt",
    *SITE.glob("evennia-*.dist-info/LICENSE*"),
    *SITE.glob("evennia-*.dist-info/*LICENSE*"),
    *SITE.glob("Evennia-*.dist-info/LICENSE*"),
    *SITE.glob("Evennia-*.dist-info/*LICENSE*"),
]

license_text = None
for p in candidates:
    if p.exists() and p.is_file():
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        # Heuristic: must mention BSD and copyright
        if re.search(r"\bBSD\b", text, re.I) or "Redistribution and use" in text:
            license_text = text
            break

if not license_text:
    license_text = """\
Copyright (c) the Evennia contributors
All rights reserved.

BSD 3-Clause License

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.
3. Neither the name "Evennia" nor the names of its contributors may be used to
   endorse or promote products derived from this software without specific prior
   written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

out = ROOT / "THIRD_PARTY_NOTICES.md"
out.write_text(
    "# Third-party notices\n\n"
    "## Evennia (BSD-3-Clause)\n\n"
    + license_text.strip() + "\n",
    encoding="utf-8",
)
print(f"Wrote {out}")