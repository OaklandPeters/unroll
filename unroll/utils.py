import itertools
import functools


def fmap(func):
    """Functional-sugar for a partial of itertools.imap.
    functools.partial(itertools.imap, func)
    See test_exotic_string_concat() for example of use.
    """
    #Not required for @unroll, but frequently useful.
    @functools.wraps(func)
    def imapper(*args, **kwargs):
        return itertools.imap(func, *args, **kwargs)
    return imapper


def call(*args, **kwargs):
    """Decorator. Call function using provided arguments."""
    def outer(func):
        return func(*args, **kwargs)
    return outer