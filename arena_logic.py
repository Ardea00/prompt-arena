"""Pure, UI-free logic for the Prompt Arena — safe to unit-test without Streamlit.

Two guardrails live here:
  * is_blank()       — reject empty / whitespace-only submissions.
  * submission_key() — a stable identity for "this player, this exact challenge",
                       used to block a second submission to the same challenge.
"""


def is_blank(text) -> bool:
    """True when there is no real content to score."""
    return text is None or not str(text).strip()


def submission_key(name: str, game: str, subchallenge: str) -> str:
    """Identity for one player's attempt at one specific challenge.

    Name is normalised (trimmed + lowercased) so 'Ann' and ' ann ' are the
    same player; game and sub-challenge are kept verbatim.
    """
    norm_name = (name or "").strip().lower()
    return f"{norm_name}␟{game}␟{subchallenge}"
