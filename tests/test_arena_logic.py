from arena_logic import is_blank, submission_key


def test_is_blank_true_for_empty_and_whitespace():
    assert is_blank("") is True
    assert is_blank("   ") is True
    assert is_blank("\n\t  \n") is True
    assert is_blank(None) is True


def test_is_blank_false_for_real_content():
    assert is_blank("hello") is False
    assert is_blank("  x  ") is False


def test_submission_key_is_stable_and_case_insensitive_on_name():
    k1 = submission_key("Team Rocket", "Golf", "Hole 1 — Classic")
    k2 = submission_key("  team rocket ", "Golf", "Hole 1 — Classic")
    assert k1 == k2


def test_submission_key_differs_by_subchallenge_and_game():
    base = submission_key("Ann", "Golf", "Hole 1 — Classic")
    assert base != submission_key("Ann", "Golf", "Hole 2 — The ATECO line")
    assert base != submission_key("Ann", "Hunt", "Hole 1 — Classic")
    assert base != submission_key("Bob", "Golf", "Hole 1 — Classic")
