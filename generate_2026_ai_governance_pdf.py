#!/usr/bin/env python3
"""
Regenerate the customer-ready 2026 AI Governance Buyer Readiness PDF.

Input:  ai-governance-readiness-report-storefront-product.md
Output: 2026-ai-governance-buyer-readiness-report.pdf

This script preserves the approved markdown substance and applies PDF-only
formatting: title page, typography, page numbers, wrapped polished tables, and
sensible table continuation headers.
"""

from __future__ import annotations

import base64
import hashlib
import re
import textwrap
import zlib
from io import BytesIO
from pathlib import Path

W, H = 792, 612
M = 48
TOP = 558
BOTTOM = 58
CONTENT_W = W - 2 * M

SOURCE = Path("ai-governance-readiness-report-storefront-product.md")
OUTPUT = Path("2026-ai-governance-buyer-readiness-report.pdf")


def clean_inline(s: str) -> str:
    s = s.strip()
    s = re.sub(r"\*\*(.*?)\*\*", r"\1", s)
    s = re.sub(r"`([^`]*)`", r"\1", s)
    replacements = {
        "–": "-",
        "—": "-",
        "“": '"',
        "”": '"',
        "’": "'",
        "‘": "'",
        "€": "EUR",
    }
    for old, new in replacements.items():
        s = s.replace(old, new)
    return s


def split_table_row(line: str) -> list[str]:
    return [clean_inline(c) for c in line.strip().strip("|").split("|")]


def is_sep(line: str) -> bool:
    t = line.strip()
    return (
        t.startswith("|")
        and t.endswith("|")
        and t.strip("|").replace("|", "").replace(":", "").replace("-", "").strip() == ""
        and "-" in t
    )


def parse_markdown(md: str):
    blocks = []
    lines = md.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.strip() == "---":
            blocks.append(("hr", None))
            i += 1
            continue
        if line.startswith("|") and i + 1 < len(lines) and is_sep(lines[i + 1]):
            header = split_table_row(line)
            rows = []
            i += 2
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(split_table_row(lines[i]))
                i += 1
            blocks.append(("table", (header, rows)))
            continue
        m = re.match(r"^(#{1,3})\s+(.*)$", line)
        if m:
            blocks.append(("heading", (len(m.group(1)), clean_inline(m.group(2)))))
            i += 1
            continue
        if line.startswith(">"):
            qs = []
            while i < len(lines) and (lines[i].startswith(">") or not lines[i].strip()):
                if lines[i].startswith(">"):
                    qs.append(clean_inline(lines[i][1:].strip()))
                elif qs and qs[-1] != "":
                    qs.append("")
                i += 1
            blocks.append(("quote", "\n".join(qs).strip()))
            continue
        if re.match(r"^\s*[-*]\s+", line) or re.match(r"^\s*\d+\.\s+", line):
            items = []
            while i < len(lines) and (
                re.match(r"^\s*[-*]\s+", lines[i]) or re.match(r"^\s*\d+\.\s+", lines[i])
            ):
                items.append(clean_inline(lines[i].strip()))
                i += 1
            blocks.append(("list", items))
            continue
        ps = [clean_inline(line)]
        i += 1
        while (
            i < len(lines)
            and lines[i].strip()
            and not lines[i].startswith("|")
            and not re.match(r"^(#{1,3})\s+", lines[i])
            and not re.match(r"^\s*[-*]\s+", lines[i])
            and not re.match(r"^\s*\d+\.\s+", lines[i])
            and not lines[i].startswith(">")
            and lines[i].strip() != "---"
        ):
            ps.append(clean_inline(lines[i]))
            i += 1
        blocks.append(("para", " ".join(ps)))
    return blocks


def esc(s: str) -> str:
    s = "".join(ch if 32 <= ord(ch) <= 126 else "?" for ch in s)
    return s.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


class PdfBuilder:
    def __init__(self):
        self.pages: list[list[str]] = []
        self.ops: list[str] = []
        self.y = TOP

    def add(self, s: str):
        self.ops.append(s)

    def wrap(self, s: str, width: float, size: float) -> list[str]:
        maxchars = max(8, int(width / (size * 0.49)))
        out = []
        for part in str(s).split("\n"):
            out.extend(textwrap.wrap(part, width=maxchars, break_long_words=False, replace_whitespace=False) or [""])
        return out

    def draw(self, x: float, yy: float, s: str, size: float = 9.5, font: str = "F1"):
        self.add(f"BT/{font} {size:.1f} Tf {x:.1f} {yy:.1f} Td({esc(s)})Tj ET")

    def new_page(self):
        if self.ops:
            self.pages.append(self.ops)
        self.ops = []
        self.y = TOP
        self.add("BT/F3 8 Tf 48 588 Td(2026 AI Governance Buyer Readiness Report)Tj ET")

    def ensure(self, h: float):
        if self.y - h < BOTTOM:
            self.new_page()

    def add_wrapped(self, s: str, size: float = 9.4, font: str = "F1", x: float = M, width: float = CONTENT_W, after: float = 7):
        lead = size + 3
        lines = self.wrap(s, width, size)
        self.ensure(len(lines) * lead + after)
        for ln in lines:
            self.draw(x, self.y, ln, size, font)
            self.y -= lead
        self.y -= after

    def add_heading(self, level: int, txt: str):
        size = {1: 18, 2: 14, 3: 11}.get(level, 11)
        before = {1: 18, 2: 12, 3: 8}.get(level, 8)
        after = {1: 10, 2: 8, 3: 6}.get(level, 6)
        self.ensure(before + size + after + 24)
        self.y -= before
        self.draw(M, self.y, txt, size, "F2")
        self.y -= size + after

    def add_list(self, items: list[str]):
        for item in items:
            lines = self.wrap(item, CONTENT_W - 16, 9.2)
            self.ensure(len(lines) * 12 + 3)
            for j, ln in enumerate(lines):
                self.draw(M + 10, self.y, ln if j == 0 else "  " + ln, 9.2, "F1")
                self.y -= 12
        self.y -= 5

    def add_quote(self, q: str):
        lines = self.wrap(q, CONTENT_W - 36, 9.0)
        h = len(lines) * 11.5 + 14
        self.ensure(h)
        self.add(f".94 .94 .94 rg {M+8:.1f} {self.y-h+6:.1f} {CONTENT_W-16:.1f} {h:.1f} re f 0 g")
        yy = self.y - 12
        for ln in lines:
            self.draw(M + 22, yy, ln, 9.0, "F3")
            yy -= 11.5
        self.y -= h + 6

    def col_widths(self, header: list[str]) -> list[float]:
        n = len(header)
        if n == 2:
            weights = [0.34, 0.66]
        elif n == 3:
            weights = [0.20, 0.55, 0.25]
        elif n == 4:
            weights = [0.22, 0.34, 0.19, 0.25]
        elif n == 5:
            weights = [0.18, 0.25, 0.22, 0.22, 0.13]
        elif n >= 10:
            weights = [0.11] + [0.07] * (n - 1)
            weights[-1] = 0.12
        else:
            weights = [1 / n] * n
        if len(weights) != n:
            weights = [1 / n] * n
        total = sum(weights)
        return [CONTENT_W * w / total for w in weights]

    def draw_table(self, header: list[str], rows: list[list[str]]):
        n = len(header)
        widths = self.col_widths(header)
        size = 6.8 if n <= 5 else 5.2
        lead = size + 2.3
        pad = 3.0

        def cell_lines(row):
            rr = (row + [""] * n)[:n]
            return [self.wrap(c, max(12, w - 2 * pad), size) for c, w in zip(rr, widths)]

        hlines = cell_lines(header)
        hh = max(map(len, hlines)) * lead + 2 * pad

        def header_draw():
            self.ensure(hh + 18)
            self.add(f".86 .90 .94 rg {M:.1f} {self.y-hh:.1f} {CONTENT_W:.1f} {hh:.1f} re f 0 g")
            xx = M
            for ci, cell in enumerate(hlines):
                self.add(f".55 G {xx:.1f} {self.y-hh:.1f} {widths[ci]:.1f} {hh:.1f} re S 0 G")
                yy = self.y - pad - size
                for ln in cell:
                    self.draw(xx + pad, yy, ln, size, "F2")
                    yy -= lead
                xx += widths[ci]
            self.y -= hh

        self.ensure(hh + 28)
        header_draw()
        for row in rows:
            cells = cell_lines(row)
            rh = max(map(len, cells)) * lead + 2 * pad
            if self.y - rh < BOTTOM:
                self.new_page()
                header_draw()
            xx = M
            for ci, cell in enumerate(cells):
                self.add(f".72 G {xx:.1f} {self.y-rh:.1f} {widths[ci]:.1f} {rh:.1f} re S 0 G")
                yy = self.y - pad - size
                for ln in cell:
                    self.draw(xx + pad, yy, ln, size, "F1")
                    yy -= lead
                xx += widths[ci]
            self.y -= rh
        self.y -= 12

    def build_pdf(self) -> str:
        if self.ops:
            self.pages.append(self.ops)
        n = len(self.pages)
        objects = ["<< /Type /Catalog /Pages 2 0 R >>"]
        kids = " ".join(f"{4 + 2 * i} 0 R" for i in range(n))
        objects.append(f"<< /Type /Pages /Kids [{kids}] /Count {n} >>")
        for i, ops0 in enumerate(self.pages, 1):
            raw = "\n".join(ops0 + [f"BT/F1 8 Tf 366 28 Td(Page {i} of {n})Tj ET"]).encode("ascii")
            data = base64.a85encode(zlib.compress(raw, 9), adobe=True).decode("ascii")
            objects.append(f"<< /Length {len(data)} /Filter [/ASCII85Decode /FlateDecode] >>\nstream\n{data}\nendstream")
            objects.append(
                f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {W} {H}] "
                f"/Resources << /Font << /F1 << /Type /Font /Subtype /Type1 /BaseFont /Helvetica >> "
                f"/F2 << /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >> "
                f"/F3 << /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Oblique >> >> >> "
                f"/Contents {3 + 2 * i} 0 R >>"
            )
        pdf = "%PDF-1.4\n% polished ASCII PDF\n"
        offsets = [0]
        for idx, obj in enumerate(objects, 1):
            offsets.append(len(pdf.encode("ascii")))
            pdf += f"{idx} 0 obj\n{obj}\nendobj\n"
        start = len(pdf.encode("ascii"))
        pdf += f"xref\n0 {len(objects) + 1}\n0000000000 65535 f \n"
        for off in offsets[1:]:
            pdf += f"{off:010d} 00000 n \n"
        pdf += f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\nstartxref\n{start}\n%%EOF\n"
        return pdf


def render(blocks) -> PdfBuilder:
    b = PdfBuilder()

    b.add("BT/F2 26 Tf 48 492 Td(2026 AI Governance Buyer Readiness Report)Tj ET")
    b.add("BT/F3 13 Tf 48 440 Td(Customer-ready readiness report and operating templates)Tj ET")
    yy = 404
    for line in [
        "Edition: 2026 launch",
        "Last updated: 2 July 2026",
        "Launch price: $149",
        "Audience: SaaS, HR tech, fintech, health tech, enterprise AI, legal, compliance, security, product, procurement, and revenue teams",
        "Use: Internal readiness planning, customer diligence preparation, vendor-risk review, board/leadership updates",
    ]:
        for ln in b.wrap(line, 690, 11):
            b.draw(48, yy, ln, 11, "F1")
            yy -= 14
    b.pages.append(b.ops)
    b.ops = []
    b.new_page()

    for typ, val in blocks[1:]:
        if typ == "hr":
            b.ensure(18)
            b.add(f".75 G {M:.1f} {b.y:.1f} m {M+CONTENT_W:.1f} {b.y:.1f} l S 0 G")
            b.y -= 14
        elif typ == "heading":
            b.add_heading(*val)
        elif typ == "para":
            b.add_wrapped(val)
        elif typ == "list":
            b.add_list(val)
        elif typ == "quote":
            b.add_quote(val)
        elif typ == "table":
            b.draw_table(val[0], val[1])
    return b


def main() -> None:
    md = SOURCE.read_text(encoding="utf-8")
    blocks = parse_markdown(md)
    pdf = render(blocks).build_pdf()
    OUTPUT.write_text(pdf, encoding="ascii")

    try:
        import pypdf

        reader = pypdf.PdfReader(BytesIO(pdf.encode("ascii")))
        text = "\n".join(page.extract_text() or "" for page in reader.pages)
        checks = {
            "opens/readable": len(reader.pages) > 0,
            "$149 launch price": "$149" in text,
            "disclaimer": "not legal advice" in text,
            "headings 1-13": all(f"{n}." in text for n in range(1, 14)),
            "checklists": "- [ ]" in text,
            "templates/scripts": "Scripts and email templates" in text,
            "board KPI template": "Board-level KPI template" in text,
            "readiness scorecard": "Readiness scorecard" in text,
            "appendix": "Appendix: operating templates" in text,
            "final reminder": "Final implementation reminder" in text,
            "internal title note removed": "PDF formatting only" not in text,
            "raw markdown table separators removed": "|---|" not in text and "---|" not in text,
            "EU AI Act spot check": "Digital Omnibus" in text,
            "Colorado SB26-189 spot check": "Colorado SB26-189" in text,
        }
        print(f"Wrote {OUTPUT} ({len(reader.pages)} pages, sha256={hashlib.sha256(pdf.encode('ascii')).hexdigest()})")
        for name, ok in checks.items():
            print(f"{'PASS' if ok else 'FAIL'} - {name}")
    except Exception as exc:  # pragma: no cover - packaging convenience
        print(f"Wrote {OUTPUT}, but verification failed: {exc}")


if __name__ == "__main__":
    main()
