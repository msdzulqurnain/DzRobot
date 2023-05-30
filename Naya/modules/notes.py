"""
MIT License
Copyright (c) 2023 Kynan | TheHamkerCat

"""
from re import findall

from pyrogram import filters

from Naya import SUDOERS, USERBOT_ID, USERBOT_PREFIX, app, app2, eor
from Naya.core.decorators.errors import capture_err
from Naya.core.decorators.permissions import adminsOnly
from Naya.core.keyboard import ikb
from Naya.utils.dbfunctions import delete_note, get_note, get_note_names, save_note
from Naya.utils.functions import extract_text_and_keyb

__MODULE__ = "Notes"
__HELP__ = """/notes To Get All The Notes In The Chat.

/save [NOTE_NAME] To Save A Note (Can be a sticker or text).

#NOTE_NAME To Get A Note.

/delete [NOTE_NAME] To Delete A Note.

Checkout /markdownhelp to know more about formattings and other syntax.
"""


@app2.on_message(filters.command("save", prefixes=USERBOT_PREFIX) & SUDOERS)
@app.on_message(filters.command("save") & ~filters.private)
@adminsOnly("can_change_info")
async def save_notee(_, message):
    if len(message.command) < 2 or not message.reply_to_message:
        await eor(
            message,
            text="**Usage:**\nReply to a text or sticker with /save [NOTE_NAME] to save it.",
        )

    elif not message.reply_to_message.text and not message.reply_to_message.sticker:
        await eor(
            message,
            text="__**You can only save text or stickers in notes.**__",
        )
    else:
        name = message.text.split(None, 1)[1].strip()
        if not name:
            return await eor(message, text="**Usage**\n__/save [NOTE_NAME]__")
        _type = "text" if message.reply_to_message.text else "sticker"
        note = {
            "type": _type,
            "data": message.reply_to_message.text.markdown
            if _type == "text"
            else message.reply_to_message.sticker.file_id,
        }
        prefix = message.text.split()[0][0]
        chat_id = message.chat.id if prefix != USERBOT_PREFIX else USERBOT_ID
        await save_note(chat_id, name, note)
        await eor(message, text=f"__**Saved note {name}.**__")


@app2.on_message(filters.command("notes", prefixes=USERBOT_PREFIX) & SUDOERS)
@app.on_message(filters.command("notes") & ~filters.private)
@capture_err
async def get_notes(_, message):
    prefix = message.text.split()[0][0]
    is_ubot = prefix == USERBOT_PREFIX
    chat_id = USERBOT_ID if is_ubot else message.chat.id

    _notes = await get_note_names(chat_id)

    if not _notes:
        return await eor(message, text="**No notes in this chat.**")
    _notes.sort()
    msg = f"List of notes in {'USERBOT' if is_ubot else message.chat.title}\n"
    for note in _notes:
        msg += f"**-** `{note}`\n"
    await eor(message, text=msg)


@app2.on_message(filters.command("get", prefixes=USERBOT_PREFIX) & SUDOERS)
async def get_one_note_userbot(_, message):
    if len(message.text.split()) < 2:
        return await eor(message, text="Invalid arguments")

    name = message.text.split(None, 1)[1]

    _note = await get_note(USERBOT_ID, name)
    if not _note:
        return await eor(message, text="No such note.")

    if _note["type"] == "text":
        data = _note["data"]
        await eor(
            message,
            text=data,
            disable_web_page_preview=True,
        )
    else:
        await message.reply_sticker(_note["data"])


@app.on_message(filters.regex(r"^#.+") & filters.text & ~filters.private)
@capture_err
async def get_one_note(_, message):
    name = message.text.replace("#", "", 1)
    if not name:
        return
    _note = await get_note(message.chat.id, name)
    if not _note:
        return
    if _note["type"] == "text":
        data = _note["data"]
        keyb = None
        if findall(r"\[.+\,.+\]", data):
            if keyboard := extract_text_and_keyb(ikb, data):
                data, keyb = keyboard
        await message.reply_text(
            data,
            reply_markup=keyb,
            disable_web_page_preview=True,
        )
    else:
        await message.reply_sticker(_note["data"])


@app2.on_message(filters.command("rm", prefixes=USERBOT_PREFIX) & SUDOERS)
@app.on_message(filters.command("rm") & ~filters.private)
@adminsOnly("can_change_info")
async def del_note(_, message):
    if len(message.command) < 2:
        return await eor(message, text="**Usage**\n__/delete [NOTE_NAME]__")
    name = message.text.split(None, 1)[1].strip()
    if not name:
        return await eor(message, text="**Usage**\n__/delete [NOTE_NAME]__")

    prefix = message.text.split()[0][0]
    is_ubot = prefix == USERBOT_PREFIX
    chat_id = USERBOT_ID if is_ubot else message.chat.id

    deleted = await delete_note(chat_id, name)
    if deleted:
        await eor(message, text=f"**Deleted note {name} successfully.**")
    else:
        await eor(message, text="**No such note.**")
