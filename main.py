import asyncio, json
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle

async def main():
    cookies = json.loads(open("./cookies.json", encoding="utf-8").read())  # might omit cookies option
    bot = await Chatbot.create(cookies=cookies)
    response = await bot.ask(prompt="""
 请将 ["steam" ,"抖音充值","阴阳师卡密","全民k歌卡密",""苹果卡中国区, "steam卡密"] 翻译成用于在礼品卡网站上显示的常见英文名 ，并以数组形式返回给我
    """, conversation_style=ConversationStyle.creative, simplify_response=True)
    print(json.dumps(response, indent=2)) # Returns
    await bot.close()

if __name__ == "__main__":
    asyncio.run(main())