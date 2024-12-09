"""This is the metaclass used by several classes in this project to enforce the singleton pattern.

Note that this metaclass creates a separate instance of the class native to each thread. This is necessary because the
application runs in Streamlit where different app instances ocupy different threads. The more elegant implementation of
the singleton pattern (commented out below) created a single instance for the class shared ACROSS ALL THREADS. This
produces difficult-to-debug errors when the application is run in Streamlit."""

import threading


class SingletonMeta(type):
    _thread_local = threading.local()

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls._thread_local, 'instances'):
            cls._thread_local.instances = {}

        if cls not in cls._thread_local.instances:
            instance = super().__call__(*args, **kwargs)
            cls._thread_local.instances[cls] = instance

        return cls._thread_local.instances[cls]


# class SingletonMeta(type):
#     _instances = {}
#
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             instance = super().__call__(*args, **kwargs)
#             cls._instances[cls] = instance
#         return cls._instances[cls]
