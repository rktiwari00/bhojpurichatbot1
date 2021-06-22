from callsmusic.callsmusic import client as USER

from pyrogram import filters

from pyrogram.types import Chat, Message, User

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)

async def pmPermit(client: USER, message: Message):

  await USER.send_message(message.chat.id,"Please do not messege me. I am busy right now./n If you want to support me then my UPI ID is ```rktiwari00@ybl```.")

  return
