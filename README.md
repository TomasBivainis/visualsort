# Visualsort

Visualsort provides functions with which you can program a sorting algortithm and then render the sorting algorithm.

## Instalation

To install the package only for use, run

```
pip install visualsort
```

in the terminal.

## Quick start

Here is an example of rendering a bubble sort:

```python
from visualsort import swap, render, compare

def bubble_sort(nums):
  for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
      if compare(i, j, nums):
        nums = swap(i, j, nums)

render(bubble_sort)
```

## Development

To set up a local development environment, run:

```
git clone git@github.com:TomasBivainis/visualsort.git
cd visualsort
pip insatll -r requirements.txt
```

## Tests

Tests can be found in the `tests` folder. To run them, run:

```
pytest
```

in the main directory.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Issues

For issues, please open a [GitHub issue](https://github.com/TomasBivainis/visualsort/issues).
