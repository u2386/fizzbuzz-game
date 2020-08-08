#!/usr/bin/env python

import pytest

from game import times, contains, and_, always, rule, any_, all_


@pytest.mark.parametrize(
    "mod, number, expected", [(3, 9, True), (4, 16, True), (3, 10, False)]
)
def test_times(mod, number, expected):
    assert times(mod)(number) is expected


@pytest.mark.parametrize(
    "target, source, exists", [("a", "bath", True), ("3", "12", False)]
)
def test_contains(target, source, exists):
    assert contains(target)(source) is exists


@pytest.mark.parametrize(
    "predicates, expected",
    [
        ((lambda _: True,), True),
        ((lambda _: True, lambda _: True), True),
        ((lambda _: False,), False),
        ((lambda _: True, lambda _: False), False),
        ((lambda _: False, lambda _: False), False),
        ((lambda _: False, lambda _: True), False),
    ],
)
def test_and(predicates, expected):
    assert and_(*predicates)(1) is expected


def test_always():
    assert always()(1)


def test_rule():
    r = rule(lambda _: True, lambda facts: facts.update(status=1))
    facts = {"status": 0}
    r(facts)
    assert facts["status"] == 1

    r = rule(lambda _: False, lambda facts: facts.update(status=1))
    facts = {"status": 0}
    r(facts)
    assert facts["status"] == 0


@pytest.mark.parametrize(
    "pred1, pred2, expected",
    [
        (lambda _: True, lambda _: True, 1),
        (lambda _: False, lambda _: True, 2),
        (lambda _: False, lambda _: False, 0),
    ],
)
def test_any(pred1, pred2, expected):
    r = any_(
        rule(pred1, lambda facts: facts.update(status=1)),
        rule(pred2, lambda facts: facts.update(status=2)),
    )
    facts = {"status": 0}
    r(facts)
    assert facts["status"] == expected


@pytest.mark.parametrize(
    "pred1, pred2, expected",
    [
        (lambda _: True, lambda _: True, 2),
        (lambda _: False, lambda _: True, 2),
        (lambda _: True, lambda _: False, 1),
        (lambda _: False, lambda _: False, 0),
    ],
)
def test_all(pred1, pred2, expected):
    r = all_(
        rule(pred1, lambda facts: facts.update(status=1)),
        rule(pred2, lambda facts: facts.update(status=2)),
    )
    facts = {"status": 0}
    r(facts)
    assert facts["status"] == expected
