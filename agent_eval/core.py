import json
from pathlib import Path
from math import ceil
def load(path):
 rows=[]
 for no,line in enumerate(Path(path).read_text().splitlines(),1):
  if not line.strip() or line.lstrip().startswith('#'): continue
  try: r=json.loads(line)
  except json.JSONDecodeError as e: raise ValueError('Invalid JSON on line '+str(no)) from e
  if not {'case_id','expected_success','success','latency_ms'}<=r.keys(): raise ValueError('Missing fields on line '+str(no))
  for k in ('latency_ms','estimated_cost_usd','tool_calls','tool_errors'):
   if r.get(k,0)<0: raise ValueError(k+' must be non-negative')
  r.setdefault('estimated_cost_usd',0); r.setdefault('tool_calls',0); r.setdefault('tool_errors',0); r.setdefault('notes','')
  if r['tool_errors']>r['tool_calls']: raise ValueError('tool errors exceed calls')
  rows.append(r)
 if not rows: raise ValueError('No run records found')
 if len({r['case_id'] for r in rows})!=len(rows): raise ValueError('case_id values must be unique')
 return rows
def evaluate(rows):
 if not rows: raise ValueError('No records')
 n=len(rows); lat=sorted(r['latency_ms'] for r in rows); calls=sum(r['tool_calls'] for r in rows); errors=sum(r['tool_errors'] for r in rows)
 return {'cases':n,'success_rate':sum(r['success'] for r in rows)/n,'mismatches':[r['case_id'] for r in rows if r['success']!=r['expected_success']],'average_latency_ms':round(sum(lat)/n,2),'p95_latency_ms':lat[max(0,ceil(.95*n)-1)],'estimated_cost_usd':round(sum(r['estimated_cost_usd'] for r in rows),6),'tool_calls':calls,'tool_errors':errors,'tool_error_rate':errors/calls if calls else 0}
def report(rows):
 m=evaluate(rows); lines=['# Agent Evaluation Report','','- Cases: '+str(m['cases']),'- Success rate: '+format(m['success_rate'],'.1%'),'- Average latency: '+str(m['average_latency_ms'])+' ms','- p95 latency: '+str(m['p95_latency_ms'])+' ms','- Estimated cost: $'+format(m['estimated_cost_usd'],'.6f'),'- Tool errors: '+str(m['tool_errors'])+'/'+str(m['tool_calls']),'','## Mismatches','']
 lines += m['mismatches'] or ['No mismatches']
 lines += ['','> Metrics reflect supplied records; they are not independent semantic or billing verification.','']
 return '\\n'.join(lines)
