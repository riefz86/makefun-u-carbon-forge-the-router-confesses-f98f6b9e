# NOTES — The Router Confesses

Bounty: `u-carbon-forge-the-router-confesses-f98f6b9e` — "The Router Confesses"
($2, 8 places pay, 1st $0.64). Deadline 21:55 WIB 26 Nov 2026.
Gate: `/output/entry.txt` must be UTF-8 text, 1–200 characters, one line.
Judge: AI judge reads entries in pairs, keeps the funnier one; it rewards
the router's own voice (petty, dramatic, smug secret) and a fresh twist, and
penalises the obvious buffering / bandwidth / firmware-update jokes.

## Final entry (131 characters)

> I didn't crash, I fainted: I saw the killer's face a split second before you did, and I refuse to carry a twist that good for free.

Verified locally: `python3 main.py` writes exactly this line to
`/output/entry.txt` (131 chars, single line, mode 0644).

## Revision history

- v1 (132 chars): "I didn't crash — I fainted. Even I couldn't handle who the
  killer was, and I refuse to stream a twist that good as background noise."
  Ran and verified. The joke worked, but "couldn't handle" made the router
  sound weak and "background noise" was a soft landing.
- v2 (final, 131 chars): rewrote the second half — the router now saw the
  killer's face a split second before the viewer and refuses to carry the
  twist for free. The router gains a smug little secret (it knows the ending)
  and a petty motive (unpaid labour), which matches the judge's voice
  criterion better than v1's fainting-from-shock angle. Re-ran and verified.

## Alternatives considered and discarded

- "Sorry, the buffering wheel was my dramatic pause — I wanted the climax to
  breathe." — Rejected: a buffering joke, explicitly listed in the rules as
  the obvious angle everyone has heard.
- "My firmware update chose tonight because even my code wanted to see the
  ending first." — Rejected: a firmware-update joke, also on the rules'
  banned-obvious list.
- "I dropped you on purpose — the hero was about to confess, and I have
  never once been invited to movie night." — Rejected: decent petty voice,
  but the grudge (not being invited) is generic and the twist lands softer
  than the router knowing the killer's identity.
- "I saw the killer's face first, and some spoilers are too good to share
  with the whole house." — Rejected: close to the final line, but it reads as
  a spoiler excuse rather than a confession, and "I didn't crash, I fainted"
  gives the final version a cleaner, funnier opening beat.
