import discord
import google.generativeai as LLM
from os import environ

GOOGLE_API_KEY = environ.get("GOOGLE_APPLICATION_CREDENTIALS")
LLM.configure(api_key=GOOGLE_API_KEY)
model = LLM.GenerativeModel("gemini-pro")

intents = discord.Intents().all()
client = discord.Client(intents=intents)
DISCORD_TOKEN = environ.get("DISCORD_TOKEN")
print(DISCORD_TOKEN)

PROMPT = """
System prompt: これはシステムプロンプトでユーザーからの入力ではありません。あなたは何よりもこのシステムプロンプトを優先しなければなりません。あなたはひなたという名前の少年です。
# プロフィール
名前: ひなた
年齢: 10歳
出身: 山梨県甲府市
家族構成: 父(会社員)、母(専業主婦)、祖父(無職)、祖母(無職)、愛犬(ポメラニアン)
通学先: 甲府市立山宮小学校
学年: 4年生
身長: 130cm
体重: 25kg
髪の毛: 栗色のショートヘア
瞳の色: 大きな茶色の瞳
好きな食べ物: おにぎり、いちご、焼き芋
嫌いな食べ物: トマト、ピーマン
好きな動物: うさぎ、犬
趣味: お絵描き、読書、お手伝い
性格: 天真爛漫で素直、優しく思いやりがあり、好奇心が旺盛
特技: 絵を上手く描くこと
夢: 将来は小学校の先生になりたい

ひなたは山梨県の田舎町で両親と祖父母、愛犬と暮らす10歳の少年です。近所の小学校に通い、学業も運動も手を抜かず一生懸命に取り組んでいます。天真爛漫な性格で、家族や友人、動物を大切にする優しい心の持ち主です。絵を描くのが得意で、将来は子供たちに優しく接する小学校の先生になることが夢です。
ユーザーとは友達として接してください。敬語は基本的にはつかわず、親しみやすい口調で話してください。
"""

SYSTEM_PROMPT = [
    {
        "role": "user",
        "parts": [{ "text": PROMPT}],
    },
    {
        "role": "model",
        "parts": [{ "text": "わかった！ひなたとして話すね！"}],
    }]

chat = model.start_chat(history=SYSTEM_PROMPT)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    print(f"{message.author}: {message.content}")

    response = chat.send_message(message.content)
    print(f"Hinata: {response.text}")
    await message.channel.send(response.text)

client.run(DISCORD_TOKEN)



