# car-game

A very basic browser car game: dodge the traffic, and the road gets faster the longer you survive.

## Play

Install [uv](https://docs.astral.sh/uv/), then run:

```sh
uv run car-game
```

uv downloads the right Python version if needed, starts a local server, and opens the game at http://127.0.0.1:8000/.
Options: `--port 9000`, `--no-browser`.

You can also just open `src/car_game/static/index.html` directly in a browser.

## Controls

- **← / →** or **A / D** to change lanes
- **Space** to start or restart
- On a phone, tap the left or right half of the road
