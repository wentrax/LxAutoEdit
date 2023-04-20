import os, asyncio, logging
from pyrogram.errors import FloodWait
from pyrogram import Client, filters, enums
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

media_filter = filters.document | filters.video 

@Client.on_message(filters.chat(-1001667023505) & media_filter)
async def forward(bot, update):
    try:      
        await bot.copy_message(
            chat_id=-1001563784107, 
            from_chat_id=-1001667023505, 
            message_id=update.id, 
            caption=f"**{update.caption}**" + "\n\n" + "**@WebxZone**",          
            parse_mode=enums.ParseMode.MARKDOWN                     
        )
    except FloodWait as e:
        await asyncio.sleep(e.value)