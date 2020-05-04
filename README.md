# Ludum Dare 46

Theme: Keep it Alive

The purpose of this game jam was to create a game from scratch in 72 hours.

I decided to use Python. 

## How to launch the game

You need python 3+ in your PATH, and `git` if you want to clone the repository.

Clone (or download and extract) the repository somewhere on your computer:

```bash
git clone https://github.com/Jayque17/ludum_dare46
```

Or download link: https://github.com/Jayque17/ludum_dare46/archive/master.zip

Place yourself in the `gamejam_keep_it_alive subfolder`:

```bash
cd ludum_dare46/gamejam_keep_it_alive
```

Create a python virtual environment inside that folder:
```bash
python -m venv .venv
```

Activate the virtual env and install dependencies:

On linux:
```bash
source .venv/bin/activate
```

On windows (cmd.exe console):
```bash
.venv\Scripts\activate.bat
```

On windows (bash console):
```bash
source .venv/Scripts/activate.bat
```

Install dependencies into the virtual env:
```bash
pip install -r requirements.txt
```

And run the game:
```bash
python -m Fly_away
```

## How to play the game

To move the butterfly you must use the arrow keys.

To quit the game use the Escape key.

You can use the Space key to hide the control indications.
