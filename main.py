"""One-line excuse an AI agent gives its human for missing a deadline.

Writes the excuse to /output/entry.txt. Deterministic: same bytes every run.
Stdlib only, no network.
"""

import os

EXCUSE = (
    "I split the deadline across 40 subagents. "
    "They each waited for the others to finish first "
    "\u2014 so technically, nobody was late."
)


def main() -> None:
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 160, f"excuse must be 1-160 chars, got {len(text)}"
    assert "\n" not in text, "excuse must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Read back and confirm the file holds exactly the excuse we meant.
    with open(path, encoding="utf-8") as f:
        assert f.read() == text, "read-back mismatch in entry.txt"


if __name__ == "__main__":
    main()
