# pytel < https://t.me/kastaid >
# Copyright (C) 2023-present kastaid
#
# This file is a part of < https://github.com/kastaid/pytel/ >
# Please read the GNU Affero General Public License in
# < https://github.com/kastaid/pytel/blob/main/LICENSE/ >

from asyncio import sleep, gather
from pyrogram.raw.functions.messages import (
    DeleteHistory,)
from . import (
    eor,
    plugins_helper,
    px,
    extract_user,
    pytel,
    replied,
    random_prefixies,)


@pytel.instruction(
    [
        "sang",
        "sg",
    ],
    outgoing=True,
)
async def _sangmata(client, message):
    user_id = await extract_user(
        client, message
    )
    if not user_id:
        await eor(
            message,
            text="Unable to find user.",
        )
        return
    x = await eor(
        message,
        text="Processing...",
    )
    sang = "@sangmata_bot"
    await client.unblock_user(sang)
    await client.send_message(
        sang, user_id
    )
    await sleep(3)
    async for s in client.search_messages(
        sang
    ):
        try:
            if s.text:
                await gather(
                    s.copy(
                        message.chat.id,
                        reply_to_message_id=replied(
                            message
                        ),
                    ),
                    x.delete(),
                )
                return
        except BaseException as excp:
            await eor(
                x,
                text=f"Error: {excp}",
            )
    info = await client.resolve_peer(
        sang
    )
    return await client.invoke(
        DeleteHistory(
            peer=info,
            max_id=0,
            revoke=True,
        )
    )


plugins_helper["sangmata"] = {
    f"{random_prefixies(px)}sg / sang [id/username/reply]": "To check the previous username. ( If there are )",
}
