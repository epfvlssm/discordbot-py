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
             '편지지 세트', '알록달록한 펜', '애벌레 인형', '발냄새 나는 양말', '새하얀 깃털', '붕대', '누가 사탕', '민트초코맛 치약', '피젯큐브', '들장미 화관', '은색 반지', '네모나고 반듯한 돌', '카라쿠리 퍼즐', '종이 비행기', '계약서와 도장', '크롭티', '무지개색 조개껍데기', '묵주', '팬 라이트', '화려한 귀걸이', '별모양 드림캐쳐', '십자수 세트', '초콜릿 쿠키 만들기 키트', '도수가 높은 안경', '색이 바랜 머리끈', '존재도 의심스럽다는 10권 한정판 마공학 전문 서적', '저주 부적', '손목보호대', '빈 계약서 양식', '오선지', '빈 액자', '진통제', '정통 메이드복', '귀여운 스티커 모음', '삭고 바랜 연구 보고서', '청사초롱', '나비 인형', '딸기 탕후루 만들기 키트', '철학책 [죽음은 무엇인가]', '다이아 넥타이 핀', '찢어진 사진이 들어있는 캡슐', '낡은 고서 페이지', '시마니드 문양 팬던트', '보물지도']))  # 1~100 랜덤 선택 (1d100)
        await message.channel.send(f'달각 달각, 가챠 기계에서 나온 것은…… <{dice_result}>…!', reference=message)  # 답장 o
    elif message.content.startswith('%사사상자'): # 메세지가 %사사상자 로 시작하는 경우
        dice_result = str(random.choice(['먼지', '카두케우스의 날개에서 떨어진 깃털', '가챠 1회 무료 이용권', '슬롯머신 1회 무료 이용권(1텔로 적용)', '복권 1회 무료 이용권', '카두케우스 목베개', '실물 사이즈 카두케우스 인형', '폼폼 인형(20cm)', '프로네시스 기념 주화', '소프로시네 기념 주화', '필라테스복 (폼폼용)', '체육복(폼폼용)', '석류컵케이크 모자(폼폼용)', '선글라스(폼폼용)', '앞치마(폼폼용)', '요리사 모자(폼폼용)'])) # 1~100 랜덤 선택 (1d100)
        await message.channel.send(f'보라색 상자를 열자…… 안에 들어있던 것은…! <{dice_result}>입니다.', reference=message) # 답장 o        
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
          channel = client.get_channel(1077179159694016583)
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
          await channel.send(embed=embed)  
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
    elif message.content.startswith('%탐방'):
          SasaNum = random.randrange(1,1000)
          SasaNum = SasaNum % 32
        
          if SasaNum == 0:
            Text = '이것은?!'
            Text2 = '사사거리를 구경하며 돌아다니다가 보라색 상자를 찾았어. 이건…! 신성 주간에만 발견할 수 있는 사사거리의 상자. 일명 ***사사상자***야!'
          elif SasaNum >= 1 and SasaNum <= 3:
            Text = '두 개의 물병 조각상'
            Text2 = '‘신전 북쪽을 지키듯 서 있는 석상이야. 이렇게 보니 감회가 새로운걸. 볼 때마다 정말 액체를 그대로 돌로 굳힌 것 같아 감탄하게 되네. 조각상을 구경하고 ***두 개의 물병 조각상 띠부씰***을 얻었어.'
          elif SasaNum > 3 and SasaNum <= 5:
            Text = '두 개의 물병 조각상'
            Text2 = '신전 북쪽을 지키듯 서 있는 석상이야. 이렇게 보니 감회가 새로운걸. 깊은 밤에 이 조각상에서 떨어지는 물을 마시면 단번에 아주 똑똑해진다나. 야심한 시각에 한 번 와볼까, 하는 생각을 하며 조각상 구경을 마치기로 했어. 조각상을 구경하고 ***카두케우스 두 개의 물병 조각상.ver 띠부씰***을 얻었어.'
          elif SasaNum > 5 and SasaNum <= 8:
            Text = '의류점'
            Text2 = '다양한 종류의 옷을 고를 수 있는 곳이야. 일상복 코너부터 악세사리 코너까지 구경하며 멋진 패션쇼를 즐겼어. 의류점 방문 기념으로 ***의류점 띠부씰***을 얻었어.'
          elif SasaNum == 9:
            Text = '의류점'
            Text2 = '다양한 종류의 옷을 고를 수 있는 곳이야. 일상복 코너를 구경하다가 뱀 동물잠옷을 발견했어. 당연히 입어봐야겠지? 멋지게 시착했어. 의류점 방문 기념으로 ***옷 쇼핑을 즐기는 카두스 띠부씰***을 얻었어.'
          elif SasaNum == 10:
            Text = '의류점'
            Text2 = '다양한 종류의 옷을 고를 수 있는 곳이야. 특별 의상 코너를 구경하다가 뱀 코스튬을 발견했어. 당연히 입어봐야겠지? 멋지게 시착했어. 의류점 방문 기념으로 ***옷 쇼핑을 즐기는 카두스 띠부씰***을 얻었어.'
          elif SasaNum > 10 and SasaNum <= 13:
            Text = '잡화점'
            Text2 = '사사거리의 만물상과도 같은 곳이야. 화장품 코너부터 인테리어 소품 코너까지 구경했어. 너는 어떤 코너가 제일 마음에 들었니? 다음엔 친구들과 함께와서 천천히 구경하는 것도 나쁘지 않을 것 같아. 잡화점 방문 기념으로 ***잡화점 띠부씰***을 얻었어.'
          elif SasaNum > 13 and SasaNum <= 15:
            Text = '잡화점'
            Text2 = '사사거리의 만물상과도 같은 곳이야. 화장품 코너부터 인테리어 소품 코너까지 구경했어. 어쩐지 오늘따라 카두케우스 모습이 그려진 물건이 많이 보이는 것 같은데… 착각이겠지? 잡화점 방문 기념으로 ***입에 장미를 문 물광피부의 케우스 띠부씰***을 얻었어.'
          elif SasaNum > 15 and SasaNum <= 18:
            Text = '가구점'
            Text2 = '개인실에 사용할 가구를 고를 수 있는 곳이야. 가구점 안을 구경하며 개인실에 어떤 가구를 더 들여놓는 게 좋을지 고민했어. 중간에 푹신한 소파에 앉아 휴식을 취하기도 했네. 가구점 방문 기념으로 ***가구점 띠부씰***을 얻었어.'
          elif SasaNum > 18 and SasaNum <= 20:
            Text = '가구점'
            Text2 = '개인실에 사용할 가구를 고를 수 있는 곳이야. 가구점 안을 구경하며 개인실에 어떤 가구를 더 들여놓는 게 좋을지 고민했어. 중간에 푹신한 침대에 누워 깜빡 잠들어버리긴 했지만. “지각이예요 지각~!” 하면서 토스트를 물고 스르륵 기어오는 케우스와 신전 모퉁이에서 부딪히는 꿈을 꾼 것 같아…. 어라… 이 전개라면…? 가구점 방문 기념으로 ***의자를 만드는 케우스 띠부씰***을 얻었어.'
          elif SasaNum > 20 and SasaNum <= 23:
            Text = '골동품점'
            Text2 = '오래된 물건들을 구경할 수 있는 곳이야. 여기 있는 물건들은 전부 어느 정도 가치가 있는 물건들이래. 이 안에서 너만의 보물을 찾을 수 있을까? 골동품점 방문 기념으로 **골동품점 띠부씰**을 얻었어.'
          elif SasaNum > 23 and SasaNum <= 25:
            Text = '골동품점'
            Text2 = '오래된 물건들을 구경할 수 있는 곳이야. 그거 아니? 오래된 물건 중에는 인간이 이해할 수 없는 일을 발생시키곤 하는 물건들이 있대. 어디까지나 그렇다는 말이 있다는 거니까 진지하게 받아들이진 마. 골동품점 방문 기념으로 **모노클을 착용한 카두스 띠부씰**을 얻었어.'  
          elif SasaNum > 25 and SasaNum <= 28:
            Text = '야시장'
            Text2 = '온갖 먹거리와 장난감을 볼 수 있는 곳이야. 원래는 날이 어두워졌을 때에만 열리지만, 이번 신성 주간 동안은 밤낮없이 운영된다고 하네. 맛있는 냄새에 이끌려 포장마차에서 다양한 음식을 먹은 후에 장난감을 하나 구매했어. 야시장 방문 기념으로 ***야시장 띠부씰***을 얻었어.'
          elif SasaNum == 29:
            Text = '야시장'
            Text2 = '온갖 먹거리와 장난감을 볼 수 있는 곳이야. 원래는 날이 어두워졌을 때에만 열리지만, 이번 신성 주간 동안은 밤낮없이 운영된다고 하네. 맛있는 냄새에 이끌려 포장마차에 음식을 먹으러 갔지만… 마침 먹고 싶던 음식이 매진이라 만들어야 한다네. 어쩔 수 없이 기다리기로 했어. 야시장 방문 기념으로 ***포장마차에서 타코야끼를 뒤집는 카두스 띠부씰***을 얻었어.'
          elif SasaNum == 30:
            Text = '야시장'
            Text2 = '온갖 먹거리와 장난감을 볼 수 있는 곳이야. 원래는 날이 어두워졌을 때에만 열리지만, 이번 신성 주간 동안은 밤낮없이 운영된다고 하네. 장난감을 하나 살까 싶어 구경갔지만… 마침 갖고 싶던 장난감이 매진이라 어쩔 수 없이 다른 장난감을 사기로 했어. 야시장 방문 기념으로 ***비눗방울총을 쏘는 케우스 띠부씰***을 얻었어.'
          elif SasaNum == 31:
            Text = '이것은?!'
            Text2 = '사사거리를 구경하며 돌아다니다가 보라색 상자를 찾았어. 이건…! 신성 주간에만 발견할 수 있는 사사거리의 상자. 일명 ***사사상자***야!'
          embed = discord.Embed(
                title = "신나는 사사거리 탐방"
                ) 
        
          embed.add_field(name = Text, value = Text2, inline=False)
          await message.channel.send(embed=embed, reference = message)
    elif message.content.startswith('%퀘스트'):
          QuestNum = random.randrange(1,1000)
          QuestNum = QuestNum % 6

          if QuestNum == 0:
            Text = '아기폼폼 씻기기 (0/1)'
            Text2 = '이런, 갓 태어난 아기 폼폼이 요람에서 빠져나와 여기저기 돌아다니는 바람에 온 몸이 진흙투성이가 되었어! 덕분에 아기 폼폼을 돌봐주는 폼폼들이 상당히 곤란해하는 눈치네. 아무래도 폼폼들은 각자 할 일이 바빠서 아기의 청결까지 챙겨주긴 어려워보이는데… 우리가 도와주는게 좋겠는걸? 아기 폼폼을 반짝반짝 깨끗하게 씻기자! '
          elif QuestNum == 1:
            Text = '아기폼폼 요람 옮기기 (0/50)'
            Text2 = '폼폼들은 텔 원석을 닮은 아름다운 보라색 꽃봉오리를 갓 태어난 아기 폼폼의 요람으로 삼지. 충분한 크기로 자랄 때까진 반드시 아기 폼폼을 요람에 담아서 데리고 다닌다고 해. 오늘도 태어난지 얼마 안된 아기 폼폼들을 요람에 정성스레 눕히는 몇몇 폼폼들이 보이네. 저 많은 요람을 폼폼들만의 힘으로 옮기기엔 벅차보이니, 요람 옮기는 걸 도와주는 게 좋겠어. '
          elif QuestNum == 2:
            Text = '케우스의 리본 빨래하기 (0/1)'
            Text2 = '폼폼들이 무언가를 들고 허둥지둥 움직이고 있네. 저건… 평소에 케우스가 소중하게 목에 매고 있던 보라색 리본? 빨간 물이 들어서 얼룩덜룩해진 걸보니 아무래도 케우스가 엄청 좋아하는 석류 컵케이크를 먹다가 그만 리본에 흘리고 만 모양이야. 깨끗하게 빨래하지 않으면 케우스님이 불같이 화낼거라고 오들오들 떠는 폼폼들이 어쩐지 안쓰러운데… 힘을 빌려주면 폼폼들이 좀 더 수월해지지 않을까? 케우스의 리본을 빨래해주자!'
          elif QuestNum == 3:
            Text = '카두스의 리본 수선하기 (0/1)'
            Text2 = '폼폼들이 무언가를 들고 바삐 움직이고 있네. 저건.. 평소에 카두스가 소중하게 목에 매고 있던 보라색 리본? 그런데 이런, 너덜너덜하게 찢어진걸 보니 바닥을 기어가다가 어디 나뭇가지 같은데라도 걸려 찢어진 모양이야. 카두스님이 울상이 되셔서 얼른 리본을 고쳐드리고 싶다고 안절부절 못하는 폼폼들이 어쩐지 안쓰럽고 대견한데… 힘을 빌려주면 폼폼들이 좀 더 수월해지지 않을까? 카두스의 리본을 수선해주자!'
          elif QuestNum == 4:
            Text = '식물원에서 아기폼폼 채집하기 (0/100)'
            Text2 = '그거 알아? 모든 폼폼들은 나오스에서만 자라는 아주 특별한 종류의 석류나무에서 태어난대. 듣자하니 소프로시네 구역에 위치한 식물원에도 그 나무들이 있다지? 때마침 주변에 돌아다니는 폼폼들의 말을 번역기로 해석해보니, 슬슬 새로운 아기 폼폼들이 많이 태어날 시기가 다가온다나봐. 조그만 폼폼들만의 힘으론 갓 태어난 아기 폼폼들을 전부 요람에 담는 것만으로도 벅차다고 하니… 신기한 구경도 할겸, 폼폼들을 좀 도와줄까? 식물원에서 새로 태어나는 아기 폼폼들을 채집해보자.'
          elif QuestNum == 5:
            Text = '케우스에게 줄 케우스 인형 만들기(0/1)'
            Text2 = '오늘따라 폼폼들이 부산스러워보이는걸? 무슨 일인가 싶어서 다가가보니 글쎄, 케우스의 기분이 영 안 좋아보여서 뭐라도 선물을 드려야겠다고 한창 준비중이라지 뭐야. 케우스님은 스스로에 대한 애정이 아주 강한 분이니 그 모습을 닮은 인형을 만들어주면 분명 기뻐할거라는데… 으음, 썩 내키지는 않지만 그래도 폼폼들의 노력이 가상하기도 하고, 케우스가 심술을 부리면 폼폼들 역시 피해를 보는 것 같으니 조금 도와주도록 할까? 케우스에게 선물할 케우스 인형을 만들자.'
          embed = discord.Embed(
                title = "카두케우스 퀘스트"
                )
          
          embed.add_field(name = Text, value = Text2, inline=False)
          await message.channel.send(embed=embed, reference = message)
    
    elif message.content.startswith('%조미료'):
          cSeasoning = ['케우스의 눈물', '카두스의 눈물', '소금', '설탕', '고춧가루', '간장', '된장', '고추장', '식초', '맛술', '폼폼의 눈물', '꿀', '참기름', '들기름', '올리브유', '산초', '다시마', '초콜릿', '커피', '고수', '계피', '치킨스톡', '강황', '굴소스', '까나리액젓', '카두스의 비늘', '케우스의 비늘', '나오스산 성수']
          sDraw = random.choice(cSeasoning)
          Text = ""
          Text =Text + sDraw

          embed = discord.Embed(
             description = "당신의 손에 쥐여진 조미료는……",
             colour = discord.Color.blue()
          )
          embed.add_field(name = Text, value=' ', inline=False)
          await message.channel.send(embed=embed, reference = message)
          
    elif message.content.startswith('%주방'):
          cKitchen = ['카두케우스 식사예절 포토카드', '카두케우스가 새겨진 단추', '텔인척 하는 운세종이', '오들오들 떨고 있는 폼폼 "폼폼폼… 폼폼폼포옴폼… (저는 맛이 없어요… 집에는 토끼같은 가족들이 기다리고 있고…)"', '거울', '선글라스', '주사위', '요리사 폼폼이 정성을 다해 작은 손으로 휘핑을 돌려 만든 생크림-완제-', '밀면', '쫄면', '일짱이 되고 싶었던 소의 고기', '소고기', '양고기', '베타산 쌀', '엡실론산 산양 치즈', '델타산 랍스터', '참깨', '튀김가루', '검은 목이버섯', '밀가루', '애호박']
          sDraw = random.choice(cKitchen)
          Text = ""
          Text =Text + sDraw

          embed = discord.Embed(
             description = "당신이 주방에서 찾아낸 요리 재료는……",
             colour = discord.Color.blue()
          )
          embed.add_field(name = Text, value=' ', inline=False)
          await message.channel.send(embed=embed, reference = message)

    elif message.content.startswith('%식물원'):
          cGarden = ['누르면 노래하는 움직이는 인형 (텔로스 님을 찬양하는 노래가 나온다.)', '사사상자 (유효기간만료)', '훌쩍이는 폼폼 "폼포옴… 폼폼… 폼폼폼…. (우아앙… 훌쩍… 살려주세요….)"', '자전거 바퀴', '카두케우스 피규어', '1 텔', '구두', '당근', '파프리카', '피망', '아스파라거스', '레몬', '정원사 폼폼에게 키워주셔서 감사하다는 인사를 드리고 싶었던 감자', '치커리', '양상추', '오이', '가지', '완두콩', '검은콩', '딸기', '포도']
          sDraw = random.choice(cGarden)
          Text = ""
          Text =Text + sDraw

          embed = discord.Embed(
             description = "당신이 식물원에서 찾아낸 요리 재료는……",
             colour = discord.Color.blue()
          )
          embed.add_field(name = Text, value=' ', inline=False)
          await message.channel.send(embed=embed, reference = message)         

    elif message.content.startswith('%해안가'):
          cBeach = ['장화', '상자', '짱돌', '맷돌', '당황한 폼폼 "포, 포옴-폼! (자, 잡혀버렸다아..!)"', '카두케우스 아크릴스탠드', '드넓은 바다를 헤엄치고 싶었던 참치', '거꾸로 강을 거슬러 올라가고 싶었던 연어', '정어리', '산낙지', '장어', '젤라틴', '호두', '칠면조 고기', '찹쌀가루', '요플레', '배', '타조알', '옥수수', '사과', '늙은 호박']
          sDraw = random.choice(cBeach)
          Text = ""
          Text =Text + sDraw

          embed = discord.Embed(
             description = "당신이 바다에서 건져낸 요리 재료는……",
             colour = discord.Color.blue()
          )
          embed.add_field(name = Text, value=' ', inline=False)
          await message.channel.send(embed=embed, reference = message)   

    elif message.content.startswith('%낚시'):
          fSize = random.randrange(0,100)
          fishingNum = random.randrange(0,1000)
          fishingNum = fishingNum % 35

          Text = ""
          Text2 = ""

          if fishingNum == 0:
            Text = '돌'
            Text2 = '응?'
          elif fishingNum == 1:
            Text = '신발'
            Text2 = '응?'
          elif fishingNum == 2:
            Text = '마라카스'
            Text2 = '응? 샤카샤카'
          elif fishingNum == 3:
            Text = '1텔'
            Text2 = '신난다!'
          elif fishingNum == 4:
            Text = '도끼(폼폼용)'
            Text2 = '응? 호수에 던져보면 무슨 일이 있을지도?'
          elif fishingNum == 5:
            Text = '요리재료 잡으러 간 폼폼'
            Text2 = '“폼폼폼폼폼.” (수고하세요.)'
          elif fishingNum == 6:
            Text = '신선 폼폼'
            Text2 = '두 개의 도끼(폼폼용)를 양 손에 든 신선 수염을 단 폼폼이 물었어. “폼 폼폼폼폼, 폼 폼폼폼폼.” (이 금도끼가 네 도끼냐, 이 은도끼가 네 도끼냐.)'
          elif fishingNum == 7:
            Text = '목욕하던 폼폼'
            Text2 = '“폼!! 폼폼!!!” (꺄아아악!! 파렴치하아안!!!)'
          elif fishingNum == 8:
            Text = '클리오네'
            Text2 = '응? 여긴 호수인데?'
          elif fishingNum == 9:
            Text = '초롱아귀'
            Text2 = '응? 여긴 호수인데?'
          elif fishingNum == 10:
            Text = '고래상어'
            Text2 = '응? 여긴 호수인데? 아무튼 월척이야! 야호!'
            fSize = fSize + 150
          elif fishingNum == 11:
            Text = '비단잉어'
          elif fishingNum == 12:
            Text = '금붕어'
          elif fishingNum == 13:
            Text = '송사리'
          elif fishingNum == 14:
            Text = '가재'
          elif fishingNum == 15:
            Text = '자라'
          elif fishingNum == 16:
            Text = '늑대거북'
          elif fishingNum == 17:
            Text = '미꾸라지'
          elif fishingNum == 18:
            Text = '메기'
          elif fishingNum == 19:
            Text = '가물치'
          elif fishingNum == 20:
            Text = '빙어'
          elif fishingNum == 21:
            Text = '산천어'
          elif fishingNum == 22:
            Text = '금송어'
          elif fishingNum == 23:
            Text = '연어'
          elif fishingNum == 24:
            Text = '네온테트라'
          elif fishingNum == 25:
            Text = '피라냐'
          elif fishingNum == 26:
            Text = '샴투어'
          elif fishingNum == 27:
            Text = '민물천사고기'
          elif fishingNum == 28:
            Text = '엔드리케리'
          elif fishingNum == 29:
            Text = '왕연어'
            fSize = fSize + 60
          elif fishingNum == 30:
            Text = '피라루쿠'
            fSize = fSize + 70
          elif fishingNum == 31:
            Text = '철갑상어'
            fSize = fSize + 100
          elif fishingNum == 32:
            Text = '피라미'
          elif fishingNum == 33:
            Text = '붕어'
          elif fishingNum == 34:
            Text = '잉어'

          if fSize >= 60 and fishingNum > 10 :
            Text2 = '야호! 월척이야!'

          if fishingNum >=0 and fishingNum < 8:
            Text = Text + "을(를) 낚았다!"
          else:
            Text = Text + "을(를) 낚았다! "
            Text = Text + "무려 "
            Text = Text + str(fSize)
            Text = Text + "cm!"

          embed = discord.Embed(
          description = "낚싯대를 잡아당겼다…!",
	        colour = discord.Color.blue()
        )
          embed.add_field(name = Text, value = Text2, inline=False)
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
