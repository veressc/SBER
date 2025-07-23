import pytest
from src.metrics import score_fn

def test_full_match():
    assert score_fn("Нью Йорк", "Нью Йорк") == 1.0

def test_no_match():
    assert score_fn("Москва", "Лондон") == 0.0

def test_partial_match():
    # один общий токен ("Джонсон") из двух
    f = score_fn("Борис Джонсон ушёл", "Джонсон Борис")
    # precision = 1/2=0.5, recall = 1/3≈0.333, f1≈0.4
    assert pytest.approx(f, rel=1e-3) == 2 * 0.5 * (1/3) / (0.5 + (1/3))

def test_empty_empty():
    assert score_fn("", "") == 1.0

def test_empty_gold():
    assert score_fn("", "Что‑то") == 0.0

def test_empty_pred():
    assert score_fn("Что‑то", "") == 0.0
