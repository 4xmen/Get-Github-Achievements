# Thank you for your support and help in the progress of the project.

Please read these notes before opening a Pull Request. Following them helps us review and merge faster.

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
4. Check that every link and image you touched opens correctly on GitHub before you submit.

## Adding a new language

1. Copy `README.md` to `README.<code>.md` and translate the text.
2. Create `assets/steps-<code>/` and translate all seven tutorials from `assets/steps/`, named `README.<achievement>-<code>.md`.
   Image paths inside tutorials stay the same (`../img/...`, `../badges/...`).
3. Point the "How to get" buttons in your README to your `assets/steps-<code>/` files.
4. Add your language to the language table at the top of **every** `README*.md` file. The table must be identical in all of them, so copy it from `README.md` after you edit it there.

## Please don't

- Open Pull Requests only to earn achievements. See the fairness section in the README.
- Commit editor or OS files (`.idea/`, `.vscode/`, `.DS_Store`).

### Thank you to all the programmers who help us in this way

#### For an open source community ❤️
