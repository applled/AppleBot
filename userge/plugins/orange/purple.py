""" MΓ³dulo criado pelo @applled - Inspirado na maravilhosa Purple <3 | Manter os crΓ©ditos para @applled """

import asyncio
import random

from userge import userge

CARREGADO = ("https://telegra.ph/file/d4eaad9d72a0c1f5fb676.gif",)


@userge.on_cmd("purple$", about={"header": "Quais as suas chances com a Purple?"})
async def purple_func(message):
    await message.client.get_user_dict(message.from_user.id)
    purp = f"""{random.choice(CARREGADO)}"""
    gerando = ["Aguarde..."]
    purple = f"""
      **   {(await userge.get_users(message.reply_to_message.from_user.id)).first_name}**
      ππππ πππππππ πππ π **Purple**
      ββββββββ
      **π€‘ Radar da Friendzone:** {random.choice(range(0,1000))}%
      **π₯Ί Chances de ganhar block:** {random.choice(range(0,10))} de 10
      **π Te acha guei:** {random.choice(range(50,100))}%
      **π Suas chances sΓ£o:** {random.choice(range(0,100))}%
       β°β’  <i>De ser Verdade ou Mentira</i>

      ββββββββ
      Se nΓ£o concordou, clique em /kickme
      π PB - @iamakima | @twapple
      <code>Teste aprovado pela Anatel Astral</code>
      """
    max_ani = len(gerando)
    for i in range(max_ani):
        await asyncio.sleep(1)
        await message.edit(gerando[i % max_ani], del_in=1)
        await message.client.send_animation(
            message.chat.id,
            animation=purp,
            caption=purple,
        )
