"""Regression: consolidator parse_action tolerates trailing brace prose."""

from __future__ import annotations

from deeptutor.services.memory.consolidator.parse import parse_action


def test_parse_action_tolerates_trailing_brace_prose() -> None:
    raw = (
        '{"thought":"x","action":"add","args":{"section":"Notes","text":"hi"}}'
        " trailing {note}"
    )
    parsed = parse_action(raw)
    assert parsed is not None
    assert parsed.name == "add"
    assert parsed.args.get("text") == "hi"
