#!/usr/bin/env python3
"""Check the guides before merging.

1. Every relative link and image in every .md file points to a file that exists.
2. The language table is identical in every README*.md and lists every README*.md.

Run from anywhere:  python3 scripts/check_readmes.py
"""
import glob
import os
import re
import sys
from urllib.parse import unquote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
REPO_BLOB = 'https://github.com/4xmen/Get-Github-Achievements/blob/main/'
LINK = re.compile(r'(?:\]\(|src=["\']|href=["\']|srcset=["\'])([^)"\'\s#]*)')
TABLE = re.compile(r'<table>.*?</table>', re.S)

errors = []


def error(path, message, line=1):
    errors.append((path, line, message))


def check_links():
    for path in sorted(glob.glob('**/*.md', recursive=True)):
        if path.startswith('node_modules'):
            continue
        text = open(path, encoding='utf-8').read()
        for match in LINK.finditer(text):
            url = match.group(1)
            line = text.count('\n', 0, match.start()) + 1
            if url.startswith(REPO_BLOB):
                target = unquote(url[len(REPO_BLOB):])
            elif url == '':
                error(path, 'empty link or image', line)
                continue
            elif re.match(r'^[a-z]+:', url):
                continue
            else:
                target = os.path.join(os.path.dirname(path), unquote(url))
            if not os.path.exists(target):
                error(path, f'broken link: {url}', line)


def check_language_tables():
    readmes = sorted(glob.glob('README*.md'))
    tables = {}
    for path in readmes:
        text = open(path, encoding='utf-8').read()
        match = TABLE.search(text)
        if match:
            tables[path] = (match.group(0), text.count('\n', 0, match.start()) + 1)
        else:
            error(path, 'language table is missing')

    if 'README.md' not in tables:
        return
    reference = tables['README.md'][0]
    for path, (table, line) in tables.items():
        if table != reference:
            error(path, 'language table differs from README.md (copy it from README.md)', line)

    listed = set(re.findall(r'href="(README[^"]*\.md)"', reference))
    for path in readmes:
        if path not in listed:
            error('README.md', f'language table does not link to {path}')
    for path in sorted(listed - set(readmes)):
        error('README.md', f'language table links to missing file {path}')


check_links()
check_language_tables()

in_actions = os.environ.get('GITHUB_ACTIONS') == 'true'
for path, line, message in errors:
    print(f'::error file={path},line={line}::{message}' if in_actions else f'{path}:{line}: {message}')

if errors:
    print(f'\n{len(errors)} problem(s) found.')
    sys.exit(1)
print('All links and language tables are OK.')
