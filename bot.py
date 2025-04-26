from aiogram import Bot, Dispatcher, types, executor
import random
import asyncio
import os

# Вместо 'YOUR_TOKEN' вставь токен, который ты получишь в BotFather
TOKEN = '8037185225:AAEdwbiVKyiTmdoH9j-dCSQ7J_Oh4SNKlSo'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Твои цитаты мотивации
motivations = [
    "Ты кузнец своей судьбы. 🔥",
    "Нет ничего невозможного. 🏆",
    "Боль временна, гордость вечна. ⚡",
    "Сегодня ты строишь своё великое завтра. 🚀",
]

# Твои упражнения для роста
growth_tips = [
    "Повисания на турнике 3 раза по 30 секунд.",
    "Йога растяжка 'собака мордой вниз'.",
    "Лечь спать до 22:30 для повышения гормона роста.",
    "Приём цинка и витамина D перед сном."
]

# План на день
daily_plan = """
🌅 Утро:
- Подъём 6:30
- Холодная вода на лицо
- Лёгкая зарядка 5 минут
- Завтрак + витамины

🧠 Учёба:
- Java теория + практика
- Английский Speaking
- Французский: базовые фразы
- Немецкий: базовые слова
- Дикция и голос
- Упражнения для роста
- 5-минутные перерывы каждые 50 минут

🌙 Вечер:
- Прогулка 15 минут
- Медитация 5 минут
- Дневник успеха
- Сон в 22:30
"""

# Опыт за выполнение задач
xp_points = 0

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! 🚀 Добро пожаловать в свой путь к успеху. Готов побеждать каждый день? 🔥\n\nНабери /plan чтобы увидеть план на день!")

@dp.message_handler(commands=['plan'])
async def plan(message: types.Message):
    await message.answer(daily_plan)

@dp.message_handler(commands=['tasks'])
async def tasks(message: types.Message):
    await message.answer("🛡️ Твои задачи на сегодня:\n- Java 3 часа\n- Английский 2 часа\n- Французский 45 мин\n- Немецкий 45 мин\n- Дикция 30 мин\n- Рост упражнения 30 мин")

@dp.message_handler(commands=['xp'])
async def xp(message: types.Message):
    global xp_points
    xp_points += 10
    await message.answer(f"🔥 Ты заработал 10 XP! Твой общий опыт: {xp_points} XP")

@dp.message_handler(commands=['motivation'])
async def motivation(message: types.Message):
    quote = random.choice(motivations)
    await message.answer(quote)

@dp.message_handler(commands=['habitica'])
async def habitica(message: types.Message):
    await message.answer("🌟 В Habitica создай ежедневные задачи:\n- Java - 3 часа\n- Английский Speaking\n- Французский базовые фразы\n- Немецкий базовые слова\n- Дикция упражнения\n- Сон до 22:30\nНаграждай себя XP за каждую выполненную задачу!")

@dp.message_handler(commands=['stats'])
async def stats(message: types.Message):
    await message.answer(f"📈 Текущий опыт: {xp_points} XP\nПродолжай идти к победе!")

@dp.message_handler(commands=['growth'])
async def growth(message: types.Message):
    tip = random.choice(growth_tips)
    await message.answer(f"🌱 Совет по росту: {tip}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
