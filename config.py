#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/YukkiChatBot >.
#
# This file is part of < https://github.com/TeamYukki/YukkiChatBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiChatBot/blob/master/LICENSE >
#
# All rights reserved.
#

from os import getenv

from dotenv import load_dotenv

load_dotenv()

# Get it from my.telegram.org
API_ID = int(getenv("API_ID", "16228908"))
API_HASH = getenv("API_HASH", "1e0ebcbec6fb07e5064f54797e0cadb5" )

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "6200405706:AAFEydrsmPn7vdUgC_huZC-1GEU2LyJwfBA")

# SUDO USERS
SUDO_USER = list(
    map(int, getenv("SUDO_USER", "5012406813").split())
)  # Input type must be interger

# You'll need a Private Group ID for this.
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001891084724"))

# Message to display when someone starts your bot
PRIVATE_START_MESSAGE = getenv(
    "PRIVATE_START_MESSAGE", 
    "اهلا بك عزيزي في بوت درايف",
)

# Database to save your chats and stats... Get MongoDB:-  https://notreallyshikhar.gitbook.io/yukkimusicbot/deployment/mongodb#4.-youll-see-a-deploy-cloud-database-option.-please-select-shared-hosting-under-free-plan-here
MONGO_DB_URI = getenv("MONGO_DB_URI", None)
