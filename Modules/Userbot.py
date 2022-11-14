
import os
import sys
import asyncio
import datetime
import time
from config import bot
from config import (HNDLR, SUDO_USERS, ALIVE_PIC, ALIVE_MSG, PING_MSG, __version__, start_time)
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram import __version__ as pyro_vr             
                

pongg = PING_MSG if PING_MSG else "sʜᴇʀɪғ ɪs ᴏɴ ғɪʀᴇ"
KAAL_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/3cb0edbe9c73edaa676d4.jpg"
Alivemsg = ALIVE_MSG if ALIVE_MSG else "sʜᴇʀɪғ ɪs ᴏɴʟɪɴᴇ ɴᴏᴡ"


manjeet = f"⁂ {Alivemsg} ⁂\n\n"
manjeet += f"━────────────────━\n"
manjeet += f"➠ **Python version** : `3.10.4`\n"
manjeet += f"➠ **Pyrogram version** : `{pyro_vr}`\n"
manjeet += f"➠ **version** : `{__version__}`\n"
manjeet += f"➠ **Kali Linux** : `Yes`\n"
manjeet += f"➠ **Database** : `Mongo atlas`\n"
manjeet += f"➠ **Database Status ** : `Functional`\n"
manjeet += f"➠ **current Branch** : `Master`\n"
manjeet += f"➠ **VC Modulesc** : `Allow`\n"
manjeet += f"➠ **Channel** : [Updates](t.me/Sherif_World)\n"
manjeet += f"➠ **Group** : [Support](https://t.me/+vrllWKqGDHxmNWQ0)\n"
manjeet += f"━────────────────━\n\n"
manjeet += f"• **Repo** : [Click here](https://github/Sherif-Sami/Music)\n"
manjeet += f"• **Commands** : [Click here](t.me/Sherif_Music/2)\n"


async def get_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    hmm = len(time_list)
    for x in range(hmm):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "
    time_list.reverse()
    up_time += ":".join(time_list)
    return up_time



@Client.on_message(filters.user(SUDO_USERS) & filters.command(["ping"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["ping"], prefixes=HNDLR))
async def ping(_, e: Message):       
      start = datetime.datetime.now()
      uptime = await get_time((time.time() - start_time))
      Fuk = await e.reply("**Pong !!**")
      end = datetime.datetime.now()
      ms = (end-start).microseconds / 1000
      await Fuk.edit_text(f"⌾ {pongg} ⌾ \n\n ༝ ᴘɪɴɢ: `{ms}` ᴍs \n ༝ ᴜᴘᴛɪᴍᴇ: `{uptime}` \n ༝ ᴠᴇʀsɪᴏɴ: `{__version__}`")




@Client.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["alive"], prefixes=HNDLR))
async def alive(xspam: Client, e: Message):
       if ".jpg" in KAAL_PIC or ".png" in KAAL_PIC:
              await xspam.send_photo(e.chat.id, KAAL_PIC, caption=manjeet)
       if ".mp4" in KAAL_PIC or ".MP4," in KAAL_PIC:
              await xspam.send_video(e.chat.id, KAAL_PIC, caption=manjeet)






@Client.on_message(filters.user(SUDO_USERS) & filters.command(["help", "cmds"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["help", "cmds"], prefixes=HNDLR))
async def restart_bot(_, message: Message):
    msg = await message.reply("`restarting bot...`")
    args = [sys.executable, "main.py"]
    await msg.edit("🕹 Commands of Sherif Userbot/n/n━────────────────━
skip - To skip the song
end - To end the song
resume - To resume the song
play - To play any song in VC
vplay - To play and video in VC
playform - To change playing data
playlist,queue- To cheçk waiting song
song - To get a song
vsong- To get a video song
broadcast,gcast - For broadcast msg
dmraid - For dm raid
dm - for dm raid
dmspam - For dm spam
kickall - For kickall members
deplayspam - To deplay any spam
pornspam - For porn spam
raid - For raid 
fspam - For fast spam
ping - To cheçk ping
alive - For check bot alive
restart - To restart the bot
git <Username> - To cheçk GitHub
id - To get group id
info - To cheçk information
join<username>- To join group or channel
leave <username>- To leave group or channel
mute - To mute someone
pin - To pin something
setpic - To set any pic in profile
setname - To set profile name
setbio - To set a bio
purge - To purge msg
stats- To cheçk user stats
tm - To make picture into link
tts - msg change into voice msg
unpin- To unpin msg
inviteall - For member adding
━────────────────━/n/n👨‍💻 Source by : @Sherif_Sami
📨 Trust guide : @Trust_Sherif
© Copy rights : @Sherif_World")
    execle(sys.executable, *args, environ)
    return
            
