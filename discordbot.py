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
    elif message.content.startswith('%사사상자'): # 메세지가 %황금상자 로 시작하는 경우
        dice_result = str(random.choice(['먼지', '가챠 1회 무료 이용권', '슬롯머신 1회 무료 이용권(1텔로 적용)', '복권 1회 무료 이용권', '안드레이아 기념 주화'])) # 1~100 랜덤 선택 (1d100)
        await message.channel.send(f'황금빛 상자를 열자…… 안에 들어있던 것은…! <{dice_result}>입니다.', reference=message) # 답장 o        
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
          SasaNum = SasaNum % 52
        
          if SasaNum == 0:
            Text = '이것은?!'
            Text2 = '카두케우스 랜드를 즐기며 돌아다니다가 황금색 상자를 찾았어. 이건…! 신성 주간에만 발견할 수 있는 카두케우스 랜드의 상자. 일명 ***황금상자***야! 응? 별로 연관이 없는 것 같은데?'
          elif SasaNum >= 1 and SasaNum <= 3:
            Text = '사자와 뱀 조각상'
            Text2 = '신전 동쪽을 지키듯 서 있는 석상이야. 이렇게 보니 감회가 새로운걸. 볼 때마다 정말 당장이라도 살아 움직일 것 같다는 생각이 들게 돼. 조각상을 구경하고 ***황혼의 시간에 사자와 뱀 조각상을 구경하는 폼폼 아크릴 키링***을 얻었어.'
          elif SasaNum > 3 and SasaNum <= 5:
            Text = '사자와 뱀 조각상'
            Text2 = '신전 동쪽을 지키듯 서 있는 석상이야. 이렇게 보니 감회가 새로운걸. 이 뱀은 언제나 위풍당당하게 서 있는 것 같네. 깊은 새벽이면 사자와 뱀이 살아 움직이며 혈투를 벌인대. 깊은 새벽에 구경오는 것도 나쁘지 않을 것 같지? 조각상을 구경하고 ***여명을 등지고 승리 포즈를 취하고 있는 케우스 포토카드***를 얻었어.'
          elif SasaNum > 5 and SasaNum <= 8:
            Text = '롤러코스터'
            Text2 = '검은 레일 위를 격렬하게 달리는 열차에 타 스릴을 즐기는 놀이기구야. 운행 코스가 여러모로 굉장해 보이는 걸. 폼폼들의 안내에 따라 롤러코스터를 타면, 중간에 찰칵 소리가 들린 것 같아. 재밌었네! 롤러코스터에서 내리면 잘 찍힌 사진과 ***롤러코스터를 타는 폼폼 아크릴 키링***을 얻을 수 있었어.'
          elif SasaNum > 9 and SasaNum <=10:
            Text = '롤러코스터'
            Text2 = '검은 레일 위를 격렬하게 달리는 열차에 타 스릴을 즐기는 놀이기구야. 운행 코스가 여러모로 굉장해 보이는 걸. 그나저나 이 열차 케우스를 닮은 것 같기도 하네... 폼폼들의 안내에 따라 롤러코스터를 타면, 중간에 찰칵 소리가 들린 것 같아. 재밌었네! 롤러코스터에서 내리면 음... 이상하게 찍혀버린 사진과 ***롤러코스터를 즐기는 케우스 포토카드***를 얻을 수 있었어.'
          elif SasaNum > 10 and SasaNum <= 13:
            Text = '후룸라이드'
            Text2 = '뱃머리에 카두케우스가 장식된 작은 나무배를 타고 물 위의 레일을 미끄러지듯 달리는 놀이기구야. 질주와 하강을 반복할 때마다 물이 엄청 튀는 걸! 운이 좋게도 별로 안 젖었지만 말야. 재밌었네! 기념으로 ***후룸라이드를 타는 폼폼 아크릴 키링***을 받았어.'
          elif SasaNum > 13 and SasaNum <= 15:
            Text = '후룸라이드'
            Text2 = '뱃머리에 카두케우스가 장식된 작은 나무배를 타고 물 위의 레일을 미끄러지듯 달리는 놀이기구야. 질주와 하강을 반복할 때마다 물이 엄청 튀는 걸! 이런 쫄딱 젖어버렸어. 조금 찝찝하지만 어쩔 수 없지. 기념으로 ***후룸라이드를 탄 후 물에 젖은 카두스 포토카드***를 받았어.'
          elif SasaNum > 15 and SasaNum <= 18:
            Text = '바이킹'
            Text2 = '배 모양을 한 커다란 그네와도 같아. 뱃머리에는…… 설명 생략할게. 폼폼들의 안내를 받아 안전바를 고정하고 잠시 기다리면, 배가 천천히 흔들리기 시작해. 점점 빨라지는데다가 회전각이 커지고 있어! 곧 배가 멈췄어. 조금 어질어질한 것 같지만 재밌었네! 기념으로 ***바이킹을 타는 폼폼 아크릴 키링***을 얻었어.'
          elif SasaNum > 18 and SasaNum <= 20:
            Text = '바이킹'
            Text2 = '배 모양을 한 커다란 그네와도 같아. 뱃머리에는 아름다운 날개를 펼치고 둘만의 시간을 보내는 카두케우스 조각상이 있어. 폼폼들의 안내를 받아 안전바를 고정하고 잠시 기다리면, 배가 천천히 흔들리기 시작해. 점점 빨라지는데다가 회전각이 커지고 있어! 곧 배가 멈췄어. 으윽… 멀미가 나는 것 같아…. 기념으로 ***칼을 입에 문 용맹한 영웅 카두스 포토카드***를 얻었어.'
          elif SasaNum > 20 and SasaNum <= 23:
            Text = '회전목마'
            Text2 = '빙글빙글 돌아가는 원판 위에서 오르내리는 마차와 목마가 있는 놀이기구야. 말과 마차 중에 골라 타면 될 것 같아. 회전목마를 타는 동안은 동화같은 분위기 덕에 꿈을 꾸는 기분을 느꼈을지도 모르겠어. 재밌었네! 기념으로 **회전목마를 타는 폼폼 아크릴 키링**을 얻었어.'
          elif SasaNum > 23 and SasaNum <= 25:
            Text = '회전목마'
            Text2 = '빙글빙글 돌아가는 원판 위에서 오르내리는 마차와 목마가 있는 놀이기구야. 말과 마차 중에 골라 타면 될 것 같아. 회전목마를 타는 동안… 어쩐지 카두케우스 그림이 자꾸 보인 것만 같은데 착각이겠지? 기념으로 **백마를 타고 왕자님 옷을 입은 그윽한 표정의 카두스 포토카드**를 얻었어.'  
          elif SasaNum > 25 and SasaNum <= 28:
            Text = '범퍼카'
            Text2 = '다들 알지? 부릉부릉~ 할 수 있는 놀이기구야. 마음대로 운전해도 돼. 범퍼카니까 말이야! 그치만 너무 쾅쾅 들이박으면 안되니까 적당히~ 안전 운전을 했어. 물론 스트레스가 풀릴 정도로 들이박기도 했지만 말야. 재밌었네! 범퍼카에서 내리자 기념으로 **범퍼카를 타는 폼폼 아크릴 키링**을 얻을 수 있었어.'
          elif SasaNum > 28 and SasaNum <= 30:
            Text = '범퍼카'
            Text2 = '다들 알지? 부릉부릉~ 할 수 있는 놀이기구야. 마음대로 운전해도 돼. 범퍼카니까 말이야! 그래서… 죽음의 레이스를 했어. 이게 또 범퍼카의 묘미 아니겠어? 범퍼카에서 내리자 기념으로 **우승컵을 든 카레이서 카두스 포토카드**를 얻을 수 있었어.'
          elif SasaNum > 30 and SasaNum <= 33:
            Text = '퍼레이드길'
            Text2 = '멋진 퍼레이드가 진행되는 넓은 길이야. 운이 좋아 퍼레이드길에 도착하자마자 멋진 퍼레이드가 막 시작하고 있었어. 퍼레이드를 처음부터 볼 수 있었네. 시작 시간은 폼폼 마음대로라니 정말인가봐. 재밌었네! 퍼레이드를 구경한 기념으로 **퍼레이드를 구경하는 폼폼 아크릴 키링**을 얻을 수 있었어.'
          elif SasaNum > 33 and SasaNum <= 35:
            Text = '퍼레이드길'
            Text2 = '멋진 퍼레이드가 진행되는 넓은 길이야. 운이 좋지 않았던 걸까? 퍼레이드길에 도착하니 퍼레이드가 끝나가고 있었어. 아쉽지만 다음 시간을 노려야겠어. 시작 시간은 폼폼 마음대로라던데 시간을 잘 맞출 수 있을지 모르겠네. 퍼레이드를 구경한 기념으로 **꽃 바구니를 물고 꽃잎을 뿌리는 카두스 포토카드**를 얻을 수 있었어.'
          elif SasaNum > 35 and SasaNum <= 38:
            Text = '포토존'
            Text2 = '카두케우스 랜드를 한층 환상적으로 만들어주는 포토존이야. 기념사진을 찍기 좋게 꾸며져 있지. 포토존 여기저기를 돌아다니며 마음에 드는 사진들을 잔뜩 남겼어. 재밌었네! 포토존 방문 기념으로 **포토존에서 사진을 찍는 폼폼 아크릴 키링**을 얻을 수 있었어.'
          elif SasaNum > 38 and SasaNum <= 40:
            Text = '포토존'
            Text2 = '카두케우스 랜드를 한층 환상적으로 만들어주는 포토존이야. 기념사진을 찍기 좋게 꾸며져 있지. 포토존 여기저기를 돌아다니며 마음에 드는 사진을 찍을까 했는데… 어째 카두케우스 포토 판넬만 잔뜩 보이는 것 같네…. 포토존 방문 기념으로 **피할 수 없는 카두케우스 아크릴 스탠드**를 얻을 수 있었어.'
          elif SasaNum > 40 and SasaNum <= 43:
            Text = '스낵바'
            Text2 = '달달한 냄새가 풍겨 오는 스낵바야. 각종 간식이 있으니 먹고 싶은 간식을 원하는 만큼 먹어도 좋을 것 같아. 마침 간식들이 전부 넉넉하게 있어 먹고 싶은 만큼 다 먹을 수 있었어. 재밌었네! 스낵바 방문 기념으로 **스낵바에서 간식을 사 먹는 폼폼 아크릴 키링**을 얻을 수 있었어.'
          elif SasaNum > 43 and SasaNum <= 45:
            Text = '스낵바'
            Text2 = '달달한 냄새가 풍겨 오는 스낵바야. 각종 간식이 있으니 먹고 싶은 간식을 원하는 만큼 먹어도 좋을 것 같아. 비록 장난을 치는 폼폼에게 걸려 간식을 못 받는 가 싶었지만…! 결국 간식을 받아 맛있게 먹을 수 있었으니 된 게 아닐까? 스낵바 방문 기념으로 **스낵바에서 앙큼하게 츄러스를 입에 물고 있는 케우스 포토카드**를 얻을 수 있었어.'
          elif SasaNum > 45 and SasaNum <= 48:
            Text = '기념품점'
            Text2 = '다양한 굿즈들이 준비되어 있는 기념품점이야. 팝업스토어는… 알지? 일반스토어에도 다양한 물건들이 있으니 일반스토어 위주로 구경하기로 했어. 구경을 하다 원하는 상품이 있으면 구매했을지도 모르겠어. 재밌었네! 기념품점 방문 기념으로 **기념품점에서 기념품을 구매하는 폼폼 아크릴 키링**을 얻을 수 있었어.'
          elif SasaNum > 48 and SasaNum <= 50:
            Text = '기념품점'
            Text2 = '다양한 굿즈들이 준비되어 있는 기념품점이야. 여기서 카두케우스 포토카드를 보관할 탑로더나 탑로더를 꾸밀 수 있는 굿즈를 사도 좋을거야. 강력 추천할게. 기념품점 방문 기념으로 **카두케우스 탑로더**를 얻을 수 있었어.'
          elif SasaNum == 51:
            Text = '이것은?!'
            Text2 = '카두케우스 랜드를 즐기며 돌아다니다가 황금색 상자를 찾았어. 이건…! 신성 주간에만 발견할 수 있는 카두케우스 랜드의 상자. 일명 ***황금상자***야! 응? 별로 연관이 없는 것 같은데?'
          embed = discord.Embed(
                title = "신나는 카두케우스 랜드"
                ) 
        
          embed.add_field(name = Text, value = Text2, inline=False)
          await message.channel.send(embed=embed, reference = message)
	
    elif message.content.startswith('%%폼폼열쇠'):
          KeyNum = random.randrange(0,1000)
          KeyNum  = KeyNum % 20
          Text = " "
          Text2 = " "
       
          if KeyNum == 0:
            Text = '병원비 지불'
            Text2 = '병원에서 건강진단을 받았습니다. 병원비 [5만 온]을 람다 섹터 소유주에게 납부합니다. 람다 섹터의 소유자가 없다면 알파에 납부합니다.'
          elif KeyNum == 1:
            Text = '복권 당첨'
            Text2 = '축하합니다! 복권에 당첨되었습니다. 당첨금 [25만 온]을 알파 섹터에서 받습니다.'
          elif KeyNum == 2:
            Text = '교도소 탈출'
            Text2 = '숟가락을 얻었습니다. 교도소에 갇혀 있을 때 사용할 수 있습니다. 1회 사용 후 소멸합니다. 타인에게 팔 수 있습니다. 거래시 가격 협상은 자유롭게 해주세요.'
          elif KeyNum == 3:
            Text = '교도소'
            Text2 = '이단 의심을 받았습니다. 교도소로 곧장 가세요. 출발지를 지나더라도 월급을 받을 수 없습니다.'
          elif KeyNum == 4:
            Text = '20주년 기념 공연'
            Text2 = '뮤 섹터로 가세요. 뮤 섹터 소유주에게 통행료를 지불합니다. 출발지를 지나갈 경우, 월급을 받습니다.'
          elif KeyNum == 5:
            Text = '에타 유학'
            Text2 = '학교 등록금을 내세요. 등록금 [10만 온]을 에타 섹터 소유주에게 납부합니다. 에타 섹터의 소유자가 없다면 알파 섹터에 납부합니다.'
          elif KeyNum == 6:
            Text = '이동'
            Text2 = '뒤로 세 칸 옮기세요.'
          elif KeyNum == 7:
            Text = '우대권'
            Text2 = '상대방이 소유한 장소에 통행료 없이 머무를 수 있습니다. 1회 사용 후 반납합니다. 중요한 순간에 사용하세요.'
          elif KeyNum == 8:
            Text = '텔레포트 장치'
            Text2 = '오미크론 섹터의 텔레포트를 타고 카파 섹터로 가세요. 텔레포트 장치 소유주에게 탑승료를 지불합니다. 출발지를 지나갈 경우 월급을 받습니다.'
          elif KeyNum == 9:
            Text = '폼폼크루즈 여행'
            Text2 = '폼폼크루즈를 타고 엡실론 섹터로 가세요. 폼폼크루즈 소유주에게 탑승료를 지불합니다. 출발지를 지나갈 경우 월급을 받습니다.'
          elif KeyNum == 10:
            Text = '대륙일주 초대권'
            Text2 = '축하합니다. 현재 위치에서부터 한 바퀴 돌아오세요. 다른 곳으로 갈 수 없으며, 출발지를 지나가면서 월급을 받습니다. 신의 축복을 지나가면서 모아놓은 헌금을 받습니다.'
          elif KeyNum == 11:
            Text = '이달의 우수 신도 수상'
            Text2 = '당신은 텔로스 신을 위하여 공헌하였습니다. 수상금 [30만 온]을 알파 섹터에서 받습니다.'
          elif KeyNum == 12:
            Text = '생일 축하'
            Text2 = '모두에게 생일 축하를 받으세요. 생일 축하합니다! 전원에게 축하금 [1만 온]씩 받습니다.'
          elif KeyNum == 13:
            Text = '장학금 혜택'
            Text2 = '장학금을 받으세요. 장학금 [10만 온]을 에타 섹터 소유주에게서 받습니다. 에타 섹터의 소유자가 없다면 알파에서 받습니다.'
          elif KeyNum == 14:
            Text = '건물 수리비 지불'
            Text2 = '정기적으로 건물을 수리하여야 합니다. 수리비 [10만 온]을 요타 섹터 소유주에게 납부하세요. 요타 섹터의 소유자가 없다면 알파 섹터에 납부합니다.'
          elif KeyNum == 15:
            Text = '신의 축복'
            Text2 = '신의 축복으로 가세요. 출발지를 지나갈 경우 월급을 받습니다.'
          elif KeyNum == 16:
            Text = '대륙여행 초청장'
            Text2 = '오미크론 섹터에서 대륙여행 초정장이 왔습니다. 오미크론 섹터로 가세요. 무료이므로 텔레포트 장치 소유주에게 탑승료를 지불하지 않습니다. 출발지를 지나갈 경우 월급을 받습니다.'
          elif KeyNum == 17:
            Text = '헌금'
            Text2 = '신의 축복에 헌금 [20만 온]을 납부하세요.'
          elif KeyNum == 18:
            Text = '관광 여행'
            Text2 = '카두케우스 랜드로 가세요. 카두케우스 랜드 소유주에게 통행료를 지불합니다. 출발지를 지나갈 경우 월급을 받습니다.'
          elif KeyNum == 19:
            Text = '잭팟'
            Text2 = '축하합니다! 크사이 섹터의 카지노에서 잭팟을 터트렸습니다. [50만 온]을 알파 섹터에서 받습니다.'

          embed = discord.Embed(
          description = "폼폼열쇠",
          colour = discord.Color.red()
         )

          embed.add_field(name = Text, value = Text2, inline=False)
          await message.channel.send(embed=embed)
	
	
    elif message.content.startswith('%퀘스트'):
          QuestNum = random.randrange(1,1000)
          QuestNum = QuestNum % 6

          if QuestNum == 0:
            Text = '굿즈폼폼과 함께 카두케우스 굿즈 기획하기(0/1)'
            Text2 = '오늘도 굿즈 담당 폼폼이 무척 바빠보이네. 카두케우스 랜드의 모든 굿즈는 이 폼폼의 머리와 손을 거쳐서 나온다던데, 그 자그만 몸으로 혼자서 이 많은 굿즈를 모두 기획하려면 여간 고생이 아니겠는걸? 우리가 조금 도와주면 훨씬 수월해지지 않을까? 굿즈 폼폼을 도와 함께 새로운 카두케우스 굿즈를 기획해보자.'
          elif QuestNum == 1:
            Text = '정비폼폼과 함께 카두케우스 랜드 정비하기(0/5)'
            Text2 = '저기 멋지게 정비 고글을 쓴 폼폼이 보여? 이 넓고 화려한 카두케우스 랜드의 모든 놀이기구 및 장비를 담당한다는 정비 폼폼이야. 조그만 몸집을 지녔다는게 믿기지 않을 정도로 신속하고 정확하게 일을 처리하는 폼폼이지만, 최근 며칠은 자잘한 놀이기구 고장이 너무 많이 일어나는 바람에 혼자서 다 처리하기 영 버겁다고 하네. 왠지 안쓰러우니 조금 도와주도록 할까? 정비 폼폼을 도와 함께 카두케우스 랜드를 정비해보도록 하자.'
          elif QuestNum == 2:
            Text = '파도풀 폼폼과 정시마다 파도풀 작동 시키기(0/6)'
            Text2 = '일정시간마다 나오스베이 파도풀에 몰아치는 시원한 파도는 전부 보이지 않는 곳에서 파도풀 폼폼이 잊지 않고 성실하게 버튼을 눌러 인공 파도 발생 장치를 작동시켜주는 덕분이라고 해. 한번이라도 파도풀을 신나게 즐겨봤다면, 이번에는 다른 사람들을 즐겁게 만들어줄 파도를 일으키는 입장이 되어보는 것도 나쁘지 않을 거라고 파도풀 폼폼이 명랑하게 제안하는데… 제법 솔깃한걸? 파도풀 폼폼과 함께 정시마다 파도풀을 작동시켜보자.'
          elif QuestNum == 3:
            Text = '나오스베이 폼폼을 도와 일일 안전요원 체험하기(0/1)'
            Text2 = '수영장은 늘 안전 사고의 위험이 따르는 곳이지. 가득이나 선지자 후보들은 예측 불가인 사람들이 많아서 안전요원 일을 겸하는 폼폼들이 애를 먹고 있다나봐. 그 말을 하며 한숨을 쉬는 나오스베이 폼폼을 보니 어쩐지 미안해지는데… 조금이라도 도와서 마음 속의 죄책감을 덜어내볼까? 나오스베이 폼폼을 도와 일일 안전요원 체험을 해보자.'
          elif QuestNum == 4:
            Text = '후룸라이드 폼폼을 도와 일일 직원 체험하기(0/1)'
            Text2 = '카두케우스 랜드의 명물 중 하나는 역시 짜릿하고 시원한 후룸라이드지! 그런만큼 하루에 이용하는 사람이 많아서 후룸라이드 폼폼은 늘 눈코 뜰새 없이 바쁘다고 하네. 늘 우리를 즐겁게 만드는데 일조해주는 폼폼들의 노고를 생각하며, 오늘은 폼폼들과 같은 위치에서 도움을 좀 보태주도록 할까? 후룸라이드 폼폼을 도와 일일 후룸라이드 직원 체험을 해보자.'
          elif QuestNum == 5:
            Text = '온천에서 카두케우스 마사지해주기(0/1)'
            Text2 = '날씨의 변화없이 언제나 온화한 성역에서도 역시 따끈한 온천욕은 포기할 수 없는 즐거움이야. 선지자 후보들에게도, 폼폼들에게도, 그리고… 어라. 카두케우스한테도?! 다행히 지금 깨어있는 쪽은 카두스이니, 큰 문제는 없겠지만… 시선이 마주치자 꾸벅 고개를 숙여 반갑게 인사하는 하얀 머리의 뱀을 보니 기분이 묘하네. 마침 딱 폼폼들의 도움을 받아 온천 마사지를 받을 예정이었다나봐. 설마, 카두케우스가 지닌 물광 피부의 비결이…? 아무튼, 폼폼들만으론 마사지에 상당히 오랜 시간이 걸릴것 같다고 하니 살짝 도움을 보태볼까? 카두케우스에게 온천 마사지를 해주도록 하자.'
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
			
    elif message.content.startswith('%카케마불'):

          MarbleDice = random.randrange(1,6)
          MarbleDice2 = random.randrange(1,6)

          Text = ""
          Text = str(MarbleDice) + "  " + str(MarbleDice2) 

          Text2 = ""
          Text2 = Text2 + str(MarbleDice+MarbleDice2) + "칸 이동가능"

          embed = discord.Embed(
          description = Text ,
          colour = discord.Color.yellow()
         )
          embed.add_field(name = Text2, value=' ', inline=False)
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
