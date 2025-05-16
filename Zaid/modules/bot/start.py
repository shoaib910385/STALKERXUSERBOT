from Zaid import app, API_ID, API_HASH
from config import ALIVE_PIC
from pyrogram import filters
import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import * 

PHONE_NUMBER_TEXT = (
    "**╭────── ˹ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ˼ ⏤͟͟͞͞★**\n**┆◍ ʜᴇʏ, ɪ ᴀᴍ : [˹𝐒ᴛᴀʟᴋᴇʀ ✘ 𝐇ᴏꜱᴛᴇʀ˼](https://t.me/Stalkeruserbot) **\n**┆● sᴛᴀʟᴋᴇʀ ᴜsᴇʀʙᴏᴛ Vᴇʀsɪᴏɴ :** `2.1.3`\n**┊● Pᴏᴡᴇʀғᴜʟ & Usᴇғᴜʟ Usᴇʀʙᴏᴛ**\n**╰─────────────────────────**\n**──────────────────────────**\n**❖ Hᴏᴡ Tᴏ Usᴇ Tʜɪs Bᴏᴛ - [Cʟɪᴄᴋ Hᴇʀᴇ](https://t.me/TIDALXUPDATES/19) **\n**──────────────────────────**\n**❖ Sᴇssɪᴏɴs Gᴇɴ Bᴏᴛ ⁚ [Sᴇssɪᴏɴ-Bᴏᴛ](https://t.me/SessionStringZBot) **\n**──────────────────────────**\n**❖ Cʟᴏɴᴇ Bᴏᴛ  ⁚ /clone [ Sᴛʀɪɴɢ Sᴇssɪᴏɴ ]**\n**──────────────────────────**\n**❖ Uᴘᴅᴀᴛᴇ ⏤͟͟͞͞  [❖ ∣ sᴛᴀʟᴋᴇʀ ᴜsᴇʀʙᴏᴛ ∣ ❖](https://t.me/lll_drx_network_lll) **\n**──────────────────────────**"
)

@app.on_message(filters.user(OWNER_ID) & filters.command("start"))
async def hello(client: app, message):
    buttons = [
              [
                  InlineKeyboardButton(text="🍁 sᴇssɪᴏɴ ɢᴇɴ ʙᴏᴛ 🍁️", url="https://t.me/SessionStringZBot"),
              ],
              [
                  InlineKeyboardButton(text="🌿 ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ 🌿", url="https://t.me/https://t.me/TIDALXUPDATES/19"),
              ],
              [
                  InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ ❄️️️", url="https://t.me/drx_supportchat"),
                  InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ ❄️️️", url="https://t.me/lll_drx_network_lll"),
              ],
              [
                  InlineKeyboardButton("𝆺𝅥⃝ᶦϻ‌ ɴᴏᴛ 𝙎𝙏𝚲𝙇𝙆𝙀𝙍", url="https://t.me/hehe_stalker"),
              ],
              ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_photo(message.chat.id, ALIVE_PIC, caption=PHONE_NUMBER_TEXT, reply_markup=reply_markup)

# © By Shashank shukla Your motherfucker if uh Don't gives credits.
@app.on_message(filters.user(OWNER_ID) & filters.command("clone"))
async def clone(bot: app, msg: Message):
    chat = msg.chat
    text = await msg.reply("❍ HOW TO USE \n\n𔓕 /clone session \n𔓕 /clone save msg code")
    cmd = msg.command
    phone = msg.command[1]
    try:
        await text.edit("❖ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ᴀ ᴍɪɴᴜᴛᴇ")
                   # change this Directry according to ur repo
        client = Client(name="Melody", api_id=API_ID, api_hash=API_HASH, session_string=phone, plugins=dict(root="Zaid/modules"))
        await client.start()
        user = await client.get_me()
        await msg.reply(f"❖ ɴᴏᴡ ʏᴏᴜ ᴀʀᴇ ʀᴇᴀᴅʏ ᴛᴏ ғɪɢʜᴛ\n\n❍ [❖ │ ɴᴏᴛ 𝙎𝙏𝚲𝙇𝙆𝙀𝙍 │ ❖](https://t.me/hehe_stalker)\n\n❖ {user.first_name}")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")
