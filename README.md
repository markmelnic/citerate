# Circular iterator (Citerate)

Bi-dimensional matrix iterator starting from any point (i, j), going layer by layer around the starting coordinates.

## Usage

    pip install citerate

As of __14 july 2021__ it contains one method `citerator`

    from citerate import citerator

## Examples

Using the example data set:

    CLOCKWISE_SET = [
        [10, 11, 12, 13, 14],
        [25, 2,  3,  4,  15],
        [24, 9,  1,  5,  16],
        [23, 8,  7,  6,  17],
        [22, 21, 20, 19, 18],
    ]

To iterate over the set layer by layer starting from coordinates (i=2, j=2), which corresponds to the value 1 and print each layer of values.

    for layer in citerate.citerator(CLOCKWISE_SET, i = 2, j = 2):
        print(layer)

Outputs:

    [1]
    [2, 3, 4, 5, 6, 7, 8, 9]
    [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

# Footnotes

- It is NOT mandatory to iterate starting from the central coordinates or for the matrix to be uniform.
- It HAS to be bi-dimenstional and consist of "list of lists".
