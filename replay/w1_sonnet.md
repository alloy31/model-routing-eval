# 사용 기반("learn by doing") 캐릭터 성장 시스템: 설계 방식, 반복된 실패, 그리고 설계자·연구자의 결론

**표기 규칙 (보고서 작성자용).** 각 항목 끝의 태그는 근거의 확인 수준이다.
- **[열람]** = 해당 페이지를 직접 가져와 내용을 읽음. 단, 가져오기 도구가 페이지를 요약해 돌려주므로 따옴표 속 문장은 "도구가 보고한 원문"이다. 최종 보고서에 직접 인용할 때는 원문 대조를 권한다.
- **[요약]** = 검색 결과 요약문으로만 확인했고 원문 페이지는 열지 못함. 신뢰도 낮음.
- **[커뮤니티]** = 팬 위키·포럼·공략 글. 개발자의 공식 진술이 아님.
- **[추정]** = 내 해석. 출처 없음.

**접근 제한 (중요).** UESP 위키(Elder Scrolls 기계적 세부사항의 표준 출처)는 WebFetch에서 전부 403이었다. curl 우회 시도는 권한 분류기가 거부했고, 이를 우회하려 하지 않았다. 그래서 Morrowind/Oblivion/Skyrim의 수치 세부는 Wikipedia와 검색 요약에 의존한다. Tim Cain 관련 위키 페이지는 로그인 장벽(Cloudflare Access)으로 열 수 없었고, DF 위키는 429, EVE 포럼 아카이브는 503/404로 열지 못했다.

---

## 1. 개별 게임의 사용 기반 성장 설계와 문제점

### Takeaway
거의 모든 사용 기반 시스템에서 "행동 횟수 → 성장"이라는 연결이 가장 값싼 행동을 반복하게 만드는 최적화 압력을 만들었다. 설계자들은 (a) 확률·속도 조정, (b) 난이도 연동, (c) 시간 기반 상한, (d) 시스템 폐기·교체 중 하나로 대응했다. UO의 매크로 문제, Oblivion의 레벨링 문제, FFII의 아군 공격 착취가 대표적이다.

### Cited Findings

#### Ultima Online (UO)
- Raph Koster의 블로그 글 "Use-based systems"(2006-07-18 게시, 페이지에는 2015-06-15 갱신 표시)에 따르면 사용 기반 시스템은 "스킬을 쓸 때마다 향상될 확률이 생기는" 방식이며, 모든 스킬에 처음부터 접근할 수 있어 "more freeform game experience"를 허용한다. 그는 "In the real world, this is called 'practice,' and we don't regard it as a bad thing"라고 쓴다. [열람] — [Koster, Use-based systems](https://www.raphkoster.com/?p=592)
- UO 초기 설계: 다른 사람이 스킬을 쓰는 것을 *관찰*해도 향상될 수 있었고, 난이도 등급이 없어 자기 수준보다 한참 낮은 과제로도 계속 배울 수 있었다. 안 쓰는 스킬은 감소(decay)했고, 총합 700점의 상한이 있었다. [열람] — [Koster](https://www.raphkoster.com/?p=592)
- 스킬마다 사용 빈도가 크게 달라서, 팀은 사용 빈도를 추적해 각 스킬의 향상 확률을 자동 조정하는 방식을 도입했다. Koster는 이 자기균형 장치가 "didn't work"였다고 말한다. 향상이 점점 느려지자 플레이어들이 매크로로 대응했고, "What broke was the feedback mechanism." 플레이어에게는 "infinite" 시간이 있어 희귀한 보상도 억제력이 되지 못했다. [열람] — [Koster](https://www.raphkoster.com/?p=592)
- 매크로 사례: 플레이어들이 강한 몬스터를 집 안에 가둬 놓고 그것을 상대로 매크로를 돌렸다. [열람] — [Koster](https://www.raphkoster.com/?p=592)
- "8×8 macroing": UO는 맵을 8×8 청크로 나누고 청크 ID로 난수 시드를 정했다. 의도는 플레이어를 이동하게 만드는 것이었으나, 플레이어들이 실험으로 "실패한 뒤 8칸 이동하면 성공 확률이 오른다"는 것을 알아냈다. Koster는 이것을 "플레이어는 실험으로 모든 시스템을 해독한다"는 자신의 법칙의 사례로 든다. [열람] — [Koster](https://www.raphkoster.com/?p=592)
- 이후 Runesabre가 빈도 기반 자동 조정 표를 손으로 짠 표(hand-coded table)로 교체했다. Koster는 그래도 사용률 추적은 해야 한다고 권고한다("The challenge is fixing the feedback loop"). 표를 없앤 뒤 "guaranteed gain"과 "power hour" 같은 메커니즘이 필요해졌다고 서술한다. [열람] — [Koster](https://www.raphkoster.com/?p=592)
- Koster의 1998년 MUD-Dev 글에서도 같은 우려가 보인다("sitting and macroing", "advancement rates for differing skill are hellish to balance out"). 검색 요약으로만 확인했고, 해당 스레드 URL은 둘 중 하나로 보이나 확정하지 못했다. [요약] — [MUD-Dev 1998/5 #6112](https://mud-dev.zer7.com/1998/5/6112) / [#6101](https://mud-dev.zer7.com/1998/5/6101)
- Guaranteed Gain System(GGS, Publish 16, 2002): 정상 사용 기반 향상이 일정 시간 없으면 최소 +0.1을 보상한다. 대상은 "play infrequently"하는 플레이어나 운이 나쁜 플레이어다. 타이머는 총 스킬 점수에 따라 달라지고 "server system clock"으로 돌아가므로 로그인하지 않아도 흐른다. 성공한 사용만 기록하고 실패는 세지 않으며, 스킬 사용이 캐릭터 수준 "at or near"일 때만 적용된다(예: Magery 90.0에서 Magic Arrow는 GGS 대상 아님). 스탯은 "up to 1 Stat point per 30 minutes", "up to 6 Stat points per day" 상한. 페이지의 예시 표(700 총점 기준 80.0–84.9 구간 +0.1당 15시간)는 "추정치"로 제시된다. **이 페이지는 매크로를 동기로 언급하지 않는다.** [열람] — [UO.com, Publish 16 (part 2)](https://uo.com/wiki/ultima-online-wiki/technical/previous-publishes/2002-2/2002-publish-16-part-2-23rd-july/)
- 별도 "Rate Over Time" 시스템(Siege Perilous, Mugen 서버)은 70 이상 구간의 향상을 고정 간격으로 제한한다(예: 70.0–79.9는 5분마다 +0.1). 검색 요약만 확인. [요약] — [UO.com, Guaranteed Gain / Rate Over Time](https://uo.com/?p=6342)

#### Elder Scrolls: Morrowind / Oblivion / Skyrim
- **Morrowind**의 속성 보너스 배율: 레벨업 때 직전 레벨업 이후 해당 속성에 속한 스킬이 몇 번 올랐는지에 따라 배율이 정해진다(×1 → 1–4회 ×2 → 5–7회 ×3 → 8–9회 ×4 → 10회 이상 ×5). UESP 토론 페이지의 사용자 기여 내용이고, 한 사용자가 테스트 실패를 보고했다. [커뮤니티·요약] — [UESP Morrowind talk:Level](https://en.m.uesp.net/wiki/Morrowind_talk:Level)
- Soren Johnson은 Morrowind의 "skill-farming"을 "플레이어 시간을 작은 보상과 맞바꾸는" 전략의 예로 든다. [열람] — [Johnson, Water Finds a Crack](https://www.designer-notes.com/game-developer-column-17-water-finds-a-crack/)
- **Oblivion** 구조: 7개의 major skill을 고르고, major skill이 합계 10점 오를 때마다 레벨업. 21개 스킬이 전투·마법·잠행에 균등 배분. 스킬 25/50/75/100에서 새 능력 해금. [열람] — [Wikipedia, Oblivion](https://en.wikipedia.org/wiki/The_Elder_Scrolls_IV:_Oblivion)
- Oblivion의 적과 전리품은 플레이어 레벨에 따라 스케일된다("become stronger, and looted weapons and armor more effective as the player levels up"). 위키피디아는 이 스케일링과 레벨링의 결합이 비판받았고, athletics·armor 같은 스킬이 *의도치 않게* 올라 캐릭터가 너무 빨리 레벨업하고 불균형하게 강한 적을 만난다고 정리한다. IGN의 Charles Onyett도 "the disjunction between enemies that scaled up according to the player's level"를 비판. [열람] — [Wikipedia, Oblivion](https://en.wikipedia.org/wiki/The_Elder_Scrolls_IV:_Oblivion)
- UESP는 이 현상을 "Leveling Problem"이라 부른다: 적이 스케일되므로 "레벨업이 오히려 적 대비 전투력을 떨어뜨릴 수 있다". "Efficient Leveling"은 레벨당 약 10회의 major skill 상승을 세 속성에 몰아 큰 속성 보너스를 얻는 방식이다. UESP 페이지는 열지 못했고 검색 요약의 표현이다. [요약] — [UESP Oblivion:Efficient Leveling](https://content1.uesp.net/wiki/Oblivion:Efficient_Leveling)
- Koster는 Oblivion의 점프로 스킬을 올리는 행동을 사용 기반 시스템 비판의 예로 든다: "There's no challenge in jumping off a hill in Oblivion," 그래서 그라인드가 생긴다. [열람] — [Koster](https://www.raphkoster.com/?p=592)
- 일부 평론가가 "레벨업을 피하려고 major skill을 일부러 쓰지 않는 플레이"를 문제로 지적했다는 서술이 있으나 출처 불명의 2차 요약이다. [요약, 커뮤니티 믿음에 가까움] — [PSU](https://www.psu.com/news/bethesda-explains-elder-scrolls-v-classes-axe/)
- 헤드라인만 확인: GamesRadar는 "전직 Elder Scrolls 개발자가 레벨 스케일링 시스템이 실수였다고 인정, Skyrim에서 결국 고쳐짐"이라고 보도했다. 본문을 열지 못해 발언자·원 인터뷰를 확인하지 못했다(검색 요약은 Nesmith라 했으나 미확인). [헤드라인만] — [GamesRadar](https://www.gamesradar.com/games/the-elder-scrolls/as-oblivion-remastered-introduces-new-fans-to-bethesdas-iconic-2006-rpg-ex-elder-scrolls-dev-admits-the-level-scaling-system-was-a-mistake-eventually-fixed-in-skyrim)
- **Skyrim**: 18개 스킬(전투·마법·잠행 균등), 스킬마다 XP 바. "After enough skills level up, the character levels up", 레벨업 시 3개 속성(Health/Magicka/Stamina) 중 하나 최대치 증가, 레벨업마다 perk point 1개. 패치 1.9에서 "Legendary" 스킬이 사실상 레벨 상한을 제거. 평론가들은 클래스 선택 제거를 호평("experiment with different skills without having to make decisions about a class early"). [열람] — [Wikipedia, Skyrim](https://en.wikipedia.org/wiki/Skyrim)
- Bruce Nesmith(Skyrim 리드 디자이너)의 2011년 Q&A(Xbox360Achievements 대담을 GameBanshee가 2011-06-06 재게재): "We looked at the skills from Oblivion for their usefulness and clarity to the player." "Some skills just weren't very useful as skills, such as Acrobatics. Others were confusing, such as Mysticism." 이 글은 스킬 정리만 다루며 레벨링·스케일링 발언은 없다. [열람] — [GameBanshee Skyrim Q&A](http://www.gamebanshee.com/k6kr)
- Todd Howard: "In Oblivion you have your eight attributes and 21 skills. Now you have 18 skills and three attributes." [요약] — [PC Gamer UK](https://www.pcgamer.com/uk/todd-howard-on-the-lessons-skyrim-has-learned-from-fallout-3/)
- Howard가 Skyrim 레벨링을 "You just play, and your skills go up as you play and the higher your skill, the more it affects your leveling… a really, really nice elegant system that kind of self-balances itself"라고 설명했다는 인용이 있다. **GamesRadar 기사를 열어 확인하려 했으나 본문이 잘려 확인 실패.** 보고서에 쓰려면 원문 확인 필요. [요약, 미검증] — [GamesRadar](https://gamesradar.com/elder-scrolls-v-skyrim-new-levelling-system-dual-wielding-non-rubbish-people-octogenarian-swedes)
- PC Gamer 헤드라인(Nesmith 관련으로 보도): "We got rid of attributes in Skyrim and you know who complained? Almost nobody". 본문·날짜·원 인터뷰 미확인. [헤드라인만] — [PC Gamer](https://www.pcgamer.com/games/the-elder-scrolls/bethesda-veteran-says-less-rpg-complexity-in-the-elder-scrolls-series-is-good-actually-we-got-rid-of-attributes-in-skyrim-and-you-know-who-complained-almost-nobody)

#### Final Fantasy II
- 전통적 경험치 레벨이 없고 "develops depending on what actions they take". 자주 쓰는 무기 종류가 숙련되며 힘·명중도 오르고, 큰 피해를 받으면 최대 HP가, MP를 많이 쓰면 최대 MP가 오른다. [열람] — [Wikipedia, Final Fantasy II](https://en.wikipedia.org/wiki/Final_Fantasy_II)
- 위키피디아는 이 시스템이 "several unintended consequences that allowed characters to gain much more experience than intended"를 낳았다고 쓰며, 캐릭터끼리 서로 공격하거나 주문을 반복 시전해 HP와 능력치를 크게 올릴 수 있었다고 설명한다. [열람] — 같은 페이지
- 河津秋敏(Akitoshi Kawazu)는 경험치 시스템에 불만이 있어 "something unpredictable for players"를 원했고, 나중에 "went too far in making the game different from the original"이라고 느껴 후속작은 전통 모델로 돌아갔다고 위키피디아가 서술한다(원 인터뷰 URL은 미확인). Final Fantasy III은 원작 시스템으로 회귀. [열람] — 같은 페이지
- 평론: G4 "sounds novel at first wound up being a huge mess", GameSpot "chaotic", GameSpy "quirky and sometimes confusing". [열람] — 같은 페이지

#### Quest 64
- 전통적 레벨업 모델이 아니며, FFII처럼 전투 내 행동에 따라 해당 능력치에 경험이 쌓인다("If the character gets hit a lot, for instance, defense will increase"). 정령을 찾으면 불·물·땅·바람 중 한 원소를 올려 새 공격을 얻고 기존 공격을 강화한다. 위키피디아에는 HP/MP/공격력의 구체적 성장 규칙이나 시스템 비판이 없다. [열람] — [Wikipedia, Quest 64](https://en.wikipedia.org/wiki/Quest_64)

#### SaGa 시리즈
- "Battle Rank": 전투에 참가한 횟수에 따라 적이 강해지고, 원작(1993)에서는 도망친 전투도 전투 수에 같게 셌다. 리메이크(Romancing SaGa 2)에서는 "플레이어의 강함에 따라 적이 강해지는" 방식으로 바꾸자는 제안이 개발 중 논쟁거리였다고 한다. [요약] — [Shacknews 인터뷰](https://shacknews.com/article/141456/romancing-saga-2-revenge-of-the-seven-interview), [RPG Site](https://www.rpgsite.net/interview/16302-romancing-saga-2-revenge-of-the-seven-interview-talking-remaking-a-niche-classic-with-shinichi-tatsuke), [Automaton](https://automaton-media.com/en/news/romancing-saga-2s-original-creator-feared-only-one-thing-about-the-remake-a-shift-to-the-action-genre/)
- Kawazu는 2021년 Wccftech 인터뷰에서 레벨 시스템이 "didn't contribute a whole lot to the underlying enjoyment"라서 시리즈가 벗어났다고 말했다. 또 Denfaminicogamer 인터뷰에서 "to help a person grow, you have to provide them with challenges"라고 말했다고 Automaton이 보도. [요약] — [Wccftech](https://wccftech.com/interview-with-saga-director-akitoshi-kawazu-saga-frontier-2-romancing-saga-future-of-the-series/), [Automaton](https://automaton-media.com/en/?p=46891)

#### Dungeon Siege
- 검색 요약에 따르면 Chris Taylor는 GameSpot 개발 중 Q&A에서 이 게임을 "skill-based class system"으로 설명했다. 스킬을 자유롭게 섞고 언제든 어떤 스킬이든 키우기 시작할 수 있으며, 단순함을 유지하면서 유연성을 주는 것이 목표였다. DS2는 하이브리드 클래스와 스킬 트리를 추가했고, DS3는 이름 붙은 캐릭터 4명으로 클래스 개념을 버렸다. **스킬이 "사용"으로 오르는 구체 규칙은 확인하지 못함.** [요약] — [GameSpot Q&A](https://www.gamespot.com/articles/dungeon-siege-qanda/1100-2625619/), [Kikizo 인터뷰](https://games.kikizo.com/features/dungeonsiege2_christaylor_interview.asp), [Engadget DS3 프리뷰](https://www.engadget.com/2011-02-23-dungeon-siege-3-preview.html)

#### Kenshi
- 스탯은 크게 7개 범주(Attributes, Weapon Skills, Combat Skills, Thievery, Athletics, Science, Trade)이며 "해당 스탯의 영향을 받는 행동을 완수함으로써" 오른다. 달리면 athletics, 맞으면 toughness가 오른다. Toughness는 0.61.0에서 도입. [커뮤니티] — [Kenshi Wiki (Fandom)](https://kenshi.fandom.com/wiki/Toughness), [GOG 공략](https://gog.com/forum/kenshi/my_kenshi_training_guide_from_zero_to_hero_part_1)
- "Stronger Opponent Logic": Martial Arts 등 전투 스킬 4종의 XP 속도가 상대의 강함과 연동된다. 약한 적과 싸우면 보상이 줄고, 스킬 약 70 이상에서는 더 강한 상대가 필요하다는 플레이어 보고. [커뮤니티] — [Kenshi Wiki: Martial Arts](https://kenshi.fandom.com/wiki/Martial_Arts)
- 알려진 착취: 사람을 침대에 눕혀 놓고 때리는 방식, 과적재·중장갑으로 훈련 속도를 올리는 방식, 훈련용 더미(치트 더미 포함). 개발자 Chris Hunt의 직접 설계 발언은 **찾지 못했다**. 훈련 더미를 실전 대체로 쓰지 않게 하려는 의도라는 Steam 사용자 주장은 미확인이다. [커뮤니티] — [GOG 공략](https://gog.com/forum/kenshi/my_kenshi_training_guide_from_zero_to_hero_part_1)

#### RuneScape
- 사용 기반(행동당 XP) 스킬 훈련 자체의 설계 근거 문서는 못 찾았다. 확인된 것은 Jagex의 장기 봇 대응 이력이다: 2011년 "Bot Nuke Day"로 약 150만 계정 정지(Jagex CEO 설명: 여러 대책을 함께 작동시킨 결과), iBot 개발사 상대 소송 승소, 2012년 상습 봇 사용자를 격리하는 "Botany Bay" 섬, 2013년 "Botwatch", 이후 골드 구매자까지 제재. [요약] — [PC Gamer](https://www.pcgamer.com/runescape-bot-nuking-event-bans-1-5-million-bots-in-one-day/), [Engadget 2013](https://www.engadget.com/2013-02-27-botters-are-losing-the-farm-with-runescapes-newest-anti-botting.html), [RuneScape 공식 뉴스](https://secure.runescape.com/m=news/a=26/bot-busting-update-legal-proceedings)

#### EVE Online
- 스킬은 실시간으로 훈련되고 로그아웃 중에도 진행된다. 더 많이 플레이한다고 빨라지지 않고, 안 해도 멈추지 않는다. [커뮤니티] — [EVE University Wiki](https://wiki.eveuniversity.org/Skill_training), [Guild Order](https://guildorder.com/games/eve/wiki/skill-training-and-the-real-time-clock)
- 설계 의도에 대한 진술("casual players keep pace with power gamers")은 포럼 사용자의 말이지 CCP 공식 발언이 아니다. [커뮤니티] — [EVE Forums 아카이브](https://forums-archive.eveonline.com/topic/128806)
- "UO의 매크로 문제에 대한 반응으로 시간 기반을 택했다"는 널리 도는 설명은 **CCP의 문서화된 진술을 찾지 못했다. 커뮤니티 믿음으로 취급할 것.**

#### Star Wars Galaxies (SWG)
- 출시 당시 34개 직업(위키피디아는 "six basic and 24 advanced"라 쓰는데 합이 30이라 수치가 안 맞음). 직업은 Novice 1개 + 4갈래×4단계 + Master 구조. 스킬은 관련 활동으로 번 XP로 *구매*했다. [열람, 위키 본문 미인용] — [Wikipedia, SWG](https://en.wikipedia.org/wiki/Star_Wars_Galaxies)
- 2005년 11월 NGE는 직업을 9개로 줄이고 진행을 combat/crafting/entertaining XP 그룹으로 나눴다. John Smedley는 NGE가 "reverse the deterioration they were seeing in the subscriber base"에 필요했다고 변호(2005 Slashdot 인터뷰, 위키피디아 인용). 2012 Reddit에서는 Combat Upgrade와 NGE에 "stupid decisions"가 있었다고 인정. 환불 요구와 이탈 보도. [열람] — 같은 페이지
- Koster의 분류상 SWG는 순수 사용 기반이 아니라 "results-based" XP 방식이다. XP를 *결과*(구체적 성과)에서 얻고, 제작 XP는 한때 "남이 내가 만든 것을 사용하는 것"과 연동됐다가("a validation that what you made actually worth something to someone") 직접 제작 XP로 바뀌었다. 출시 3일 전 한 디자이너가 진행 속도를 10배 늦추려 했으나 Koster가 되돌렸다("making literally thousands of blaster bolts" 요구는 너무 그라인드). SWG의 지침: "More tools, not more power." [열람] — [Koster](https://www.raphkoster.com/?p=592)
- NGE의 동기는 구독자 감소였지 "스킬 시스템의 구조적 결함"의 문서화된 진단이 아니다(Smedley 진술 기준). [열람] — [Wikipedia, SWG](https://en.wikipedia.org/wiki/Star_Wars_Galaxies)

#### Mount & Blade / Kingdom Come: Deliverance
- Bannerlord: 스킬은 쓸수록 오르며, 학습 속도(learning rate)와 학습 한계(learning limit)가 있고 한계를 넘으면 향상이 둔화한다. 속성과 focus point가 이 둘을 올린다. 배율 수치는 출처마다 충돌한다(예: focus 1.25배, 한계 +30). TaleWorlds 공식 설명은 찾지 못했다. [커뮤니티] — [Mount & Blade Wiki](https://mountandblade.fandom.com/wiki/Skills_(Bannerlord)), [Gamewatcher](https://www.gamewatcher.com/mount-and-blade-2-levelling-guide), [PCGamesN](https://www.pcgamesn.com/mount-blade-2-bannerlord/mount-blade-2-bannerlord-skills)
- KCD: 클래스 없이 관련 행동으로 스킬이 오른다. KCD2에서는 스킬을 능동적으로 써야 XP를 얻고, "Main Level"은 모든 스탯에서 파생되는 평균 같은 값이며, perk는 스킬 레벨 요건으로 잠겨 있다. Warhorse 개발자의 설계 진술은 못 찾았다. [커뮤니티] — [KCD Wiki](https://kingdom-come-deliverance.fandom.com/wiki/Skills_(KCD)), [KCD wiki.gg Main Level](https://kingdomcomedeliverance.wiki.gg/wiki/Main_Level)

#### Project Zomboid
- 서드파티 가이드 기준: 스킬 책이 해당 스킬의 XP 배율을 올리는 핵심 가속기이고, 레벨은 영구적이며 안 써도 감소하지 않고, 레벨업으로 perk point를 주지 않는다. 레벨당 XP 수치는 가이드마다 달라 신뢰하지 않았다. Indie Stone 개발자의 설계 설명과 "수면 관련 착취"는 확인하지 못했다. [커뮤니티] — [pindrop.gg](https://pindrop.gg/project-zomboid/skills), [XGamingServer](https://xgamingserver.com/blog/project-zomboid-skills-leveling-guide/)

#### Dwarf Fortress
- 스킬은 사용으로 오른다. 버전별 위키 기준 대부분의 민간 스킬은 사용당 30 XP, smoothing·fortification 조각·engraving·mining은 10 XP. 안 쓰면 "rusty" → "very rusty"로 감퇴한다. 학습·녹 속도는 creature raw의 `SKILL_RATES`로 조정 가능. 모험 모드는 정확한 XP를 보여주지만 요새 모드는 보여주지 않는다. Tarn Adams의 설계 발언은 찾지 못했다. [요약, 커뮤니티] — [DF Wiki: Experience](https://dwarffortresswiki.org/index.php/DF2014:Experience), [DF Wiki: Rust](https://dwarffortresswiki.org/index.php/Rust), [버그 트래커](https://dwarffortressbugtracker.com/view.php?id=2877)

### Inferences
- [추정] 실패의 공통 구조는 "성장 단위 = 행동 횟수"일 때 *가장 싸고 안전하고 빠른 행동*이 최적해가 된다는 것이다. UO(매크로), Oblivion(점프·Efficient Leveling), FFII(아군 공격), Kenshi(침대 위 사람 때리기)가 모두 이 구조다.
- [추정] 대응 방식은 크게 넷이다. ① 확률 조정(UO 빈도 표 → 실패), ② 난이도·상대 강도 연동(Kenshi Stronger Opponent Logic, UO GGS의 "at or near" 조건), ③ 시간 기반 상한(EVE, UO Rate Over Time), ④ 시스템 폐기(FFIII, NGE, Skyrim의 스킬 정리). ③은 착취를 없애는 대신 행동과 성장의 연결 자체를 끊는다.
- [추정] SWG의 NGE 전환은 "사용 기반 시스템의 실패"로 단순화하면 안 된다. 문서화된 이유는 구독자 감소이고, SWG 자체가 순수 사용 기반이 아니라 결과 기반 XP 구매 방식이었다.

### Gaps
- UESP의 Morrowind/Oblivion/Skyrim 레벨링·트레이너·스킬 XP 표(원전 수준의 수치)는 접근 불가로 직접 확인 못 함.
- UO "Power Hour"의 정확한 정의·도입 시기는 신뢰할 만한 출처를 못 찾음(Koster 글에 이름만 등장).
- Kenshi의 Chris Hunt, KCD의 Warhorse, Project Zomboid의 Indie Stone, Dwarf Fortress의 Tarn Adams, TaleWorlds의 설계 의도를 직접 밝힌 1차 자료는 찾지 못함.
- Dungeon Siege, SaGa(글림머·사용 기반 능력치 성장), Quest 64의 정확한 성장 규칙, RuneScape XP 곡선과 훈련 설계에 대한 1차 자료는 확인 못 함.
- Rolston이 Oblivion 레벨링을 어떻게 평가했는지(2006년 은퇴 인터뷰에서 "처음엔 Morrowind의 명백한 밸런스 결함의 치료제로 인식됐다"는 검색 요약이 있었으나 미확인)와 Todd Howard의 Skyrim 레벨링 원문 인용은 검증 못 함.
- Skyrim의 제작·인챈트 스킬 파밍 착취에 대한 문서는 찾지 못함(커뮤니티에 널리 알려진 것으로 보이나 출처 없음).

---

## 2. 문서화된 일반 실패 유형과 유명한 문구의 원전

### Takeaway
"Given the opportunity, players will optimize the fun out of a game"의 원전은 Soren Johnson의 Game Developer 2011년 3월호 칼럼 "Water Finds a Crack"(Designer Notes에 2011-06-12 재게재)이다. 사용 기반 시스템에 대한 가장 상세한 개발자 진단은 Raph Koster의 "Use-based systems"이며, 핵심은 "성장 보상 장치를 재미의 위치와 분리하면 플레이어가 재미 없는 쪽으로 최적화한다"는 것이다.

### Cited Findings
- **Johnson 인용 원문**: "Many players cannot help approaching a game as an optimization puzzle. What gives the most reward for the least risk?... Given the opportunity, players will optimize the fun out of a game." 칼럼의 예시는 Civilization III/IV, Ultima Online, Morrowind, Super Mario Bros.이다. 원 게재: Game Developer 2011년 3월호, Designer Notes 게시 2011-06-12. [열람] — [Johnson, Water Finds a Crack](https://www.designer-notes.com/game-developer-column-17-water-finds-a-crack/)
- Johnson이 분류한 두 부류: ① 지배 전략(dominant strategy)이 다른 선택을 무의미하게 만듦(MMO의 "tank-mages", Civ의 "infinite city sleaze"), ② 플레이어의 시간을 작은 보상과 맞바꾸는 전략(Morrowind 스킬 파밍). 처방: 상황에 따라 최선이 달라지도록 지배 전략에 비용을 붙인다, 지루한 반복에 보상하는 메커니즘을 제거한다, 모든 착취를 없애지는 않는다(Super Mario Bros. 1UP 트릭처럼 숙련을 보상하는 것도 있다), 가능하면 착취를 켜고 끌 수 있게 한다. [열람] — 같은 칼럼
- 이 문구가 Johnson의 더 이른 강연·글에서 처음 나왔는지는 확인하지 못했다. 검색으로 확인되는 가장 이른 출처가 위 칼럼이다. [요약] — [검색 결과 목록](https://www.designer-notes.com/writings)
- **Koster: 피드백 메커니즘 실패와 매크로 유인** — 향상 확률을 자동으로 낮추는 장치는 느린 향상만 만들었고 플레이어는 "infinite" 시간으로 매크로를 돌렸다. [열람] — [Koster](https://www.raphkoster.com/?p=592)
- **Koster: 플레이어는 시스템을 해독한다** — 8×8 매크로 사례를 "players will decode every system through experimentation" 법칙의 예로 든다. [열람] — [Koster](https://www.raphkoster.com/?p=592)
- **Koster: 반복이 지루한 이유는 도전이 없기 때문** — "Practice is only boring when it doesn't challenge and teach the player." 심리적 요인(bottomfeeding, 실패 비용이 없음)이 있으므로 "the systems must adapt to the psychology." [열람] — [Koster](https://www.raphkoster.com/?p=592)
- **Koster: 밸런스 부담** — 손으로 짠 향상률 표는 플레이어가 착취를 찾아낼 때마다 갱신해야 한다("A hand-coded advancement rate table will always need to be updated as players discover exploits that drive them towards one skill or another"). 1998년 MUD-Dev 글에서도 스킬별 향상률 조정이 "hellish"하다고 썼다. [열람/요약] — [Koster](https://www.raphkoster.com/?p=592), [MUD-Dev 1998](https://mud-dev.zer7.com/1998/5/6112)
- **정체성 상실/만능화 문제**: 직접 정리한 1차 개발자 자료는 못 찾았다. 관련 단서: Koster는 UO/SWG를 다시 만든다면 "모든 스킬을 배우게 하되 가지고 다닐 수 있는 도구를 제한해 '오늘 누구가 되고 싶은지' 고르게" 하겠다고 댓글에서 말했다. SWG의 지침은 "More tools, not more power". UO에는 총합 700점 상한이 있었다. [열람] — [Koster](https://www.raphkoster.com/?p=592) / Skyrim 평론가 John Bedford(Eurogamer)는 게임이 "all-around character"를 만들고 싶은 플레이어에게 맞춰졌다고 썼고, 패치 1.9의 Legendary 스킬은 사실상 레벨 상한을 없앴다. [열람] — [Wikipedia, Skyrim](https://en.wikipedia.org/wiki/Skyrim)
- **읽기 어려운 진행**: FFII는 G4 "huge mess", GameSpot "chaotic", GameSpy "quirky and sometimes confusing"으로 평가됐고, Kawazu 본인이 "the only one who understood it among the staff"였다고 회고했다(위키피디아 서술). [열람] — [Wikipedia, FFII](https://en.wikipedia.org/wiki/Final_Fantasy_II) / Skyrim 쪽 Nesmith는 스킬을 "usefulness and clarity to the player" 기준으로 점검했다고 말한다. [열람] — [GameBanshee](http://www.gamebanshee.com/k6kr)
- **Oblivion의 레벨링 문제**: 스킬이 비자발적으로 올라 캐릭터가 너무 빨리 레벨업하고, 스케일되는 적이 불균형해지는 문제를 위키피디아가 정리. UESP는 "Leveling Problem"으로 명명. [열람/요약] — [Wikipedia](https://en.wikipedia.org/wiki/The_Elder_Scrolls_IV:_Oblivion), [UESP](https://content1.uesp.net/wiki/Oblivion:Efficient_Leveling)
- **Tim Cain(요약 위키의 2차 정리)**: 스킬 기반 XP가 부르는 퇴화 행동으로 "약한 적과 싸워 전투 스킬 만렙 만들기", "벽에 주문 반복 시전"을 들고, 완화책으로 사용당 수익 체감, 실패에도 XP 부여를 제안한다고 한다. 해당 위키 페이지는 로그인 장벽으로 열지 못했고 Cain 본인의 영상·강연도 확인하지 못했다. [요약, 2차] — [turbo-wiki (검색 결과 URL)](https://turbo-wiki.pages.dev/tim-cain/system-design/skill-based-xp)
- **Bethesda의 Skyrim 개편 이유(문서화된 것)**: 스킬 수를 줄이고 속성을 3개로 단순화(Howard 요약 발언), 쓸모가 없거나(Acrobatics) 혼란스러운(Mysticism) 스킬 정리(Nesmith 2011 Q&A). 클래스 선택 제거의 이유를 "인위적 선택 강요 대신 쓰는 스킬이 클래스를 형성"으로 정리한 보도가 있으나 2차 요약이다. [열람/요약] — [GameBanshee](http://www.gamebanshee.com/k6kr), [PC Gamer UK](https://www.pcgamer.com/uk/todd-howard-on-the-lessons-skyrim-has-learned-from-fallout-3/), [PlayStation LifeStyle](https://www.playstationlifestyle.net/?p=133817)
- **Skyrim에서 major/minor skill 제거에 대한 Bethesda의 직접 설명**: 요청받은 항목이었으나, Nesmith·Howard가 "왜 major/minor 구분을 없앴는가"를 직접 설명한 원문은 확인하지 못했다. Skyrim에서는 모든 스킬이 레벨에 기여한다는 구조(위키피디아)만 확인된다.

### Inferences
- [추정] Johnson의 두 부류와 Koster의 진단을 합치면, 설계가 막아야 할 것은 "착취" 그 자체보다 "플레이어의 가장 쉬운 선택이 가장 재미없는 선택이 되는 구조"다.
- [추정] 정체성 상실("모두가 만능")은 문서화가 약하다. 가장 가까운 근거는 UO의 총합 상한(700)과 Koster의 "도구 제한" 발언이고, 상한 없는 Skyrim은 Legendary 스킬로 오히려 상한을 제거했다.
- [추정] FFII 사례는 "읽기 어려운 진행"과 "착취 가능성"이 서로 얽혀 있음을 보여준다. 플레이어가 규칙을 이해하지 못하면 의도된 플레이가 아닌 실험적 해법에 의존하게 된다.

### Gaps
- Johnson 문구의 더 이른 기원(GDC 강연 등)은 미확인.
- Bethesda가 Skyrim에서 major/minor 스킬을 제거한 이유에 대한 직접 인터뷰 원문(Game Informer, Howard/Nesmith 팟캐스트 등)은 열지 못함.
- "Koster의 법칙" 목록 원문(Koster's Laws of Online World Design)은 이번에 직접 열지 못함. 위 인용은 "Use-based systems" 글 안의 서술이다.
- Tim Cain의 1차 자료(YouTube 영상 등)는 위치를 확인하지 못함.

---

## 3. 성공 사례로 평가되는 설계와 작동 요인

### Takeaway
"성공"의 근거는 대부분 개발자의 평가가 아니라 시장·평론·커뮤니티 반응이다. 작동한 요소로 가장 자주 나온 것은 ① 난이도·상대 강도 연동, ② 한계/상한과 체감 수익, ③ 안 쓰면 감퇴(rust), ④ 접근 가능한 성장 읽기 쉬움, ⑤ 단일 레벨 지표 통합(Skyrim, KCD2)이다. "rested/first-time bonus", "learn from failure", "teacher 요건"을 명시적으로 다룬 문서화된 사례는 거의 못 찾았다.

### Cited Findings
- **Skyrim**: 모든 스킬이 각자의 XP 바를 갖고, 충분히 오르면 캐릭터 레벨이 오르고 perk point를 준다. 평론가는 클래스 제거와 perk 시스템을 호평했다(예: VanOrd "forms around the way you play, but allows for tweaking so that you retain a sense of control"). [열람] — [Wikipedia, Skyrim](https://en.wikipedia.org/wiki/Skyrim) / Howard가 "the higher your skill, the more it affects your leveling… self-balances"라고 설명했다는 인용은 **미검증**. [요약] — [GamesRadar](https://gamesradar.com/elder-scrolls-v-skyrim-new-levelling-system-dual-wielding-non-rubbish-people-octogenarian-swedes)
- **UO GGS**: 불운과 간헐적 플레이에 대한 보상(catch-up). 시간은 서버 시계로 흐르고, 스킬 사용이 캐릭터 수준에 가까울 때만 적용되며, 실패한 사용은 세지 않고, 스탯 획득에 시간·일 단위 상한이 있다. 유료 서버 외에 Rate Over Time 서버는 70 이상에서 고정 간격 향상. [열람/요약] — [UO.com Publish 16](https://uo.com/wiki/ultima-online-wiki/technical/previous-publishes/2002-2/2002-publish-16-part-2-23rd-july/), [UO.com GGS/RoT](https://uo.com/?p=6342)
- **Kenshi**: 상대가 강할수록 전투 스킬 XP가 커지는 "Stronger Opponent Logic". 약한 적은 보상이 줄어 파밍이 어려워진다. 한계: 침대 착취·훈련 더미 등 우회가 남아 있다. [커뮤니티] — [Kenshi Wiki](https://kenshi.fandom.com/wiki/Martial_Arts), [GOG 공략](https://gog.com/forum/kenshi/my_kenshi_training_guide_from_zero_to_hero_part_1)
- **Bannerlord**: 학습 한계(learning limit)를 넘으면 향상이 둔화되고, focus point와 속성이 학습 속도·한계를 올린다. 즉 *무엇을 많이 쓰든* 한계까지는 오르되, 그 이상은 투자를 해야 한다. 수치는 출처마다 충돌. [커뮤니티] — [Mount & Blade Wiki](https://mountandblade.fandom.com/wiki/Skills_(Bannerlord)), [Gamewatcher](https://www.gamewatcher.com/mount-and-blade-2-levelling-guide)
- **KCD2**: 스킬 XP는 해당 행동을 능동적으로 해야 오르고, Main Level은 스탯들의 평균에서 파생, perk는 스킬 레벨로 잠금. [커뮤니티] — [KCD wiki.gg Main Level](https://kingdomcomedeliverance.wiki.gg/wiki/Main_Level)
- **Dwarf Fortress**: 안 쓰면 rusty → very rusty로 감퇴하므로 특화가 유지된다. 요새 모드는 XP를 숨기고 모험 모드는 정확한 XP를 보여준다. [요약, 커뮤니티] — [DF Wiki: Rust](https://dwarffortresswiki.org/index.php/Rust), [DF Wiki: Experience](https://dwarffortresswiki.org/index.php/DF2014:Experience)
- **Project Zomboid**: 스킬 책이 XP 배율을 주는 "학습 자원" 구조, 레벨은 영구적. [커뮤니티] — [pindrop.gg](https://pindrop.gg/project-zomboid/skills)
- **EVE Online**: 활동량과 무관한 실시간 스킬 훈련으로 스킬 파밍 유인을 없앴다. [커뮤니티] — [EVE University Wiki](https://wiki.eveuniversity.org/Skill_training)
- **Koster가 권하는 설계 원칙(원문)**: 스킬은 도전을 이기기 위한 도구여야 하고("A skill is supposed to be a tool you use to defeat a challenge"), 성장이 아니라 게임 자체에 재미의 부담을 둬야 한다("you've placed the burden for fun where it should be: on the game, and not on the advancement"). 사용률을 항상 추적하고, 결과 기반(results-based) 진행은 구체적 성과와 연결하며, Privateer Online 구상에서는 훈련·도전 뒤 NPC 길드에 "dues"를 내야 인증이 유지되게 하려 했다. [열람] — [Koster](https://www.raphkoster.com/?p=592)
- **FFII에서 FFIII로의 회귀**는 시스템이 시장에서 받아들여지지 않은 사례로 위키피디아에 기록돼 있다. [열람] — [Wikipedia, FFII](https://en.wikipedia.org/wiki/Final_Fantasy_II)
- **SaGa**: Battle Rank는 "전투 횟수"에 따라 적이 강해지고 도망도 횟수에 포함된다. 리메이크는 플레이어 강함에 맞춘 스케일링 방향을 논의했다. 성공·실패 평가는 확인하지 못함. [요약] — [RPG Site](https://www.rpgsite.net/interview/16302-romancing-saga-2-revenge-of-the-seven-interview-talking-remaking-a-niche-classic-with-shinichi-tatsuke)

### Inferences
- [추정] 가장 일관된 "작동 요소"는 *성장량을 행동 횟수가 아닌 과제 난이도에 묶는 것*이다(Kenshi, UO GGS의 "at or near" 조건). 이것이 Koster의 "도전이 없는 연습은 지루하다"에 대한 구체적 해법이다.
- [추정] 상한·학습 한계(Bannerlord), 총합 상한(UO 700), 감퇴(DF, UO)는 모두 "모든 것을 다 잘하는 캐릭터"를 막아 정체성을 만드는 장치로 기능한다. 다만 이 목적을 개발자가 명시한 문서는 못 찾았으므로 해석일 뿐이다.
- [추정] 시간 기반(EVE)은 착취를 제거하지만 "내가 한 일이 곧 나"라는 서사를 포기한다. "you become what you do" 목표와는 충돌한다.
- [추정] Skyrim식 통합(스킬 XP → 단일 레벨 → perk)은 읽기 쉽고 클래스 선택이 필요 없지만, 불필요한 스킬을 잘라 내는 대가(스킬 수 감소)를 치렀다.

### Gaps
- "rested bonus", "first-time bonus", "실패에서 배우기" 규칙, "teacher/trainer 요건"을 명시적으로 다룬 개발자 자료는 거의 없었다. 확인된 유사물: UO GGS가 실패 사용을 세지 않음, Tim Cain(2차)이 실패에도 XP를 주자고 제안, Zomboid의 스킬 책. Morrowind/SWG의 트레이너 제도는 접근 가능한 출처에서 확인하지 못했다.
- 위 "성공" 판단은 대부분 커뮤니티·평론 수준이며, 정량적 데이터(유지율, 만족도)는 찾지 못함.

---

## 4. 사용 기반 진행에 관한 학술·GDC 자료

### Takeaway
사용 기반 스킬 시스템과 착취·동기를 직접 다룬 동료 심사 논문은 찾지 못했다. 가장 쓸 만한 1차 자료는 개발자 글(Koster 블로그, Johnson 칼럼)이고, 학술 문헌의 "skill-based progression"은 보통 *플레이어*의 숙련을 뜻해 캐릭터 스킬과 혼동하기 쉽다.

### Cited Findings
- Koster "Use-based systems"는 사용 기반 시스템의 설계 문제를 상세히 다룬 가장 직접적인 개발자 자료다(위 1·2·3절). [열람] — [Koster](https://www.raphkoster.com/?p=592)
- Johnson "Water Finds a Crack"은 Game Developer 2011년 3월호 칼럼으로 착취·최적화 행동을 일반 원리로 정리한다. [열람] — [Designer Notes](https://www.designer-notes.com/game-developer-column-17-water-finds-a-crack/)
- 진행 시스템 분류 연구: 진행을 skill-based, XP-based, item-based, narrative, social, hybrid의 여섯 유형으로 나누는 도서 챕터가 있다. 여기서 skill-based는 "게임 메커닉에 대한 플레이어의 향상"에 묶인 진행으로, 캐릭터 스킬과 다른 개념이다. [요약] — [InTechOpen 챕터](https://www.intechopen.com/online-first/1221745)
- 실무 글: XP는 플레이어 숙련의 추정치일 뿐이며, 도전이 없는 반복을 강요하면 게임 내 진행이 실제 숙련과 분리된다는 주장(비동료 심사). 또 그라인드는 플레이어의 선택지가 한두 개로 줄어들 때 생기며 목표에 이르는 길을 늘리면 줄어든다는 Game Developer 기고. [요약] — [Game Developer: Dissecting Progress](https://gamedeveloper.com/design/dissecting-progress), [Game Developer: When Game Design Becomes a Grind](https://www.gamedeveloper.com/design/when-game-design-becomes-a-grind)
- "Learning by doing"을 직접 다룬 논문은 교육용 게임 연구 Cutting & Iacovides(2022, CHI PLAY)로, 내재적으로 통합된 교육 게임에서 학습이 더 높았다는 결과다. 캐릭터 성장 시스템과는 거리가 있다. [요약] — [White Rose eprints](https://eprints.whiterose.ac.uk/189921/1/LearningByDoingCuttingAndIacovides090822.pdf)
- GDC/관련 강연 단서(내용 미검증, 제목·존재만 확인): Josh Sawyer의 속성 튜닝 강연 "Gods and Dumps Attribute Tuning"(GDC Vault), Obsidian "Five Hard Lessons of RPG Design"(GDC Europe), Damion Schubert의 그라인드 강연(GDC Online 2010). [요약] — [GDC Vault](https://gdcvault.com/play/1023481/Gods-and-Dumps-Attribute-Tuning), [Game Developer: Obsidian's Five Hard Lessons](https://www.gamedeveloper.com/design/gdc-europe-obsidian-s-five-hard-lessons-of-rpg-design)

### Inferences
- [추정] 학술 쪽 빈칸을 메우는 가장 실용적인 방법은 MMO 봇·골드파밍 연구(경제·매크로)와 자기결정이론(유능감·자율성) 문헌을 따로 조사하는 것이다. 이번 조사에서는 다루지 못했다.
- [추정] 개발자 1차 자료가 사실상 "문헌"의 중심이다. Koster 글의 본문은 약 18.7만 자인데 그중 앞 10만 자만 읽었다(댓글 포함 후반부 미열람).

### Gaps
- 사용 기반 스킬 + 착취 행동 + 동기를 연결한 동료 심사 논문은 찾지 못함.
- GDC Vault 강연들(Schubert, Sawyer, Obsidian)의 실제 내용은 열람하지 못해 사용 기반 진행에 대한 주장을 확인하지 못함.
- Koster 글 후반부(offset 100000 이후)와 그의 "Laws of Online World Design" 원문은 미열람.
