
__all__ = [
    "deep_get",
]


def deep_get(dictionary: dict, *keys, default=None):
    """Safely return the value of an arbitrarily nested map

    Inspired by https://bit.ly/3a0hq9E
    """

    import functools
    import collections

    return functools.reduce(
        lambda d, key: d.get(key, default) if isinstance(d, collections.Mapping) else default, keys, dictionary
    )


