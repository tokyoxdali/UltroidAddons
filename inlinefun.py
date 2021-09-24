#
# Ultroid - UserBot
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
# .tweet made for ultroid

# .uta ported from Dark-Cobra

"""
✘ Commands Available -

• `{i}uta <search query>`
    Inline song search and downloader.

• `{i}doge <search query>`
    Create a doge meme sticker.

• `{i}gglax <query>`
    Create google search sticker with text.

• `{i}stic <emoji>`
    Get random stickers from emoji.

• `{i}frog <text>`
    make text stickers.

• `{i}tweet <text>`
    make twitter posts.
"""

import random

from plugins.stickertools import deEmojify
from telethon.errors import (ChatSendInlineForbiddenError,
                             ChatSendStickersForbiddenError)

from . import *


@ultroid_cmd(pattern="tweet ?(.*)")
async def tweet(e):
    wai = await eor(e, "`Processing...`")
    text = e.pattern_match.group(1)
    if not text:
        return await wai.edit("`Give me Some Text !`")
    try:
        results = await e.client.inline_query("twitterstatusbot", text)
        await results[0].click(
            e.chat_id,
            silent=True,
            hide_via=True,
        )
        await wai.delete()
    except ChatSendStickersForbiddenError:
        await wai.edit("Sorry boss, I can't send Sticker Here !!")
    except Exception as m:
        await eor(e, str(m))


@ultroid_cmd(pattern="stic ?(.*)")
async def tweet(e):
    if len(e.text) > 5 and e.text[5] != " ":
        return
    wai = await eor(e, "`Processing...`")
    text = e.pattern_match.group(1)
    if not text:
        return await wai.edit("`Give me Some Emoji !`")
    try:
        results = await e.client.inline_query("sticker", text)
        num = random.randrange(0, len(results) - 1)
        await results[num].click(
            e.chat_id,
            silent=True,
            hide_via=True,
        )
        await wai.delete()
    except ChatSendStickersForbiddenError:
        await wai.edit("Sorry boss, I can't send Sticker Here !!")


@ultroid_cmd(pattern="doge ?(.*)")
async def doge_sticker(e):
    wai = await eor(e, "`Processing...`")
    text = e.pattern_match.group(1)
    if not text:
        return await wai.edit("`Give me Some Text !`")
    try:
        results = await e.client.inline_query("dogestickerbot", text)
        await results[0].click(
            e.chat_id,
            silent=True,
            hide_via=True,
        )
        await wai.delete()
    except ChatSendStickersForbiddenError:
        await wai.edit("Sorry boss, I can't send Sticker Here !!")
    except Exception as m:
        await eor(e, str(m))


@ultroid_cmd(pattern="gglax ?(.*)")
async def gglax_sticker(e):
    wai = await eor(e, "`Processing...`")
    text = e.pattern_match.group(1)
    if not text:
        return await wai.edit("`Give me Some Text !`")
    try:
        results = await e.client.inline_query("googlaxbot", text)
        await results[0].click(
            e.chat_id,
            silent=True,
            hide_via=True,
        )
        await wai.delete()
    except ChatSendStickersForbiddenError:
        await wai.edit("Sorry boss, I can't send Sticker Here !!")
    except Exception as m:
        await eor(e, str(m))


@ultroid_cmd(pattern="frog ?(.*)")
async def honkasays(e):
    wai = await eor(e, "`Processing...`")
    text = e.pattern_match.group(1)
    if not text:
        return await wai.edit("`Give Me Some Text !`")
    try:
        if not text.endswith("."):
            text = text + "."
        if len(text) <= 9:
            results = await e.client.inline_query("honka_says_bot", text)
            await results[2].click(
                e.chat_id,
                silent=True,
                hide_via=True,
            )
        elif len(text) >= 14:
            results = await e.client.inline_query("honka_says_bot", text)
            await results[0].click(
                e.chat_id,
                silent=True,
                hide_via=True,
            )
        else:
            results = await e.client.inline_query("honka_says_bot", text)
            await results[1].click(
                e.chat_id,
                silent=True,
                hide_via=True,
            )
        await wai.delete()
    except ChatSendStickersForbiddenError:
        await wai.edit("Sorry boss, I can't send Sticker Here !!")


@ultroid_cmd(pattern="uta ?(.*)")
async def nope(doit):
    ok = doit.pattern_match.group(1)
    a = await eor(doit, "`Processing...`")
    if not ok:
        if doit.is_reply:
            (await doit.get_reply_message()).message
        else:
            return await eor(
                doit,
                "`Sir please give some query to search and download it for you..!`",
            )
    sticcers = await doit.client.inline_query("Lybot", f"{(deEmojify(ok))}")
    await sticcers[0].click(
        doit.chat_id,
        reply_to=doit.reply_to_msg_id,
        silent=True if doit.is_reply else False,
        hide_via=True,
    )
    await a.delete()
