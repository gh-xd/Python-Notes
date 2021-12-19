# https://python3-cookbook.readthedocs.io/zh_CN/latest/c08/p25_creating_cached_instances.html
import logging

a = logging.getLogger('foo')
b = logging.getLogger('bar')
assert a is not b

c = logging.getLogger('foo')
assert a is c

