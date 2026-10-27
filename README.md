# Dead Air

An analog-horror stalker game. Recover six VHS tapes while something hunts you.

This repo is the update source for the Dead Air Windows app. Every time the app
opens it checks `version.json` here, and if `build` is higher than what it has,
it downloads `game/index.html` and plays the new version.

## Releasing an update
1. Edit the game and rebuild the app page:
   `python3 tools/build_app_html.py <web-version.html> game/index.html`
2. Bump `build` (and `version`) in `version.json`.
3. Commit and push to `main`. Apps pick it up on their next launch
   (GitHub can take up to ~5 minutes to serve the new file).

Fonts in `game/fonts` are under the SIL Open Font License / Apache 2.0 (licenses included).
