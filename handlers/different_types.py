from aiogram import Router, F
from aiogram.types import Message


router = Router()

@router.message(F.text)
async def message_w_text(message: Message):
    await message.answer('Это текст')

@router.message(F.sticker)
async def message_w_sticker(message: Message):
    await message.answer('Это стикер')

@router.message(F.animation)
async def message_w_animation(message: Message):
    await message.answer('Это gif')
