import typing
import unittest
import panther_config

__all__ = ["PantherPythonFilterTestCase"]


class PantherPythonFilterTestCase(unittest.TestCase):
    @staticmethod
    def _callFilterFunc(
        pfilter: panther_config.detection.PythonFilter, obj: typing.Any
    ) -> typing.Callable[[typing.Any], bool]:
        import ast
        import pickle
        from panther_config._utilities import serialize_func

        func_module = pickle.loads(serialize_func(pfilter.func))

        ns = dict(typing=typing, panther_config=panther_config)

        exec(ast.unparse(func_module), ns)
        return ns[pfilter.func.__name__](obj, pfilter.params)

    def assertFilterIsValid(
        self, obj: panther_config.detection.PythonFilter
    ) -> typing.NoReturn:
        self.assertIsInstance(obj, panther_config.detection.PythonFilter)

    def assertFilterMatches(
        self, test_filter: panther_config.detection.PythonFilter, obj: typing.Any
    ) -> typing.NoReturn:
        result = self._callFilterFunc(test_filter, obj)

        self.assertTrue(result)

    def assertFilterNotMatches(
        self, test_filter: panther_config.detection.PythonFilter, obj: typing.Any
    ) -> typing.NoReturn:
        result = self._callFilterFunc(test_filter, obj)

        self.assertFalse(result)
