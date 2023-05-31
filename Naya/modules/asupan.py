import random
from random import choice

from pyrogram import enums, filters
from pyrogram.enums import MessagesFilter

from Naya import *


@app.on_message(filters.command("asupan"))
async def _(client, message):
    y = await eor(message, text="<b>🔍 Mencari Video Asupan...</b>")
    try:
        asupannya = []
        async for asupan in client.search_messages(
            "@AsupanNyaSaiki", filter=MessagesFilter.VIDEO
        ):
            asupannya.append(asupan)
        video = random.choice(asupannya)
        await video.copy(
            message.chat.id,
            caption=f"<b>Asupan By <a href=tg://user?id={app.me.id}>{app.me.first_name} {app.me.last_name or ''}</a></b>",
            reply_to_message_id=message.id,
        )
        await y.delete()
    except Exception:
        await y.edit("<b>Video tidak ditemukan silahkan ulangi beberapa saat lagi</b>")


@app.on_message(filters.command("cewe"))
async def _(client, message):
    y = await eor(message, text="<b>🔍 Mencari Ayang...</b>")
    try:
        ayangnya = []
        async for ayang in client.search_messages(
            "@AyangSaiki", filter=MessagesFilter.PHOTO
        ):
            ayangnya.append(ayang)
        photo = random.choice(ayangnya)
        await photo.copy(
            message.chat.id,
            caption=f"<b>Ayang By <a href=tg://user?id={app.me.id}>{app.me.first_name} {app.me.last_name or ''}</a></b>",
            reply_to_message_id=message.id,
        )
        await y.delete()
    except Exception:
        await y.edit("<b>Ayang tidak ditemukan silahkan ulangi beberapa saat lagi</b>")


@app.on_message(filters.command("cowo"))
async def _(client, message):
    y = await eor(message, text="<b>🔍 Mencari Ayang...</b>")
    try:
        ayang2nya = []
        async for ayang2 in client.search_messages(
            "@Ayang2Saiki", filter=MessagesFilter.PHOTO
        ):
            ayang2nya.append(ayang2)
        photo = random.choice(ayang2nya)
        await photo.copy(
            message.chat.id,
            caption=f"<b>Ayang By <a href=tg://user?id={app.me.id}>{app.me.first_name} {app.me.last_name or ''}</a></b>",
            reply_to_message_id=message.id,
        )
        await y.delete()
    except Exception:
        await y.edit("<b>Ayang tidak ditemukan silahkan ulangi beberapa saat lagi</b>")


@app.on_message(filters.command("anime"))
async def anim(client, message):
    iis = await eor(message, text="🔎 <code>Search Anime...</code>")
    await message.reply_photo(
        choice(
            [
                jir.photo.file_id
                async for jir in client.search_messages(
                    "@animehikarixa", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"**Upload by {app.me.mention}**",
    )

    await iis.delete()


@app.on_message(filters.command("anime2"))
async def nimek(client, message):
    erna = await eor(message, text="🔎 <code>Search Anime...</code>")
    await message.reply_photo(
        choice(
            [
                tai.photo.file_id
                async for tai in client.search_messages(
                    "@Anime_WallpapersHD", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"**Upload by {app.me.mention}**",
    )

    await erna.delete()


@app.on_message(filters.command("pap"))
async def bugil(client, message):
    kazu = await eor(message, text="🔎 <code>Nih PAP Nya...</code>")
    await message.reply_photo(
        choice(
            [
                lol.photo.file_id
                async for lol in client.search_messages(
                    "@mm_kyran", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption="<b>Buat Kamu...</b>",
    )

    await kazu.delete()


__MODULE__ = "Asupan"
__HELP__ = f"""
/asupan - Untuk mengirim video asupan random. 

/cewe - Untuk mengirim photo cewek random.
           
/cowo - Untuk mengirim photo cowok random.

/anime - Untuk mengirim photo anime random.
           
/anime2 - Untuk mengirim photo anime random.

/pap - Untuk mengirim photo pap random.
"""