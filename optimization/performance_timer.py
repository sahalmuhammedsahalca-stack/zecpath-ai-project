import time


def measure_time(function, *args):

    start = time.time()

    result = function(*args)

    end = time.time()

    return {

        "execution_time": round(end - start, 4),

        "result": result

    }