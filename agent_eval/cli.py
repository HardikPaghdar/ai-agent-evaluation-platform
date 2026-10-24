import argparse
from pathlib import Path
from .core import load,report
def main():
 p=argparse.ArgumentParser(); p.add_argument('input'); p.add_argument('--out',default='reports/evaluation.md'); a=p.parse_args(); rows=load(a.input); out=Path(a.out); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(report(rows)); print('Evaluated',len(rows),'cases ->',out)
if __name__=='__main__': main()
