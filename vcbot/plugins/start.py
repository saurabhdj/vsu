from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from config import BOT_USERNAME


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, m: Message):
    if m.chat.type == "private":
        await m.reply_text(
            f"✨ **Hello there, I am a telegram group video streaming bot.**\n\n💭 **I was created to stream videos in group "
            f"video chats easily.🏻",
            reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/VeezSupportGroup"),
                    InlineKeyboardButton(
                        "📣 Channel", url="https://t.me/levinachannel")
                ],[
                    InlineKeyboardButton(
                        "👩🏻‍💻 Developer", url="https://t.me/dlwrml")
                ]]
            ))
