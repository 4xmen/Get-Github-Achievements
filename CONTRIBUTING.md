# Thank you for your support and help in the progress of the project.

Please read these notes before opening a Pull Request. Following them helps us review and merge faster.

## How to contribute

1. **Fork** this repository and create a branch for your change, e.g. `fix/french-typos` or `lang/italian`.
2. Make your change and commit it.
3. Run the check (needs Python 3.8 or newer, nothing to install):

   ```bash
   python3 scripts/check_readmes.py
   ```

   It prints every broken link and every language table that doesn't match `README.md`, with file and line.
4. Open a Pull Request into `main` and fill in the template.

## What happens after you open a Pull Request

| Step | Who | What |
|------|-----|------|
| 1 | GitHub | Runs the **README check** (the same script as above). If it fails, open the *Checks* tab, fix the listed lines and push again. |
| 2 | @YasinDehfuli | Gets a review request automatically. |
| 3 | You | Answer review comments and push fixes to the same branch. Every comment must be resolved. |
| 4 | @YasinDehfuli | Merges with **Squash and merge**, so your PR becomes one clean commit on `main`. Your branch is deleted automatically. |

Contributors can't push directly to `main`. Every change goes through a Pull Request.
If this is your first Pull Request here, the check may wait until a maintainer approves it to run.

## Project layout

| Path | What it holds |
|------|---------------|
| `README.md` | English guide (the source every translation follows) |
| `README.<code>.md` | Translated guide, e.g. `README.de.md` |
| `assets/steps/` | English step-by-step tutorials, one file per achievement |
| `assets/steps-<code>/` | Translated tutorials, e.g. `assets/steps-de/README.yolo-de.md` |
| `assets/badges/` | Achievement badge images |
| `assets/img/<achievement>/` | Tutorial screenshots |
| `assets/img/btn-<code>.png` | Optional translated "How to get" button |

## General rules

1. Keep the layout of `README.md`. Translations and fixes should change text, not structure or appearance.
2. One topic per Pull Request (one language, or one fix). Work in a new branch and keep commits neat and readable.
3. Explain *why* in the Pull Request description, especially when you change a small section or add a new file.
4. Run `python3 scripts/check_readmes.py` before you submit.

## Adding a new language

1. Copy `README.md` to `README.<code>.md` and translate the text.
2. Create `assets/steps-<code>/` and translate all seven tutorials from `assets/steps/`, named `README.<achievement>-<code>.md`.
   Image paths inside tutorials stay the same (`../img/...`, `../badges/...`).
3. Point the "How to get" buttons in your README to your `assets/steps-<code>/` files.
4. Add your language to the language table at the top of **every** `README*.md` file. The table must be identical in all of them, so copy it from `README.md` after you edit it there. The check fails if any table is different.

## Please don't

- Open Pull Requests only to earn achievements. See the fairness section in the README.
- Commit editor or OS files (`.idea/`, `.vscode/`, `.DS_Store`).

### Thank you to all the programmers who help us in this way

#### For an open source community ❤️
