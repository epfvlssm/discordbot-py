from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
import random
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # else:
    #     await message.channel.send('callback: ' + message.content)

    if message.content == '!call':
        await message.channel.send("callback!")

    if message.content.startswith('#hello'):  # 메세지가 #hello로 시작하는 경우
        await message.channel.send(f'{message.author.mention}, hello!')  # 답장 x
    elif message.content.startswith('❈안녕하세요'):  # 메세지가 #안녕하세요 로 시작하는 경우
        await message.channel.send(f'{message.author.display_name}, 안녕하세요!', reference=message)  # 답장
    elif message.content.startswith('%다이스'):  # 메세지가 dice로 시작하는 경우
        dice_result = str(random.randint(1, 100))  # 1~100 랜덤 선택 (1d100)
        await message.channel.send(f'도르르륵, 주사위의 눈은… <{dice_result}>!', reference=message)  # 답장 o
    elif message.content.startswith('%가챠'):  # 메세지가 ❈가챠 로 시작하는 경우
        dice_result = str(random.choice(
            ['모르는 이름이 써진 네임택', '티 타임용 쿠키세트', '작은 씨앗', '챙 넓은 모자', '고래 인형', '워터볼', '검은 강아지 인형', '동화책 [어느 숲속 이야기]', '텔 원석',
             '건네 준 사람과의 추억이 재생되는 거울 모양 마도구', '민들레 홀씨', '새장', '모조 다이아', '새하얀 천', '금박장식 비녀', '고사성어 사전', '별자리 무드등',
             '「쉽게 배우는 마공학 이론」', '새하얀 양 인형', '실타래', 'SEI☆의 사인지', '무선마이크', '목이 기다란 도마뱀 인형', '공룡이 그려진 동화책', '낡은 누더기 옷',
             '행운 기원 팔찌', '기념품가게 팔찌', '향수', '화상 연고', '의료용 안대', '목화 다발', '자개 장식', '공단 리본', '레이스가 달린 원피스', '물감', '긴 천',
             '편지지 세트', '알록달록한 펜', '애벌레 인형', '발냄새 나는 양말', '새하얀 깃털', '붕대', '누가 사탕', '민트초코맛 치약', '피젯큐브', '들장미 화관', '은색 반지', '네모나고 반듯한 돌', '카라쿠리 퍼즐', '종이 비행기', '계약서와 도장', '크롭티', '무지개색 조개껍데기', '묵주', '팬 라이트', '화려한 귀걸이', '별모양 드림캐쳐', '십자수 세트', '초콜릿 쿠키 만들기 키트', '도수가 높은 안경']))  # 1~100 랜덤 선택 (1d100)
        await message.channel.send(f'달각 달각, 가챠 기계에서 나온 것은…… <{dice_result}>…!', reference=message)  # 답장 o
    elif message.content.startswith('%슬롯머신'):
          await message.channel.send(f'현재 슬롯머신은 점검중입니다.', reference=message)
        
    elif message.content.startswith("❈복권"):
          Text = ""
          number = [1, 2, 3, 4, 5, 6, 7] # 배열크기 선언해줌
          count = 0
          for i in range(0, 7):
              num = random.randrange(1, 46)
              number[i] = num
              if count >= 1:
                  for i2 in range(0, i):
                      if number[i] == number[i2]:  # 만약 현재랜덤값이 이전숫자들과 값이 같다면
                          numberText = number[i]
                          print("작동 이전값 : " + str(numberText))
                          number[i] = random.randrange(1, 46)
                          numberText = number[i]
                          print("작동 현재값 : " + str(numberText))
                          if number[i] == number[i2]:  # 만약 다시 생성한 랜덤값이 이전숫자들과 또 같다면
                              numberText = number[i]
                              print("작동 이전값 : " + str(numberText))
                              number[i] = random.randrange(1, 46)
                              numberText = number[i]
                              print("작동 현재값 : " + str(numberText))
                              if number[i] == number[i2]:  # 만약 다시 생성한 랜덤값이 이전숫자들과 또 같다면
                                  numberText = number[i]
                                  print("작동 이전값 : " + str(numberText))
                                  number[i] = random.randrange(1, 46)
                                  numberText = number[i]
                                  print("작동 현재값 : " + str(numberText))

              count = count + 1
              Text = Text + "  " + str(number[i])

          print(Text.strip())
          embed = discord.Embed(
              title="카두케우스 복권",
              description=Text.strip(),
              colour=discord.Color.red()
          )
          await message.channel.send(embed=embed)
    elif message.content.startswith('%동전'):
          randomNum = random.randrange(1, 9)
          print(randomNum)
          if randomNum == 1:
              await message.channel.send(embed=discord.Embed(description=':coin: '+ '뒷면이 나왔다!'))
          if randomNum == 2:
              await message.channel.send(embed=discord.Embed(description=':coin: ' + '앞면이 나왔다!'))
          if randomNum ==3:
              await message.channel.send(embed=discord.Embed(description=':coin: '+ '뒷면이 나왔다!'))
          if randomNum ==4:
              await message.channel.send(embed=discord.Embed(description=':coin: ' + '앞면이 나왔다!'))
          if randomNum ==5:
              await message.channel.send(embed=discord.Embed(description=':coin: '+ '뒷면이 나왔다!'))
          if randomNum ==6:
              await message.channel.send(embed=discord.Embed(description=':coin: ' + '앞면이 나왔다!'))
          if randomNum ==7:
              await message.channel.send(embed=discord.Embed(description=':coin: '+ '뒷면이 나왔다!'))
          if randomNum ==8:
              await message.channel.send(embed=discord.Embed(description=':coin: ' + '앞면이 나왔다!'))     
    elif message.content.startswith('%이용가이드'):
          embed = discord.Embed(title="가챠봇 이용가이드",description="가챠봇을 이용하기 위한 명령어 키워드들입니다", color=0x00aaaa)
          embed.add_field(name="%가챠", value="1텔을 소모하여 선지자 후보들의 호불호 아이템을 랜덤으로 뽑습니다.", inline=False)
          embed.add_field(name="%다이스", value="1d100 다이스를 굴립니다.", inline=False)
          embed.add_field(name="%슬롯머신", value="슬롯머신을 돌립니다.잭팟을 노려봅시다!", inline=False)
          embed.add_field(name="%동전", value="동전의 앞면과 뒷면 중 한가지를 보여줍니다.", inline=False)
          embed.add_field(name="%노래방", value="0점부터 100점 사이의 점수를 랜덤으로 출력합니다. 당신의 노래 실력을 뽐내보세요.", inline=False)
          await message.channel.send(embed=embed)
    else:
        start = message.content.find('[')
        end = message.content.find(']')
        if (start != -1 and end != -1) and start < end:  # [] 조건 찾기. [, ]가 존재해야 하고, 닫는 괄호가 여는 괄호보다 앞에 있으면 안된다.
            mention_keyword = message.content[start + 1:end].strip().split(
                '/')  # /를 기준으로 나눠 리스트로 저장. 현재 받은 메세지에는 /가 없으므로 그냥 ['다이스'] 로 저장된다.
            first_keyword = mention_keyword[0].strip()
            if first_keyword == '다이스':
                dice_result = str(random.randint(1, 100))
                await message.channel.send(f'다이스를 굴리자... <{dice_result}>이 나왔다.', reference=message)  # 답장 o


try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
