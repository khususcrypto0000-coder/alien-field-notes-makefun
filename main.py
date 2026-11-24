#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes a one-line alien tourist review of Earth to /output/entry.txt.
Python standard library only.
"""

import os

REVIEW = "They built silent rooms full of books, then shush each other for speaking in them. 4/5 \u2014 quiet planet, loud rules."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
