from aiogram import executor
from src.dispatcher import dp
import src.handlers as handlers


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)