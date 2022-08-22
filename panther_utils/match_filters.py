import typing

from panther_config import detection

__all__ = ["deep_equal"]


def deep_equal(path: str, value: typing.Any) -> detection.PythonFilter:
    keys = path.split(".")
    return detection.PythonFilter(
        func=_filter_equal_inner,
        params=dict(keys=keys, expected=value)
    )


def _filter_equal_inner(obj: dict, params: typing.Dict[str, typing.Any]) -> bool:
    import functools
    import collections

    keys = params["keys"]
    expected = params["expected"]

    actual = functools.reduce(
        lambda d, key: d.get(key, None) if isinstance(d, collections.Mapping) else None,
        keys,
        obj,
    )

    return actual == expected
