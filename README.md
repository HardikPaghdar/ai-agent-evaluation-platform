# AI Agent Evaluation Platform

A deterministic evaluator for recorded agent runs: success rate, mismatches, latency, estimated cost and tool errors. Synthetic sample data included. This evaluates supplied run records; it does not execute agents or judge semantic quality.

Run: `pip install -r requirements.txt`; `python -m agent_eval.cli examples/runs.jsonl`; `pytest`.
