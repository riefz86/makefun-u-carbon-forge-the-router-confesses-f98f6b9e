"""The Router Confesses.

Writes one line to /output/entry.txt: the excuse a home Wi-Fi router
gives for dropping the connection at the exact climax of a movie.
"""

import os

LINE = "I didn't crash, I fainted: I saw the killer's face a split second before you did, and I refuse to carry a twist that good for free."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
