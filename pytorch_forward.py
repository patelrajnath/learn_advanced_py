from typing import Callable, Any


def _forward_unimplemented(self, *input_forward: Any) -> None:
    r"""Defines the computation performed at every call.

    Should be overridden by all subclasses.

    .. note::
        Although the recipe for forward pass needs to be defined within
        this function, one should call the :class:`Module` instance afterwards
        instead of this since the former takes care of running the
        registered hooks while the latter silently ignores them.
    """
    raise NotImplementedError


class MyModule(object):
    def __init__(self):
        super(MyModule, self).__init__()

    # Trick mypy into not applying contravariance rules to inputs by defining
    # forward as a value, rather than a function.  See also
    # https://github.com/python/mypy/issues/8795

    forward: Callable[..., Any] = _forward_unimplemented

    def _call_impl(self, *input_forward, **kwargs):
        return self.forward(*input_forward, **kwargs)

    __call__: Callable[..., Any] = _call_impl


class ForwardTest(MyModule):
    def __init__(self):
        super(ForwardTest, self).__init__()

    @staticmethod
    def forward(x):
        print("Yes forward called")
        x += 10
        return x


f = ForwardTest()
print(f(12))
