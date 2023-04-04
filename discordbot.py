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
             '편지지 세트', '알록달록한 펜', '애벌레 인형', '발냄새 나는 양말', '새하얀 깃털', '붕대', '누가 사탕', '민트초코맛 치약', '피젯큐브', '들장미 화관', '은색 반지', '네모나고 반듯한 돌', '카라쿠리 퍼즐', '종이 비행기', '계약서와 도장', '크롭티', '무지개색 조개껍데기', '묵주', '팬 라이트', '화려한 귀걸이', '별모양 드림캐쳐', '십자수 세트', '초콜릿 쿠키 만들기 키트', '도수가 높은 안경', '색이 바랜 머리끈', '존재도 의심스럽다는 10권 한정판 마공학 전문 서적', '저주 부적', '손목보호대', '빈 계약서 양식', '오선지', '빈 액자', '진통제', '정통 메이드복', '귀여운 스티커 모음', '시그마 섹터 발행 학술지', '청사초롱', '나비 인형', '딸기 탕후루 만들기 키트', '철학책 [죽음은 무엇인가]', '다이아 넥타이 핀', '찢어진 사진이 들어있는 캡슐', '낡은 고서 페이지', '시마니드 문양 팬던트', '보물지도']))  # 1~100 랜덤 선택 (1d100)
        await message.channel.send(f'달각 달각, 가챠 기계에서 나온 것은…… <{dice_result}>…!', reference=message)  # 답장 o
    elif message.content.startswith('%박물상자'): # 메세지가 %황금상자 로 시작하는 경우
        dice_result = str(random.choice(['먼지', '가챠 1회 무료 이용권', '슬롯머신 1회 무료 이용권(1텔로 적용)', '복권 1회 무료 이용권', '디카이오시네 기념 주화', '화석발굴키트', '공룡뼈조립키트', '공룡모형', '공룡옷(폼폼용)', '유물발굴키트', '하이로우 1회 무료 이용권(1텔로 적용)', '카두케우스 다키마쿠라', '빈백(폼폼용)', '판 꾸미기 아이템'])) # 1~100 랜덤 선택 (1d100)
        await message.channel.send(f'커다란 상자를 열자…… 안에 들어있던 것은…! <{dice_result}>입니다.', reference=message) # 답장 o        
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
        SasaNum = SasaNum % 42

        if SasaNum == 0:
            Text = '이것은?!'
            Text2 = '박물관을 구경하며 돌아다니다가 거대한 상자를 찾았어. 이건…! 신성 주간에만 발견할 수 있는 박물관의 상자. 일명 ***박물상자***야! 거대하네….'
        elif SasaNum >= 1 and SasaNum <= 3:
            Text = '중앙홀'
            Text2 = '둥근 중앙 홀로 들어서면 가장 먼저 거대한 공룡 뼈가 눈에 들어올거야. 아주 먼 옛날, 그러니까 신께서 이 땅을 떠나신 것보다도 훨씬 전의 세계는 어땠을까? 잠깐 사색에 잠겨보는 것도 좋을 것 같네. 중앙홀 관람 기념으로 ***중앙홀 뱃지***를 얻었어.'
        elif SasaNum > 3 and SasaNum <= 5:
            Text = '중앙홀'
            Text2 = '둥근 중앙 홀로 들어서면 가장 먼저 거대한 공룡 뼈가 눈에 들어올거야. 아주 먼 옛날, 그러니까 신께서 이 땅을 떠나신 것보다도 훨씬 전의 세계에는 이런 생물들도 살았던 거겠지. 새삼 재앙이 얼마나 무서운 것이었는지 느꼈네. 중앙홀 관람 기념으로  ***카두케우르사우르스 뱃지***를 얻었어.'
        elif SasaNum > 5 and SasaNum <= 8:
            Text = '인문관'
            Text2 = '인류사의 흐름을 되짚어볼 수 있는 곳이야. 인간이 이렇게 많은 발전을 했다는 걸 알 수 있었어. 이런 역사를 쌓아올릴 수 있던 것도 텔로스 신의 가호가 있어 가능했던거겠지. 인문관 관람 기념으로 ***인문관 뱃지***를 얻었어.'
        elif SasaNum > 9 and SasaNum <=10:
            Text = '인문관'
            Text2 = '인류사의 흐름을 되짚어볼 수 있는 곳이야. 재앙을 맞이하기 전의 문화에 대한 문헌 자료를 보니 새삼 재앙이 얼마나 많은 것을 앗아갔는지 생각하게 되었네. 인문관 관람 기념으로 ***우아하게 독서를 하는 카두스 뱃지***를 얻었어.'
        elif SasaNum > 10 and SasaNum <= 13:
            Text = '자연관'
            Text2 = '자연사의 흐름을 되짚어볼 수 있는 곳이야. 과거부터 현재까지 이어지는 자연의 역사를 시대 순으로 감상할 수 있지. 재앙 이전의 자료들이 유실된 건 아쉽지만… 어쩔 수 없는거겠지. 시그마 학자들의 분석과 유추로 만족하자. 자연관 관람 기념으로 ***자연관 뱃지***를 얻었어.'
        elif SasaNum > 13 and SasaNum <= 15:
            Text = '자연관'
            Text2 = '자연사의 흐름을 되짚어볼 수 있는 곳이야. 과거부터 현재까지 이어지는 자연의 역사를 시대 순으로 감상할 수 있다는데… 유독 뱀 생태계에 대한 설명이 눈에 들어오는 건 기분탓일까? 자연관 관람 기념으로 *** 사족보행 케우스 뱃지***를 얻었어.'
        elif SasaNum > 15 and SasaNum <= 18:
            Text = '과학관'
            Text2 = '이 곳에서는 과학사의 흐름을 살펴볼 수 있대. 특히 마공학에 관련된 부분이 눈에 들어오네. 마공학의 등장 이후로는 순수과학의 비중이 확 줄어들었다나봐. 지식이 늘어난 것 같아 유익한 시간이었네. 과학관 관람 기념으로 ***과학관 뱃지***를 얻었어.'
        elif SasaNum > 18 and SasaNum <= 20:
            Text = '과학관'
            Text2 = '이 곳에서는 과학사의 흐름을 살펴볼 수 있대. 음, 음, 그렇구나. 하는 기분으로 과학관을 돌아보았어. 조금 어려운 느낌이긴 했지만, 그럴수도 있지! 각종 전시품들은 신기해보였네. 과학관 관람 기념으로 ***과학자 가운과 뱅글이 안경을 착용한 카두스 뱃지***를 얻었어.'
        elif SasaNum > 20 and SasaNum <= 23:
            Text = '미술관'
            Text2 = '이 곳에서는 미술사의 흐름을 살펴볼 수 있대. 예술에 비중을 엄청 둔 느낌이지? 다양한 미술 분야의 작품을 시대 순으로 따라가며 예술의 발전을 한 눈에 본 기분이네. 예술은 이런식으로 발전해왔구나. 미술관 관람 기념으로 ***미술관 뱃지***를 얻었어.'
        elif SasaNum > 23 and SasaNum <= 25:
            Text = '미술관'
            Text2 = '이 곳에서는 미술사의 흐름을 살펴볼 수 있대. 예술에 비중을 엄청 둔 느낌이지? 다양한 미술 분야의 작품이 있어. 이상하게 뱀과 관련된 예술 작품을 많이 본 느낌이지만…. 착각… 이겠지? 미술관 관람 기념으로 ***조각같은 몸매를 뽐내는 케우스 뱃지***를 얻었어.'
        elif SasaNum > 25 and SasaNum <= 28:
            Text = '육지관'
            Text2 = '본격적인 육지 생태계를 살펴볼 수 있는 곳이야. VR 마도구를 통해 다양한 생물을 확인해 볼 수 있었어. 물론, 멸종한 생물도 포함이었지. 유익한 시간이었네. 육지관 체험 기념으로 ***육지관 뱃지***를 얻었어.'
        elif SasaNum > 28 and SasaNum <= 30:
            Text = '육지관'
            Text2 = '본격적인 육지 생태계를 살펴볼 수 있는 곳이야. VR 마도구를 통해 다양한 생물을 확인해 볼 수 있었어. 어쩐지 뱀만 보고 나온 기분이지만… 다음엔 다른 생물도 봐볼까 싶네. 육지관 체험 기념으로 ***지층을 감싸고 있는 카두스 뱃지***를 얻었어.'
        elif SasaNum > 30 and SasaNum <= 33:
            Text = '바다관'
            Text2 = '마치 바다 속에 있는 것처럼 해양 생태계를 살펴볼 수 있는 곳이야. VR 마도구를 통해 바닷속에 들어간 기분을 느낄 수 있었지. 바닷속에는 이렇게 많은 생물들이 사는구나. 유익한 시간이었네. 바다관 체험 기념으로 ***바다관 뱃지***를 얻었어.'
        elif SasaNum > 33 and SasaNum <= 35:
            Text = '바다관'
            Text2 = '마치 바다 속에 있는 것처럼 해양 생태계를 살펴볼 수 있는 곳이야. VR 마도구를 통해 바닷속에 들어간 기분을 느낄 수 있었지. 설정을 잘못했던 탓일까? 너무 깊숙한 곳으로 들어와버렸나봐. 깜깜한 바닷속과 가끔씩 보이는 기괴하게 생긴 심해 생물들만 볼 수 있었네. 바다관 체험 기념으로 ***인어 케우스 뱃지***를 얻었어.'
        elif SasaNum > 35 and SasaNum <= 38:
            Text = '하늘관'
            Text2 = '우리가 살아가는 땅의 대기 구성과 분포에 대한 설명이 포함되어 있는 곳이야. VR 마도구를 통해 비행생물을 확인해볼 수 있었네. 평소엔 듣기 힘든 새의 울음 소리를 들을 수 있었어. 유익한 시간이었네. 하늘관 체험 기념으로 ***하늘관 뱃지***를 얻었어.'
        elif SasaNum > 38 and SasaNum <= 40:
            Text = '하늘관'
            Text2 = '우리가 살아가는 땅의 대기 구성과 분포에 대한 설명이 포함되어 있는 곳이야. VR 마도구를 통해 비행생물을 확인해볼 수 있었네. 눈 앞으로 익룡떼가 지나갔어! 으악! 깜짝 놀라버렸네…. 하늘관 체험 기념으로 ***성스러운 빛을 내뿜는 카두케우스 뱃지***를 얻었어.'
        elif SasaNum == 41:
            Text = '이것은?!'
            Text2 = '박물관을 구경하며 돌아다니다가 거대한 상자를 찾았어. 이건…! 신성 주간에만 발견할 수 있는 박물관의 상자. 일명 ***박물상자***야! 거대하네….'
        embed = discord.Embed(
            title = "신나는 박물관 관람"
        )

        embed.add_field(name = Text, value = Text2, inline=False)
        await message.channel.send(embed=embed, reference = message)

    elif message.content.startswith('%폼폼열쇠'):
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
            Text2 = '상대방이 소유한 장소에 통행료 없이 머무를 수 있습니다. 한 번에 한 장만 소유할 수 있으며, 1회 사용 후 반납합니다. 중요한 순간에 사용하세요.'
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

    elif message.content.startswith('%카케열쇠'):
        KeyNum = random.randrange(0,1000)
        KeyNum  = KeyNum % 21
        Text = " "
        Text2 = " "

        if KeyNum == 0:
            Text = '병원비 지불'
            Text2 = '부상을 입어 병원에 방문하여 치료를 받았습니다. 병원비 [20만 온]을 람다 섹터 소유주에게 납부합니다. 람다 섹터의 소유자가 없다면 알파에 납부합니다.'
        elif KeyNum == 1:
            Text = '투자 실패'
            Text2 = '새로운 기술 연구에 투자했으나… 성과가 없었습니다. 투자비 [50만 온]을 잃습니다.'
        elif KeyNum == 2:
            Text = '교도소 탈출'
            Text2 = '숟가락을 얻었습니다. 교도소에 갇혀 있을 때 사용할 수 있습니다. 1회 사용 후 소멸합니다. 타인에게 판매할 수 있습니다. 거래시 가격 협상은 자유롭게 해주세요.'
        elif KeyNum == 3:
            Text = '교도소'
            Text2 = '이단 의심을 받았습니다. 교도소로 곧장 가세요. 출발지를 지나더라도 월급을 받을 수 없습니다.'
        elif KeyNum == 4:
            Text = '20주년 기념 공연 굿즈 구매'
            Text2 = '뮤 섹터로 가세요. 뮤 섹터 소유주에게 통행료와 굿즈 구입비 [20만 온]을 지불합니다. 출발지를 지나갈 경우, 월급을 받습니다. '
        elif KeyNum == 5:
            Text = '에타 유학'
            Text2 = '학교 등록금을 내세요. 등록금 [10만 온]을 에타 섹터 소유주에게 납부합니다. 에타 섹터의 소유자가 없다면 알파 섹터에 납부합니다.'
        elif KeyNum == 6:
            Text = '이동'
            Text2 = '뒤로 세 칸 옮기세요.'
        elif KeyNum == 7:
            Text = '바가지'
            Text2 = '상대방이 소유한 장소에 1.5배의 통행료를 내고 머무를 수 있습니다. 이 카케열쇠를 뽑은 후 처음으로 도착하는 섹터에 자동으로 적용되며, 1회 적용 후 사라집니다. 본인의 팀이 소유한 섹터에는 적용되지 않습니다.'
        elif KeyNum == 8:
            Text = '텔레포트 장치'
            Text2 = '오미크론 섹터의 텔레포트를 타고 카파 섹터로 가세요. 텔레포트 장치 소유주에게 탑승료와 팁 [10만 온]을 지불합니다. 출발지를 지나갈 경우 월급을 받습니다.'
        elif KeyNum == 9:
            Text = '폼폼크루즈 여행'
            Text2 = '폼폼크루즈를 타고 엡실론 섹터로 가세요. 폼폼크루즈 소유주에게 탑승료와 팁 [10만 온]을 지불합니다. 출발지를 지나갈 경우 월급을 받습니다.'
        elif KeyNum == 10:
            Text = '대륙일주 초대권'
            Text2 = '축하합니다. 현재 위치에서부터 한 바퀴 돌아오세요. 다른 곳으로 갈 수 없으며, 출발지를 지나가면서 월급을 받습니다. 신의 축복을 지나가면서 모아놓은 헌금을 받습니다.'
        elif KeyNum == 11:
            Text = '이달의 우수 신도 수상'
            Text2 = '당신은 텔로스 신을 위하여 공헌하였습니다. 수상금 [60만 온]을 알파 섹터에서 받습니다.'
        elif KeyNum == 12:
            Text = '파티 초대권'
            Text2 = '선지자 후보들 앞에서 장기자랑을 하세요. 다른 게임 참가자들이 정한 상금을 알파 섹터에서 지불합니다. 상금은 최소 10만 온에서 최대 50만 온 까지 지정이 가능합니다. 장기자랑을 하지 않을 시에는 벌금을 10만 온 지불해야 합니다.'
        elif KeyNum == 13:
            Text = '장학금 혜택'
            Text2 = '장학금을 받으세요. 장학금 [20만 온]을 에타 섹터 소유주에게서 받습니다. 에타 섹터의 소유자가 없다면 알파 섹터에서 받습니다.'
        elif KeyNum == 14:
            Text = '건물 수리비 지불'
            Text2 = '정기적으로 건물을 수리하여야 합니다. 수리비 [소유한 랜드마크 수 x 10만 온]을 요타 섹터 소유주에게 납부하세요. 요타 섹터의 소유자가 없다면 알파 섹터에 납부합니다.'
        elif KeyNum == 15:
            Text = '세금 납부'
            Text2 = '세금을 내야 합니다. [소유한 섹터 수 x 10만 온]을 알파 섹터에 납부하세요. '
        elif KeyNum == 16:
            Text = '대륙여행 초청장'
            Text2 = '오미크론 섹터에서 대륙여행 초정장이 왔습니다. 오미크론 섹터로 가세요. 무료이므로 텔레포트 장치 소유주에게 탑승료를 지불하지 않습니다. 출발지를 지나갈 경우 월급을 받습니다.'
        elif KeyNum == 17:
            Text = '신의 축복'
            Text2 = '신의 축복으로 가세요. 출발지를 지나갈 경우 월급을 받습니다.'
        elif KeyNum == 18:
            Text = '헌금'
            Text2 = '신의 축복에 헌금 [40만 온]을 납부하세요.'
        elif KeyNum == 19:
            Text = '관광 여행'
            Text2 = '카두케우스 랜드로 가세요. 카두케우스 랜드 소유주에게 통행료와 기념품 구입비 [20만 온]을 지불합니다. 출발지를 지나갈 경우 월급을 받습니다. '
        elif KeyNum == 20:
            Text = '밑장빼기'
            Text2 = '이런. 크사이의 카지노에서 밑장을 빼다 걸렸습니다. 벌금으로 [50만 온]을 크사이 섹터 소유주에게 지불합니다.'

        embed = discord.Embed(
            description = "카두케우스 열쇠",
            colour = discord.Color.purple()
        )

        embed.add_field(name = Text, value = Text2, inline=False)
        await message.channel.send(embed=embed)

    elif message.content.startswith('%퀘스트'):
        QuestNum = random.randrange(1,1000)
        QuestNum = QuestNum % 6

        if QuestNum == 0:
            Text = '사서폼폼을 도와 장서관 책 제자리에 꽂기 (0/10)'
            Text2 = '장서관의 사서폼폼은 언제나 바빠. 혼자서 그 넓고 커다란 장서관의 장서들을 항상 제자리에 배열하고 관리하는 건 결코 쉬운 일이 아니거든. 가득이나 일손이 부족한 탓에 늘 중노동에 시달리느라 안색이 영 좋지만은 않은 모양인데… 기왕 이렇게 된 거, 우리가 좀 도와주도록 할까? 사서 폼폼을 도와 장서관의 책들을 원래 있던 서가의 자리에 꽂아주자.'
        elif QuestNum == 1:
            Text = '아기폼폼 이유식 먹이기(0/10)'
            Text2 = '요람을 둘러싼 폼폼들이 엄청 분주해보이네. 배고픈 아기 폼폼들에게 이유식을 먹일 시간인 모양인데… 이런, 요람이 저렇게나 많은데 하나같이 울음소리가 들리는 걸 보면 아무래도 배고파서 잠이 깬 한 아기폼폼의 울음소리에 다른 아기폼폼들도 덩달아 깨서 우는 모양이야. 폼폼들이 곤란해보이니 좀 도와줄까? 아기폼폼들에게 이유식을 먹이자.'
        elif QuestNum == 2:
            Text = '아기폼폼 이유식 만들기(0/10)'
            Text2 = '어디선가 우렁찬 울음소리가 들리고 있어. 고개를 돌려보니 요람 속의 아기 폼폼 하나가 큰 소리로 울고 있네. 아무래도 배가 고픈 모양인데… 하필 어른 폼폼들이 다들 일하느라 바빠서 이유식을 만들어줄 수 있는 상황이 아닌가봐. 아마 주방에 가면 폼폼 전용 이유식을 만드는 재료가 있을텐데… 살짝 도움을 주도록 할까? 아기 폼폼에게 먹일 이유식을 만들도록 하자.'
        elif QuestNum == 3:
            Text = '카두스를 위한 인형 만들기(0/1)'
            Text2 = '이번에도 폼폼들이 부산스럽게 움직이고 있어. 무슨 일인가 싶어서 다가가보니 글쎄, 일전에 케우스님에게 인형을 만들어 드렸더니 카두스님이 자신을 위한 인형은 없다는 사실에 내심 섭섭해하셔서 비상이 걸렸다지 뭐야. 아무래도 카두스를 위해 뭐라도 인형을 만들어줘야할 것 같은데… 폼폼들이 참 고생이 많아. 그치? 평소에 다정하게 아이들을 대하는 카두스에게는 그래도 케우스에 비해 대체로 유감이 덜하기도 해서 그리 거부감이 드는 사안은 아니니… 조금 도와주도록 할까? 카두스에게 선물할 인형을 만들자.'
        elif QuestNum == 4:
            Text = '전시회장의 경비폼폼을 도와 일일 경비 서기(0/1)'
            Text2 = '전시회장에는 귀중한 전시품들이 많은 탓에, 경비 폼폼이 24시간 내내 불철주야 내부 순찰을 돌며 수고를 해주고 있다고 해. 자신은 아주 강인한 폼폼이지만, 아무래도 혼자 모든 관의 경비를 돌다보니 종종 놓치는 부분도 있을 것 같고 거듭된 철야로 인한 피로도 상당해서 하루라도 좋으니 경비 서는 걸 도와줄 수 있겠냐고 부탁해오는데… 좀 안쓰러우니 살짝 도와주도록 할까? 경비 폼폼을 도와 전시회장에서 일일 경비를 서보자.'
        elif QuestNum == 5:
            Text = '공예관에서 폼폼 침대 만들어주기(0/1)'
            Text2 = '공예관에는 정말 다양한 장비가 구비되어 있어서 마음만 먹으면 누구나 원하는 걸 만들 수 있다고 해. 그게 사람용이든, 폼폼용이든 가리지 않고 말야. 마침 최근에 폼폼들 중 몇몇이 모여서 침대가 너무 낡은 탓에 불편해서 통 못 잤다면서 푸념을 늘어놓는 걸 얼핏 들은 기억이 있는데… 늘 수고하는 폼폼들의 숙면을 위해, 조그만 선물을 하나 해주도록 할까? 공예관에서 폼폼용 침대를 만들어보자.'
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
            colour = discord.Color.purple()
        )
        embed.add_field(name = Text2, value=' ', inline=False)
        await message.channel.send(embed=embed, reference = message)

    elif message.content.startswith('%하이로우'):

        HighLow = random.randrange(1,7)
        HighLow2 = random.randrange(1,7)

        Text = ""
        Text = str(HighLow + HighLow2)

        embed = discord.Embed(
        description = "높은 수일까, 낮은 수일까? 결과는... " ,
        colour = discord.Color.purple()
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
