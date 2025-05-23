# logger.py
from loguru import logger
import sys

# Удаляем стандартный обработчик (если не нужен)
logger.remove()

# Добавляем свой формат с временем и сообщением
logger.add(
    sink=sys.stdout,  # Вывод в консоль (можно добавить файл)
    format="<green>{time:HH:mm:ss}</green> - <red>{level}</red>: <level>{message}</level>",
    colorize=True,  # Сохраняем цвета
    level="DEBUG",   # Минимальный уровень логирования
)
