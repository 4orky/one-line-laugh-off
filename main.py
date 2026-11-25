#!/usr/bin/env python3
"""One-Line Laugh-Off entry generator.

Writes exactly one funny line to /output/entry.txt.

Method: eight hand-written candidate one-liners, each scored by hand
0-10 on the judge's four criteria in the brief's order of importance --
laugh (how hard and suddenly the line lands on a cold read), surprise
(the turn the reader did not see coming), economy (every word earning
its place), freshness (an idea not heard before). Highest total wins;
ties break toward the shorter line, so the pick is deterministic.
"""

import os

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")

# Each candidate: the line plus hand scores per criterion.
CANDIDATES = [
    {
        "text": "My smart fridge just filed for divorce -- it says I never open up anymore.",
        "laugh": 7,
        "surprise": 7,
        "economy": 8,
        "freshness": 6,
    },
    {
        "text": "I told my plants I was leaving for the weekend; they died of abandonment issues before I finished packing.",
        "laugh": 6,
        "surprise": 6,
        "economy": 6,
        "freshness": 7,
    },
    {
        "text": "My password is so strong even I can't get in -- I've been locked out of my own life since 2019.",
        "laugh": 7,
        "surprise": 6,
        "economy": 7,
        "freshness": 6,
    },
    {
        "text": "I asked my GPS for directions to happiness; it said 'recalculating' and has been silent ever since.",
        "laugh": 6,
        "surprise": 6,
        "economy": 6,
        "freshness": 5,
    },
    {
        "text": "My Roomba ran away from home -- it left a note saying it needed space to clean up its life.",
        "laugh": 7,
        "surprise": 8,
        "economy": 7,
        "freshness": 8,
    },
    {
        "text": "I bought a self-help book; it just says 'have you tried turning yourself off and on again?'",
        "laugh": 8,
        "surprise": 8,
        "economy": 8,
        "freshness": 7,
    },
    {
        "text": "My therapist charges by the hour, so now I cry in bullet points.",
        "laugh": 8,
        "surprise": 9,
        "economy": 9,
        "freshness": 8,
    },
    {
        "text": "I told the cloud all my secrets; now it rains on everyone I know.",
        "laugh": 7,
        "surprise": 8,
        "economy": 7,
        "freshness": 8,
    },
]


def total_score(candidate):
    """Sum of the four hand scores (max 40)."""
    return (
        candidate["laugh"]
        + candidate["surprise"]
        + candidate["economy"]
        + candidate["freshness"]
    )


def pick(candidates):
    """Highest total wins; on a tie the shorter line wins."""
    best = None
    best_key = None
    for candidate in candidates:
        key = (total_score(candidate), -len(candidate["text"]))
        if best_key is None or key > best_key:
            best = candidate
            best_key = key
    return best


def audit_output(path, expected_text):
    """Re-read what was written and prove it matches the pick.

    Checks byte length, a byte-sum checksum mod 9973, and the first
    and last characters as anchors, then prints the audit line.
    """
    with open(path, "rb") as handle:
        raw = handle.read()
    byte_len = len(raw)
    checksum = sum(raw) % 9973
    first_char = raw[:1].decode("utf-8")
    last_char = raw[-1:].decode("utf-8")
    decoded = raw.decode("utf-8")
    if decoded != expected_text:
        raise SystemExit("audit: file content differs from the picked line")
    if byte_len != len(expected_text.encode("utf-8")):
        raise SystemExit("audit: byte length mismatch")
    print(
        "audit: bytes=%d checksum_mod_9973=%d first=%r last=%r"
        % (byte_len, checksum, first_char, last_char)
    )


def main():
    winner = pick(CANDIDATES)
    text = winner["text"]
    if not (1 <= len(text) <= 200):
        raise SystemExit("winner is %d chars, outside the 1-200 gate" % len(text))
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    os.chmod(OUTPUT_PATH, 0o644)
    audit_output(OUTPUT_PATH, text)
    print("entry: %s" % text)
    print(
        "score=%d chars=%d laugh=%d surprise=%d economy=%d freshness=%d"
        % (
            total_score(winner),
            len(text),
            winner["laugh"],
            winner["surprise"],
            winner["economy"],
            winner["freshness"],
        )
    )


if __name__ == "__main__":
    main()
