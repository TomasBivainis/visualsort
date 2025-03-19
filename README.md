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

## Documentation

Documentation for the library functions can be found [here](https://tomasbivainis.github.io/visualsort/visualsort.html).

If you have added functions to the library, you can generate an updated version of the documentation with `pdoc` by typing the following command in the main directory:

```
pdoc visualsort --no-search --output-dir docs
```

This will automatically generate updated documentation in HTML format in the `docs` folder.

For it to be able to automatically generate the documentation you will need to use the same code documentation format as the previous functions.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Issues

For issues, please open a [GitHub issue](https://github.com/TomasBivainis/visualsort/issues).
