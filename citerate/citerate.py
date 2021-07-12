def iterator(data: list, i: int, j: int, clockwise: bool = True) -> list:
    """Analyse data using a range based percentual proximity
    algorithm and calculate the linear maximum likelihood estimation.

    Args:
        data (list): Data set to iterate over.

    Optional args:
        clockwise (bool): Iterate clockwise / anticlockwise.

    Raises:
        ValueError: Weights can only be either 0 or 1

    Yields:
        list: Matrix layer.
    """

    yield [data[i][j]]

    wpx = i
    hpx = j
    ilev = 0
    for d in range(min(len(data), len(data[0]))):
        ilev += 1
        layer = []
        # top row
        wpos = wpx - ilev
        for i in range(hpx - ilev, hpx + ilev):
            if not (i < 0 or wpos < 0) and not wpos >= len(data):
                layer.append(data[wpos][i])
        # right column
        hpos = hpx + ilev
        for i in range(wpx - ilev, wpx + ilev):
            if not (i < 0 or hpos < 0) and not hpos >= len(data):
                layer.append(data[i][hpos])
        # bottom row
        wpos = wpx + ilev
        for i in reversed(range(hpx - ilev + 1, hpx + ilev + 1)):
            if not (i < 0 or wpos < 0) and not wpos >= len(data):
                layer.append(data[wpos][i])
        # left column
        hpos = hpx - ilev
        for i in reversed(range(wpx - ilev + 1, wpx + ilev + 1)):
            if not (i < 0 or hpos < 0) and not hpos >= len(data):
                layer.append(data[i][hpos])

        if layer:
            yield layer
        else:
            break
