#!/usr/bin/env python3
"""Read-only Obsidian vault inventory."""
import argparse,csv,json,os,sys
from pathlib import Path
KINDS={'.md':'markdown','.png':'image','.jpg':'image','.jpeg':'image','.svg':'image','.webp':'image','.gif':'image','.bmp':'image','.pdf':'document','.txt':'text','.log':'text','.csv':'data','.json':'data','.yaml':'configuration','.yml':'configuration','.toml':'configuration','.py':'script','.sh':'script','.zsh':'script','.ps1':'script'}
def ensure_output_outside(root, output):
 output=output.resolve(strict=False)
 try: output.relative_to(root.resolve())
 except ValueError: return
 raise ValueError(f'report output must be outside the source vault: {output}')
def scan(root):
 root=root.resolve(strict=True)
 if not root.is_dir(): raise NotADirectoryError(root)
 files=[]; dirs=[]; warnings=[]
 def onerror(e): warnings.append(str(e))
 for current,names,filenames in os.walk(root,followlinks=False,onerror=onerror):
  base=Path(current); names.sort(); filenames.sort(); kept=[]
  for name in names:
   p=base/name
   if p.is_symlink(): warnings.append(f'directory symlink not traversed: {p.relative_to(root)}')
   else: dirs.append(p.relative_to(root).as_posix()); kept.append(name)
  names[:]=kept
  for name in filenames:
   p=base/name
   try:
    link=p.is_symlink(); size=None if link else p.stat().st_size
    files.append({'path':p.relative_to(root).as_posix(),'extension':p.suffix.lower(),'kind':'symlink' if link else KINDS.get(p.suffix.lower(),'other'),'size_bytes':size,'empty':False if link else size==0})
   except OSError as e: warnings.append(f'{p}: {e}')
 files.sort(key=lambda x:x['path'].casefold()); dirs.sort(key=str.casefold)
 return {'root':str(root),'file_count':len(files),'directory_count':len(dirs),'files':files,'directories':dirs,'warnings':warnings}
def main():
 ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('root',type=Path); ap.add_argument('--json-out',type=Path); ap.add_argument('--csv-out',type=Path); a=ap.parse_args()
 try:
  d=scan(a.root)
  for output in (a.json_out,a.csv_out):
   if output is not None: ensure_output_outside(Path(d['root']),output)
  if a.json_out: a.json_out.parent.mkdir(parents=True,exist_ok=True); a.json_out.write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
  if a.csv_out:
   a.csv_out.parent.mkdir(parents=True,exist_ok=True)
   with a.csv_out.open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=['path','extension','kind','size_bytes','empty']); w.writeheader(); w.writerows(d['files'])
  if not a.json_out and not a.csv_out: print(json.dumps(d,indent=2))
  else: print(json.dumps({k:v for k,v in d.items() if k not in ('files','directories')}))
  return 1 if d['warnings'] else 0
 except (OSError,ValueError) as e: print(f'inventory error: {e}',file=sys.stderr); return 2
if __name__=='__main__': raise SystemExit(main())
