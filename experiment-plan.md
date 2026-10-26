# FlakeHunter — Experiment Plan

## 1. Objective

The goal is to investigate whether FlakeHunter can identify flaky tests using fewer test executions than a fixed-rerun approach, while maintaining useful detection accuracy.

## 2. Approaches to Compare

- **Fixed reruns:** Run each selected test a predefined number of times.
- **Adaptive diagnosis:** Choose additional test executions based on the results collected so far.
- **Order variation:** Change test execution order to investigate possible order-dependent failures.

## 3. Test Cases

The initial test collection will include:

- Stable tests that consistently pass.
- Deterministic failing tests.
- Intermittent tests that sometimes pass and sometimes fail.
- Tests affected by shared state or execution order.
- Timing-sensitive tests, introduced in a controlled environment.

## 4. Evaluation Metrics

- Number of test executions.
- Flaky-test detection precision and recall.
- Total diagnostic time.
- Correctness of suspected-cause classifications.
- Performance under different execution budgets.

## 5. Experimental Method

1. Establish a baseline using fixed reruns.
2. Run the same test cases using the proposed adaptive strategy.
3. Keep test cases, execution environments, and comparison budgets consistent where possible.
4. Repeat experiments to account for randomness.
5. Record all outcomes and compare the results.
6. Investigate false positives, missed flakes, and incorrect cause classifications.

## 6. Success Criteria

Success will be defined after measuring the baseline. The adaptive approach should reduce test executions without an unacceptable loss in detection quality.

No performance improvement will be claimed until supported by measured results.

## 7. Current Status

The initial test examples and problem statement have been created. The detector, benchmark suite, and comparative experiments are still to be implemented.

