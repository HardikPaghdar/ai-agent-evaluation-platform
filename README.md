# AI Agent Evaluation Platform

Evaluate recorded agent runs with deterministic metrics for task success, expected-vs-observed mismatches, latency, supplied cost estimates and tool errors. Sample runs are synthetic. This tool does not execute agents or judge semantic answer quality.

## Run
`pip install -r requirements.txt`
`python -m agent_eval.cli examples/runs.jsonl --out reports/evaluation.md`
`pytest`

Provider cost must be populated from actual usage metadata. Keep a stable case set to compare agent versions.
