import time


def measure_processing_time(function, *args):

    start_time = time.perf_counter()

    result = function(*args)

    end_time = time.perf_counter()

    return {
        "result": result,
        "processing_time_seconds": round(
            end_time - start_time,
            6
        )
    }