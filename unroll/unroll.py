#!/usr/bin/env python
# coding: utf-8
"""
    unroll
    ~~~~~~~~~~~~~~~~
Tool for writing multi-line comprehensions in Python.

Inspired and modified form the @unroll decorator, as presented by Steve Wedig.
Available at: http://code.google.com/p/lingospot/

Written and tested for Python 2.6


@todo: Consider removing fmap
"""
__author___ = 'Oakland Peters (oakland.peters@gmail.com)'
#VERISON: Pre-releases: a:alpha, b:beta, c/rc-release candidate
__verison__ = '0.2' 
__copyright__ = 'Copyright (c) 2014 Oakland Peters'
__license__ = 'MIT'

import functools



def unroll(*converters):
    """Wraps output of function with one or more converter functions."""
    if len(converters) == 0:
        converters = (iter,)
    for i, func in enumerate(converters):   #tuple of callable
        assert(callable(func)), "converter #{0} is not callable.".format(i)
    #Compose all converter functions
    convert = compose(*converters)
     
    @functools.wraps(convert)
    def outer(func): #pylint: disable=C0111
        @functools.wraps(func)
        def inner(*args, **kwargs): #pylint: disable=C0111
            return convert(func(*args, **kwargs))
        return inner
    return outer


#==============================================================================
#    Local Utility
#==============================================================================
def compose(inner, *others):
    """Compose inner function with any number of additional functions."""
    for i, func in enumerate((inner,)+others):
        assert(callable(func)), "function #{0} is not callable.".format(i)
    
    accumulator = inner
    for func in others:
        accumulator = _compose(accumulator, func) 
    return accumulator
def _compose(inner, outer):
    """result( arguments ) = outer( inner( arguments )"""
    @functools.wraps(outer)
    def composed(*a, **kw ):    #pylint: disable=C0111
        return outer(inner(*a, **kw))
    return composed
