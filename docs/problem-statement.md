# FlakeHunter: Problem Statement (Draft v0.1)

## The problem
A flaky test is an automated test that sometimes passes and sometimes fails on the exact same code. In a local experiment, a test with a random condition failed 2 out of 10 runs with no code change.

## Who is affected
- Developers waiting on continuous integration see random red builds and lose time rerunning them.
- Teams that learn to ignore failures can miss real bugs.
- Shared test infrastructure spends compute on reruns.

## Why rerunning is not enough
Rerunning until a test passes hides the problem instead of diagnosing it. Detecting rare flakiness by brute-force reruns is expensive, and reruns do not explain why a test is flaky.

## What FlakeHunter will investigate
Whether a pytest plugin can detect flaky tests with fewer reruns than a naive "run N times" approach, and suggest likely causes such as timing, test order, or shared state.

## Non-goals (for now)
- Not a replacement for fixing flaky tests, only a tool to find and diagnose them.
- Not supporting languages other than Python and pytest at first.

## Success and failure (targets to set after baseline measurements)
- Success: detection with fewer reruns than the naive baseline at similar accuracy (numbers to be defined after measuring the baseline).
- Failure: no measurable improvement over the baseline, which we would report honestly.

## Status
Prior-art search not yet done. Novelty is unknown. Repository is private until disclosure risks are considered.
