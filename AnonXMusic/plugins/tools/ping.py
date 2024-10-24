from pyrogram import Client, filters
import psutil
import time
from datetime import timedelta
import logging
from AnonXMusic import app
from config import PING_IMG_URL

@app.on_message(filters.command(["ping", "alive"]))
async def ping(client, message):
    try:
        uptime_seconds = time.time() - bot_start_time
        uptime = str(timedelta(seconds=int(uptime_seconds)))

        ram = psutil.virtual_memory()
        ram_usage = f"{ram.percent}% used ({ram.used / (1024 ** 3):.2f} GB of {ram.total / (1024 ** 3):.2f} GB)"

        cpu_usage = f"{psutil.cpu_percent()}%"

        disk = psutil.disk_usage('/')
        disk_usage = f"{disk.percent}% used ({disk.used / (1024 ** 3):.2f} GB of {disk.total / (1024 ** 3):.2f} GB)"

        response = f"{client.mention} is pinging...<a href='{PING_IMG_URL}'>.</a>"
        reply = await message.reply(response)

        stats_message = (
            f"System Stats\n"
            f"Uptime: {uptime}\n"
            f"RAM Usage: {ram_usage}\n"
            f"CPU Usage: {cpu_usage}\n"
            f"Disk Usage: {disk_usage}\n"
        )

        await message.reply(stats_message)  

        await message.reply_photo(
            photo=PING_IMG_URL,
            caption=stats_message
        )

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        error_message = "An error occurred while retrieving system stats."
        await message.reply(error_message)