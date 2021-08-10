def add(x: int, y: int = 1) -> int:
    """Returns $x + y$.

    Args:
        x: The first parameter.
        y: The second parameter. Default={default}.

    Returns:
        Added value.

    Examples:
        Examples should be written in doctest format.

        >>> add(1, 2)
        3

    !!! note
        You can use the [Admonition extension of
        MkDocs](https://squidfunk.github.io/mkdocs-material/extensions/admonition/).

    Note:
        `Note` section is converted into the Admonition.
    """
    return x + y
