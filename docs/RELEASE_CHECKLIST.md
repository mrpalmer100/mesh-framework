# CUTTING A RELEASE -- the checklist (adopted 2026-08-27)

Adopted after two consecutive releases shipped front-door drift
(a URL-encoded badge that dodged a text replace; version strings
at v3.27.6 while the tree tagged v3.28.0). The lesson both times:
hand edits to generated or duplicated facts. The checklist is
short because the tooling does the work; the ORDER is the point.

1. BUMP pyproject.toml version. This is the single source of
   truth; nothing else is hand-edited for version.
2. CHANGELOG entry for the new version (its date feeds the
   generated banner).
3. RUN python tools/sync_doc_facts.py -- regenerates README
   version/banner/counts and runs the FRONT-DOOR TRIPWIRE.
   The run must end "ok front-door version tripwire". Any
   FRONTDOOR-STALE line is fixed (or, for genuine history
   citations, waived with <!-- version-ok -->) before
   proceeding.
4. docs/history/RELEASE_NOTES_vX.Y.Z.md written (house format:
   the five numbers of NORTH_STAR section 2b at the top, with the
   delta (zero is written as zero) and any SM_EMERGENCE row that
   moved; then headline, claims count, the one-paragraph version, also-in-
   release). The README featured paragraph is updated to the new
   release BY HAND (it is editorial, not generated) -- the
   tripwire will catch it if forgotten, because a stale version
   string without a history link trips.
5. VERIFY: tools/verify_corpus.py cold result recorded in
   docs/VERIFY_STATUS.md; README badge numerator = passing,
   denominator = code-backed (the tripwire checks the
   denominator and passing <= backed).
6. ZENODO_RELEASE_NOTE.md (release notes live ONLY in
   docs/history/RELEASE_NOTES_vX.Y.Z.md -- no root copy; the root
   duplicates were removed 2026-09-09)
   updated (the GitHub release body).
7. Evidence hygiene: every campaign's /tmp checkpoints exported
   to analysis/ (standing rule); the release zip cut ONLY after
   steps 1-6 all pass.

A release where step 3 was not run, or did not end clean, is not
a release.
