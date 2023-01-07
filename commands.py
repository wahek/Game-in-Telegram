import calculation
import view

from bot_config import dp, bot
from aiogram import types


@dp.message_handler(commands=['start'])
async def start_bot(messege: types.Message):
    await bot.send_message(messege.from_id, text=f'{messege.from_user.first_name}'
                                                 f', привет! Я вижу ты хочешь сыграть в конфеты. '
                                                 f'Если ты хочешь чтобы я объяснил правила, напиши /help '
                                                 f'или давай начинать играть, я жду от тебя цифру')
    print(f'{messege.from_user.id} - {messege.from_user.username}')
    print(f'{messege.from_user.first_name} - {messege.from_user.last_name}')


@dp.message_handler(commands=['help'])
async def rules_bot(messege: types.Message):
    await bot.send_message(messege.from_id, text='Правила простые: ты играешь против компьютера. Право первого хода '
                                                 'за тобой, затем ходитесь по очереди. '
                                                 'На столе лежат 150 конфет, за один ход можно взять максимум 28 '
                                                 'конфет. Тот кто делает последний ход, '
                                                 'тот забирает все конфеты своего оппонента. Попробуй забрать все '
                                                 'конфеты')


# @dp.message_handler(commands=['go'])
# async def choice_bot(messege: types.Message):
#     global choice
#     choice = calculation.choice()
#     await bot.send_message(messege.from_id, text=f'Подкидываю монетку\n{view.print_choice(choice)}')
#     return choice

@dp.message_handler()
async def candies_bot(message: types.Message):
    # global choice

    if 0 < int(message.text) < 29:
        calculation.set_total(calculation.candies_play_user(message.text))
        await bot.send_message(message.from_id,
                               text=f'{message.from_user.first_name} забирает {message.text} конфет. '
                                    f'Осталось {calculation.get_total()} конфет')
        if calculation.get_total() < 0:
            await bot.send_message(message.from_id, text='А вот и победитель!!!, ты забираешь все конфеты')
            calculation.set_total(150)
        else:
            if calculation.get_total() > 58:
                await bot.send_message(message.from_id,
                                       text=f'Бот забирает {calculation.candies_play_bot_random()} конфет. '
                                            f'Осталось {calculation.get_total()} конфет')
            else:
                if calculation.get_total() > 28:
                    await bot.send_message(message.from_id,
                                           text=f'Бот забирает {calculation.candies_bot_win()} конфет. '
                                                f'Осталось {calculation.get_total()} конфет')
                else:
                    await bot.send_message(message.from_id,
                                           text=f'Бот забирает {calculation.get_total()} конфет. '
                                                f'Осталось {calculation.set_total(0)} конфет '
                                                f'Ха, Бот тебя обыграл, не плачь, попробуй ещё раз')
                    calculation.set_total(150)

    else:
        await bot.send_message(message.from_id, text=f'{message.from_user.first_name} Не жадничай, '
                                                     f'у нас тут всё по правилам')
