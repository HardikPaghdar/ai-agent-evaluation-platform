import pytest
from agent_eval.core import load,evaluate,report

def test_sample_report():
 rows=load('examples/runs.jsonl'); m=evaluate(rows)
 assert m['cases']==4 and m['tool_errors']==1 and 'Mismatches' in report(rows)

def test_duplicate_id_rejected(tmp_path):
 row='{"case_id":"x","expected_success":true,"success":true,"latency_ms":1}'
 p=tmp_path/'runs.jsonl'; p.write_text(row+'\\n'+row)
 with pytest.raises(ValueError): load(p)
