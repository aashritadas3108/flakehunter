# FlakeHunter

A research and engineering project to detect and diagnose flaky tests in Python projects that use pytest.

> **Status: early development.** Nothing is implemented yet except project setup and a sanity test. This README describes goals, not finished features.

## The problem

A flaky test is an automated test that sometimes passes and sometimes fails on the exact same code. Flaky tests cause random red builds in continuous integration, waste developer time on reruns, and teach teams to ignore failures, which can hide real bugs.

Rerunning a failed test until it passes masks the problem without diagnosing it, and detecting rare flakiness by brute-force reruns gets expensive on large test suites.

See [docs/problem-statement.md](docs/problem-statement.md) for details.

## What this project investigates

Whether a pytest plugin can detect flaky tests using fewer reruns than a fixed "run N times" baseline, and report how much evidence supports each verdict. Whether this beats existing approaches is **unknown** and will be tested against them.

Existing tools are reviewed in [docs/prior-art.md](docs/prior-art.md).

## Planned work

- [ ] Baseline detector that reruns tests a fixed number of times
- [ ] Evaluation on real open-source projects
- [ ] Adaptive rerun strategy, compared against the baseline
- [ ] Failure analysis and honest reporting of results

## Setup (Windows, PowerShell)

```powershell
git clone https://github.com/aashritadas3108/flakehunter.git
cd flakehunter
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install pytest
```

## Running the tests

```powershell
pytest
```

## Results

No experiments have been run yet. Benchmark results will be added here once they exist, with the methodology used to produce them.

## Limitations

- Early stage: the design and the evaluation method are still being defined.
- Initial scope is Python and pytest only.

## Project notes

- This repository is private while originality and disclosure questions are being considered.
- License: not yet chosen.
