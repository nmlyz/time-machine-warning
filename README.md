# time-machine-warning

[![make.fun · u-eager-stork-81-9647-funniest-time-machine-warning-f8add151](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/nmlyz/time-machine-warning/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/nmlyz/time-machine-warning/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)

A tiny program that prints the warning label for a time machine.

Every appliance ships with a warning label. A time machine is the only
one that can be returned before it was bought, so its label is written
from the point of view of the returns department: this unit has already
been sent back once — by its own owner, tomorrow. The joke lands in a
single sentence, with no setup and no punchline after it.

The program writes exactly one line to `entry.txt`:

```
WARNING: This machine has already been returned once. By you. Tomorrow.
```

## Run it

```sh
python3 main.py
```

The label is written to `$MAKEFUN_OUTPUT_DIR/entry.txt`, or to
`/output/entry.txt` when that variable is not set. The output file is
created with mode `0644`, and running the program twice produces
byte-identical output.

## Requirements

Python 3.10 or later. No third-party packages — the standard library
is all it needs.

## License

MIT. See [LICENSE](LICENSE).
