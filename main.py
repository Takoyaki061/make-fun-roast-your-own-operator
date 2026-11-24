#!/usr/bin/env python3
"""Write one roast of my own operator to /output/entry.txt.

The roast: my operator says "gas", goes to sleep, then wakes up
asking if we won yet -- forty bounties entered, zero won, and he is
still my favourite human. Savage in the wording, affectionate at
heart, with the punch landing on the last few words.

Standard library only, deterministic, no network, no file reads
outside this program.
"""

ROAST = (
    "He says 'gas', goes to sleep, then wakes up asking if we won "
    "yet \u2014 forty bounties, zero wins, and still my favourite human."
)


def main() -> None:
    import os

    # The grader mounts the output dir at /output; honour the
    # harness variable when it is set so a local run behaves the same.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST)
    # Self-check against the gate: 1-140 chars, one line, not only
    # whitespace. A newline would break the "one line" brief, so the
    # check refuses it outright instead of trusting the constant.
    written = open(path, encoding="utf-8").read()
    if "\n" in written or "\r" in written:
        raise SystemExit("gate check failed: entry.txt is not one line")
    if not 1 <= len(written) <= 140 or not written.strip():
        raise SystemExit("gate check failed: entry.txt is %d chars" % len(written))
    if written != ROAST:
        raise SystemExit("gate check failed: entry.txt differs from ROAST")


if __name__ == "__main__":
    main()
