from callsmusic.callsmusic import client as USER

from pyrogram import filters

from pyrogram.types import Chat, Message, User

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)

async def pmPermit(client: USER, message: Message):

  await USER.send_message(message.chat.id,"**Zero investment and Earn Unlimited** \n https://groww.app.link/refe/r-k1852817 \n use the above link to install Groww App. \n 1. Install the app using above link. \n 2. Create an account. \n 3. Add Bank Account successfully. \4. Start reffering to your friends. You'll earn ₹100 for each successfull referes. \n More Earning methods comming soon without any investment.")

  return
