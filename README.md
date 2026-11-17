# car-game

## 🏎️ [Play Three Lanes now →](https://adammorgan778.github.io/car-game/)

A simple car game for your phone or browser: dodge the traffic, grab coins, and survive as the road gets faster.

## Controls

- **Phone:** drag your finger left and right to steer
- **Desktop:** ← / → or A / D to steer, Space or Enter to start
- Each coin is worth 10 points; your best score is saved on your device

## Run it locally

Install [uv](https://docs.astral.sh/uv/), then run:

```sh
uv run car-game
```

uv downloads the right Python version if needed, starts a local server, and opens the game at http://127.0.0.1:8000/.
Options: `--port 9000`, `--no-browser`.

The game is a single file, [`docs/index.html`](docs/index.html), which GitHub Pages serves from the `docs/` folder on `main`.

## Poem

The road has a poem: [Three Lanes](POEM.md).
