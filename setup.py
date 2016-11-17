import cx_Freeze


executables = [cx_Freeze.Executable("main.py")]
cx_Freeze.setup(
    name="Snakeion",
    options={"build_exe":{"packages":["pygame"], "include_files":["images/apple.png", "images/snakeBd.png", "images/snakebg.png", "images/snakeHead.png"]}},
    description="Snake Game",
    executables=executables
)
