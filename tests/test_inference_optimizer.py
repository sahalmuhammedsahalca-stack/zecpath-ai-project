from performance_scaling.inference_optimizer import InferenceOptimizer


def test_inference_measurement():

    optimizer = InferenceOptimizer()

    result = optimizer.measure(
        lambda value: value * 2,
        5,
    )

    assert result["result"] == 10
    assert result["performance"]["success"] is True
    assert optimizer.average_inference_time() >= 0