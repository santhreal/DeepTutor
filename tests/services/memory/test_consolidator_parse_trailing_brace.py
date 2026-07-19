"""Regression: consolidator parse must tolerate trailing brace prose."""

from __future__ import annotations

from deeptutor.services.memory.consolidator.parse import _parse_ops_response
from deeptutor.services.memory.ops import AddOp


def test_parse_ops_response_tolerates_trailing_brace_prose() -> None:
    raw = (
        '{"ops":[{"op":"add","section":"S","text":"ok","refs":[]}]}'
        " Note: }"
    )
    ops = _parse_ops_response(raw)
    assert len(ops) == 1
    assert isinstance(ops[0], AddOp)
    assert ops[0].text == "ok"
