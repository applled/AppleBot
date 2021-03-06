""" Manter os crΓ©ditos | @applled - Info de Animes """

from pyrogram.errors import BadRequest

from userge import Message, userge


@userge.on_cmd(
    "ani",
    about={
        "header": "MΓ³dulo criado pelo @applled - Assista Animes Legendados",
        "como usar": "{tr}ani nome da pesquisa",
    },
    del_pre=True,
    allow_channels=False,
)
async def appled_tweet(message: Message):
    await message.edit(f"πΏπππππππ πππππ, πππππππππππ...", del_in=3, log=__name__)
    reply = message.reply_to_message
    reply_id = reply.message_id if reply else None
    if message.input_str:
        input_query = message.input_str
    elif reply:
        if reply.text:
            input_query = reply.text
        elif reply.caption:
            input_query = reply.caption
    if not input_query:
        return await message.err("Lembre-se de fazer o comando + pesquisa", del_in=5)

    x = await userge.get_inline_bot_results("@AniCatBot ", input_query)
    try:
        await message.delete()
        await userge.send_inline_bot_result(
            chat_id=message.chat.id,
            query_id=x.query_id,
            result_id=x.results[0].id,
            reply_to_message_id=reply_id,
            hide_via=True,
        )
    except (IndexError, BadRequest):
        await message.err(
            "EntΓ£o, vocΓͺ precisa digitar alguma coisa apΓ³s o comando, tΓ‘ bom? E se for pornogrΓ‘fico, vΓ‘ se tratar.",
            del_in=5,
        )
