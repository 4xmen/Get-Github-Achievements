# Contributing

Thank you for helping! This project is a guide, so most contributions are text: fixing a mistake, improving a translation or adding a new language.
Please read this page before you open a Pull Request. Following it helps us review and merge faster.

## What you can help with

| You want to | Edit these files |
|-------------|------------------|
| Fix a typo or wrong info in English | `README.md` and/or `assets/steps/` |
| Fix or improve a translation | `README.<code>.md` and/or `assets/steps-<code>/` |
| Add a new language | See [Adding a new language](#adding-a-new-language) |
| Update an achievement because GitHub changed it | Start with English (`README.md` + `assets/steps/`). Translations can follow in their own Pull Requests. |
| Change the check, workflows or templates (`scripts/`, `.github/`) | Open an issue first, so we can agree on it. |

Found a problem but can't fix it? [Open an issue](https://github.com/4xmen/Get-Github-Achievements/issues/new/choose).

## How to contribute

1. **Fork** this repository and create a branch for your change, e.g. `fix/french-typos` or `lang/italian`.
2. Make your change and commit it.
3. Run the check (needs Python 3.8 or newer, nothing to install):

   ```bash
   python3 scripts/check_readmes.py
   ```

   It prints every problem with its file and line. Fix all errors before you push. Warnings are fine.
4. Open a Pull Request into `main` and fill in the template.

## Rules

1. **One topic per Pull Request.** One language or one fix. Don't mix several languages in one Pull Request.
2. **Keep the layout of `README.md`.** Translations and fixes change text, not structure: same sections, same order, same images.
3. **English first.** When an achievement changes, update `README.md` and `assets/steps/` first. Translations follow.
4. **Link to your own language.** `README.<code>.md` links only to `assets/steps-<code>/`. If a tutorial isn't translated yet, link to the English one in `assets/steps/`. Never link to another language's folder.
5. **Share images.** Tutorials in every language use the same screenshots from `assets/img/<achievement>/` and badges from `assets/badges/`. Don't copy images per language.
6. **Don't rename or move existing files.** Other websites link to them, and those links would break.
7. **Don't commit** editor or OS files (`.idea/`, `.vscode/`, `.DS_Store`) or generated files.

## Project layout

| Path | What it holds |
|------|---------------|
| `README.md` | English guide. Every translation follows it. |
| `README.<code>.md` | Translated guide, e.g. `README.de.md` |
| `assets/steps/` | English step-by-step tutorials, one file per achievement |
| `assets/steps-<code>/` | Translated tutorials for `README.<code>.md` |
| `assets/img/<achievement>/` | Tutorial screenshots, shared by all languages |
| `assets/img/btn.png`, `assets/img/btn-<code>.png` | "How to get" button, English and translated (optional) |
| `assets/badges/` | Achievement badge images |
| `scripts/check_readmes.py` | The check that runs on every Pull Request |
| `.github/` | Workflow, code owners, issue and Pull Request templates |

### Achievements

| Achievement | English tutorial | Screenshots |
|-------------|------------------|-------------|
| Quickdraw | `assets/steps/README.quickdraw.md` | `assets/img/quickdraw/` |
| YOLO | `assets/steps/README.yolo.md` | `assets/img/yolo/` |
| Galaxy Brain | `assets/steps/README.galaxy-brain.md` | `assets/img/galaxy-brain/` |
| Pull Shark | `assets/steps/README.pull-shark.md` | `assets/img/pull-shark/` |
| Starstruck | `assets/steps/README.starstruck.md` | `assets/img/starstruck/` |
| Pair Extraordinaire | `assets/steps/README.pair-extraordinaire.md` | `assets/img/pair-extraordinaire/` |
| Public Sponsor | `assets/steps/README.publicsponsor.md` | `assets/img/public-sponsor/` |

A translated tutorial is named `README.<achievement>-<code>.md`, e.g. `assets/steps-de/README.yolo-de.md`.
The older `ar`, `chs` and `ja` folders use `README.<achievement>.md`, and `pl` uses `README.<achievement>.pl.md`. Keep those names (rule 6).

### Languages

The code is the part of the file name between `README.` and `.md`. Use the code that is already there.
A few older codes are not ISO codes: `chs` is Chinese, `hin` is Hindi and `am` is Armenian.

| Language | Code | Guide | Tutorials |
|----------|------|-------|-----------|
| English | – | `README.md` | `assets/steps/` |
| Persian | `fa` | `README.fa.md` | `assets/steps-fa/` |
| Arabic | `ar` | `README.ar.md` | `assets/steps-ar/` |
| German | `de` | `README.de.md` | `assets/steps-de/` |
| French | `fr` | `README.fr.md` | `assets/steps-fr/` |
| Russian | `ru` | `README.ru.md` | `assets/steps-ru/` |
| Turkish | `tr` | `README.tr.md` | `assets/steps-tr/` |
| Dutch | `nl` | `README.nl.md` | `assets/steps-nl/` |
| Chinese | `chs` | `README.chs.md` | `assets/steps-chs/` |
| Spanish | `es` | `README.es.md` | `assets/steps-es/` |
| Indonesian | `id` | `README.id.md` | `assets/steps-id/` |
| Hindi | `hin` | `README.hin.md` | `assets/steps-hin/` |
| Japanese | `ja` | `README.ja.md` | `assets/steps-ja/` |
| Armenian | `am` | `README.am.md` | `assets/steps-am/` |
| Swahili | `sw` | `README.sw.md` | `assets/steps-sw/` |
| Portuguese | `pt` | `README.pt.md` | `assets/steps-pt/` |
| Bengali | `bn` | `README.bn.md` | `assets/steps-bn/` |
| Vietnamese | `vi` | `README.vi.md` | `assets/steps-vi/` |
| Polish | `pl` | `README.pl.md` | `assets/steps-pl/` |

## Adding a new language

1. Pick the two-letter [ISO 639-1 code](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) of your language, e.g. `it` for Italian.
   Check the table above first: if your language is already there, improve it instead.
2. Copy `README.md` to `README.<code>.md` and translate the text.
3. Create `assets/steps-<code>/`. Copy every file from `assets/steps/` into it as `README.<achievement>-<code>.md` and translate it.
   Image paths inside tutorials stay the same (`../img/...`, `../badges/...`).
4. In `README.<code>.md`, point both links of every achievement (the badge and the "How to get" button) to your `assets/steps-<code>/` files.
5. Optional: add a translated button as `assets/img/btn-<code>.png`, the same size as `assets/img/btn.png`.
6. Add your language to the end of the language table in `README.md`. Each row has up to 6 languages:

   ```html
   <td align="center"><a href="README.<code>.md"><img src="https://img.shields.io/badge/Lang-<Language>-<color>.svg" alt="<code>"></a></td>
   ```

   Then copy the whole table from `README.md` into **every** `README*.md`. The tables must be identical.
7. Add your language to the [Languages](#languages) table on this page.
8. Run the check. It fails if a table is different, a link is broken or a tutorial folder is missing.

## What the check tests

`scripts/check_readmes.py` runs on every Pull Request. It fails when:

- a link or image in any `.md` file points to a file that doesn't exist, or is empty
- the language table isn't identical in every `README*.md`, or doesn't list every `README*.md`
- a `README.<code>.md` has no `assets/steps-<code>/` folder, or the other way round
- a README links to another language's tutorials
- a file in `assets/steps-<code>/` doesn't match any tutorial in `assets/steps/`

A tutorial that isn't translated yet is only a warning.

## What happens after you open a Pull Request

| Step | Who | What |
|------|-----|------|
| 1 | GitHub | Runs the **README check**. If it fails, open the *Checks* tab, fix the listed lines and push again. |
| 2 | @YasinDehfuli | Gets a review request automatically. |
| 3 | You | Answer review comments and push fixes to the same branch. Every comment must be resolved. |
| 4 | @YasinDehfuli | Merges with **Squash and merge**, so your Pull Request becomes one clean commit on `main`. Your branch is deleted automatically. |

If this is your first Pull Request here, the check may wait until a maintainer approves it to run.

## Branch rules for `main`

`main` is protected, so every change is reviewed and checked:

- Changes go in only through a Pull Request. Nobody pushes to `main` directly.
- The **README check** must pass.
- @YasinDehfuli (code owner) must approve. A new push after the approval needs a new approval.
- All review comments must be resolved.
- Pull Requests are merged with **Squash and merge** only.
- `main` can't be force-pushed or deleted.

Repository admins can merge their own Pull Requests without an approval, but they can't push to `main` directly either.

## Please don't

- Open Pull Requests only to earn achievements. See the fairness section in the README.
- Open a Pull Request that only changes spacing or formatting.

### Thank you to all the programmers who help us in this way

#### For an open source community ❤️
