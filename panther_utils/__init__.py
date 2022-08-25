import typing

__all__ = ["PantherEvent"]


class PantherEvent(typing.Protocol):
    def udm(self, key: str) -> typing.Any:
        pass

    def udm_path(self, key: str) -> typing.Optional[str]:
        pass

    def get(self, key: str, default: typing.Any = None) -> typing.Any:
        pass
