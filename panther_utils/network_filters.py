import typing

from panther_config import detection

__all__ = ["ip_in_range"]


def ip_in_cidr(path: str, cidr: str) -> detection.PythonFilter:
    keys = path.split(".")
    return detection.PythonFilter(
        func=_ip_in_range, params=dict(keys=keys, cidr=cidr)
    )


def _ip_in_range(obj: dict, params: typing.Dict[str, typing.Any]) -> bool:
    import ipaddress

    keys = params["keys"]
    cidr = params["cidr"]

    ipaddress.

    return actual == expected
