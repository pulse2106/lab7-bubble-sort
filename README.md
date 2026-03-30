# Bubble Sort Visualizer (Python)

This project demonstrates Bubble Sort with two views:

- a terminal-based visualization in `terminal_sort.py`
- a Pygame bar-graph visualization in `visual_sort.py`

## Project Structure

- `terminal_sort.py`: Bubble Sort logic with terminal rendering helpers.
- `visual_sort.py`: Pygame window visualizer for Bubble Sort.
- `tests/test_main.py`: Pytest tests for sorting behavior.
- `requirements.txt`: Project dependencies.
- `REPORT.md`: Report file.
- `JOURNAL.md`: Interaction log.

## Requirements

- Python 3.10+
- Dependencies from `requirements.txt`

## Installation

```bash
pip install -r requirements.txt
```

## Run

Terminal version:

```bash
python terminal_sort.py
```

Pygame version:

```bash
python visual_sort.py
```

In the Pygame window, press `Space` to start sorting.

## Test

```bash
pytest -q
```

## Notes

- Bubble Sort time complexity is $O(n^2)$ (average and worst case).
- Bubble Sort space complexity is $O(1)$ (in-place sorting).
- Visualization code in both scripts is adapted from external references noted in source comments.
