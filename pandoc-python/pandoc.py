import os
import re
from subprocess import run
from glob import glob
from sys import argv
import yaml

def build(dir: str):
    os.chdir(dir)

    markdown = sorted(glob('*.md'))

    cmd = [
        'pandoc', '-s',
        '-L', os.path.join(os.environ['LUA_FILTER'], 'deletebody.lua'),
        markdown[0],
        '-t', 'markdown'
    ]
    ret = run(cmd, capture_output=True, text=True)
    cmd = [
        'pandoc', '-sN',
        '--template', os.path.join(os.environ['TEMPLATES'], 'template.tex'),
        '-M', os.environ['crossrefYaml'],
        '-L', os.path.join(os.environ['LUA_FILTER'], 'filters.lua'),
        '-F', 'pandoc-crossref',
        '-F', 'mermaid-filter',
        '-o', dir + '.tex'
    ]
    matched = re.search(r'---((.|\s)+)---', ret.stdout)
    if matched is not None:
        meta = yaml.safe_load(matched.groups()[0])
        if 'top-level-division' in meta:
            cmd += ['--top-level-division', meta['top-level-division']]

    cmd += markdown
    run(cmd)
    os.chdir('..')

if __name__ == "__main__":
    for i in range(1, len(argv)):
        build(argv[i])