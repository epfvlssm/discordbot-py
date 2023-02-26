from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
import random
from discord.ext import commands
from discord.utils import get
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
        embed = discord.Embed(
        description = '도르르륵, 주사위의 눈은…'
        )
        embed.add_field(name = dice_result, value=' ', inline=False)
        await message.channel.send(embed=embed, reference = message)
    elif message.content.startswith('%가챠'):  # 메세지가 ❈가챠 로 시작하는 경우
        dice_result = str(random.choice(
            ['모르는 이름이 써진 네임택', '티 타임용 쿠키세트', '작은 씨앗', '챙 넓은 모자', '고래 인형', '워터볼', '검은 강아지 인형', '동화책 [어느 숲속 이야기]', '텔 원석',
             '건네 준 사람과의 추억이 재생되는 거울 모양 마도구', '민들레 홀씨', '새장', '모조 다이아', '새하얀 천', '금박장식 비녀', '고사성어 사전', '별자리 무드등',
             '「쉽게 배우는 마공학 이론」', '새하얀 양 인형', '실타래', 'SEI☆의 사인지', '무선마이크', '목이 기다란 도마뱀 인형', '공룡이 그려진 동화책', '낡은 누더기 옷',
             '행운 기원 팔찌', '기념품가게 팔찌', '향수', '화상 연고', '의료용 안대', '목화 다발', '자개 장식', '공단 리본', '레이스가 달린 원피스', '물감', '긴 천',
             '편지지 세트', '알록달록한 펜', '애벌레 인형', '발냄새 나는 양말', '새하얀 깃털', '붕대', '누가 사탕', '민트초코맛 치약', '피젯큐브', '들장미 화관', '은색 반지', '네모나고 반듯한 돌', '카라쿠리 퍼즐', '종이 비행기', '계약서와 도장', '크롭티', '무지개색 조개껍데기', '묵주', '팬 라이트', '화려한 귀걸이', '별모양 드림캐쳐', '십자수 세트', '초콜릿 쿠키 만들기 키트', '도수가 높은 안경']))  # 1~100 랜덤 선택 (1d100)
        await message.channel.send(f'달각 달각, 가챠 기계에서 나온 것은…… <{dice_result}>…!', reference=message)  # 답장 o
    elif message.content.startswith('%슬롯머신'):
          SlotMachine = [ '🐋', '🍺', '🍇', '🃏','7️⃣', ':tomato:', ':strawberry:', ':eggplant:', ':apple:', ':pineapple:', ':lemon:', ':melon:', ':kiwi:', ':snake:', ':hatched_chick:', ':gift:', ':star2:', ':tangerine:']
          sFirst = random.choice(SlotMachine)
          sSecond = random.choice(SlotMachine)
          sThird = random.choice(SlotMachine)
          Text = '' 
          Text =Text + sFirst
          Text =Text + sSecond
          Text =Text + sThird

          embed = discord.Embed(
          description = Text .strip(),
          colour = discord.Color.purple()
        )
          await message.channel.send(embed=embed, reference = message)        
    elif message.content.startswith("❈복권"):
          channel = client.get_channel(1077114613981794335)
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
              colour=discord.Color.purple()
          )
          await message.channel.send(embed=embed)
    elif message.content.startswith('%동전'):
          randomNum = random.randrange(1,1000)
          randomNum = randomNum % 2
          
          if randomNum == 0:
              await message.channel.send(embed=discord.Embed(description= ' :coin: ' + '뒷면이 나왔다!'), reference = message)
          elif randomNum == 1:
              await message.channel.send(embed=discord.Embed(description= ' :coin: ' + '앞면이 나왔다!'), reference = message)     
    elif message.content.startswith('%이용가이드'):
          embed = discord.Embed(title="가챠봇 이용가이드",description="가챠봇을 이용하기 위한 명령어 키워드들입니다", color=0xbc40fb)
          embed.add_field(name="%가챠", value="선지자 후보들과 직ㆍ간접적으로 연관된 아이템이 등장합니다. 1텔을 소모하여 랜덤 아이템을 하나 얻을 수 있습니다.", inline=False)
          embed.add_field(name="%다이스", value="1d100 다이스를 굴립니다.", inline=False)
          embed.add_field(name="%슬롯머신", value="드르륵 탁. 슬롯머신을 돌립니다. 잭팟을 노려봅시다!", inline=False)
          embed.add_field(name="%동전", value="앞, 뒤 중 한 가지를 보여줍니다.", inline=False)
          embed.add_field(name="%노래방", value="0점부터 100점 사이의 점수를 랜덤으로 출력합니다. 당신의 노래 실력을 뽐내보세요.", inline=False)
          embed.add_field(name="%운세", value="오늘의 운세. 당신의 오늘 운을 시험해보세요. 운세 쪽지는 하루에 한번만 뽑을 수 있습니다.", inline=False)
          await message.channel.send(embed=embed)
    elif message.content.startswith('%노래방'):
         score = random.randrange(0,101)

         Text = ' '
         Text = Text + str(score)
         Text = Text + '점!'

         if score == 100:
             Text2 = '환상적인 목소리! 당신이~ 👍***짱***이랍니다~'
         elif score <= 99 and score >= 95:
             Text2 = '노래를 너~어무 잘불러서 카두케우스 ***기절!***🤩'
         elif score <= 94 and score >= 90:
             Text2 = '한곡 더~ 듣고 싶은 실력! **불↘러→줄↘꺼↗죠↗??**🎤”'
         elif score <= 89 and score >= 85:
             Text2 = '이렇게 잘 부를수가?!😃 매~력이~ 넘쳐요~'
         elif score <= 84 and score >= 80:
             Text2 = '카두케우스 완~전 **두근!** 🥰정말 멋져요~~'
         elif score <= 79 and score >= 70:
             Text2 = '목소리에~ 매력이 철철~ 하트💜하트💜~'
         elif score <= 69 and score >= 60:
             Text2 = '지금 딱 좋아요!!😉 그 느낌으로 한! 곡! 더!!'
         elif score <= 59 and score >= 50:
             Text2 = '점수는 점수일 뿐. 즐거우면 100점이죠~😌'
         elif score <= 49 and score >= 10:
             Text2 = '너~~어 노래에 조금만 더 ***집!중!*** 🙁'
         elif score <= 9 and score >= 0:
             Text2 = '이 점수! 어쩌면 좋지? 진짜 모르게쒀요오~ 😯'
         embed = discord.Embed(
         description = '당신의 점수는! 두구두구…',
         colour = discord.Color.purple()
         )
         embed.add_field(name = Text, value = Text2, inline=False)
         await message.channel.send(embed=embed, reference = message)
    elif message.content.startswith('%운세'):
          fortuneNum = random.randrange(1,1000)
          fortuneNum = fortuneNum % 14

          if fortuneNum == 0:
            Text = '대길[大吉]'
            Text2 = '봄이 되어 봄빛을 손에 쥐며 오래된 가지에도 꽃이 피듯 운세가 열린다. 구름 사다리와 같이 오르기 힘든 곳까지도 오를 수 있게 된다.'
          elif fortuneNum == 1:
            Text = '길[吉]'
            Text2 = '봄이 되면 말도 기운이 솟아 뛰어다니는 것처럼 차차 운이 다가온다. 하늘에서부터 행운이 당신을 향해 다가와, 무엇이든 생각하는 대로 될 것.'
          elif fortuneNum == 2:
            Text = '중길[中吉]'
            Text2 = '대전환의 운기. 길흉이 혼연하여 공사 모두 매우 바쁘며 고생도 많은 시기이다. 그러나 참고 버티어 똑똑히 방향을 확인하고 나아가면 응당한 결과가 따를 것이다.'
          elif fortuneNum == 3:
            Text = '소길[小吉]'
            Text2 = '변화가 많을 운기이다. 마음을 정직하게 하여, 만사에 침착하고 남들에게 사랑받는 사람이 되면 모든 일에 좋을 것이다.'
          elif fortuneNum == 4:
            Text = '말소길[末小吉]'
            Text2 = '치우치지 않고 올바른 길을 가면 길은 열린다. 그러나 올바른 사람일수록 간사한 이로부터 방해를 받아 잘못을 일으키기도 한다. 마음을 가라앉히고 믿음을 가질 것.'
          elif fortuneNum == 5:
            Text = '반길[半吉]'
            Text2 = '이제까지 사소한 실수의 훼방으로 인해 일이 풀리지 않았다. 그러나 앞으로는 차츰차츰 일이 풀릴 조짐이 있다. 잘못을 뉘우치고 복을 빌면 결국은 운도 열릴 것이다.'
          elif fortuneNum == 6:
            Text = '말길[末吉]'
            Text2 = '가진 물건이 다하여, 다시 시작하는 모습이므로 소원은 이루워질 것이다. 성급히 서두르는 것은 좋지 않다.'
          elif fortuneNum == 7:
            Text = '평[平]'
            Text2 = '언제나와 같은 길이다. 길이 되는가 흉이 되는가는 자신에게 있으므로, 스스로를 굳게 믿는 것이 좋다.'
          elif fortuneNum == 8:
            Text = '말흉[末凶]'
            Text2 = '대전환의 운기. 공사 모두 바쁘며 고생도 많은 시기이다. 운이 틔지 않아 일이 뜻대로 풀리지 않고 엉뚱한 곳으로 튀기도 한다. 참고 버티어 중심을 잡는 것이 좋다.'
          elif fortuneNum == 9:
            Text = '반흉[半凶]'
            Text2 = '과거의 잘못이 들춰지고, 지금껏 되어오던 일에 사소한 실수나 훼방이 끼어들어 일이 풀리지 않기 시작한다. 잘못을 뉘우치고 이상의 우를 범하지 않도록 해야한다.'
          elif fortuneNum == 10:
            Text = '소흉[小凶]'
            Text2 = '가진 물건이 다한 모습이다. 성급히 서두르다가 일을 망칠 수 있으니 몸가짐을 조심하고 여유를 갖는 것이 좋다.'
          elif fortuneNum == 11:
            Text = '흉[凶]'
            Text2 = '만사에 바람직하지 못한 곳에서 근심에 빠지는가 하면 매사를 어렵게 만드는 습성이 있으니 운이 틔기 어렵다. 작은 일에 유념하면서 몸가짐을 조심하는 것이 좋다.'
          elif fortuneNum == 12:
            Text = '대흉[大凶]'
            Text2 = '모든 나뭇잎이 떨어지고 그 위에 새하얀 눈이 덮이듯, 운이 보이지 않는다. 경거망동 하지 않고 기다리는 것 밖에는 도리가 없다.'
          elif fortuneNum == 13:
            Text = '2텔?!'
            Text2 = '운세 종이 대신에 텔이 나왔다!'
          embed = discord.Embed(
                title = "오늘의 운세"
                )
          
          embed.add_field(name = Text, value = Text2, inline=False)
          await message.channel.send(embed=embed, reference = message)    
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
