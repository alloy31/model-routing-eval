# 사용 기반 성장 (use-based / "learn by doing" progression)

> 조사일 2026-11-15. 출처 표기 규칙: **[열람]** = 해당 페이지를 직접 열어 확인한 내용, **[검색요약]** = 검색 결과 요약·스니펫으로만 확인했고 원문 페이지는 열지 못한 내용(403 등), **[통념]** = 개발자 발언·공식 문서가 아닌 커뮤니티/2차 자료의 주장. 인용문은 원문(영어) 그대로 두었다. 열람 도구가 긴 인용을 잘라서 돌려준 경우가 있어, 따옴표 안 문장은 원문의 일부 구절일 수 있다. 보고서에 직접 인용하기 전에 원문 대조를 권한다.

## 1. 각 게임의 시스템은 구체적으로 어떻게 작동했고, 무엇이 잘못됐나

### Takeaway
거의 모든 사례에서 같은 일이 일어났다. "행동하면 그 능력이 오른다"는 규칙이 "성장을 위해 의미 없는 행동을 반복한다"로 뒤집혔고(UO의 매크로, Morrowind의 벽 달리기, FF2의 아군 때리기, SWG의 홀로그라인딩), 설계자는 상한·확률 보정·보장 획득·가치 기반 XP 같은 패치를 겹겹이 쌓았다. 실패의 직접 원인은 규칙 자체보다 "도전이 없는 행동에도 보상이 나온다"는 점과 "성장 공식이 플레이어에게 해독되어 최단 경로가 드러난다"는 점이었다.

### Cited Findings

#### 기원 (테이블탑, 초기 CRPG)
- RuneQuest(Chaosium, 1978)는 D&D의 레벨 방식과 달리 캐릭터가 능력을 직접 올리며, 향상 판정은 현재 기술 수치보다 높게 굴려야 성공한다. 즉 잘할수록 더 오르기 어렵다. [검색요약] — [Wikipedia: RuneQuest](https://en.wikipedia.com/wiki/RuneQuest), [DM David](https://dmdavid.com/tag/5-role-playing-products-that-shaped-how-i-play-dungeons-dragons-1977-1978/)
- Dungeon Master(1987)는 추상적인 경험치·레벨 대신 기술을 사용해서 직접 올리는 방식을 썼다. [검색요약] "최초의 사용 기반 CRPG"라는 주장은 확인하지 못했다. — [NextQuest](https://nextquest.dev/games/dungeon-master), [Giant Bomb](https://www.giantbomb.com/games/3030-18518/)

#### Ultima Online (1997)
- Raph Koster의 정의: 사용 기반 시스템은 "one where you have a chance of improvement every time you use the skill"이며, 모든 플레이어가 처음부터 모든 기술에 접근할 수 있다. [열람] — [Raph Koster, "Use-based systems" (2006-07-18)](https://www.raphkoster.com/?p=592)
- 초기 설계에서는 남이 기술을 쓰는 것을 지켜보기만 해도 오를 수 있었다: "originally, it had a chance of going up if you observed someone else using it". 난이도 등급이 없어 "내 수준보다 낮은 과제"라는 구분도 없었다. [열람] — [Koster, "Use-based systems"](https://www.raphkoster.com/?p=592)
- 총합 700점 상한과 자동 감소: 쓰지 않는 기술은 떨어지고, 상한에 닿으면 "when you hit that threshold, and gained a point, a point was automatically lost from somewhere else". 상한에서는 기술 하나를 포기하고 다른 기술을 배울 수 있었다. [열람] — [Koster, "Use-based systems"](https://www.raphkoster.com/?p=592)
- 기술마다 사용 빈도가 달랐다(검술은 매우 자주, 죽은 자와 대화하기는 드물게). 해법으로 "The solution to this was to dynamically track the frequency of use of all skills."를 택해 빈도에 맞춰 상승 확률을 조정했지만 유지되지 않았다. 상승률은 계속 느려졌고 플레이어는 드문 성공 굴림을 쫓아 매크로를 돌렸다. Koster의 진단: "The thing players had an infinite amount of was time", "What broke was the feedback mechanism", "With a use-based system, we were rolling dice to see when people were going to advance." [열람] — [Koster, "Use-based systems"](https://www.raphkoster.com/?p=592)
- 8x8 매크로: UO는 자원을 8×8 타일 "chunk" 단위로 저장했다. Koster가 난수 시드를 chunk egg의 id로 주자고 제안했고("we instead should seed it with the id of the chunk egg"), 플레이어는 실패 후 8타일 이동하면 확률이 달라진다는 것을 알아내 "8×8 macroing"을 만들었다. Koster는 여기서 자신의 법칙을 인용한다: "No matter what you do, players will decode every formula, statistic, and algorithm in your world via experimentation." [열람] — [Koster, "Use-based systems"](https://www.raphkoster.com/?p=592)
- 그 밖의 악용: 강한 몬스터를 자기 집 안에 가둬 놓고 기술을 올렸다. 이후 빈도 추적 표는 수작업 표로 교체됐고, Koster는 이를 "a series of increasingly outré systems such as “guaranteed gain” and “power hour”"로 이어진 과정으로 묘사한다. [열람] — [Koster, "Use-based systems"](https://www.raphkoster.com/?p=592)
- Koster는 UO 팀이 초기부터 매크로와 조용한 전쟁을 벌였으며, 그 동기는 골드 파머가 아니라 사용 기반 시스템의 구조 자체였다고 썼다. [검색요약, 문장 원문 미확인] — [Koster, "Use-based systems"](https://www.raphkoster.com/?p=592)
- Publish 4 (2000-03-08) 공식 노트: "The chance to learn a skill will be increased during the first hour of play each day for each character."(= 파워 아워), "The skill usage table will no longer fluctuate based on how often skills are used.", "With skill gain being increased in general, we have made changes to make macroing no longer yield better skill gain results than normal game play.", "Skills will generally require human intervention in order to raise them." [열람] — [UO.com Publish 04](https://uo.com/wiki/ultima-online-wiki/technical/previous-publishes/2000-2/2000-publish-04-8th-march/)
- Publish 5 (2000-04)에서는 Mining 등 일부 기술을 안티 매크로 코드에서 제외하고, 나머지는 여전히 이동해야 오르게 했다. [검색요약] — [UO.com Publish 05](https://uo.com/?p=11148)
- 2001-09-20 개발팀 코멘트는 파워 아워가 일반 플레이로 성장하도록 돕는 장치였지만 하드코어 플레이어가 캐릭터를 훨씬 빨리 완성하게 했고 캐주얼 플레이어에게는 이득이 작았다고 인정하며, 대체재로 Guaranteed Gain System을 제안했다. [검색요약, 원문 403] — [UO Stratics, Team Comment 2001-09-20](https://uo.stratics.com/content/interviews/prophet.shtml)
- Guaranteed Gain System (Publish 16, 2002-07-23): "GGS tracks each successful use of a skill, and whether or not skill points were gained in the wake of that success.", 일정 시간 동안 못 오르면 "GGS will award the character a minimum skill point gain as compensation." 실패한 사용에는 적용되지 않는다. 대상은 "those who play infrequently and those who suffer from consistent bad luck". 타이머는 총 기술 점수가 높을수록 길어진다(예: 기술 80.0–84.9 구간에서 +0.1당 총합 350일 때 3.0시간, 700일 때 15.0시간. 115–120 구간은 총합 700일 때 51.0시간). 스탯은 30분에 1점, 하루 6점까지. [열람] — [UO.com Publish 16](https://uo.com/wiki/ultima-online-wiki/technical/previous-publishes/2002-2/2002-publish-16-part-2-23rd-july/)
- Soren Johnson은 지배 전략의 예로 UO의 "tank-mage" 빌드를 든다(클래스가 없는 시스템에서 모두가 같은 최적 빌드로 수렴한 사례). [열람] — [Soren Johnson, "Water Finds a Crack"](https://www.designer-notes.com/?p=369)

#### The Elder Scrolls: Daggerfall → Morrowind → Oblivion → Skyrim
- Daggerfall: 레벨 = floor((S − S0 + 28) / 15). S는 Primary 기술 3개 + 가장 높은 Major 2개 + 가장 높은 Minor 1개의 합이다. 즉 해당 기술 합계가 15 오를 때마다 1레벨. 레벨업마다 능력치 4~6점. Primary 기술이 100에 닿으면 다른 기술은 95를 넘길 수 없다. [검색요약] — [UESP, Daggerfall:Leveling and Skills](https://en.uesp.net/wiki/Daggerfall:Leveling_and_Skills)
- Morrowind: Major/Minor 기술이 합쳐서 10번 오르면 레벨업 자격이 생긴다. 트레이너에게 돈을 내고 올린 것과 스킬북으로 올린 것도 계산된다. 레벨업 때 능력치 배수는 직전 레벨 이후 그 능력치가 관할하는 기술의 상승 횟수로 정해진다: 0회 = 1점, 1–4회 = 2×, 5–7회 = 3×, 8–9회 = 4×, 10회 이상 = 5×. Miscellaneous 기술은 레벨 진행에는 안 들어가지만 배수에는 들어간다. [검색요약] — [UESP, Morrowind:Level](https://en.uesp.net/wiki/Morrowind:Level)
- Morrowind의 악용에 대한 Soren Johnson의 서술: "A classic example is the skill system from Morrowind, which rewards players for repeating any activity.", "Running into a wall for hours increases the Athletics skill while jumping over and over again increases the Acrobatics skill.", "Many players couldn't stop themselves from spending hours doing mindless activities for these cheap rewards." [열람] — [Soren Johnson, "Water Finds a Crack" (Game Developer 2011-03, 블로그 2011-06-12)](https://www.designer-notes.com/?p=369)
- Oblivion: 능력치 보너스는 관할 기술의 상승 수로 정해지고 10회 이상이면 +5(상한). 보너스는 10번째 Major 기술 상승 시점에 고정되며 다음 레벨로 이월되지 않는다. "Efficient leveling"은 매 레벨 능력치 3개에 대해 각각 10회씩 기술을 올려 +5/+5/+5를 받는 플레이 방식이다. 조언으로 과레벨링을 피하고 능력치당 Major 기술을 하나만 고르라는 내용이 실려 있다. [검색요약, UESP 원문 403] — [UESP, Oblivion:Leveling](https://en.uesp.net/wiki/Oblivion:Leveling), [UESP, Oblivion:Efficient Leveling](https://content1.uesp.net/wiki/Oblivion:Efficient_Leveling)
- Bruce Nesmith(전 Bethesda 디자이너)는 Oblivion의 적 레벨 스케일링에 대해 "I think the world levelling with you was a mistake"라고 말했고, Skyrim에 대해서는 "we came up with a much, much better way to continue to provide the player challenge"라고 했다. [열람] — [VideoGamer, Talal Musa (2025-04-28 갱신)](https://www.videogamer.com/news/elder-scrolls-iv-oblivion-levelling-system-mistake-admits-designer-haunts-remaster)
- Oblivion Remastered(2025)는 레벨링 설계를 바꿨다. 원작은 Major 기술을 올리고 잠을 자야 레벨업했지만, 리마스터는 모든 기술 계열에서 XP를 받고 올릴 능력치를 플레이어가 고른다. Nesmith: "They actually went ahead and changed the game design underneath". [열람] — [VideoGamer](https://www.videogamer.com/news/elder-scrolls-iv-oblivion-levelling-system-mistake-admits-designer-haunts-remaster)
- Skyrim에서 클래스를 없앤 이유(Todd Howard, Game Informer 팟캐스트 2011-02 인용 보도): "What we found in Oblivion – you start the game, you pick your race and you play for a while.", "And sort of our thought process was, what if that guy never asked that?", "You just play, and your skills go up as you play and the higher your skill, the more it affects your leveling." [열람, 2차 보도] — [PSU (2011-02-07)](https://www.psu.com/news/bethesda-explains-elder-scrolls-v-classes-axe/)
- 같은 시기 보도: 이전 작품은 플레이어가 기술과 클래스가 무엇을 하는지 제대로 이해하기 전에 고르게 했다는 것이 Bethesda의 설명이다. [검색요약, 원문 열람 실패(451). 어느 Escapist 기사인지 특정하지 못함] — [The Escapist, "Skyrim Designer Defends Scrapping Class Choice" 스레드](https://forums.escapistmagazine.com/threads/214961)
- Skyrim 패치 1.5: Smithing 상승이 제작 개수가 아니라 제작물의 가치에 따라 정해지게 바뀌었다(철 단검 대량 제작 대응으로 해석됨. Bethesda는 상세를 밝히지 않았다는 보도). 팬 실험에서는 XP가 가치의 제곱근에 대략 비례했다. [검색요약, 수치는 통념] — [CinemaBlend](https://cinemablend.com/games/Skyrim-Patch-1-5-Adds-Kill-Cameras-Fixes-Smithing-40479.html), [팬 실험 블로그](https://gamingqna.blogspot.com/2012/04/how-does-value-affect-gain-of-smithing.html)
- Skyrim 패치 1.9(2013): 100에 도달한 기술을 Legendary로 만들면 15로 초기화되고 퍽 포인트가 환급되어 다시 올릴 수 있다. 사실상 전체 레벨 상한이 사라졌다. [검색요약] — [UESP, Skyrim:Patch](https://content1.uesp.net/wiki/Skyrim:Patch)
- Nesmith는 2023년 MinnMax 대담에서 "하면 는다" 방식이 차기작에서도 "absolutely going to continue"라고 말했다고 보도됐다. [검색요약] — [GamingBolt](https://gamingbolt.com/the-elder-scrolls-6-will-feature-the-same-leveling-system-as-skyrim)
- Nesmith: "I think that through Skyrim, Bethesda has wanted to have the game get out of its own way.", "I was actually one who aggressively pushed for streamlining." (VideoGamer 인터뷰를 인용한 80.lv 기사, 2024-10-21) [열람] — [80.lv](https://80.lv/articles/bethesda-doesn-t-plan-to-bring-back-cut-rpg-stats-in-the-elder-scrolls-6)
- PC Gamer 기사 제목에 실린 발언: "We got rid of attributes in Skyrim and you know who complained? Almost nobody". [제목만 열람, 본문 미확인] — [PC Gamer](https://www.pcgamer.com/games/the-elder-scrolls/bethesda-veteran-says-less-rpg-complexity-in-the-elder-scrolls-series-is-good-actually-we-got-rid-of-attributes-in-skyrim-and-you-know-who-complained-almost-nobody)

#### Final Fantasy II (1988)
- 경험치 레벨 대신 전투 중 행동으로 성장한다. 특정 무기 종류를 자주 쓰면 그 숙련도와 힘·명중이 오르고, 큰 피해를 받으면 최대 HP가, MP를 많이 쓰면 최대 MP가 오른다. [열람] — [Wikipedia: Final Fantasy II](https://en.wikipedia.org/wiki/Final_Fantasy_II) (근거: Final Fantasy Origins 매뉴얼 p.22, GameTrailers 2007)
- 의도하지 않은 사용: 플레이어가 캐릭터끼리 서로 공격하게 하고 주문을 반복 시전해 HP와 능력을 의도보다 훨씬 크게 키웠다. [열람] — [Wikipedia: Final Fantasy II](https://en.wikipedia.org/wiki/Final_Fantasy_II)
- 설계자 Akitoshi Kawazu(2012, Jeremy Parish 인터뷰): "The system is more about nurture than nature now. You don't choose what you are in the beginning." 악용을 예상했느냐는 질문에 "No, I had no idea. [laughs] I had no idea people would use it to essentially grind levels." 아군 공격이 가능했던 이유: "I thought that if characters were put to sleep, well, it makes sense to wake them up faster by hitting them. That's the reason why I put that in." [열람] — [Retronauts (원 게재 1UP 2012-10, 재게재 2017-11-13)](https://retronauts.com/article/670/akitoshi-kawazu-on-the-reasoning-behind-sagas-insanity)
- 평가: G4는 능력치 성장 시스템이 처음엔 참신하게 들리지만 "wound up being a huge mess"라고 했고, GameSpot은 "chaotic", GameSpy는 "quirky and sometimes confusing"이라고 했다. PSP판은 난이도가 낮아져 레벨링 악용의 필요가 줄었다는 평(GameSpy). [열람] — [Wikipedia: Final Fantasy II](https://en.wikipedia.org/wiki/Final_Fantasy_II)
- 결과: "Due to both negative feedback and a lack of understanding within Square's staff" Final Fantasy III는 1편의 전통적인 시스템으로 돌아갔다. [열람] — [Wikipedia: Final Fantasy II](https://en.wikipedia.org/wiki/Final_Fantasy_II) (근거: Retronauts/Parish 2017)

#### SaGa 시리즈
- Kawazu는 FF2의 "nurture" 방식을 SaGa로 가져가면서 문제를 하나 명시했다: "I wanted to incorporate that kind of nurture system, but I needed to differentiate the characters so that they wouldn't all be clones of each other at the end." 시리즈의 공통 주제는 "Allowing the players to play the game the way they would like to play it." [열람] — [Retronauts](https://retronauts.com/article/670/akitoshi-kawazu-on-the-reasoning-behind-sagas-insanity)
- Romancing SaGa 계열은 능력치가 전투 중 행동에 따라 오르고, 기술은 전투에서 여러 번 써서 익힌다. 동시에 적의 강함이 전투 횟수에 연동된다(Battle Rank/Event Rank). Romancing SaGa 2 원작에서는 도망쳐도 전투 횟수로 계산됐다. [검색요약, 2차 자료] — [Automaton](https://automaton-media.com/en/news/romancing-saga-2-revenge-of-the-seven-will-keep-its-powerful-enemies-but-running-away-wont-make-them-progressively-stronger-producer-says/), [SaGa Wiki: Event Rank](https://saga.fandom.com/wiki/Event_Rank), [RPGamer](https://rpgamer.com/?p=123155)

#### Quest 64 (1998)
- 전통적인 레벨업이 없고, FF2처럼 전투 중 수행에 따라 능력치별로 경험이 쌓인다(예: 자주 맞으면 방어가 오른다). 원소 정령을 찾아 원소를 강화한다. GameSpot과 IGN의 결론은 RPG 입문자에게는 무난하지만 숙련자에게는 너무 단순하다는 것이었다. [열람] — [Wikipedia: Quest 64](https://en.wikipedia.org/wiki/Quest_64)

#### Dungeon Siege (2002)
- 근접·원거리·전투 마법·자연 마법 능력이 얼마나 자주 쓰느냐에 따라 발달한다. [검색요약] — [GameSpot review](https://gamespot.com/reviews/dungeon-siege-review/1900-2860893/)
- Chris Taylor는 이를 "skill-based class system"으로 불렀고, 캐릭터의 클래스는 플레이 방식으로 정해진다고 설명했다. 숙련자는 한 영역에 특화하고 초보자는 분산할 것으로 예상했다. [검색요약] — [GameSpot Q&A](https://www.gamespot.com/articles/dungeon-siege-qanda/1100-2625619/), [GameBanshee preview](https://www.gamebanshee.com/news/66371-dungeon-siege-preview-v15-66371.html), [Kikizo](https://games.kikizo.com/features/dungeonsiege2_christaylor_interview.asp)

#### Star Wars Galaxies (2003) — 사용 기반이 아니라 "결과 기반"
- Koster는 SWG를 UO의 사용 기반과 구분해 "결과 기반"으로 설명한다. 모든 주요 활동에 고유한 XP 종류를 두었다: "We set out to define a type of XP for every major activity in the game". 직업은 30개 이상, 각 18개 기술: "In SWG there were over 30 professions, each with 18 skills". [열람] — [Koster, "Designing a Living Society in SWG, part one" (2015-04-21)](https://www.raphkoster.com/?p=25717)
- 가장 좋았다고 평가한 아이디어는 남이 내가 만든 물건을 실제로 사용할 때 제작 XP가 들어오는 것("the notion of crafting XP being granted when someone else actually used something you crafted")이었으나, 데이터베이스 부하 때문에 잘리고 제작 행위 자체에 XP를 주는 방식으로 밀려났다. [열람] — [Koster, "Use-based systems"](https://www.raphkoster.com/?p=592), [Koster, "Designing a Living Society"](https://www.raphkoster.com/?p=25717)
- 출시 3일 전 한 디자이너가 성장 속도를 전부 10배 느리게 만들었다("the designer in charge of advancement rates went through them and made them all ten times slower"). Koster가 되돌렸지만 게임은 여전히 그라인드가 심했다고 썼다. [열람] — [Koster, "Use-based systems"](https://www.raphkoster.com/?p=592)
- 반대되는 Koster의 다른 서술: "people think of SWG as grindy, but it actually had the fastest advancement of any MMO at the time it came out." [열람] — [Koster, "Did Star Wars Galaxies Fail?" (2015-04-27)](https://www.raphkoster.com/?p=25829)
- Jedi 해금과 홀로크론: 원래 설계는 캐릭터마다 무작위로 정해진 행동 목록을 몰래 달성하면 Jedi가 열리는 것이었다("Every player would randomly roll up a different set of actions they needed to undertake.", "The player would not be told that they had checked off an item."). 이후 필요한 직업을 알려 주는 Holocron이 드롭되자 플레이어는 무차별 대입을 했다: "They simply started at A and learned every skill. In order." 결과: "Everyone started playing everything they didn't like.", "But most just macroed their way or grinded their way through it all", "Satisfaction fell off a cliff.", "one month after Holocron drops began, we started losing subs, instead of gaining them." Koster의 결론: "a system that worked better when nobody knew how it worked." [열람] — [Koster, "A Jedi Saga" (Game Developer, 2015-04-17)](https://www.gamedeveloper.com/design/a-jedi-saga)
- AFK 매크로: SOE 커뮤니티 공지는 SWG가 매크로는 결국 피할 수 없다는 전제로 설계됐다고 밝히면서, 긴 매크로는 여전히 쓸 수 있지만 반복(loop)과 자기 호출은 막겠다고 했다. 2004년 포럼에는 버프봇, AFK 서베이, Image Designer 매크로 그라인딩이 문제로 올라와 있다. [검색요약, 날짜 미확인, 아카이브 사본] — [SWGEmu 아카이브](https://www.swgemu.com/archive/scrapbookv51/data/20070127170800), [Allakhazam](https://wow.allakhazam.com/story.html?story=4008)
- NGE(2005): 직업이 34개에서 9개로 줄었다. [검색요약. 검색 도구가 돌려준 URL이 문서 제목과 맞지 않아 원문 대조 필요] — [Wikipedia "Star Wars Galaxies"로 표시된 검색 결과](https://www.wikipedia.org/wiki/Hal_Horn), 배경은 [MassivelyOP, "The Game Archaeologist: Star Wars Galaxies' NGE"](https://massivelyop.com/2015/08/22/the-game-archaeologist-star-wars-galaxies-nge/). Damion Schubert(2015-08-23)는 NGE의 논리를 일부 플레이어가 떠나도 "their defections would be swamped by new people signing up"일 것이라는 기대로 요약하고, 실제로는 기존 커뮤니티가 "went to the press and poisoned the well"했다고 평가한다. [열람] — [Zen of Design](https://www.zenofdesign.com/a-retrospective-on-the-swg-new-game-experience)

#### EVE Online (2003) — 행동과 성장을 분리
- EVE는 연습으로 능력이 오르지 않는다. 훈련할 기술을 고르면 오프라인 중에도 실시간으로 훈련된다. [검색요약] — [Engadget, "EVE Evolved: EVE's skill system demystified" (2008)](https://www.engadget.com/2008-05-05-eve-evolved-skill-system-demystified-part-1.html)
- 스킬 큐 도입(2009) 때 CCP의 우려는 긴 큐가 접속을 줄일 수 있다는 것이었고 24시간 창으로 제한했다. [검색요약] — [Engadget (2009-02-04)](https://www.engadget.com/2009-02-04-long-awaited-skill-queue-coming-to-eve-online.html). 2014년에 24시간 제한을 없앴다. CCP 글은 큐가 없던 시절 플레이어가 알람 시계로 훈련을 계획했다고 회고한다. [검색요약] — [CCP, "Longer Queues Expected"](https://www.eveonline.com/news/view/longer-queues-expected-skill-training-above-and-beyond-24-hours)
- Learning 스킬(훈련 속도를 올리는 스킬) 제거(2010-11-25 공지): CCP Greyscale은 "They're really not much use in the long run"이라고 썼다. 투자한 SP는 환급됐고 모든 캐릭터가 기본 능력치 12점을 받았다. [열람] — [CCP dev blog, "Learning skills are going away"](https://www.eveonline.com/news/view/learning-skills-are-going-away-1)

#### RuneScape (2001)
- 2011년 10월 "Bot Nuking Day"에 하루 동안 약 150만 봇 계정이 제거됐다. Jagex는 매일 10만~20만 개의 봇 계정이 생성된다고 밝혔다. [검색요약] — [RuneScape Wiki](https://runescape.wiki/w/Bot_Nuking_Day), [PC Gamer](https://www.pcgamer.com/runescape-bot-nuking-event-bans-1-5-million-bots-in-one-day/)
- Jagex CEO Mark Gerhard: "I want to know that if I'm putting in 30 minutes this evening, that that 30 minutes is equal to everyone else's 30 minutes." [검색요약] — [Engadget (2011-12-21)](https://www.engadget.com/2011-12-21-free-for-all-jagex-answers-more-questions-about-nuking-bots.html)
- RuneScape 창작자 Andrew Gower는 후속작 Brighter Shores에 대해 "you're never going to completely eliminate bots"라고 말했고, 경제가 봇에 무너지지 않도록 설계했으며 로그아웃 중에도 활동이 이어지게 했다고 설명했다. [검색요약] — [Yahoo Tech](https://tech.yahoo.com/general/articles/runescape-creators-mmo-unorthodox-solution-185258698.html)

#### Kenshi (2018)
- 캐릭터는 특별한 능력 없이 매우 약하게 시작하고, 어떤 일을 많이 할수록 그 일을 잘하게 된다. [검색요약] — [The Register (2019-05-31)](https://www.theregister.co.uk/2019/05/31/kenshi_sandblasted_swordpunk_where_the_dungeon_master_wants_everyone_dead/)
- 일부 기술의 XP 획득률은 상대의 강함에 따라 조정된다("Stronger Opponent Logic"). 강한 상대는 많은 XP를, 약한 상대는 거의 주지 않는다. [검색요약, 위키 원문 열람 실패] — [Kenshi Wiki: Stronger Opponent Logic](https://www.kenshi.wiki/w/Stronger_Opponent_Logic)
- Strength는 타격이 막혀도 오르고, 방어 성공은 타격 XP의 40%를 준다. 무거운 것을 나르는 것으로도 오른다. Toughness는 피해 저항과 기절 기준을 정하며, "죽은 척" 상태에서 일어나게 하면 XP가 한꺼번에 들어온다는 것이 플레이어 가이드의 설명이다. [검색요약, 뒤쪽은 통념] — [Kenshi Wiki: Strength](https://kenshi.wiki/w/Strength), [Kenshi Wiki: Toughness](https://kenshi.fandom.com/wiki/Toughness)
- 개발자 Chris Hunt의 발언(PC Gamer 기사 제목): "Too many games let their players succeed", "that's mind-numbingly boring to me". [제목만 열람] — [PC Gamer](https://www.pcgamer.com/games/survival-crafting/too-many-games-let-their-players-succeed-says-developer-of-notoriously-tough-survival-rpg-kenshi-and-thats-mind-numbingly-boring-to-me)

#### Mount & Blade II: Bannerlord / Kingdom Come: Deliverance
- Bannerlord 공식 개발 블로그: 포커스 포인트를 기술에 투자하면 그 기술의 경험 획득이 빨라지고, 한번 넣은 포인트는 되돌릴 수 없다. 레벨 0에 포커스가 없는 기술은 아무리 연습해도 오르지 않는다. [검색요약, 원문 403] — [TaleWorlds Dev Blog 23/08/18](https://www.taleworlds.com/en/Games/Bannerlord/Blog/74)
- 가이드 기준 수치: 포커스 1점당 학습 속도 1.25배, 학습 한계 +30. 능력치 10 + 포커스 5일 때 소프트 캡 330. 능력치를 올리면 관련 기술이 더 빨리 자란다. [검색요약, 2차 자료] — [Mount & Blade Wiki](https://mountandblade.fandom.com/wiki/Skills_(Bannerlord)), [Windows Central](https://www.windowscentral.com/everything-you-need-know-about-skills-and-leveling-mount-blade-ii-bannerlord)
- KCD: 기술은 사용해야 XP가 쌓이고, 각 퍽에는 기술 레벨 요건이 있다. 플레이어 팁으로 훈련 교관 Bernard와의 대련 반복, 약초 채집으로 Strength를 올리는 퍽 활용이 공유된다. [검색요약, 2차 자료·통념] — [PowerPyx](https://www.powerpyx.com/kingdom-come-deliverance-how-to-level-up-all-stats-skills/), [GameSkinny](https://www.gameskinny.com/n2ee9/kingdom-come-deliverance-herbalism-skill-guide)
- Daniel Vávra는 2014–2015년 인터뷰에서 클래스 제한이 없고("you can be anyone you want") 기술·퍽·스탯 구조를 쓴다고 설명했다. [검색요약] — [GamingBolt](https://gamingbolt.com/kingdom-come-deliverance-interview-making-the-most-complete-rpg-ever)

#### Project Zomboid
- The Indie Stone의 2013년 블로그: 스킬북은 XP 배수를 주며 읽은 만큼 배수가 커지고, 레벨이 오르면 다음 권이 필요하다. 초급 목공 책은 바로 읽을 수 있지만 여러 밤이 걸린다. [검색요약, 원문 403] — [Project Zomboid 공식 블로그 (2013-04)](https://projectzomboid.com/blog/news/2013/04/crawling-flesh-hungry-zombies/)
- 책의 배수는 해당 권이 다루는 2개 레벨 구간(1–2, 3–4 …)에만 적용된다. [검색요약, 통념] — [Steam 가이드](https://steamcommunity.com/sharedfiles/filedetails/comments/2583048409)

#### Dwarf Fortress 모험 모드
- 돌 던지기로 Throwing을 올릴 수 있고, 위키는 토사물·흙·작은 돌을 계속 던지는 반복으로 능력치와 Throwing을 약 10분 만에 Legendary까지 올릴 수 있다고 적는다. [검색요약] — [DF Wiki: Thrower](https://dwarffortresswiki.org/index.php/DF2014:Thrower), [DF Wiki: Adventurer mode FAQ](https://dwarffortresswiki.org/index.php/Adventurer_mode_F.A.Q.)
- 능력치 상승은 모든 기술에서 얻은 총 경험에 기반하고 어떤 능력치가 오를지는 무작위다. 모험 모드 능력치는 시작값의 2배 또는 시작값 + 종족 평균 중 큰 값으로 상한이 걸린다(구버전 v0.31/v0.34 문서 기준). [검색요약] — [DF Wiki: v0.34 Adventurer mode](https://dwarffortresswiki.org/index.php/v0.34:Adventurer_mode)

### Inferences
- 사례들은 세 갈래로 나뉜다. (a) 순수 사용 기반: UO, FF2, Quest 64, Dungeon Siege, Kenshi, DF. (b) 사용 기반 + 메타 레벨: Daggerfall/Morrowind/Oblivion/Skyrim, Bannerlord, KCD. (c) 사용 기반의 대안: SWG(활동별 XP, 결과 기반), EVE(시간 기반). Oblivion의 악명은 사용 기반 자체보다 (b)의 결합부, 즉 기술 상승 → 레벨 → 능력치 배수 → 적 스케일링으로 이어지는 연쇄에서 나왔다. 평소 쓰는 기술을 Major로 두면 레벨이 빨리 오르고 능력치 보너스는 낮아져 세계만 강해진다.
- UO와 SWG Jedi의 공통점은 공식이 해독되는 순간 시스템의 성격이 바뀌었다는 점이다(8x8, 홀로크론). 숨겨진 규칙에 기대는 설계는 커뮤니티가 있는 게임에서는 수명이 짧다.
- FF2는 "세계의 논리로 타당한 행동(잠든 동료를 때려 깨우기)"을 허용한 것이 성장 규칙과 만나 악용 경로가 됐다. 행동의 대상·맥락을 성장 규칙이 구분하지 않으면 생기는 문제다.
- 싱글 플레이 게임(Morrowind, FF2, Kenshi, DF)의 악용은 그 플레이어의 경험만 망치지만, MMO(UO, SWG, RuneScape)에서는 경제·공정성 문제로 번져 운영 비용(안티 매크로, 봇 밴)을 만든다. 인디 싱글 게임이라면 후자의 압력은 약하다.

### Gaps
- UESP의 Oblivion/Skyrim 기계 상세 페이지와 Stratics의 2001년 UO 팀 코멘트는 403으로 직접 열지 못했다. 위 수치는 검색 요약에 의존한다.
- "EVE의 시간 기반 훈련은 사용 기반 그라인드에 대한 반작용으로 설계됐다"는 서술을 뒷받침하는 CCP의 1차 발언은 찾지 못했다. 과제 설명의 이 전제는 미확인이다.
- Dungeon Siege의 사용 기반 시스템에 대한 Chris Taylor의 사후 평가, 그리고 후속작에서 이 시스템이 어떻게 바뀌었는지에 대한 1차 자료를 찾지 못했다.
- Quest 64에서 HP는 피격, MP는 시전, 민첩은 이동으로 오른다는 세부는 확인하지 못했다(Wikipedia는 "맞으면 방어가 오른다"는 예만 든다).
- FF2의 "행동 취소로 숙련도 올리기" 버그와 리메이크별 성장 규칙 변경(능력치 감소 제거 등)은 이번 조사에서 출처를 확보하지 못했다.
- Kenshi 개발자 Chris Hunt가 성장 시스템(맞으면서 강해지는 Toughness 등)의 설계 의도를 직접 설명한 발언은 찾지 못했다. Kenshi 위키 두 페이지는 열람에 실패했다(404/402).
- KCD의 "learning by doing"에 대한 Warhorse의 설계 의도 발언, DF 모험 모드 기술 그라인딩에 대한 Tarn Adams의 발언은 찾지 못했다.
- RuneScape의 스킬 설계 자체에 대한 Andrew Gower의 당시 발언은 찾지 못했다(Brighter Shores 관련 발언만 확인).
- SWG NGE를 SOE가 직접 설명한 1차 자료(예: John Smedley 발언)는 이번에 확보하지 못했다.

## 2. 문서화된 일반적 실패 양상은 무엇이고, 잘 알려진 명제의 원출처는 어디인가

### Takeaway
핵심 명제 세 개의 원출처를 확인했다. Soren Johnson의 "Given the opportunity, players will optimize the fun out of a game."(Game Developer 2011년 3월호 칼럼 "Water Finds a Crack"), Raph Koster의 "players will decode every formula"와 자동화 법칙(The Laws of Online World Design), 그리고 Koster의 사용 기반 진단("There's no challenge in jumping off a hill in Oblivion"). 세 글이 공통으로 가리키는 실패의 뿌리는 도전 없는 반복에 보상이 붙는 구조와, 플레이어가 자기 시간을 과소평가한다는 심리다.

### Cited Findings
- 원문과 귀속: "Given the opportunity, players will optimize the fun out of a game."은 Soren Johnson 본인의 문장이다. 칼럼 첫머리 인용구는 Raph Koster의 *A Theory of Fun*에서 왔지만 이 문장은 그 인용의 일부가 아니다. Game Developer 2011년 3월호에 실렸고 블로그에는 2011-06-12에 게재됐다. 바로 앞 문장은 "What strategy provides the highest chance – or even a guaranteed chance – of success?". [열람] — [Soren Johnson, "Water Finds a Crack"](https://www.designer-notes.com/?p=369)
- 같은 칼럼의 원리: "any hole a player can possibly find in the game's design will be inevitably abused over and over." 플레이어는 시간을 안전과 맞바꾸지만 자기 시간을 과소평가할 위험이 있고, 쉬운 보상은 처음엔 좋지만 게임이 "until the game begins to feel like a grind"가 된다. [열람] — [Johnson](https://www.designer-notes.com/?p=369)
- 지배 전략: "Games lose their dynamic quality once a strategy emerges that dominates under all conditions." 예시로 Civilization의 ICS("Players who pursued this strategy... were always aware that they were breaking the game but often simply couldn't stop themselves.")와 UO의 tank-mage. [열람] — [Johnson](https://www.designer-notes.com/?p=369)
- Koster의 법칙(1): "Macroing, botting, and automation: No matter what you do, someone is going to automate the process of playing your world." 따름정리는 플레이어가 자동화하는 부분을 보면 게임의 어느 부분이 지루한지 알 수 있다는 내용이다("Looking at what parts of your game players tend to automate is a good way to determine which parts" …). [열람, 따름정리 뒷부분은 요약] — [Koster, "The Laws of Online World Design"](https://www.raphkoster.com/games/laws-of-online-world-design/the-laws-of-online-world-design/)
- Koster의 법칙(2): "No matter what you do, players will decode every formula, statistic, and algorithm in your world via experimentation." 같은 문서의 Lambert's Laws: "Players will eventually find the shortest path to the cheese." Hyrup's Loophole Law: "If something can be abused, it will be." [열람] — [Koster, Laws](https://www.raphkoster.com/games/laws-of-online-world-design/the-laws-of-online-world-design/)
- 같은 문서의 Baron's Design Dichotomy 중 누적형 캐릭터 모델: "anyone can reach the pinnacle of achievement by mere persistence." [열람] — [Koster, Laws](https://www.raphkoster.com/games/laws-of-online-world-design/the-laws-of-online-world-design/)
- 사용 기반에 대한 Koster의 핵심 진단: 연습은 도전하고 가르칠 때는 괜찮다(헤드샷, 악곡 연습). 사용 기반 시스템에는 그 도전이 없었다: "There's no challenge in jumping off a hill in Oblivion". 가장 큰 장벽은 기계적이 아니라 심리적이다: "Now, the biggest barrier here isn't mechanical, it's psychological.", "Players are bottomfeeding the system". [열람] — [Koster, "Use-based systems"](https://www.raphkoster.com/?p=592)
- 측정의 문제: 수작업으로 만든 성장률 표는 플레이어가 악용을 찾아낼 때마다 갱신해야 하므로 지속적인 지표 추적이 필요하다. [열람, 요약] — [Koster, "Use-based systems"](https://www.raphkoster.com/?p=592)
- 정체성 상실("모두가 같은 만능 캐릭터"): Kawazu는 FF2식 육성에서 캐릭터가 끝에 가면 서로의 복제품이 되는 문제를 의식해 SaGa에서 캐릭터를 차별화했다고 말했다("so that they wouldn't all be clones of each other at the end"). [열람] — [Retronauts](https://retronauts.com/article/670/akitoshi-kawazu-on-the-reasoning-behind-sagas-insanity)
- 싫어하는 플레이의 강요: SWG 홀로크론 이후 "Everyone started playing everything they didn't like." 보상(Jedi)이 크면 플레이어는 좋아하지 않는 행동도 전부 한다. [열람] — [Koster, "A Jedi Saga"](https://www.gamedeveloper.com/design/a-jedi-saga)
- 읽기 어려운 성장: FF2의 시스템은 "chaotic"(GameSpot), "quirky and sometimes confusing"(GameSpy)으로 평가됐고, Square 내부에서도 이해가 부족했다는 서술이 있다. [열람] — [Wikipedia: Final Fantasy II](https://en.wikipedia.org/wiki/Final_Fantasy_II)
- 이해 전 선택의 문제: Skyrim 이전 작품은 플레이어가 기술과 클래스를 이해하기 전에 고르게 했다. [검색요약, 원문 열람 실패] — [The Escapist 스레드](https://forums.escapistmagazine.com/threads/214961). 같은 취지의 Todd Howard 발언은 [PSU](https://www.psu.com/news/bethesda-explains-elder-scrolls-v-classes-axe/)에서 열람 확인.
- 운영자 관점: 관리자가 효율적 자동 플레이를 반대한 이유는 "the game had been tuned to a given player efficiency rate"이기 때문이다. Koster는 UO 리드 프로그래머 Rick Delashmit조차 "he was running three separate characters at once, where two of them were simply thoroughly scripted bots"였다고 회고한다. [열람] — [Koster, "A brief history of botting" (2008-03-25)](https://www.raphkoster.com/?p=1670)
- 그라인드의 정의에 대한 업계 글: 플레이어의 실력과 지식이 진행에 영향을 주지 못할 때, 그리고 선택지가 한두 개로 줄어들 때 그라인드가 생긴다. [검색요약] — [Game Developer, "When Game Design Becomes a Grind"](https://www.gamedeveloper.com/design/when-game-design-becomes-a-grind)

### Inferences
- 문서화된 실패 양상을 정리하면 여섯 가지다. (1) 도전 없는 행동의 반복(벽 달리기, 점프, 돌 던지기). (2) 자동화 유인(UO 매크로, SWG AFK, RuneScape 봇). (3) 재미의 최적화 제거(efficient leveling, 홀로그라인딩). (4) 정체성 수렴(tank-mage, FF2의 복제 캐릭터). (5) 읽기 어려운 성장(FF2, Oblivion의 능력치 배수). (6) 균형 유지 비용(기술별 사용 빈도 차이, 성장률 표의 지속 보수).
- Koster와 Johnson의 진단을 합치면 사용 기반의 약점은 "행동 횟수"를 세는 데 있다. 횟수는 가장 싼 행동으로 채워진다. 반대로 결과·난이도·맥락을 세면 같은 "하면 는다"가 도전을 요구하게 된다.
- "Players will optimize the fun out"은 플레이어 탓이 아니라 설계자 책임이라는 맥락으로 쓰였다. Johnson의 처방은 악용을 처벌하는 것이 아니라 최적 경로가 지루하지 않게 규칙을 고치는 것이다(Civ 4의 오버플로 이월).

### Gaps
- Josh Sawyer의 "degenerate gameplay" 발언과 Pillars of Eternity의 퀘스트 전용 XP 근거는 1차 출처를 찾지 못했다. 포럼의 2차 해석만 있었다.
- Koster의 "silent war against macroing" 구절은 검색 요약으로만 확인했고 원문 문장을 대조하지 못했다. Koster 글은 본문과 댓글이 매우 길어 열람 도구가 앞 100,000자만 읽었다.
- "everyone becomes a jack-of-all-trades"를 Elder Scrolls에 대해 개발자가 직접 인정한 발언은 찾지 못했다. Skyrim에서 모든 기술을 100으로 올릴 수 있다는 점에 대한 비판은 커뮤니티 통념으로 분류해야 한다.

## 3. 어떤 설계가 성공으로 평가되고, 무엇이 그것을 작동하게 했나

### Takeaway
살아남은 설계는 사용 기반을 버린 것이 아니라 한정했다. 총량 상한(UO 700점), 투자한 곳만 빨리 자라게 하는 학습 속도·한계(Bannerlord), 상대 강함에 비례한 XP(Kenshi), 가치에 비례한 XP(Skyrim 1.5), 준비 행동을 요구하는 배수(Project Zomboid의 책), 보장 획득(UO GGS), 벌칙을 보너스로 바꾼 프레이밍(WoW 휴식 경험치)이 반복해서 등장하는 장치다. Koster의 결론은 한 단계 더 나아가, 기술은 목적이 아니라 수단이어야 한다는 것이다.

### Cited Findings
- 총량 상한과 교환: UO는 총합 700점 상한을 두고 상한에서 한 기술을 포기하고 다른 기술을 배울 수 있게 했다. Koster의 SWG도 플레이어가 선택하도록 유도하는 스킬 상한을 골랐다("we selected a skill cap that encouraged players to do so"). [열람] — [Koster, "Use-based systems"](https://www.raphkoster.com/?p=592), [Koster, "Designing a Living Society"](https://www.raphkoster.com/?p=25717)
- 방향 지정(up 표시): UO Publish 4에서 기술을 "up"으로 표시해야 특정 방식으로 오르게 했다("You will need to mark a skill as “up” in order for it raise in this manner."). [열람] — [UO.com Publish 04](https://uo.com/wiki/ultima-online-wiki/technical/previous-publishes/2000-2/2000-publish-04-8th-march/)
- 사람의 개입 요구: "Skills will generally require human intervention in order to raise them."와 매크로가 일반 플레이보다 유리하지 않게 하는 조정. [열람] — [UO.com Publish 04](https://uo.com/wiki/ultima-online-wiki/technical/previous-publishes/2000-2/2000-publish-04-8th-march/)
- 보장 획득과 불운 완화: UO GGS는 성공한 사용만 세고, 일정 시간 못 오르면 최소 상승을 준다. 총 기술 점수가 높을수록 타이머가 길어지는 체감 구조다. [열람] — [UO.com Publish 16](https://uo.com/wiki/ultima-online-wiki/technical/previous-publishes/2002-2/2002-publish-16-part-2-23rd-july/)
- 첫 시간 보너스의 한계: UO 파워 아워(하루 첫 1시간 상승 확률 증가)는 하드코어 플레이어에게 더 유리했다는 개발팀 자체 평가가 있다. [검색요약] — [UO Stratics Team Comment](https://uo.stratics.com/content/interviews/prophet.shtml)
- 벌칙을 보너스로: WoW의 휴식 시스템은 처음에 몇 시간 플레이 후 경험치가 100%에서 50%로 떨어지는 벌칙이었다. Rob Pardo: "Beta players universally hated this idea and were screaming bloody murder." 같은 수학을 200%에서 시작해 100%로 내려가는 보너스로 바꿨다(기사 소제목 "Make It A Bonus"). [열람] — [Game Developer, "GDC: Blizzard's Core Game Design Concepts" (2010-03-11)](https://www.gamedeveloper.com/game-platforms/gdc-blizzard-s-core-game-design-concepts)
- 결과 기반 XP: SWG의 "남이 내 제작물을 실제로 썼을 때 XP" 아이디어는 그 일이 의미 있었음을 검증해 준다는 이유로 Koster가 가장 좋게 평가했지만 구현 부담으로 잘렸다. [열람] — [Koster, "Use-based systems"](https://www.raphkoster.com/?p=592)
- 가치 기반 XP: Skyrim 1.5는 Smithing 상승을 제작 개수에서 제작물 가치 기준으로 바꿨다. [검색요약] — [CinemaBlend](https://cinemablend.com/games/Skyrim-Patch-1-5-Adds-Kill-Cameras-Fixes-Smithing-40479.html)
- 사전 선택 제거: Skyrim은 클래스와 Major/Minor 구분을 없애고 "the higher your skill, the more it affects your leveling"으로 바꿨다. 사용한 기술이 곧 정체성이 되게 하고 efficient leveling의 유인을 없앴다. [열람, 2차 보도] — [PSU](https://www.psu.com/news/bethesda-explains-elder-scrolls-v-classes-axe/)
- 스케일링 수정: Nesmith는 Oblivion의 세계 전체 스케일링을 실수로 보고 Skyrim의 방식이 훨씬 낫다고 평가했다. [열람] — [VideoGamer](https://www.videogamer.com/news/elder-scrolls-iv-oblivion-levelling-system-mistake-admits-designer-haunts-remaster)
- 재투자 경로: Skyrim 1.9의 Legendary 기술은 100이 된 기술을 15로 되돌려 다시 키우게 해 상한 도달 후에도 성장을 이어 가게 했다. [검색요약] — [UESP, Skyrim:Patch](https://content1.uesp.net/wiki/Skyrim:Patch)
- 투자한 곳만 자란다: Bannerlord는 포커스와 능력치가 학습 속도와 학습 한계를 정하고, 포커스는 되돌릴 수 없다. 사용 기반이면서도 캐릭터가 모든 것에 능해지지 않는다. [검색요약] — [TaleWorlds Dev Blog](https://www.taleworlds.com/en/Games/Bannerlord/Blog/74), [M&B Wiki](https://mountandblade.fandom.com/wiki/Skills_(Bannerlord))
- 상대 난이도 비례: Kenshi의 Stronger Opponent Logic은 약한 상대에게서 거의 XP를 주지 않는다. [검색요약] — [Kenshi Wiki](https://www.kenshi.wiki/w/Stronger_Opponent_Logic)
- 잘할수록 오르기 어렵게: RuneQuest는 향상 판정이 현재 기술 수치를 넘어야 해 자연스러운 체감이 생긴다. [검색요약] — [Wikipedia: RuneQuest](https://en.wikipedia.com/wiki/RuneQuest)
- 준비 행동 요구: Project Zomboid는 책을 읽어야 XP 배수가 붙고, 레벨 구간마다 다음 권이 필요하다. [검색요약] — [Project Zomboid 블로그](https://projectzomboid.com/blog/news/2013/04/crawling-flesh-hungry-zombies/)
- 그라인드에 대한 세계의 반응: SaGa는 전투 횟수에 따라 적이 강해져 무의미한 전투 반복의 이득을 줄인다. Romancing SaGa 2 리메이크는 도망이 적 강화로 이어지지 않게 완화했다. [검색요약] — [Automaton](https://automaton-media.com/en/news/romancing-saga-2-revenge-of-the-seven-will-keep-its-powerful-enemies-but-running-away-wont-make-them-progressively-stronger-producer-says/)
- 능력치 상한: DF 모험 모드는 능력치를 시작값의 2배(또는 시작값 + 종족 평균)로 제한한다. [검색요약, 구버전 문서] — [DF Wiki](https://dwarffortresswiki.org/index.php/v0.34:Adventurer_mode)
- 행동과 성장의 완전 분리: EVE는 플레이 시간과 무관하게 실시간으로 훈련된다. 이후 CCP는 훈련 속도를 올리는 Learning 스킬을 "not much use in the long run"이라며 없애고 전원에게 능력치를 지급했다. [열람] — [CCP dev blog](https://www.eveonline.com/news/view/learning-skills-are-going-away-1)
- 혼합형: Oblivion Remastered는 모든 기술에서 XP를 받고 능력치는 플레이어가 고르는, 원작과 Skyrim의 중간 방식을 택했다. [열람] — [VideoGamer](https://www.videogamer.com/news/elder-scrolls-iv-oblivion-levelling-system-mistake-admits-designer-haunts-remaster)
- Koster의 처방: 재미의 체크리스트 항목(첫 항목 "Do you have to prepare for the challenge?", 그 밖에 지형·핵심 동사·실력·여러 성공 상태·실패 비용)을 하나씩 충족시키면 결과물은 사용 기반처럼 보이지 않을 수 있다. Privateer Online에서 계획한 대안은 훈련 → 도전 통과 → NPC 길드에 회비를 내고 자격을 유지하는 인증 모델이었다. 결론: "skills, levels, abilities — these are properly regarded as enablers, and not as the point". [열람, 체크리스트는 요약] — [Koster, "Use-based systems"](https://www.raphkoster.com/?p=592)
- Johnson의 처방: 가능하면 악용 여부를 플레이어가 켜고 끌 수 있게 하라. "Ultimately, the designer can't go wrong putting the player in control of his or her own experience." 모든 악용을 없애는 것은 과할 수 있다(Super Mario Bros.의 무한 1-UP은 발견의 재미). [열람] — [Johnson](https://www.designer-notes.com/?p=369)
- Koster의 SWG 자평: "it was the least grindy per session, and the most sticky on a week or month basis." [열람] — [Koster, "Did Star Wars Galaxies Fail?"](https://www.raphkoster.com/?p=25829)

### Inferences
- 성공 장치를 기능별로 묶으면 다섯 가지다. (1) 무엇을 세는가를 바꾼다: 횟수 대신 결과·가치·상대 난이도(Skyrim 1.5, Kenshi, SWG의 잘린 아이디어). (2) 총량을 묶어 선택을 강제한다: 총합 상한, 비가역 포커스, 능력치 상한(UO, Bannerlord, DF). (3) 운과 시간의 편차를 줄인다: 보장 획득, 보너스 프레이밍(UO GGS, WoW). (4) 성장 앞에 준비·맥락을 둔다: 책, 교관, 인증(Zomboid, KCD, Privateer Online 안). (5) 세계가 반응한다: 전투 횟수 연동 적 강화(SaGa), 단 Oblivion식 전면 스케일링은 실패 사례.
- "you become what you do"를 목표로 하는 게임에는 (2)가 특히 중요하다. 상한이 없으면 시간이 지날수록 모든 캐릭터가 같은 만능형으로 수렴해 "무엇을 했는가"가 정체성을 만들지 못한다. UO의 "한 점 오르면 다른 곳에서 한 점 빠진다"는 규칙은 현재의 행동이 과거의 정체성을 대체하게 하는 가장 직접적인 구현이다.
- Kenshi와 Skyrim이 호평받는 이유를 개발자 발언으로 직접 확인하지는 못했다. 다만 두 게임 모두 성장의 원천을 "위험이 있는 실제 플레이"에 묶었다는 점에서 Koster의 진단(도전 없는 연습이 문제)과 일치한다.
- "실패에서 배운다" 규칙은 UO GGS에서는 반대로 구현됐다(실패한 사용은 보장 획득에서 제외). 실패에 보상을 주면 일부러 실패하는 그라인드가 생길 수 있어, 실패 보상은 위험 비용(Kenshi의 부상·기절)이 동반될 때만 안전하다.

### Gaps
- "실패에서 배운다"(예: 실패 시에만 XP) 규칙을 쓴 디지털 게임의 개발자 설명은 찾지 못했다. 테이블탑(Burning Wheel, Dungeon World 등)의 사례는 이번 조사 범위에서 확인하지 않았다.
- 교관·훈련 요건(Morrowind 트레이너, KCD 교관)이 그라인드를 줄였는지 늘렸는지에 대한 개발자 평가는 찾지 못했다. Morrowind에서는 트레이너 구매가 레벨 진행에 계산된다는 사실만 확인했다.
- 각 장치의 효과를 수치로 비교한 자료(예: 패치 전후 매크로 비율, 이탈률)는 SWG 홀로크론 이후 가입자 감소 서술 외에는 없었다.
- Kenshi, Bannerlord, Project Zomboid의 설계 근거는 공식 블로그·위키의 검색 요약에 의존한다. 원문 열람이 필요하다.

## 4. 사용 기반 성장, 플레이어 동기, 악용 행동에 관한 학술·GDC 자료가 있는가

### Takeaway
사용 기반 성장만 다룬 학술 논문은 찾지 못했다. 가장 가까운 것은 Zagal & Altizer의 캐릭터 성장 시스템 분류(FDG 2014)와 그라인드 경험을 자기결정이론으로 나눈 한국 논문이며, 실무 쪽 근거는 대부분 개발자 글(Koster, Johnson)과 GDC 강연 보도(Pardo 2010, Koster의 SWG 회고, UO 포스트모템 2018)다.

### Cited Findings
- José P. Zagal & Roger Altizer, "Examining 'RPG elements': Systems of character progression", FDG 2014. 초록: "In this article we unpack the term 'RPG elements' by examining a single element: mechanisms and systems for character progression in paper and pencil RPGs." 발표 슬라이드 목차에는 성장 시스템의 매력, 부정적 성장(불가피한 것, 선택에 의한 것, 우연에 의한 것), 경계적 성장(선불형, 불안정형), 디지털 RPG의 성장이 들어 있다. [검색요약, 본문 미열람] — [DBLP](https://dblp1.uni-trier.de/rec/conf/fdg/ZagalA14.html), [SlideShare](https://de.slideshare.net/josezagal1/rpg-systemsof-regressiontalk03slideshare)
- MMORPG 그라인드 경험을 자율성·유능감·관계성·긍정 정서 네 차원으로 나눈 한국 논문이 있다("Grinding in-Autonomy, Grinding in-Competence, Grinding in-Relatedness and Grinding in-Positive affect"). [검색요약, 본문 미열람] — [KoreaScience](https://koreascience.kr/article/JAKO202219441666855.do)
- John Hopson, "Behavioral Game Design" (Gamasutra, 2001-04-27): 강화 계획(변동 비율 등)을 게임 설계에 적용한 글. 10년 뒤 회고에서 Hopson은 "People had been making games with random loot drops for years before anyone pointed out that they were creating variable ratio schedules."라고 썼고, 게임을 스키너 상자로 부르는 비판에 대해 스키너 상자는 조건화를 연구하는 실험 도구일 뿐이라고 답했다. [검색요약] — [Game Developer, "10 Years of Behavioral Game Design with Bungie's Research Boss"](https://gamedeveloper.com/design/10-years-of-behavioral-game-design-with-bungie-s-research-boss)
- 변동 비율 계획은 고정 비율보다 높은 반응률을 내지만 게임에서 선호되지는 않을 수 있다는 프린스턴 기술 보고서가 있다. [검색요약] — [Princeton CS TR-931](https://www.cs.princeton.edu/techreports/2012/931.pdf)
- 프레이밍 효과 사례 분석: WoW 휴식 시스템을 벌칙이 보상으로 재구성된 사례로 다룬 글. [검색요약] — [Psychology of Games (2010)](https://www.psychologyofgames.com/2010/03/framing-and-world-of-warcrafts-rest-system/)
- GDC 2010, Rob Pardo(Blizzard) 강연 보도: 휴식 시스템의 기원과 "Easy to learn and almost impossible to master." [열람] — [Game Developer](https://www.gamedeveloper.com/game-platforms/gdc-blizzard-s-core-game-design-concepts)
- GDC 2021 SWG 포스트모템(Koster, Vogel)과 GDC 2018 UO 포스트모템(Garriott, Long, Koster, Vogel)이 존재한다. [검색요약, 보도 페이지 403] — [MassivelyOP, GDC 2021](https://massivelyop.com/2021/07/23/gdc-2021-star-wars-galaxies-was-a-complex-game-of-corporate-greed-and-fan-love/), [MassivelyOP, GDC 2018](https://massivelyop.com/2018/03/28/gd-2018-ultima-online-post-mortem-with-richard-garriott-starr-long-raph-koster-and-rich-vogel/)
- EVE Online의 "예외성"이 CCP의 의식적 설계 결정의 결과라고 보는 DiGRA 논문이 있다. [검색요약, 본문 미열람] — [DiGRA Digital Library](https://dl.digra.org/index.php/dl/article/download/672/672)
- Koster의 선집 *Postmortems: Selected Essays Volume One*이 UO를 상세히 다룬다. [검색요약] — [Everand](https://www.everand.com/book/538467094/Postmortems-Selected-Essays-Volume-One)

### Inferences
- UO의 초기 기술 상승("쓸 때마다 확률로 오른다")은 Hopson이 설명한 변동 비율 강화와 구조가 같다. Koster의 "rolling dice" 표현과 맞물려, 사용 기반 + 확률 상승은 매크로를 가장 강하게 유인하는 조합으로 볼 수 있다. 이 연결은 조사자의 추론이며 두 저자가 직접 연결한 것은 아니다.
- 이 주제의 지식은 학술 문헌보다 개발자 회고에 훨씬 많이 쌓여 있다. 보고서의 근거는 Koster(2006, 2015), Johnson(2011), Kawazu(2012), Howard(2011), Nesmith(2023–2025)의 1차 발언을 축으로 삼는 것이 안전하다.

### Gaps
- Zagal & Altizer 논문 본문에서 사용 기반 성장을 별도 범주로 다루는지 확인하지 못했다(본문은 [Academia.edu](https://www.academia.edu/6789775/Examining_RPG_Elements_Systems_of_Character_Progression)에 있다고 한다).
- 사용 기반 성장 시스템에서의 플레이어 행동을 실증한 HCI/게임학 논문(예: 로그 분석, 실험)은 찾지 못했다. Google Scholar, ACM DL, DiGRA를 직접 검색하지는 못했다.
- 자기결정이론(Ryan, Rigby, Przybylski)이나 과잉정당화 효과를 사용 기반 성장에 직접 적용한 문헌은 확인하지 못했다.
- GDC Vault에서 사용 기반 성장을 주제로 한 강연은 찾지 못했다. Bethesda의 Skyrim 레벨링 설계를 다룬 GDC 강연이 있는지도 확인하지 못했다.
- Hopson의 2001년 원문은 직접 열지 못했다.
