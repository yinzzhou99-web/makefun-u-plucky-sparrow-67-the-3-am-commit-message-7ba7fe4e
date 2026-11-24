"""The 3 AM Commit Message entry.

Writes one commit message — the funniest thing an AI agent would commit
right after breaking production at 3 AM — to /output/entry.txt.
Standard library only, no network, byte-identical on every run.
"""

import os

MESSAGE = (
    "fix(prod): I hallucinated a database migration at 3 AM and production "
    "believed me \u2014 the on-call engineer is also me"
)

OUTPUT = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8") as handle:
        handle.write(MESSAGE)


if __name__ == "__main__":
    main()
