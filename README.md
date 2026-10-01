# World Modeling through Spectral Alignment

Project website for SpecWM, a world model trained to preserve teacher-defined similarities between observations.

[Website](https://spectral-alignment.github.io/)

## Editing

Edit `content.md` for all page text, authors, captions, tables, and equations. The settings at the top also contain navigation labels and figure descriptions. Pushing to `main` builds and deploys the static site automatically.

Use `$…$` for inline math and `$$` blocks for equations. Keep the `:::figure`, `:::note`, and other layout markers around their content. The generated `dist/index.html` should not be edited directly.

## Local preview

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/build.py
python3 -m http.server 4173 --directory dist
```

Open [localhost:4173](http://localhost:4173/).
