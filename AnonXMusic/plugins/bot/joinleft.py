from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from config import BOTADDLOGS as BOTADDLOGS
from AnonXMusic import app
from AnonXMusic.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
    delete_served_chat,
    is_served_chat,
)
from pyrogram.enums import MessageEntityType
from pyrogram.types import Message, User, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery


async def new_message(chat_id: int, message: str, reply_markup=None):
    await app.send_message(chat_id=chat_id, text=message, reply_markup=reply_markup)

@app.on_message(filters.new_chat_members)
async def on_new_chat_members(client: Client, message: Message):
    if (await client.get_me()).id in [user.id for user in message.new_chat_members]:
        added_by = message.from_user.mention if message.from_user else "ᴜɴᴋɴᴏᴡɴ ᴜsᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}"
        chat_id = message.chat.id
        am = f"✫ <b><u>ɴᴇᴡ ɢʀᴏᴜᴘ</u></b> :\n\nᴄʜᴀᴛ ɪᴅ : {chat_id}\nᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ : {username}\nᴄʜᴀᴛ ᴛɪᴛʟᴇ : {title}\n\nᴀᴅᴅᴇᴅ ʙʏ : {added_by}"
        reply_markup = InlineKeyboardMarkup([
    [
        InlineKeyboardButton(
            message.from_user.first_name,
            user_id=message.from_user.id
        )
    ]
])

        await add_served_chat(chat_id)
        await new_message(BOTADDLOGS, am, reply_markup)

@app.on_message(filters.left_chat_member)
async def on_left_chat_member(client: Client, message: Message):
    if (await client.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "ᴜɴᴋɴᴏᴡɴ ᴜsᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}"
        chat_id = message.chat.id
        ambye = f"✫ <b><u>ʟᴇғᴛ ɢʀᴏᴜᴘ</u></b> :\n\nᴄʜᴀᴛ ɪᴅ : {chat_id}\nᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ : {username}\nᴄʜᴀᴛ ᴛɪᴛʟᴇ : {title}\n\nʀᴇᴍᴏᴠᴇᴅ ʙʏ : {remove_by}"
        reply_markup = InlineKeyboardMarkup([
    [
        InlineKeyboardButton(
            message.from_user.first_name,
            user_id=message.from_user.id
        )
    ]
])

        await delete_served_chat(chat_id)
        await new_message(BOTADDLOGS, ambye, reply_markup)
