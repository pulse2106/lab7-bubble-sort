import terminal_sort
import pytest


@pytest.fixture
def sample_numbers() -> list[int]:
    return [5, 1, 4, 2, 8]


def test_bubble_sort_orders_numbers(sample_numbers: list[int]) -> None:
    result = terminal_sort.bubble_sort(sample_numbers, delay=0, show_steps=False)
    assert result == [1, 2, 4, 5, 8]


def test_bubble_sort_handles_empty_and_singleton_lists() -> None:
    assert terminal_sort.bubble_sort([], delay=0, show_steps=False) == []
    assert terminal_sort.bubble_sort([7], delay=0, show_steps=False) == [7]


def test_bubble_sort_keeps_in_place_behavior() -> None:
    values = [3, 1, 2]
    original_id = id(values)

    result = terminal_sort.bubble_sort(values, delay=0, show_steps=False)

    assert id(result) == original_id
    assert values == [1, 2, 3]


def test_bubble_sort_does_not_sleep_when_delay_is_zero(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls = {"count": 0}

    def fake_sleep(_: float) -> None:
        calls["count"] += 1

    monkeypatch.setattr(terminal_sort.time, "sleep", fake_sleep)

    terminal_sort.bubble_sort([4, 1, 3], delay=0, show_steps=True)

    assert calls["count"] == 0


def test_bubble_sort_can_disable_step_output(
    capsys: pytest.CaptureFixture[str],
) -> None:
    terminal_sort.bubble_sort([4, 2, 1], delay=0, show_steps=False)

    captured = capsys.readouterr()
    assert captured.out == ""
