import time

from performance_scaling.inference_optimizer import InferenceOptimizer
from performance_scaling.resume_batch_processor import ResumeBatchProcessor
from performance_scaling.load_balancer import LoadBalancer
from performance_scaling.microservice_scaler import MicroserviceScaler
from performance_scaling.load_simulator import LoadSimulator
from performance_scaling.performance_benchmark import PerformanceBenchmark
from performance_scaling.scalability_controller import ScalabilityController


def mock_ai_processing(resume):

    time.sleep(0.001)

    return {
        "candidate_id": resume["candidate_id"],
        "score": 85,
    }


def main():

    resumes = [
        {
            "candidate_id": f"CAND{i:03d}"
        }
        for i in range(1, 21)
    ]

    print("=" * 60)
    print("DAY 60 PERFORMANCE BENCHMARK")
    print("=" * 60)

    # Inference
    optimizer = InferenceOptimizer()

    for resume in resumes[:5]:

        optimizer.measure(
            mock_ai_processing,
            resume,
        )

    print("\nInference:")
    print(
        optimizer.optimization_summary()
    )

    # Batch processing
    batch_processor = ResumeBatchProcessor(
        batch_size=5
    )

    print("\nBatch Processing:")
    print(
        batch_processor.summary(
            resumes
        )
    )

    # Cache
    print("\nCaching:")

    from performance_scaling.cache_manager import CacheManager

    cache = CacheManager()

    cache.set(
        "CAND001",
        {"score": 90},
    )

    print(
        {
            "cache_hit":
                cache.get("CAND001") is not None,
            "cache_size":
                cache.size(),
        }
    )

    # Load balancing
    load_balancer = LoadBalancer(
        [
            "resume-service-1",
            "resume-service-2",
            "resume-service-3",
        ]
    )

    print("\nLoad Balancing:")
    print(
        load_balancer.distribute(12)
    )

    # Scaling
    scaler = MicroserviceScaler(
        min_instances=1,
        max_instances=5,
        requests_per_instance=100,
    )

    controller = ScalabilityController(
        scaler
    )

    print("\nScalability:")
    print(
        controller.evaluate(350)
    )

    # Performance benchmark
    benchmark = PerformanceBenchmark()

    benchmark_result = benchmark.run(
        mock_ai_processing,
        resumes,
        repetitions=2,
    )

    print("\nPerformance Benchmark:")
    print(benchmark_result)

    # Load simulation
    simulator = LoadSimulator(
        workers=5
    )

    print("\nSimulated Load:")

    load_result = simulator.run(
        mock_ai_processing,
        resumes,
    )

    print(load_result)

    print("\n" + "=" * 60)
    print("DAY 60 BENCHMARK COMPLETED")
    print("=" * 60)


if __name__ == "__main__":
    main()