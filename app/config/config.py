from pathlib import Path

# корневая папка проекта - app/
BASE_DIR = Path(__file__).resolve().parent.parent
# папка с логами
LOG_DIR = BASE_DIR.joinpath('logs').joinpath('log.json')
# папка с изображением и инструкциями
DOC_DIR = BASE_DIR.joinpath('misc').joinpath('instruction.txt')