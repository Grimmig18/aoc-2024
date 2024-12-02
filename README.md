# aoc-2024
First 11 days of AOC (am on vacation afterwards)

## How to run
To run a specific file/program you can either use the `Python AOC day` debug configuration in `.vscode/launch.json`:
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python AOC day",
            "type": "debugpy",
            "request": "launch",
            "program": "${file}",
            "env": { "PYTHONPATH": "${workspaceFolder}"}
        }
    ]
}
```
... or run python from your preferred CLI using:
```bash
py -m aoc-2024.DAY_FOLDER.FILE
```
substituting `DAY_FOLDER` and `FILE` with the respective folder and file names.
This command must be run from the `PARENT` directory of the `aoc-2024` folder
```
PARENT
└- aoc-2024
   ├-parser
   ├-day_0_setup
   ├-day_1_location_ids
   ├-...
```

## Clutter
Because of modularization there are a lot of `.pycache` folders and `__init__.py` files.
To configure VS Code to not display them, add `**/__pycache__` and `**/__init__.py` to your `Files: Exclude` settings (`files.exclude`).
