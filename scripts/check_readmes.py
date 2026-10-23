#!/usr/bin/env python3
"""Check the guides before merging.

1. Every relative link and image in every .md file points to a file that exists.
2. The language table is identical in every README*.md and lists every README*.md.
3. Every README.<code>.md has a tutorial folder assets/steps-<code>/ and the other way round.
4. A README links only to its own tutorials (or to the English ones), never to another language's.
5. Every file in assets/steps-<code>/ translates a tutorial from assets/steps/.
   A tutorial that isn't translated yet is only a warning.

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
LINK = re.compile(r'(?:\]\(|src=["\']|href=["\']|srcset=["\'])([^)"\'\s]*)')
CODE_BLOCK = re.compile(r'^[ \t]*```.*?^[ \t]*```', re.S | re.M)
TABLE = re.compile(r'<table>.*?</table>', re.S)
STEPS_FOLDER = re.compile(r'assets/steps(?:-[^/"\')\s]+)?/')

errors = []
warnings = []


def error(path, message, line=1):
    errors.append((path, line, message))


def warning(path, message, line=1):
    warnings.append((path, line, message))


def read(path):
    with open(path, encoding='utf-8') as f:
        return f.read()


def line_of(text, index):
    return text.count('\n', 0, index) + 1


def check_links():
    for path in sorted(glob.glob('**/*.md', recursive=True)):
        if path.startswith('node_modules'):
            continue
        # Examples inside ``` code blocks aren't real links. Keep their newlines so line numbers stay right.
        text = CODE_BLOCK.sub(lambda m: '\n' * m.group(0).count('\n'), read(path))
        for match in LINK.finditer(text):
            url, anchor = match.group(1).split('#', 1) if '#' in match.group(1) else (match.group(1), '')
            line = line_of(text, match.start())
            if url == '' and anchor:
                continue
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
        text = read(path)
        match = TABLE.search(text)
        if match:
            tables[path] = (match.group(0), line_of(text, match.start()))
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


def translation_of(achievement, code, names):
    """Return the file in assets/steps-<code>/ that translates this achievement, if any."""
    for name in (f'README.{achievement}-{code}.md', f'README.{achievement}.{code}.md', f'README.{achievement}.md'):
        if name in names:
            return name
    return None


def check_structure():
    achievements = sorted(os.path.basename(p)[len('README.'):-len('.md')] for p in glob.glob('assets/steps/README.*.md'))
    codes = sorted(p[len('README.'):-len('.md')] for p in glob.glob('README.*.md'))
    folders = sorted(p[len('assets/steps-'):] for p in glob.glob('assets/steps-*') if os.path.isdir(p))

    for code in codes:
        if code not in folders:
            error(f'README.{code}.md', f'tutorial folder assets/steps-{code}/ is missing')
    for code in folders:
        if code not in codes:
            error(f'assets/steps-{code}', f'README.{code}.md is missing for this tutorial folder')

    for code in folders:
        names = sorted(os.listdir(f'assets/steps-{code}'))
        known = {translation_of(a, code, names) for a in achievements}
        for name in names:
            if name not in known:
                error(f'assets/steps-{code}/{name}',
                      f'not a translation of a tutorial in assets/steps/ (name it README.<achievement>-{code}.md)')
        for achievement in achievements:
            if translation_of(achievement, code, names) is None:
                warning(f'assets/steps-{code}', f'README.{achievement}-{code}.md is not translated yet')

    for code in [None] + codes:
        path = 'README.md' if code is None else f'README.{code}.md'
        own = 'assets/steps/' if code is None else f'assets/steps-{code}/'
        text = read(path)
        for match in STEPS_FOLDER.finditer(text):
            if match.group(0) not in (own, 'assets/steps/'):
                error(path, f'links to another language\'s tutorial {match.group(0)} (use {own})',
                      line_of(text, match.start()))


check_links()
check_language_tables()
check_structure()

in_actions = os.environ.get('GITHUB_ACTIONS') == 'true'
for level, problems in (('warning', warnings), ('error', errors)):
    for path, line, message in problems:
        print(f'::{level} file={path},line={line}::{message}' if in_actions else f'{path}:{line}: {level}: {message}')

if errors:
    print(f'\n{len(errors)} problem(s) found.')
    sys.exit(1)
print('All links, language tables and tutorial folders are OK.')
