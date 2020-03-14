"""Add the boilerplate's directories to Python's site-packages path.
"""
import os
import site
import sys

here = os.path.dirname(os.path.abspath(__file__))
path = lambda *a: os.path.join(here, *a)


def init_environment():
    prev_sys_path = list(sys.path)

    if os.path.exists(path('vendor')):
        for directory in os.listdir(path('vendor')):
            full_path = path('vendor/%s' % directory)
            if os.path.isdir(full_path):
                site.addsitedir(full_path)

    # Move the new items to the front of sys.path. (via virtualenv)
    new_sys_path = []
    for item in list(sys.path):
        if item not in prev_sys_path:
            new_sys_path.append(item)
            sys.path.remove(item)
    sys.path[:0] = new_sys_path


init_environment()
