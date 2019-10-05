import time
from contextlib import contextmanager

@contextmanager
def timethis(laber):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('{}:{}'.format(laber,end-start))


if __name__ == '__main__':
    with timethis('counting'):
        n = 10000000
        while n > 0:
            n -= 1









