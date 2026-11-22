# 사용 기반("learn by doing") 캐릭터 성장 시스템: 설계 방식, 반복된 실패, 개발자·연구자의 결론

> **작성 기준 (보고서 작성자용 범례)**
> - **[1차]** 개발자 본인의 글·발언을 직접 열어 확인한 것. **[2차]** 언론이 개발자 발언을 인용·요약한 것(원문은 직접 열지 못함). **[위키]** 팬/커뮤니티 위키(메커니즘 수치 확인용, 개발자 의도의 증거는 아님). **[통설]** 커뮤니티에서 널리 믿지만 1차 근거를 찾지 못한 것.
> - 인용문은 원문 언어 그대로 두었다. 열어보지 못한 자료는 Gaps에 명시했다. 위키 수치는 2026-11 시점에 내려받은 판본이며 패치에 따라 달라질 수 있다.
> - 조사 시점: 2026-11-19. 일부 사이트(UO Stratics, Fandom, pzwiki 등)는 직접 접근이 막혀 Wayback Machine 사본을 읽었고, 해당 링크는 아카이브 URL로 표기했다.

---

## 1. 각 게임의 사용 기반 성장 시스템은 구체적으로 어떻게 작동했고, 무엇이 잘못되었으며, 설계자는 어떻게 대응했는가

### Takeaway
거의 모든 사용 기반 시스템은 같은 경로를 밟았다. "행동 = 성장"이라는 규칙이 (a) 가장 싸고 안전한 반복 행동(벽에 달리기, 점프, 아군 때리기, 매크로)을 낳고, (b) 개발자가 그 구멍을 막으려고 만든 보정 장치가 다시 새 구멍이나 불만을 낳았다. 대응은 크게 세 방향이었다. ① 성장을 "결과(results)" 기반이나 시간 기반으로 옮기거나, ② 캡·감쇠·난이도 조건으로 행동 보상을 깎거나, ③ 아예 클래스/레벨 구조로 되돌렸다(FF III, SWG NGE, Skyrim의 단순화).

### Cited Findings

#### Ultima Online (UO)
- **기본 정의와 초기 설계.** Koster는 사용 기반 시스템을 "every time you use the skill, you have a chance of improvement"로 정의한다. UO는 "straight-up use-based"였고, 원래는 다른 사람이 스킬 쓰는 것을 *관찰*해도 오를 확률이 있었으며, 과제 난이도 개념이 없어 "너무 쉬워서 못 배운다"는 판정이 불가능했다. 쓰지 않는 스킬은 원래 감쇠했고, 총 700 스킬 포인트 캡에 닿은 뒤 한 점을 얻으면 다른 어딘가에서 한 점이 자동으로 빠졌다(Koster의 기억에 의한 서술). — [Raph Koster, "Use-based systems" (2006-07-18) [1차]](https://www.raphkoster.com/?p=592)
- **1차 실패: 스킬별 사용 빈도 차이.** 검(swords)은 자주 휘두르고 spirit speak는 드물게 쓰므로, 동일 확률이면 검이 너무 빨리 마스터된다. 팀은 사용 빈도를 동적으로 추적해 빈도가 높은 스킬의 성공 확률을 낮추는 "자기 균형" 장치를 만들었다. Koster 평: "It didn't work." 기준선이 없어 모든 것이 점점 느려졌고, 플레이어는 "1000번에 한 번" 오르는 것을 노리고 매크로를 돌렸다(확률은 다시 1/10,000이 됨). "What broke was the feedback mechanism — the reward of advancement came so incredibly infrequently that playing 'the right way' no longer had any incentives." — [Koster, Use-based systems [1차]](https://www.raphkoster.com/?p=592)
- **"난이도 있는 도전에서만 성장" 시도의 부작용.** 연습용 허수아비처럼 이미 아는 일을 반복해서는 오르지 않게 하자 "Soon people started trapping powerful monsters in their houses to macro on instead. Ooops." — [Koster [1차]](https://www.raphkoster.com/?p=592)
- **8×8 매크로(결정론적 난수 시드 문제).** 지도는 8×8 타일 "chunk"로 나뉘고 자원은 "chunk egg"라는 고유 ID 오브젝트에 저장됐다. 시스템 시계 대신 chunk egg ID로 난수를 시드하면(Koster가 자문에서 제안) 같은 사람·스킬·레벨은 같은 결과가 나와 "he'd be guaranteed to fail there until the heat death of the universe"가 된다. 의도는 플레이어가 이동하게 하는 것이었지만 플레이어들이 "pure scientific experimentation"으로 8타일 이동 후 성공률이 오른다는 것을 알아내 "8×8 macroing"이 생겼다. Koster는 이를 법칙의 사례로 든다: "No matter what you do, players will decode every formula, statistic, and algorithm in your world via experimentation." — [Koster [1차]](https://www.raphkoster.com/?p=592)
- **이후 대응.** Koster가 팀을 떠난 뒤 Runesabre가 빈도 기반 표를 손으로 쓴 advancement 표로 대체했다. Koster: 이 표는 "will always need to be updated as players discover exploits"이므로 사용 빈도 지표를 반드시 유지하라. 이후 "guaranteed gain"과 "power hour" 같은 "increasingly outré systems"가 필요해졌고, Koster는 그 논리를 모른다고 했다. — [Koster [1차]](https://www.raphkoster.com/?p=592)
- **Koster가 밝힌 매크로 전쟁의 동기.** "we waged a silent war against macroing from very early on — not because of the gold farmers, as that was much less of a concern back then, but because of the basic mechanics of a use-based system." — [Koster [1차]](https://www.raphkoster.com/?p=592)
- **Power hour (공식 팀 코멘트, 2001-09-20).** 공식 설명: power hour는 플레이어가 "normal game play"(스킬 성장 극대화를 목적으로 행동을 맞추지 않는 플레이)로 스탯·스킬을 얻도록 돕기 위해 설계되었다. 그러나 개발팀 스스로 세 가지 부작용을 적었다. (1) "Excessive power gaming potential" — 캐주얼의 확률을 올려주는 동시에 하드코어가 훨씬 쉽게 극단으로 몰아 캐릭터를 단시간에 맥스로 만들 수 있다. (2) "Only modest benefit to casual players" — 시스템이 하루 1시간 플레이를 가정하는데 실제로는 주 1~2일 몰아서 하는 사람이 많다. (3) "Unintuitive for new players" — 켜졌다 꺼졌다 하는 성장 결과를 일부러 가르쳐야 한다. — [UO Stratics Team Comment, 2001-09-20 (Wayback 사본) [1차]](https://web.archive.org/web/2023/https://uo.stratics.com/content/interviews/prophet.shtml)
- **같은 코멘트가 제시한 "원하는 스킬 성장 시스템" 요건.** 일상 플레이에서 성장할 것("essentially guaranteed to gain some amount of skill during any casual play session, provided they use their skills in ways that are at least mildly challenging"), 어느 정도의 파워게이밍 지원, 풀 육성에 합리적으로 긴 총 시간, 그리고 성장 행동이 현재 레벨에 맞아야 할 것("they should not have to gain skill through the repeated failure of a very difficult task, and they should not be able to easily gain skill through the repetition of overly easy tasks"). — [Team Comment 2001-09-20 [1차]](https://web.archive.org/web/2023/https://uo.stratics.com/content/interviews/prophet.shtml)
- **Guaranteed Gain System (GGS), Publish 16 (2002-07-23).** 사용 기반 판정에 "추가"되는 장치다. 성공한 사용이 있었는데 일정 시간 성장이 없으면 최소 0.1을 강제 지급한다. 실패한 사용은 GGS에 카운트되지 않는다. 타이머는 서버 시계 기준이라 로그오프 중에도 흐르고, 총 스킬 포인트가 높을수록 타이머가 길어진다. 난이도 기반 스킬은 현재 레벨 부근에서 성공할 때만 보장되며, 예컨대 Magery 90에서 Magic Arrow를 쏴도 GGS로도 오르지 않는다. 공식 표의 예상 간격(0.1 상승당): 총 700포인트일 때 0~4.9 구간은 5분, 40~44.9는 1.8시간, 80~84.9는 15시간, 115~120은 51시간. 스탯 상승은 30분당 1점, 하루 6점 상한. — [UO.com Publish 16 [1차]](https://uo.com/wiki/ultima-online-wiki/technical/previous-publishes/2002-2/2002-publish-16-part-2-23rd-july/), [UO.com GGS 설명](https://uo.com/?p=6342), [Team Comment 2001-09-20 [1차]](https://web.archive.org/web/2023/https://uo.stratics.com/content/interviews/prophet.shtml)
- **익스플로잇 단속 증언.** 초기 개발자 Chris Mayer는 서비스 초기에 "raise a player's skill in a way that went against the game's design principles"하는 익스플로잇 사용자를 추적하는 일을 맡았다고 회고한다. — [Game Developer, "Braving Britannia" 발췌 (2018-07-13) [2차]](https://gamedeveloper.com/design/book-excerpt-a-behind-the-scenes-look-at-building-i-ultima-online-i-)
- **Koster의 사후 평가.** SWG 글에서: "In UO, of course, we were using a use-based skill system. The issues there are many. It encourages grinding." — [Koster, "Designing a Living Society in SWG, part one" (2015-04-21) [1차]](https://www.raphkoster.com/?p=25717)

#### Daggerfall / Morrowind / Oblivion / Skyrim (The Elder Scrolls)
- **Daggerfall.** Arena의 경험치 시스템을 "플레이어가 역할을 실제로 수행하는 것을 보상하는" 시스템으로 대체했다는 서술. — [Wikipedia: Daggerfall [2차]](https://en.wikipedia.org/wiki/The_Elder_Scrolls_II:_Daggerfall). 스킬 캡 규칙: 3개 Primary 스킬 중 하나가 100이 되어 "mastered"되면 다른 모든 스킬의 자연 최대치는 95가 된다. — [UESP Daggerfall:Skills [위키]](https://en.uesp.net/wiki/Daggerfall:Skills)
- **Morrowind 스킬 성장.** 27개 스킬, 클래스당 Major 5·Minor 5·Misc 17. 스킬은 주로 사용으로 오르며, 행동별 고정 값이 쌓인다(Athletics로 1초 달리기 0.02, 매우 좋은 흥정 Mercantile 30). 필요량 = (SkillValue+1) × ClassFactor(Major 0.75 / Minor 1 / Misc 1.25) × Specialization(해당 전문 분야 0.8). 트레이너·스킬북·퀘스트 보상으로도 직접 올릴 수 있다. — [UESP Morrowind:Skills [위키]](https://en.uesp.net/wiki/Morrowind:Skills)
- **Morrowind 레벨업 규칙.** Major/Minor 스킬 상승 10회가 쌓이면 휴식 시 레벨업(Misc는 진행도에 불산입). 올릴 속성 3개를 고르는데, 해당 레벨 동안 그 속성 관할 스킬(Misc 포함)이 오른 횟수에 따라 배수 ×1(0회), ×2(1~4), ×3(5~7), ×4(8~9), ×5(10+)가 붙는다. Luck은 배수가 없다. 모든 속성 100 이후의 추가 레벨은 Health +10 외에 사실상 보상이 없다. — [UESP Morrowind:Level [위키]](https://en.uesp.net/wiki/Morrowind:Level)
- **Morrowind 최적화 문제.** UESP는 속성 배수를 맞추려면 각 속성마다 Misc 스킬을 최소 하나 남겨두라는 캐릭터 생성 요령과, 매 레벨업에 ×5 배수 두 개를 노리는 계획 레벨링을 설명한다. Morrowind는 총 2300회 스킬 상승을 허용하고 ×5 배수를 끝까지 채우는 데 최대 840회만 필요하므로 "extraneous" 상승은 낭비해도 된다고 적는다. — [UESP Morrowind:Level [위키]](https://en.uesp.net/wiki/Morrowind:Level)
- **Soren Johnson의 Morrowind 사례.** "A classic example is the skill system from Morrowind, which rewards players for repeating any activity. Running into a wall for hours increases the Athletics skill while jumping over and over again increases the Acrobatics skill. Many players couldn't stop themselves from spending hours doing mindless activities for these cheap rewards." — [Soren Johnson, Game Developer 칼럼 17 [1차]](https://www.designer-notes.com/game-developer-column-17-water-finds-a-crack/)
- **Oblivion 레벨업.** Major 스킬 합산 10회 상승이 레벨업 조건(Minor는 레벨업 진행에 불산입), 침대에서 휴식해야 반영. 레벨업 때 3개 속성을 올리며, 직전 레벨 동안 그 속성 관할 스킬(Major+Minor)이 오른 횟수에 따라 +1(0회)/+2(1~4)/+3(5~7)/+4(8~9)/+5(10+). — [UESP Oblivion:Leveling [위키]](https://en.uesp.net/wiki/Oblivion:Leveling)
- **"Leveling Problem".** UESP: 대부분의 일반 NPC가 플레이어와 함께 레벨업하고 소환되는 크리처도 레벨에 따라 바뀌며, 15레벨부터는 스탯이 플레이어 레벨에 직접 연동되는 변종이 나온다(예: Ogre는 플레이어가 레벨업할 때마다 체력 26 증가). 반면 플레이어는 레벨업이 곧 전투력 상승이 아니다. Speechcraft·Mercantile만 훈련해 레벨을 올리면 적만 강해지고, Blade와 Strength가 100이 되면 이후 레벨은 칼 피해를 올리지 못하는데 적 체력은 계속 오른다. 결론: "it is very possible for leveling up to decrease the player's combat effectiveness relative to enemies. This issue is sometimes known as the 'Leveling Problem.'" 레벨 10~15 부근에서 난이도가 급등한다고 서술. — [UESP Oblivion:Leveling [위키]](https://en.uesp.net/wiki/Oblivion:Leveling)
- **"Efficient Leveling"(UESP 용어).** 매 레벨업마다 세 속성 모두에 +5가 붙도록 관할 스킬을 정확히 10포인트씩 올리는 전략으로, 5/5/5 방식은 레벨당 Minor 20 + Major 10 포인트가 필요하며 "extensive planning and careful training"이 필요하다. UESP는 필수가 아니라고 하면서도 하는 이유를 "because they enjoy the process of optimization" 등으로 적는다. — [UESP Oblivion:Efficient Leveling [위키]](https://en.uesp.net/wiki/Oblivion:Efficient_Leveling), [UESP Oblivion:Leveling [위키]](https://en.uesp.net/wiki/Oblivion:Leveling)
- **레벨업과 스킬 캡의 어긋남.** Major 스킬이 모두 100이 된 후에도 레벨을 올리는 법으로, 제한 100을 넘기는 무료 스킬 부스트로 진행도를 쌓거나, 감옥 복역으로 Major 스킬을 깎은 뒤 다시 올린다는 방법이 UESP에 문서화되어 있다. — [UESP Oblivion:Leveling [위키]](https://en.uesp.net/wiki/Oblivion:Leveling)
- **Oblivion 클래스 선택 문제 (Todd Howard).** Game Informer 팟캐스트에서: "What we found in Oblivion is people would play, and even though they played for a half hour and then they picked their class, it's still – in the scheme of the games we make – not enough time to really understand all the skills and how they work. So people would play, and the general pattern would be they'd play for like, three hours and then 'oh I picked the wrong skills, I'm going to start over'". Skyrim의 해법은 "You just play, and your skills go up as you play and the higher your skill, the more it affects your leveling." — [PlayStation Universe, 2011-02-07 (Game Informer 팟캐스트 인용) [2차]](https://www.psu.com/news/bethesda-explains-elder-scrolls-v-classes-axe/)
- **Skyrim 속성 단순화 (Howard, IGN 인용).** "In Oblivion you have your eight attributes and 21 skills. Now you have 18 skills and three attributes." / "What we found is that all those attributes actually did something else." / "Now when you level up you can just raise your Magicka." — [GameBanshee가 전한 IGN "Five Changes from Oblivion to Skyrim" (2011-04) [2차]](http://www.gamebanshee.com/k638)
- **Bruce Nesmith의 속성 제거 발언.** Press Box PR 인터뷰에서 자신이 "led the charge"했다고 말하며, "It was about getting the character system out of the player's way. You don't have your head buried in menus, stats and rules." 또 "We got rid of attributes in Skyrim and you know who complained? Almost nobody… I love the whole idea that you do something, you get better at it. That's now a hallmark of the Elder Scrolls series because you play the character you want to play and you just get better at playing that character." — [GamesRadar (Press Box PR 인터뷰 인용) [2차]](https://www.gamesradar.com/games/rpg/we-got-rid-of-attributes-in-skyrim-and-you-know-who-complained-almost-nobody-former-bethesda-lead-pushed-for-a-streamlined-rpg-where-you-dont-have-your-head-buried-in-menus-stats-and-rules)
- **Nesmith의 Oblivion 레벨 스케일링 평가.** VideoGamer 인터뷰(Oblivion Remastered 출시 직후 보도): 자신이 두 레벨링 시스템 모두에 "very substantial hand and voice"가 있었고 수치 로직은 자신의 작업이었다고 하면서 "I think the world leveling with you was a mistake, and that's proven out by the fact it did not happen the same way in Skyrim." Skyrim은 "much, much better"이며 "'the dungeon went up in levels with me.'" 같은 무의미감을 피한다고 평가. — [GamesRadar (VideoGamer 인터뷰 인용) [2차]](https://www.gamesradar.com/games/the-elder-scrolls/as-oblivion-remastered-introduces-new-fans-to-bethesdas-iconic-2006-rpg-ex-elder-scrolls-dev-admits-the-level-scaling-system-was-a-mistake-eventually-fixed-in-skyrim)
- **Skyrim 시스템 구조.** 클래스·Major/Minor 구분이 없고 스킬마다 퍽 트리가 있다. 스킬을 쓰면 "Skill XP"가 쌓여 스킬이 오르고, 스킬이 오를 때마다 "Character XP"가 쌓인다(스킬 상승이 캐릭터 XP를 올리는 유일한 방법). 높은 레벨의 스킬을 올릴수록 캐릭터 XP가 많이 쌓인다. 레벨업 시 Health/Magicka/Stamina 중 하나 +10, 퍽 1점. 표준 게임에서는 수면 없이 어디서나 레벨업 가능(서바이벌 모드에서는 수면 필요). — [UESP Skyrim:Leveling [위키]](https://en.uesp.net/wiki/Skyrim:Leveling)
- **Skyrim 스킬 XP 규칙.** 특정 행동이 주는 스킬 XP는 일정하지만 다음 레벨에 필요한 XP는 레벨에 따라 증가한다(공식 근사: 스킬 레벨의 약 1.95제곱에 비례, fSkillUseCurve). 성공한 사용이 실패보다 XP를 더 준다(예: 자물쇠를 따면 부러뜨린 것보다 Lockpicking XP가 많음). 스킬마다 난이도 차가 커서 보석 공예만으로 Smithing을 100까지 쉽게 올릴 수 있지만 One-handed는 오래 걸린다. Rested/Well Rested/Lover's Comfort/Guardian Stone 보너스는 서로 곱연산으로 쌓인다. Destruction XP는 난이도가 Adept보다 높으면 줄어든다. — [UESP Skyrim:Leveling [위키]](https://en.uesp.net/wiki/Skyrim:Leveling)
- **Skyrim에서 남은 익스플로잇/구멍.** Essential NPC는 전투 스킬 훈련 허수아비로 쓸 수 있다. 오프닝(Helgen)에서 무한 레벨링 방법이 있다. 트레이너는 레벨당 총 5회만 쓸 수 있다. 패치 1.9부터 스킬을 100에서 "legendary"로 만들어 15로 리셋하면 레벨 상한(81)이 사실상 사라지며, 모든 퍽(251개)을 얻으려면 레벨 252(누적 809,475 XP)와 모든 스킬 100이 필요하다. — [UESP Skyrim:Leveling [위키]](https://en.uesp.net/wiki/Skyrim:Leveling)
- **Skyrim의 스케일링 변화.** UESP: Skyrim의 레벨링은 "in response to criticisms of Oblivion's leveling system" 바뀌었다. 적은 이름별 고정 레벨(Bandit 1, Bandit Thug 9, Highwayman 14 …)이고 플레이어 레벨은 나올 수 있는 변종의 범위에 영향을 주며, 던전마다 레벨 범위가 있고 적 종류별로 성장 상한(plateau)이 있다. — [UESP Skyrim:Leveling [위키]](https://en.uesp.net/wiki/Skyrim:Leveling)
- **Howard의 Skyrim 스케일링 설명(2011년 출시 전 인터뷰).** PC Gamer 기사는 "Oblivion's progressions system, which had creatures levelling at the same rate as the player, has been overhauled"라고 쓰고 Howard를 인용한다: "[Skyrim]'s a lot more like Fallout 3, where as you level up you are going to see harder things, but the easier things stay around as well." 기사는 이를 Oblivion 후반 레벨의 "boring battle-churn"을 끝내는 것으로 서술한다(이 표현은 기자의 평이다). — [PC Gamer, "Todd Howard on the lessons Skyrim has learned from Fallout 3" [2차, 원문 확인]](https://www.pcgamer.com/uk/todd-howard-on-the-lessons-skyrim-has-learned-from-fallout-3/)

#### Final Fantasy II
- **시스템.** FF II는 경험치 레벨이 없고, 전투에서 각 캐릭터가 한 행동에 따라 능력치가 자란다(특정 무기를 자주 쓰면 그 무기 숙련과 힘·명중이 오름). — [Wikipedia: Final Fantasy II [2차]](https://en.wikipedia.org/wiki/Final_Fantasy_II)
- **Kawazu의 의도.** "The argument was that the system is more about nurture than nature now. You don't choose what you are in the beginning… If one character uses a lot of magic, then they'll naturally become a mage. It's not something you decide at the beginning." 이유 두 가지: 스토리상 특정 캐릭터가 특정 역할을 해야 함, 그리고 nurture 개념. — [Retronauts, Kawazu 인터뷰(2012년 진행) [1차]](https://retronauts.com/article/670/akitoshi-kawazu-on-the-reasoning-behind-sagas-insanity)
- **파티원 공격 익스플로잇.** 인터뷰어가 "Attacking their own party members to get stronger"를 예상했는지 묻자 Kawazu: "No, I had no idea. [laughs] I had no idea people would use it to essentially grind levels… I thought that if characters were put to sleep, well, it makes sense to wake them up faster by hitting them… I never realized it would become a way to increase your hit points or whatever." — [Retronauts [1차]](https://retronauts.com/article/670/akitoshi-kawazu-on-the-reasoning-behind-sagas-insanity)
- **이후.** 부정적 반응과 개발진 이해 부족으로 FF III는 전통적 시스템으로 돌아갔다. Kawazu는 이후 첫 SaGa에서 사용 기반 스탯 상승을 이어갔고, Wikipedia는 Kawazu가 나중에 팀이 지나치게 멀리 갔다고 느꼈다고 서술한다. — [Wikipedia: Final Fantasy II [2차]](https://en.wikipedia.org/wiki/Final_Fantasy_II)
- **평가.** 회고 리뷰는 FF II를 진행 시스템 때문에 가장 호불호가 갈리는 시리즈 작품 중 하나로 평하고, 일부 리뷰는 "proficiency system not unlike what's found in The Elder Scrolls"(IGN)라고 불렀다. — [Wikipedia: Final Fantasy II [2차]](https://en.wikipedia.org/wiki/Final_Fantasy_II)

#### Quest 64
- 전통적 레벨업 모델이 아니라, FF II처럼 전투에서의 수행에 따라 능력치별로 경험이 쌓인다(예: 많이 맞으면 방어가 오름). 마법은 정령 아이템으로 속성을 골라 올린다. 발매 시 GameRankings 54%로 혼평이었고 비판은 깊이 부족에 집중됐다. — [Wikipedia: Quest 64 [2차]](https://en.wikipedia.org/wiki/Quest_64). 개발자 발언은 찾지 못했다(Gaps).

#### SaGa 시리즈
- Kawazu는 FF II의 교훈을 SaGa에 반영했다고 말한다. 핵심 논리: "if you make every character do the same actions, they all become the same kind of character that swings a sword and casts spells. That sort of thing might not actually be so much fun… I needed to differentiate the characters so that they wouldn't all be clones of each other at the end. That's where the races came in." 시리즈 공통 주제는 "Allowing the players to play the game the way they would like to play it." — [Retronauts [1차]](https://retronauts.com/article/670/akitoshi-kawazu-on-the-reasoning-behind-sagas-insanity)
- Wikipedia 기준 시리즈 3번째 Game Boy 작품(Sa・Ga 3)은 앞 두 작품의 "non-level-based individualized growth system"을 없애고 FF식 경험치·전체 스탯 레벨링을 도입했으며, Romancing SaGa 3는 적이 함께 강해지는 레벨 스케일링을 도입했다. — [Wikipedia: SaGa (series) [2차]](https://en.wikipedia.org/wiki/SaGa_(series))

#### Dungeon Siege
- 클래스를 고르지 않고, 특정 유형의 무기나 마법을 쓸수록 해당 숙련이 오른다. 숙련 레벨이 오르면 Strength/Dexterity/Intelligence 포인트가 늘어 HP·마나·피해량에 영향을 준다. Chris Taylor는 Diablo 공식을 개선하려고 "클래스 선택 개념 자체를 없애려" 했다. — [Wikipedia: Dungeon Siege [2차]](https://en.wikipedia.org/wiki/Dungeon_Siege). 이 게임의 실패 양상을 문서화한 개발자 자료는 찾지 못했다(Gaps).

#### RuneScape
- **XP 곡선.** 다음 레벨 필요 XP는 대략 이전보다 10% 많고, 레벨 99는 총 13,034,431 XP이며 약 30레벨 이후 7레벨마다 필요량이 두 배가 된다. — [OSRS Wiki: Experience [위키]](https://oldschool.runescape.wiki/w/Experience)
- **RuneScape Classic의 fatigue 시스템.** 일정 XP를 얻으면 침대/침낭에서 잠깐 자야 했고, 깨려면 captcha를 풀어야 했다. 피로가 100%면 훈련은 가능하지만 잘 때까지 XP를 못 받는다. RuneScape 2는 이 시스템을 없애면서 "anti-macro technology"로 random events를 도입했다. 랜덤 이벤트는 매크로를 방해하고 정상 플레이어에게 작은 보상을 주도록 설계됐다. — [OSRS Wiki: Random events [위키]](https://oldschool.runescape.wiki/w/Random_events)
- **랜덤 이벤트의 퇴조.** RS3에서 더 나은 안티매크로 소프트웨어가 개발되며 단계적으로 폐지됐고, OSRS에서도 최신 매크로 클라이언트가 랜덤 이벤트를 쉽게 풀 수 있다는 점이 확인됐다. 또 정상 플레이어가 공격적 몹에 둘러싸인 상태에서 퍼즐을 못 풀어 텔레포트당하는 문제가 불만이었다. 2014-08-28 개발자 블로그 후 투표에서 86.6%가 공격적 이벤트 제거·필수 이벤트의 선택화에 찬성해 반영됐다. — [OSRS Wiki: Random events [위키]](https://oldschool.runescape.wiki/w/Random_events)
- **매크로 대응 연표.** 2007-12-10 Jagex가 매크로 종식을 겨냥한 대규모 업데이트(자유 거래 제거 포함)를 했고 봇이 크게 줄었으나 반응이 엇갈려 국민투표 결과 상당수가 2011-02-01 제거됐다. 2011-10-25 "ClusterFlutterer"(Nuke Day)는 reflection/injection 봇을 겨냥했고 Jagex는 이것이 전체 봇의 98%였다고 판단했으며 그 시점에 150만 봇 계정을 밴했다고 밝혔다. 제재 시 스탯 초기화·아이템 삭제도 이뤄졌다. — [OSRS Wiki: Botting [위키]](https://oldschool.runescape.wiki/w/Botting)
- **RuneScape 창시자의 현재 입장.** Andrew Gower(Fen Research, *Brighter Shores*)는 PC Gamer 인터뷰에서 "Obviously, you're never going to completely eliminate bots… So our approach has been more to make it so that they don't negatively impact the game." 경제를 봇이 많아도 깨지지 않게 설계했다고 말했다(2024-03-27 80.lv 보도). — [80.lv [2차]](https://80.lv/articles/a-new-mmo-by-runescape-s-dev-will-legitimately-let-players-bot-the-game)

#### EVE Online (시간 기반 훈련)
- **메커니즘.** 캐릭터는 "real world time"으로 패시브 스킬 훈련을 하며 접속하지 않아도 진행된다. 스킬 큐는 최대 50개·10년분이며, 2014-11-04 "Phoebe" 이전에는 24시간 이내 시작분만 큐잉할 수 있었다. 일부 스킬은 선행 스킬이 필요하고 훈련 시간이 길다(타이탄 스킬은 프리깃의 8배). — [Wikipedia: Eve Online [2차]](https://en.wikipedia.org/wiki/Eve_Online)
- **CCP의 큐 설계 우려(2009).** CCP의 Eris Discordia는 개발자 블로그 "More Queue Queue"에서 스킬 큐를 도입하면 "some players might just set a queue for a year and become less active in EVE. That's not what a massively multiplayer ONLINE game is about"이라 우려했고 24시간 윈도우로 타협했다. — [Engadget, 2009-02-04 [2차]](https://www.engadget.com/2009-02-04-long-awaited-skill-queue-coming-to-eve-online.html)
- **시간 기반이 UO 매크로에 대한 "반응"이었다는 주장은 근거를 찾지 못했다.** 포럼에서는 "플레이하려고 레벨링하지 않게 해준다", "캐주얼이 파워게이머와 보조를 맞춘다" 같은 해석이 나오지만 모두 플레이어 의견이다(Gaps). 이 포럼 글은 검색 결과 요약으로만 확인했고 직접 열어보지 않았다. — [통설: EVE 포럼 아카이브(검색 요약)](https://forums-archive.eveonline.com/topic/128806)

#### Star Wars Galaxies (SWG)
- **원 설계.** 출시 시 34개 프로필(6 기본 + 24 고급 외; Wikipedia 본문 안에서 수치가 합산되지 않음). 프로필은 Novice, 4개 독립 가지, Master로 이루어진 트리이며 스킬은 "related activity"로 얻은 XP로 구매했다. NGE 후 9개 프로필로 줄었고 진행은 combat/crafting/entertaining 3개 XP 계열로 나뉘었다. — [Wikipedia: Star Wars Galaxies [2차]](https://en.wikipedia.org/wiki/Star_Wars_Galaxies)
- **Koster의 SWG 설계 논리.** UO의 사용 기반 문제를 피하려고 "define a type of XP for every major activity in the game"을 시도했다("XP is more about results, rather than the mere action"). 그러나 "Crafting (and even the performance professions) therefore fell victim to the classic grinding problems anyway." 제작 XP를 "다른 플레이어가 내 물건을 쓸 때" 주는 사회적 결과 기반 안은 DB 부하 때문에 접혔다. — [Koster, "Designing a Living Society in SWG, part one" (2015-04-21) [1차]](https://www.raphkoster.com/?p=25717), [Koster, Use-based systems [1차]](https://www.raphkoster.com/?p=592)
- **SWG의 보정 방식.** 베타 중 스킬 사용 비율을 추적해 skill box별 정적 XP 요구량을 정했고(UO 표와 같은 방식), 도전(몬스터/제작)마다 난이도 값을 붙여 XP를 조절했다. 출시 3일 전 진행 속도 담당 디자이너가 모든 성장 속도를 10배 느리게 바꿨고(라이브 베타 서버에 반영) Koster가 되돌렸다("making literally thousands of blaster bolts to advance one skill box"). 그래도 "it was still too grindy". — [Koster, Use-based systems [1차]](https://www.raphkoster.com/?p=592)
- **Koster의 사후 평가(2015).** SWG는 "the fastest advancement of any MMO at the time it came out"였고 세션 길이는 짧았으며 주간 총 플레이 시간은 가장 높았다고 주장한다. 그룹 XP 변경은 이탈률을 두 배로 만들었고 롤백 후에도 50% 높은 상태로 남았다("worse, in percentage terms, than the NGE was"). 이는 지표 설계 오류("how many Master Merchants are there?" vs "how many people run a shop?")와 연결된다. 이 수치들은 Koster 본인의 주장이다. — [Koster, "Did Star Wars Galaxies Fail?" [1차]](https://www.raphkoster.com/?p=25829)
- **Jedi 해금 설계 실패.** 원래 Jedi 슬롯은 여러 게임 시스템을 두루 해본 플레이어에게 열릴 계획이었으나, 출시 두 달 전 Koster가 "무작위 프로필 목록" 방식으로 바꿨다. Koster는 이를 실수로 평가했다. 플레이어가 여러 프로필을 두루 하는 "jack-of-all-trades"가 되기는 매우 어려워 Jedi 첫 등장 시점을 "a decade"로 추정했고, SOE가 힌트를 주자 플레이어가 기존 프로필을 버리고 Jedi를 쫓는 경험이 불만이었다는 서술. — [Wikipedia (Koster 인터뷰 인용) [2차]](https://en.wikipedia.org/wiki/Star_Wars_Galaxies)
- **NGE.** 2005-11 NGE는 프로필을 9개로 줄이고 전투를 실시간 FPS 유사 방식으로 바꿨다. 언론은 깊이와 복잡성 감소를 비판했고, SOE의 Smedley는 구독자 감소를 되돌리기 위해 필요했다고 옹호했다. CBS 기사에 따르면 Smedley는 Combat Upgrade와 NGE가 LucasArts와 SOE의 합의였다고 밝혔다. — [Wikipedia [2차]](https://en.wikipedia.org/wiki/Star_Wars_Galaxies), [GameBanshee가 전한 CBS News 기사 [2차]](http://www.gamebanshee.com/w84)

#### Mount & Blade / Bannerlord
- **Bannerlord 공식 개발 블로그(2018-08-23 게시).** 스킬을 올리려면 관련 행동을 해야 한다(One Handed는 한손 무기로 공격을 명중). 스킬이 오르면 캐릭터 레벨 바가 차고 가득 차면 레벨업하며 focus point 2개를 받는다. focus는 해당 스킬 경험치 획득을 가속하지만 한 번 투자하면 영구 고정이고, "skills that are shown as level 0 and have no focus points invested in them cannot progress, no matter how much you practice them." — [TaleWorlds Dev Blog (Wayback) [1차]](https://web.archive.org/web/2024/https://www.taleworlds.com/en/Games/Bannerlord/Blog/74)
- **현재 규칙 (커뮤니티 위키).** 스킬 증가율은 focus point와 속성 투자에 좌우된다. "learning limit"은 소프트 캡(= focus×30 + (속성점−1)×10)이며 넘으면 더 느리게 오른다. 속성 10, focus 5에서 소프트 캡은 330이고 하드 캡은 1023. 스킬별 XP 획득법이 다르다(예: Steward는 부대 규모·식량 종류, Charm은 동료를 사절로 두는 방식). — [Mount & Blade Wiki: Skills (Bannerlord) (Wayback) [위키]](https://web.archive.org/web/2024/https://mountandblade.fandom.com/wiki/Skills_(Bannerlord))

#### Kingdom Come: Deliverance (KCD)
- Warhorse 관련 보도(2018): 캐릭터 생성이 없고 클래스도 없으며 "The more you do any particular thing, the better and more adept at it you become."; 트레이너가 특정 스킬을 가르치며 진행을 가속하거나 연습 공간을 제공한다(서기에게 읽기 배우기). — [Shacknews, 2018-02-13 (기자 서술, 개발자 직접 인용 아님) [2차]](https://www.shacknews.com/article/103330/are-there-classes-in-kingdom-come-deliverance)
- 개발진 발언을 전한 기사: 자주 하는 행동(잠행, 검술)이 스킬을 올리고, 드물게 쓰는 스킬은 "Lehrer"(교사)에게 돈을 내고 올릴 수 있다. — [mein-mmo.de (MMORPG.com 인용) [2차]](https://mein-mmo.de/en/kingdom-come-deliverance-skill-ruestungssystem,97873)
- 위키: 스킬은 "repeatedly" 쓰며 오르고 스킬 레벨업 후 perk를 고른다(페이지가 stub). — [KCD Wiki.gg [위키]](https://kingdomcomedeliverance.wiki.gg/wiki/Skills)

#### Kenshi
- **개발사 선언(Steam 스토어 페이지).** "Absolutely no Level-scaling. The world does not level up along with you, and the shops don't change their inventory to only items matching your level. At the start of the game almost everyone will be stronger than you." 또한 "No 'hero' characters with artificially stronger stats", "Characters will grow and become stronger with experience, not just in their stats but their appearance too." — [Kenshi Steam 스토어 (appdetails API) [1차]](https://store.steampowered.com/app/233860/Kenshi/)
- **Chris Hunt 초기 인터뷰(GameStar, 2011).** "There will be a lot of skills too, covering physical stats, weapon proficiencies, combat skills, and non-combat skills." 성장 방식에 대한 발언은 이 발췌에 없다. — [GameBanshee (GameStar 인터뷰 인용) [2차]](http://www.gamebanshee.com/xy6r)
- **Strength 훈련 메커니즘(커뮤니티 위키).** 근력 XP는 주로 공격으로 얻는다(적중마다, 막혀도 지급; 방어 성공 시 40%, 맞기만 하면 10%). 무기의 요구 Strength가 현재 근력보다 20 높으면 스윙당 110% XP를 받고 "the fastest way to train Strength is through combat". 무거운 짐을 지고 걷는 것도 훈련이며, 70% encumbrance에서 최대 25% STR XP에 도달하고 그 이상은 Athletics XP만 깎는다(다른 캐릭터를 업으면 50%까지 가능). 위키가 "safe way"로 소개하는 방법은 철광석 등으로 배낭을 채워 경비병 뒤를 따라 도시를 돌아다니는 것이다. — [Kenshi Wiki: Strength (Wayback) [위키]](https://web.archive.org/web/2024/https://kenshi.fandom.com/wiki/Strength)
- **훈련 허수아비의 상한.** Simple Training Dummy는 Melee Attack을 최대 5까지, MkII는 10까지 올릴 수 있다(상위 단계는 확인 못 함). — [Kenshi Wiki: Training Dummy (Wayback) [위키]](https://web.archive.org/web/2024/https://kenshi.fandom.com/wiki/Training_Dummy)

#### Project Zomboid
- **XP/레벨 구조(build 41.78.16 기준).** 스킬은 구체적 과제로 XP를 얻는다. 패시브 스킬(Strength, Fitness)은 "significantly more experience points"가 필요해 레벨 1에 1,500 XP가 필요한 반면 목공(carpentry)은 75 XP. 일반 스킬 0→4 누적은 1,275 XP. — [PZwiki: Skills (Wayback) [위키]](https://web.archive.org/web/2024/https://pzwiki.net/wiki/Skills)
- **스킬북.** 해당 스킬의 XP 획득 배율을 올린다. crafting·survivalist 범주에만 있으며 스킬당 5권(두 레벨 구간마다 1권)이고 해당 레벨 구간에만 적용된다. 배율은 읽은 비율(10% 단위)에 따라 올라간다. 캐릭터 생성 시 시작 레벨이 있는 스킬은 영구 XP 보너스를 받지만 Strength/Fitness는 이 보너스의 영향을 받지 않는다. — [PZwiki: Skills (Wayback) [위키]](https://web.archive.org/web/2024/https://pzwiki.net/wiki/Skills)

#### Dwarf Fortress (Fortress/Adventure)
- **XP 규칙.** 대부분의 민간 스킬은 사용당 30 XP(채굴·연마·조각·요새 조각은 10), 군사 스킬은 실전이 훈련보다 XP가 많다. 레벨당 필요량은 (400 + 100×새 레벨) XP이며 Legendary는 15레벨 이상이고 전투 스킬은 그 위로도 계속 스케일한다. 이상 기분(strange mood)으로 작품을 완성하면 해당 스킬에 20,000 XP. — [DF Wiki: Experience (DF2014) [위키]](https://dwarffortresswiki.org/index.php/DF2014:Experience), [DF Wiki: Skill (DF2014) [위키]](https://dwarffortresswiki.org/index.php/DF2014:Skill)
- **Skill rust(미사용 감쇠).** 오래 쓰지 않으면 "rusty", 이어서 "very rusty"가 되고 더 지나면 영구 경험치 손실이 일어난다. 기본 설정 [SKILL_RATE:100:8:16:16]. 스킬과 속성은 모두 관련 활동으로 훈련되고 서로 교차 훈련된다. — [DF Wiki: Skill [위키]](https://dwarffortresswiki.org/index.php/DF2014:Skill)
- **Adventure mode의 훈련 편법 (커뮤니티 문서).** Adventure mode FAQ는 "Most of these skill-raising techniques involve repeatedly entering the same keystrokes"라며 매크로 사용을 권하고, 무해한 작은 동물과 반복해서 wrestle하기, 일부러 맞으며 방어 스킬 올리기, 위쪽 z-레벨로 화살을 쏴 탄약을 회수하며 훈련하기("may be considered a bug and/or exploit") 등을 소개한다. 이 문서가 어느 버전 기준인지는 확인하지 못했다. — [DF Wiki: Adventurer mode F.A.Q. [위키]](https://dwarffortresswiki.org/index.php/Adventurer_mode_F.A.Q.)
- **현황.** Adventure Mode는 2025-01-23 Steam/itch.io에 정식 출시됐다. — [Kitfox/Bay 12 보도자료 [1차]](https://gamespress.com/DWARF-FORTRESS-ADVENTURE-MODE-NOW-AVAILABLE)

### Inferences
- UO 사례는 보정 장치의 연쇄를 보여준다: 빈도 기반 확률 조정 → 매크로 → 난이도 필터 → 몬스터 가둬 매크로 → 결정론적 시드 → 8×8 → 손 코딩 표 → power hour → GGS. 각 단계가 앞 단계의 플레이어 대응을 막으려는 시도였다. 지표(사용 빈도)를 보정 입력으로 쓰면 그 지표 자체가 게임 대상이 된다.
- Morrowind→Oblivion→Skyrim은 "행동 기반 스킬 성장을 어떻게 캐릭터 레벨과 연결할 것인가"의 세 가지 답이다. (1) 속성 배수 최적화를 요구해 계획 레벨링을 유발했고(Morrowind/Oblivion), (2) 거기에 적 스케일링이 겹쳐 레벨업이 오히려 약해지는 역설이 생겼으며(Oblivion), (3) Skyrim은 속성과 클래스를 제거하고 적을 고정 레벨 중심으로 바꿨다.
- FF II·SaGa·Quest 64 계열은 "스탯 성장 규칙이 플레이어에게 보이지 않거나 직관과 어긋날 때" 어떤 일이 벌어지는지의 사례이며, Kawazu가 의도하지 않은 방향(아군 공격)이 곧 표준 공략이 되었다.
- 소규모 개발에서 의미 있는 선례: Bannerlord의 focus/learning limit(성장을 빠르게 하되 총량은 제한), Kenshi의 "레벨 스케일링 없음 + 훈련 상한", DF의 사용 기반 XP + 감쇠 조합이다. 모두 "무엇을 하느냐가 곧 무엇이 되느냐"를 유지하면서 단순 반복의 한계 효용을 낮추는 방식이다.

### Gaps
- **Skyrim이 Major/Minor 스킬을 없앤 이유에 대한 직접 발언**은 찾지 못했다. 확인한 것은 클래스 선택 문제(Howard)와 속성 제거(Nesmith)이며, Major/Minor 폐지는 UESP가 "클래스가 없어 구분이 사라졌다"고 설명하는 정도다.
- Howard의 IGN 원문과 Game Informer 팟캐스트 원본은 열지 못하고 GameBanshee·PSU의 인용으로만 확인했다. Nesmith의 Press Box PR·VideoGamer 원 인터뷰도 GamesRadar 인용으로만 확인했다.
- **UO power hour의 정확한 작동 방식**(시간 창의 조건 등)과 도입 시점은 확인하지 못했다. 2001-09-20 팀 코멘트의 평가만 확보했고, 같은 곳의 다른 코멘트(2001-05-04)는 403으로 읽지 못했다. UO의 skill gain 확률 공식도 확인하지 못했다.
- **EVE:** CCP가 시간 기반 훈련을 도입한 이유에 대한 1차 발언(예: Hilmar, Fanfest)은 찾지 못했다. "UO 매크로에 대한 반응"이라는 틀은 근거가 없는 통설/추정으로 취급해야 한다.
- **Kenshi:** 개발자가 사용 기반 성장의 설계 이유를 밝힌 1차 발언을 찾지 못했다(Rezzed 2018 인터뷰가 있다는 검색 요약은 열어보지 못함). Training Dummy MkIII 상한도 확인 못 했다.
- **KCD:** Warhorse의 설계 의도 직접 인용과 스킬별 XP 수치는 찾지 못했다(언론 서술과 stub 위키뿐).
- **Project Zomboid:** The Indie Stone의 설계 의도 발언은 찾지 못했다. 위키 수치는 build 41.78.16 기준이며 Build 42에서 달라졌을 수 있다.
- **Dwarf Fortress:** Tarn Adams의 설계 의도 발언은 찾지 못했다. Adventure mode FAQ는 버전이 불명이고 2025년 Steam 판의 스킬 규칙은 확인하지 못했다.
- **Quest 64, Dungeon Siege:** 개발자 자료와 실패 양상 문서를 찾지 못했다. Quest 64의 "성장이 매우 느리다/cherry-tapping" 같은 서술은 열어보지 못한 팬 리뷰에서만 나왔으므로 사용하지 않았다.
- Daggerfall의 구체적 스킬 상승·레벨업 수식(UESP Daggerfall:Level 페이지는 404)과 원작 Mount & Blade(Warband)의 숙련도 규칙은 조사하지 못했다.

---

## 2. 문서화된 일반적 실패 양상, 그리고 유명한 문구의 원전

### Takeaway
실패 양상은 반복적이다. (1) 가장 싼 반복 행동으로 성장을 쥐어짜는 퇴행적 그라인드, (2) 반복 보상이 희박할 때 생기는 매크로/봇 유인, (3) 플레이어가 공식을 해독해 "재미를 최적화로 지워버리는" 현상, (4) 모두가 같은 만능형/지배 빌드로 수렴하는 정체성 상실, (5) 읽기 어려운 성장, (6) 사용 빈도 차이·적 스케일링 같은 밸런스 문제. 유명 문구의 원전은 대부분 개발자 본인의 글로 확인된다.

### Cited Findings

#### 원전 확인
- **"Given the opportunity, players will optimize the fun out of a game."** Soren Johnson의 Game Developer 2011년 3월호 칼럼 "Water Finds a Crack"(칼럼 17)의 문장이며 Designer Notes 블로그에는 2011-06-12에 게재됐다. 바로 앞 문장은 "Many players cannot help approaching a game as an optimization puzzle." 뒤는 "Games, however, are so complex that it is difficult to anticipate exactly how players will optimize a game until after release". — [Soren Johnson [1차]](https://www.designer-notes.com/game-developer-column-17-water-finds-a-crack/)
- **"Water finds a crack"**는 Civilization 개발팀이 쓰던 표현으로, "any hole a player can possibly find in the game's design will be inevitably abused over and over." 위험한 점은 한번 익스플로잇을 알게 된 플레이어는 "never be able to play the game again without using it"이라는 것. — [Soren Johnson [1차]](https://www.designer-notes.com/game-developer-column-17-water-finds-a-crack/)
- **같은 글의 "단일 지배 전략" 논점.** "tank-mage"는 MMO 약칭으로 UO에서 중갑과 강력한 피해 주문을 둘 다 가진 혼합 빌드가 다른 빌드를 대체한 데서 나왔다. "a single, dominant strategy actually takes away choice from a game because all other options are provably sub-optimal. The sweet spot for game design is when a specific decision is right in some circumstances but not in others." — [Soren Johnson [1차]](https://www.designer-notes.com/game-developer-column-17-water-finds-a-crack/)
- **Johnson의 반대 논점.** "designers can go too far by trying to remove all exploits." 판단 기준은 "Does the exploit drown out all other play styles, or is it a fun, alternative way to play? Does the degenerate strategy create an endless grind, or is it a quick shortcut…?" 예로 슈퍼 마리오의 거북이 껍데기 무한 생명 트릭이 의도된 기능이었다는 것을 든다. — [Soren Johnson [1차]](https://www.designer-notes.com/game-developer-column-17-water-finds-a-crack/)
- **"players will trade time for safety"와 시간 과소평가.** 같은 글은 플레이어가 자기 시간을 과소평가해 자기 즐거움을 깎는 지점까지 간다고 하며 Morrowind 스킬 시스템을 "classic example"로 든다. — [Soren Johnson [1차]](https://www.designer-notes.com/game-developer-column-17-water-finds-a-crack/)
- **Koster의 법칙 문구.** "No matter what you do, players will decode every formula, statistic, and algorithm in your world via experimentation." (Use-based systems 글, 2006-07-18). — [Koster [1차]](https://www.raphkoster.com/?p=592)
- **Bethesda 발언:** 1장에 정리한 Howard(클래스 선택 후 3시간 만에 재시작; [PSU [2차]](https://www.psu.com/news/bethesda-explains-elder-scrolls-v-classes-axe/))와 Nesmith("getting the character system out of the player's way", "almost nobody" complained; [GamesRadar [2차]](https://www.gamesradar.com/games/rpg/we-got-rid-of-attributes-in-skyrim-and-you-know-who-complained-almost-nobody-former-bethesda-lead-pushed-for-a-streamlined-rpg-where-you-dont-have-your-head-buried-in-menus-stats-and-rules))를 참조. 두 발언 모두 사용 기반 성장 자체의 실패가 아니라 *사전 선택 구조의 문제*와 *복잡성*을 이유로 든다.

#### 실패 양상별 문서화된 증거
1. **퇴행적 그라인드(싼 반복 행동).**
   - Morrowind: 벽에 달리기/점프 반복(Johnson 위 인용).
   - Oblivion: Koster는 "people jumping everywhere in order to improve the stats and skills related to dodging" 사례를 인용하고, 원인을 "There's no challenge in jumping off a hill in Oblivion, and therefore, the grind rears its ugly head"로 분석한다. 핵심 진단은 "practice that isn't challenging your skills and helping you learn is boring." — [Koster [1차]](https://www.raphkoster.com/?p=592)
   - Skyrim: Essential NPC를 훈련 허수아비로 쓰기, Helgen 무한 레벨링 — [UESP Skyrim:Leveling [위키]](https://en.uesp.net/wiki/Skyrim:Leveling)
   - FF II: 아군 공격 — [Retronauts [1차]](https://retronauts.com/article/670/akitoshi-kawazu-on-the-reasoning-behind-sagas-insanity)
   - Dwarf Fortress adventure mode: 무해한 동물과 반복 wrestle — [DF Wiki FAQ [위키]](https://dwarffortresswiki.org/index.php/Adventurer_mode_F.A.Q.)
   - Kenshi: 무거운 배낭을 메고 경비병을 따라다니기 — [Kenshi Wiki [위키]](https://web.archive.org/web/2024/https://kenshi.fandom.com/wiki/Strength)
2. **매크로/봇 유인.**
   - Koster: 보상이 "so incredibly infrequently"해지면 "playing 'the right way' no longer had any incentives" — [Koster [1차]](https://www.raphkoster.com/?p=592)
   - Koster는 무조건 반복이 아니라 *도전 없는 반복*이 문제라고 구분한다. 현실의 "practice"는 나쁘지 않지만 게임에서는 "There's no cost to failure. The topology of the space is irrelevant. There are no differing abilities. No skill required"(Grammar of Gameplay에서 가져온 "fun checklist" 항목들)일 때 bottom-feeding이 된다고 한다. — [Koster [1차]](https://www.raphkoster.com/?p=592)
   - RuneScape: fatigue+captcha(RSC), random events(RS2), Nuke Day(2011), 2007년 대규모 조치와 투표에 의한 일부 철회 — 1장 참조.
   - 학술: De Paoli는 Tibia 사례에서 봇/매크로가 레벨링의 반복·지루한 과제를 소프트웨어로 옮긴다고 분석한다(4장).
3. **"재미를 최적화로 지움".**
   - Johnson 원문(위). Soren의 글 서두에는 Koster의 *A Theory of Fun* 인용문이 에피그래프로 달려 있는데, 거기에 "the destiny of games is to become boring, not to be fun"이라는 구절이 있다(발췌가 중간에서 잘림). — [Soren Johnson [1차]](https://www.designer-notes.com/game-developer-column-17-water-finds-a-crack/)
   - Oblivion Efficient Leveling은 최적화 자체가 목적인 플레이로 문서화됐다(1장). Koster는 "humans seek advantage"이므로 일부 플레이어는 "play it straight"하려 해도 남이 편법으로 앞서가는 것을 보면 굴복한다고 주장한다. — [Koster [1차]](https://www.raphkoster.com/?p=592)
4. **정체성 상실/만능형 수렴.**
   - Kawazu: 같은 행동을 시키면 "they all become the same kind of character that swings a sword and casts spells" → SaGa에 종족(고정 요소) 도입. — [Retronauts [1차]](https://retronauts.com/article/670/akitoshi-kawazu-on-the-reasoning-behind-sagas-insanity)
   - Johnson의 tank-mage(위).
   - Skyrim: legendary 시스템으로 레벨 상한이 사실상 제거되어 모든 스킬 100·모든 퍽 취득이 가능하다는 구조적 사실. — [UESP Skyrim:Leveling [위키]](https://en.uesp.net/wiki/Skyrim:Leveling) (이것이 정체성 상실인지는 해석이며 Bethesda 발언은 확인하지 못함.)
   - Morrowind: 총 2300회 스킬 상승 허용 대비 최대 효율에 필요한 상승은 840회. 즉 시간만 쓰면 모든 속성 100이 가능하다. — [UESP Morrowind:Level [위키]](https://en.uesp.net/wiki/Morrowind:Level)
   - UO는 총 700 포인트 캡과 미사용 스킬 감쇠로 전문화를 강제했다(1장). 총량 캡의 반대 사례(캡 폐지/상향)는 Skyrim legendary와 UO GGS 표의 115~120 구간에서 보인다.
5. **읽기 어려운 성장.**
   - Morrowind/Oblivion: 속성 배수 규칙을 이해하고 "extensive planning"해야 효율이 나온다(UESP). Howard는 Oblivion 플레이어들이 30분 플레이로는 "all the skills and how they work"를 이해할 수 없다고 했다. UO power hour는 새 플레이어에게 "Unintuitive"하다고 팀이 인정했다. SaGa/FF II는 규칙을 모르는 상태에서 성장한다.
6. **밸런스.**
   - 스킬별 사용 빈도 차이(Koster, UO). Oblivion 스케일링과 성장의 어긋남(UESP, Nesmith). SWG의 Master 수 같은 잘못된 지표로 결정(Koster 2015). Kawazu는 첫 Final Fantasy의 자유로운 파티 구성(전원 White Mage 파티는 클리어가 어려울 수 있음)에 대해 "we weren't really worried about that affecting the balance or anything like that"라고 말했다. 이는 FF II의 사용 기반 성장이 아니라 FF I 직업 선택에 관한 발언이지만, 당시 밸런스를 플레이어의 시행착오에 맡기는 태도를 보여준다. — [Retronauts [1차]](https://retronauts.com/article/670/akitoshi-kawazu-on-the-reasoning-behind-sagas-insanity)
7. **무엇이 보상되는가.** Koster는 2002년 포럼 문장을 인용한다: "you only do what you are rewarded for." 그리고 "A lot of MMO design, especially in the last decade, has been about preventing behaviors, rather than enabling them." — [Koster, SWG part one [1차]](https://www.raphkoster.com/?p=25717)
8. **스킬은 목적이 아니라 수단.** Koster: "skills, levels, abilities — these are properly regarded as enablers, and not as the point… If the game becomes getting the tool, then you have a nice little rat race going that is inevitably going to be a grind." — [Koster [1차]](https://www.raphkoster.com/?p=592)

### Inferences
- Johnson과 Koster는 같은 현상을 서로 다른 수준에서 서술한다. Johnson은 *플레이어 행동 법칙*(최적화/해독)을, Koster는 *시스템 진단*(도전 없는 행동에 보상, 피드백 루프의 붕괴)을 다룬다. 둘을 합치면: 공식이 단순할수록 해독이 빠르고, 보상 행동에 도전이 없으면 그 해독은 곧 그라인드가 된다.
- Bethesda가 든 이유는 모두 *사용 기반의 철학적 실패*가 아니라 *진입 장벽과 복잡성*이다. 즉 Skyrim은 "행동으로 성장"을 버린 것이 아니라 "사전 선택 + 속성 예산 관리"를 버렸다. Nesmith는 "you do something, you get better at it"을 시리즈의 상징으로 평가한다.
- 정체성 상실 문제는 사용 기반 시스템에서 구조적이다. 시간이 충분하면 모든 행동을 반복해 모든 것을 얻을 수 있기 때문이다. 이를 막는 수단은 UO의 총량 캡·감쇠, Bannerlord의 focus 영구 고정처럼 *시간 외의 희소 자원*을 끼우는 것으로 보인다(3장).

### Gaps
- Johnson 칼럼 이전에 같은 문장을 다른 곳에서 먼저 썼는지(예: Game Developer 지면 이전 강연)는 확인하지 못했다. 검색 중 "비슷한 문장을 다른 사람이 말했다"는 블로그가 있었으나 원문 확인에 실패했다.
- "Everyone becomes a jack-of-all-trades"를 Skyrim/Morrowind에 대해 개발자가 직접 문제로 언급한 1차 자료는 찾지 못했다(SWG의 Jedi 해금에서만 jack-of-all-trades가 Koster 언급으로 등장하며, 이는 다른 맥락이다).
- Koster 글의 댓글란에는 "use-based systems suck for achievers", "하루에 한 번만 개선 굴림(RuneQuest 방식)" 같은 독자 의견이 있으나 Koster 본인의 말이 아니라 사용하지 않았다.
- Tim Cain이 skill-use XP를 비판했다는 요약은 팬 위키(turbo-wiki.pages.dev) 2차 요약으로만 보였고 1차 자료(강연 영상)를 확인하지 못해 제외했다.

---

## 3. 성공으로 평가받는 설계와 그것이 작동한 이유 (캡, 체감, rested/first-time 보너스, 사용 맥락, 실패 학습, 교사 요건 등)

### Takeaway
"성공"의 정의는 문서마다 다르지만, 오래 유지된 설계는 공통적으로 (1) 사용에 *감쇠 곡선*을 붙이고, (2) *총량이나 슬롯*에 희소한 상한을 두고, (3) 성장이 *난이도·맥락*(자기 수준에 맞는 도전)에 반응하게 하고, (4) 레벨업/적 스케일링과의 결합을 느슨하게 하고, (5) 드물게 쓴 스킬을 위한 *보정 경로*(교사·책)를 둔다. 순수한 "쓰면 는다"가 오래 간 사례는 문서에서 확인하지 못했다.

### Cited Findings
- **감쇠(체감) 곡선.** Skyrim: 행동당 XP는 일정하고 다음 레벨 필요량이 스킬 레벨의 약 1.95제곱에 비례해 커져, 초반에 몇 번 막기만 해도 오르던 Block이 후반에는 훨씬 많이 필요하다. 거인의 공격을 막으면 더 빨리 오른다(도전이 클수록 XP). — [UESP Skyrim:Leveling [위키]](https://en.uesp.net/wiki/Skyrim:Leveling). RuneScape: 필요 XP가 레벨당 ~10% 증가·7레벨마다 2배. — [OSRS Wiki: Experience [위키]](https://oldschool.runescape.wiki/w/Experience). DF: 레벨당 (400+100×레벨) XP. — [DF Wiki [위키]](https://dwarffortresswiki.org/index.php/DF2014:Skill)
- **전문화 비용 구조.** Morrowind는 Major 0.75/Minor 1/Misc 1.25 배율과 전문 분야 0.8로, 같은 행동이라도 선택에 따라 성장 비용이 달라진다. — [UESP Morrowind:Skills [위키]](https://en.uesp.net/wiki/Morrowind:Skills)
- **총량 캡/주 스킬 캡.** UO의 700 총 스킬 포인트(캡 도달 시 다른 스킬에서 한 점 감소)와 미사용 스킬 감쇠. — [Koster [1차]](https://www.raphkoster.com/?p=592). Daggerfall의 Primary 마스터 시 다른 스킬 자연 최대 95. — [UESP Daggerfall:Skills [위키]](https://en.uesp.net/wiki/Daggerfall:Skills). Bannerlord의 learning limit 소프트 캡과 focus 영구 고정, "no focus, no progress". — [TaleWorlds 블로그 [1차]](https://web.archive.org/web/2024/https://www.taleworlds.com/en/Games/Bannerlord/Blog/74), [M&B Wiki [위키]](https://web.archive.org/web/2024/https://mountandblade.fandom.com/wiki/Skills_(Bannerlord))
- **사용 맥락/난이도 조건.** UO GGS는 난이도 기반 스킬에서 "in or around your current skill level"로 성공했을 때만 보장하고 너무 쉬운 행동(Magery 90의 Magic Arrow)은 보장하지 않는다. — [UO.com Publish 16 [1차]](https://uo.com/wiki/ultima-online-wiki/technical/previous-publishes/2002-2/2002-publish-16-part-2-23rd-july/). Koster가 SWG에 도입한 도전별 난이도 값. — [Koster [1차]](https://www.raphkoster.com/?p=592). Kenshi는 무기 요구 근력 대비 XP 비율로 보상하고 허수아비를 단계별 상한(MkI→5)으로 제한한다. — [Kenshi Wiki: Training Dummy (Wayback) [위키]](https://web.archive.org/web/2024/https://kenshi.fandom.com/wiki/Training_Dummy)
- **실패 처리 규칙.** Skyrim은 성공 사용이 실패보다 XP가 많지만 실패에도 XP를 준다. — [UESP Skyrim:Leveling [위키]](https://en.uesp.net/wiki/Skyrim:Leveling). 반대로 UO GGS는 실패한 사용을 카운트하지 않는다. — [UO.com Publish 16 [1차]](https://uo.com/wiki/ultima-online-wiki/technical/previous-publishes/2002-2/2002-publish-16-part-2-23rd-july/). Koster는 "There's no cost to failure"를 bottom-feeding의 조건으로 꼽는다. — [Koster [1차]](https://www.raphkoster.com/?p=592). Kenshi 스팀 설명은 "survival will always be a struggle", 부상이 스탯에 영향을 준다고 적는다. — [Steam [1차]](https://store.steampowered.com/app/233860/Kenshi/)
- **Rested / 최초 1회 보너스.** Skyrim의 Rested/Well Rested/Lover's Comfort/Guardian Stone 경험치 보너스는 곱연산 중첩. — [UESP Skyrim:Leveling [위키]](https://en.uesp.net/wiki/Skyrim:Leveling). Morrowind는 스킬북을 처음 열 때 스킬이 오르고, 스킬이 100이면 대신 캐릭터 레벨 진행 포인트 1을 준다. — [UESP Morrowind:Level [위키]](https://en.uesp.net/wiki/Morrowind:Level). RSC의 fatigue(자야 XP 지급)는 일종의 "휴식 필요" 규칙이지만 설계 목적은 안티매크로였다. — [OSRS Wiki: Random events [위키]](https://oldschool.runescape.wiki/w/Random_events). UO GGS 타이머는 서버 시계 기준이라 로그오프 중에도 흐른다(일종의 오프라인 보상). — [UO.com [1차]](https://uo.com/wiki/ultima-online-wiki/technical/previous-publishes/2002-2/2002-publish-16-part-2-23rd-july/)
- **교사/훈련 요건.** Morrowind·Oblivion·Skyrim은 돈을 내는 트레이너가 있고 Skyrim은 레벨당 5회 제한. — [UESP Skyrim:Leveling [위키]](https://en.uesp.net/wiki/Skyrim:Leveling), [UESP Oblivion:Leveling [위키]](https://en.uesp.net/wiki/Oblivion:Leveling). KCD는 드물게 쓰는 스킬을 위해 교사를 둔다. — [mein-mmo [2차]](https://mein-mmo.de/en/kingdom-come-deliverance-skill-ruestungssystem,97873). UO는 원래 관찰만으로도 오르던 것이 문제였다(Koster). PZ 스킬북은 레벨 구간별로만 적용된다. — [PZwiki (Wayback) [위키]](https://web.archive.org/web/2024/https://pzwiki.net/wiki/Skills)
- **느린 물리 스탯.** PZ의 Strength/Fitness는 필요 XP가 훨씬 크고 시작 보너스를 받지 않는다. — [PZwiki (Wayback) [위키]](https://web.archive.org/web/2024/https://pzwiki.net/wiki/Skills). Kenshi 근력 XP는 70% 하중에서 25%로 상한이 걸린다. — [Kenshi Wiki [위키]](https://web.archive.org/web/2024/https://kenshi.fandom.com/wiki/Strength)
- **미사용 감쇠.** DF의 skill rust(영구 손실까지) — [DF Wiki [위키]](https://dwarffortresswiki.org/index.php/DF2014:Skill). UO의 미사용 스킬 감쇠 — [Koster [1차]](https://www.raphkoster.com/?p=592).
- **스케일링 분리.** Kenshi는 "Absolutely no Level-scaling"을 광고 문구로 쓴다. — [Steam [1차]](https://store.steampowered.com/app/233860/Kenshi/). Skyrim은 이름별 고정 레벨과 plateau. — [UESP Skyrim:Leveling [위키]](https://en.uesp.net/wiki/Skyrim:Leveling)
- **시간 기반 대안(EVE).** 훈련을 *시간*에 묶어 행동 반복을 무의미하게 만든다. 단점으로 CCP는 큐 때문에 플레이어가 접속을 줄일 수 있다고 우려했다. — [Wikipedia: Eve Online [2차]](https://en.wikipedia.org/wiki/Eve_Online), [Engadget [2차]](https://www.engadget.com/2009-02-04-long-awaited-skill-queue-coming-to-eve-online.html)
- **"결과 기반" 전환(Koster).** 행동이 아닌 구체적 결과에 보상한다("results-based"), 도전 난이도 값을 붙인다, 사용 지표를 유지한다. 그러나 "The result might not look much like a use-based system once you were done." 또 Privateer Online용으로 기획했던 자격(certification) 모델: 훈련 + 도전 + "dues"(길드에 내는 비용, 못 내면 자격 상실). — [Koster [1차]](https://www.raphkoster.com/?p=592)
- **지표를 보정 입력이 아닌 진단 도구로.** Koster는 사용 빈도 지표를 유지하라고 권고한다. SWG에서는 지표 질문을 잘못 잡아 결정이 어긋났다("how many Master Merchants" vs "how many people run a shop"). — [Koster [1차]](https://www.raphkoster.com/?p=592), [Koster, Did SWG Fail? [1차]](https://www.raphkoster.com/?p=25829)
- **봇을 막지 않고 무해화하는 접근.** Gower의 "make it so that they don't negatively impact the game"(경제·인스턴싱 설계). — [80.lv [2차]](https://80.lv/articles/a-new-mmo-by-runescape-s-dev-will-legitimately-let-players-bot-the-game)

### Inferences
- "성공"의 증거로 가장 강한 것은 *오래 유지되며 반복해서 되돌아오는 설계*다: Skyrim 방식(스킬 XP → 캐릭터 레벨, 곱연산 보너스, 체감 곡선), RuneScape의 지수 XP 곡선, DF의 XP+감쇠. 반대로 UO·SWG는 보정이 누적되며 복잡해졌다는 점에서 "초기 단순 규칙 + 지표 감시"와 "보정 장치의 누적" 사이의 비용 차이를 보여준다.
- 각 요소는 서로 다른 실패 양상에 대응한다: 체감 곡선→싼 반복 행동의 한계효용, 총량 캡/focus→만능형 수렴, 난이도 조건→매크로·허수아비, 교사/책→희박한 스킬의 정체, 스케일링 분리→레벨업이 약해지는 역설.
- 시간 기반(EVE)과 결과 기반(Koster)은 "행동 반복"을 보상에서 떼어내는 두 가지 방법이다. 둘 다 "당신이 하는 일이 곧 당신이 된다"는 직관을 일부 포기한다는 점은 인디 개발자가 "you become what you do"를 유지하려면 판단해야 할 지점이다.

### Gaps
- 이들 설계가 "성공적"이었다는 정량 근거(리텐션, 이탈률 등)는 Koster의 SWG 주장 외에는 찾지 못했다. Skyrim·RuneScape·EVE의 성공은 상업적 성과에서 추론한 것이지 해당 성장 시스템 덕이라는 개발자 증언은 확인하지 못했다.
- Bannerlord의 현재 수치는 커뮤니티 위키와 2018 개발 블로그 사이에 불일치 가능성이 있다(블로그는 레벨당 focus 2점으로 서술하나 커뮤니티 가이드는 다른 수치를 말한다는 검색 요약이 있었으나 열어보지 못함).
- KCD, Kenshi, PZ의 "성공" 요인에 대한 개발자 설명은 찾지 못했다.

---

## 4. 사용 기반 성장·플레이어 동기·익스플로잇 행동에 대한 학술/GDC 자료

### Takeaway
사용 기반 성장만을 직접 다룬 학술 논문은 찾지 못했다. 인접 자료로는 (a) 자동화(봇/매크로)가 반복적 레벨링을 어떻게 바꾸는지 분석한 Game Studies 논문(De Paoli, 2013), (b) 달성 동기 안에 "Mechanics"(규칙 분석·최적화) 요인을 분리해낸 Nick Yee의 동기 모델, (c) 개발자 쪽 1차 글(Johnson, Koster)이 있다. GDC 쪽은 UO 사후 분석 세션의 존재만 확인했고 내용은 열어보지 못했다.

### Cited Findings
- **De Paoli, "Automatic-Play and Player Deskilling in MMORPGs" (Game Studies, vol. 13 issue 1, 2013).** 봇·매크로 등이 레벨링을 자동화하는 것을 "automatic-play"로 규정하고, 플레이어의 "deskilling"과 봇의 "enskilling"을 이론화한다. 사례는 Tibia이며 2009-01 CipSoft의 안티봇 캠페인을 계기로 2009-01~2010-06 동안 공식 포럼 1,485페이지(페이지당 20개 글)와 게임 문서를 수집해 근거이론(grounded theory)으로 분석했다. — [Game Studies (Wayback 사본) [1차 학술]](https://web.archive.org/web/2024/https://gamestudies.org/1301/articles/depaoli_automatic_play)
  - 논문이 인용하는 문헌: MMORPG 레벨링을 반복적이고 지루하며 파편화된 과제의 집합으로 보고 Castronova가 시지프스 비유를 제안했다는 서술. 또한 Tibia에서 공식적으로 도입된 핫키/에임봇 같은 자동화도 플레이어 숙련을 "deskill"한다고 느낀 사례를 분석한다("official deskilling"). — [De Paoli [1차 학술]](https://web.archive.org/web/2024/https://gamestudies.org/1301/articles/depaoli_automatic_play)
  - 한계: 이 논문의 대상은 *경험치 기반 레벨링(몬스터 처치)*이며 스킬 사용 기반 성장 시스템 자체의 실험이 아니다.
- **Nick Yee, 플레이어 동기 모델.** MMORPG 플레이어 설문에서 10개 요인이 3개 상위 요인으로 묶였다(현재 데이터셋 3,200명, 39문항). Achievement 요인 안에 Advancement(목표 달성·빠른 레벨링·자원 축적에서 만족을 얻음)와 Mechanics(수치 메커니즘을 분석·이해하는 데서 만족, 목적은 "templating or optimizing a character")가 있다. — [Nick Yee, "A Model of Player Motivations" [1차 학술]](https://nickyee.com/daedalus/archives/print/001298.php)
- **Koster의 "fun checklist"는 *A Grammar of Gameplay*에서 가져온 것**으로 명시된다(도전 전 준비 여부, 공간 위상의 중요성, 핵심 동사, 능력의 다양성, 다중 성공 상태·실패 비용 등). 사용 기반 시스템이 이 항목을 만족하지 못해 "bottomfeeding"이 된다는 분석. — [Koster [1차]](https://www.raphkoster.com/?p=592)
- **GDC.** Koster 블로그에 따르면 GDC 2018(샌프란시스코)에서 Richard Garriott, Starr Long, Rich Vogel, Koster가 UO 20주년 "Classic Game Postmortem"을 진행했고(1시간 강연 + 1.5시간 Q&A), 이 세션에는 "development takeaways"가 있으며 그보다 앞서 GDC Online(오스틴)에서 진행한 별도의 UO 사후 분석이 있다고 한다. — [Koster 블로그: Ultima Online at 20](https://www.raphkoster.com/?p=32248), [Koster 블로그: UO postmortem from GDC2018](https://www.raphkoster.com/?p=32112). GDC Vault에도 "Classic Game Postmortem: Ultima Online" 항목이 있다(검색 결과로만 확인). — [GDC Vault](https://gdcvault.com/play/1016629/Classic-Game-Postmortem-Ultima). 슬라이드/영상 내용은 열어보지 못해 스킬 시스템에 관한 발언은 확인하지 못했다.
- **GDC Vault "Motivating Casual Players: Non-Traditional Character Progression and Player Retention"** 세션이 검색에 나왔으나 내용을 열어보지 못했다. — [GDC Vault](https://gdcvault.com/play/1012883/Motivating-Casual-Players-Non-Traditional)

### Inferences
- Yee의 Mechanics 요인은 "플레이어가 공식을 분석해 최적화한다"는 행동의 동기적 기반을 제공한다. Johnson/Koster의 "optimize the fun out"과 연결해 해석할 수 있으나, 두 자료가 서로를 인용하지는 않는다. 이는 내 추론이다.
- De Paoli의 틀(반복 과제 → 자동화)은 UO/RuneScape의 매크로 문제와 구조가 같고, 사용 기반 시스템은 *반복 과제가 성장 그 자체*이므로 자동화 유인이 더 직접적이다(추론).

### Gaps
- 사용 기반(use-based/learning-by-doing) 성장 시스템 자체를 다룬 동료심사 논문, 또는 스킬 시스템의 익스플로잇 행동을 계량한 실증 연구는 찾지 못했다. 검색에서 나온 봇 탐지 논문(auto-leveling 탐지)과 Irdeto 블로그는 열어보지 못해 인용하지 않았다.
- GDC Vault의 UO 사후 분석, 동기 세션은 영상/슬라이드를 열지 못해 스킬 시스템에 관해 무엇을 말하는지 확인하지 못했다. Koster의 책 *Postmortems: Selected Essays Volume One*에도 UO·SWG 회고가 있다고 하나 읽지 못했다.
- Soren Johnson의 Designer Notes 팟캐스트에서 이 주제를 다룬 에피소드가 있는지는 확인하지 못했다.
