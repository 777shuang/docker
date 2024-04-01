import os
import re
from glob import glob
from sys import argv
import pypandoc
import yaml

def build(dir: str):
    os.chdir(dir)

    markdown = sorted(glob('*.md'))

    extra_args = [
        '-sN',
        '--template', os.path.join(os.environ['TEMPLATES'], 'template.tex'),
        '-M', os.environ['crossrefYaml']
    ]

    meta = pypandoc.convert_text(
        markdown[0],
        'markdown',
        'markdown',
        extra_args=['--standalone'],
        filters=[os.path.join(os.environ['LUA_FILTER'], 'deletebody.lua')]
    )

    matched = re.search(r'---((.|\s)+)---', meta)
    if matched is not None:
        meta_yaml = yaml.safe_load(matched.groups()[0])
        if 'top-level-division' in meta_yaml:
            extra_args += ['--top-level-division', meta_yaml['top-level-division']]

    pypandoc.convert_file(
        markdown,
        'latex',
        format='markdown-auto_identifiers',
        outputfile=dir + 'tex',
        filters=[os.path.join(os.environ['LUA_FILTER'], 'filters.lua'), 'pandoc-crossref', 'mermaid-filter'],
        extra_args=extra_args
    )

    os.chdir('..')

if __name__ == "__main__":
    for i in range(1, len(argv)):
        build(argv[i])