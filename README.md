# Bubble Sort Visualizer (Python)

This project demonstrates the Bubble Sort algorithm in Python.

The script prints the list after each comparison step and pauses for 1.5 seconds so you can follow how values move through the array.

## Project Structure

- `main.py`: Bubble Sort implementation and a sample function call.
- `REPORT.md`: Project report template.
- `JOURNAL.md`: Interaction log.

## Requirements

- Python 3.10+ (or any recent Python 3 version)
- No external Python packages are required

## Installation

1. (Optional) Create a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Expected Behavior

- The list is printed repeatedly as the algorithm progresses.
- The final returned list is sorted in ascending order.

## Notes

- Time complexity of Bubble Sort is $O(n^2)$ in average and worst cases.
- Space complexity is $O(1)$ for in-place sorting.
- The current script uses a fixed `time.sleep(1.5)` delay for each inner-loop step.
