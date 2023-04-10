from pathlib import Path

# корневая папка проекта - app/
BASE_DIR = Path(__file__).resolve().parent.parent
# папка с логами
LOG_DIR = BASE_DIR.joinpath('logs').joinpath('log.json')
# путь к базе данных
DB_PATH = BASE_DIR.joinpath('db').joinpath('data.sqlite')