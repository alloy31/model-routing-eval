# 사용 기반(use-based) 캐릭터 성장: 설계, 실패 모드, 대응, 학술·GDC 자료

> **읽는 법**
> - 모든 사실 뒤에 출처 링크를 붙였다. 따옴표 안의 문장은 출처에서 확인된 문장이다(원문 또는 요약 도구가 추출한 문장; 등급 표기 참고). 독일어 인용은 원문을 먼저 쓰고 번역을 덧붙였다. 따옴표가 없는 문장은 출처의 paraphrase다.
> - 출처 등급: **[1차]** 개발자 본인의 말 또는 공식 문서를 원문으로 확인함. **[1차·추출]** 개발자 발언이지만 WebFetch 요약 도구가 뽑은 문장이라 출판 전 원문 대조가 필요함. **[2차]** 기자, 블로그, 재인용. **[팬위키]** 커뮤니티 위키. **[검색요약]** 검색 결과 발췌만 확인했고 원문은 열지 못함(403·402·429 응답). **[통념]** 커뮤니티 믿음이며 문서로 확인되지 않음.
> - **사용하지 말 것:** RPG Codex의 "Codex Exclusive - Elder Scrolls: Skyrim Interview with Bethesda"(2011-09-11, https://rpgcodex.net/article.php?id=218)는 풍자 글이다. "Lots of skills is complex…", "We know gamers like 50…" 같은 문장이 검색에서 Todd Howard 발언처럼 보이지만 Bethesda 발언이 아니다.
> - WebFetch 요약에서 얻은 인용은 [1차·추출]로 표시했다. 최종 보고서에 쓰기 전에 원문을 대조해야 한다.

---

## 핵심 질문 1: 시스템은 구체적으로 어떻게 작동했고, 무엇이 잘못되었나

### Takeaway
사용 기반 성장은 "행동 한 번마다 확률적으로 오른다"는 규칙을 공유한다. 실패의 공통 원인은 행동 비용이 낮고 보상률이 계산 가능할 때, 플레이어가 설계자보다 빨리 최적 루프를 찾아낸다는 점이다. UO는 확률을 보정할수록 매크로 경쟁이 심해졌고, Elder Scrolls 계열은 "레벨에 기여하는 스킬 소수" 규칙이 효율 공략(efficient leveling)을 낳았다. SWG는 힌트 장치 하나가 "모든 스킬을 전부 배우기"로 무너졌다.

### Cited Findings

#### Ultima Online (1997~)
- **기본 규칙:** 스킬 사용마다 "a chance of improvement every time you use the skill"이 있었다. 초기에는 다른 플레이어가 스킬을 쓰는 것을 지켜보는 것만으로도 올랐고, 난이도 등급이 없어 사소한 행동도 학습 대상이었다 — [Koster, "Use-based systems" (2006-07-18)](https://raphkoster.com/?p=592) [1차·추출]
- **상한과 감쇠:** 미사용 스킬은 감쇠했고, 총 스킬 포인트는 700으로 상한이 있었다. 한 스킬이 오르면 다른 스킬 하나가 내려갔다 — 같은 출처 [1차·추출]
- **문제 1, 빈도 보정의 역효과:** 검술처럼 자주 쓰는 스킬이 너무 빨리 오르자 빈도 기반으로 확률을 조정했다. Koster는 기준선(baseline)이 사실상 사라져 전체 성장이 늦어졌다고 본다(요약 기반 paraphrase). 플레이어는 "chasing after the one time in a thousand that they would go up"을 하며 실효 확률이 "one in ten thousand"까지 떨어졌다고 보고되었다 — 같은 출처 [1차·추출]
- **문제 2, 8×8 매크로:** 맵을 64타일 청크로 나누고, 청크 ID로 RNG 시드를 정했다. 그래서 8타일 이동이 확률을 바꾼다는 사실을 플레이어가 실험으로 찾아냈다. Koster는 "플레이어는 실험을 통해 모든 공식과 알고리즘을 해독한다"는 자신의 법칙을 인용한다(paraphrase) — 같은 출처 [1차·추출]
- **문제 3, 가두기 매크로:** 실제 도전에만 보상을 주는 방식도 실패했다(paraphrase). 플레이어는 강한 몬스터를 집 안에 가두고 매크로로 사냥했다 — 같은 출처 [1차·추출]
- **대응 A, Power hour:** Koster는 "guaranteed gain"과 "power hour" 같은 메커니즘이 rate를 재조정하려고 추가되었다고 쓴다 — 같은 출처 [1차·추출]. 2001년 개발자 코멘트에 따르면 power hour는 가벼운 플레이어에게 도움이 되지만 하드코어 플레이어가 빠르게 맥스를 찍기 쉽게 만들었다. 또 플레이어가 한 시간에 몰아서 스킬을 올리는 경향이 있었다 — [UO Team Comment, 2001-09-20](https://uo.stratics.com/content/interviews/evocare.shtml) [검색요약, 원문 403]
- **대응 B, Guaranteed Gain System(GGS):** 2002-07-23 Publish 16 Part 2에서 발표되었다 — [uo.com Publish 16 Part 2](https://uo.com/?p=11189) [검색요약]. 규칙은 다음과 같다. 성공한 사용만 추적한다. 일정 시간 동안 획득이 없으면 최소 0.1을 지급한다. 타이머는 서버 시계 기준이라 로그오프 상태에서도 진행한다. 난이도 기반 스킬은 현재 스킬 근처의 과제만 인정한다. 또 실패한 시도는 타이머에 포함되지 않는다 — [uo.com, GGS/RoT/기타 가속 장치 (공식 문서 재수록)](https://uo.com/?p=6342) [1차 공식 문서 재수록]
- **GGS 타이머 예(총 스킬 700 기준):** 0.0–4.9 구간 5분, 50.0–54.9 구간 2.3시간, 100.0–104.9 구간 32.0시간. 같은 페이지의 표는 총 350/500/700 세 가지 조건으로 나뉜다 — 같은 출처 [1차 공식 문서 재수록]
- **RoT(Rate Over Time):** 70.0 이상 구간에서 일정 간격으로만 올랐다. 이 규칙은 Siege Perilous와 Mugen 서버에만 적용되었다. 일일 리셋은 오후 8시(EST)였다 — 같은 출처 [1차 공식 문서 재수록]. 검색 요약에서 이것을 UO 전체 규칙으로 혼동한 기록이 있으니 주의할 것.
- **가속 장치:** Accelerated Gains Quests(신규 캐릭터·신규 스킬, 최대 50% 가속), Scroll of Alacrity(15분간 스킬 체크당 0.2–0.5), Scrolls of Transcendence(즉시 포인트 추가) — 같은 출처 [1차 공식 문서 재수록]
- **Koster의 설계 비평:** 반복 자체가 핵심 문제가 아니며, 연습은 도전적이고 배우게 해줄 때 의미가 있다는 취지다(paraphrase). 그는 "There's no challenge in jumping off a hill in Oblivion."이라고 쓴다. 플레이어가 advantage를 찾고 bottomfeed하는 심리를 가장 큰 장벽으로 꼽으며, 실패 비용 부재, 무관한 지형, 능력 차이 부재, 필요 기술 부재가 이를 키운다고 봤다 — [Koster, "Use-based systems"](https://raphkoster.com/?p=592) [1차·추출]
- **XP 대비 비판:** Koster는 XP가 "arbitrary"하며 "leading to oddities like getting better at crafting because you have slain a lot of orcs"라는 결과를 낳는다고 본다. 결과 기반 시스템은 다시 XP로 되돌아가기 쉽다고 지적한다 — 같은 출처 [1차·추출]

#### The Elder Scrolls: Daggerfall → Morrowind → Oblivion
- **Daggerfall(레벨 공식):** 레벨은 스킬 시스템에서 계산된다. 공식은 L = floor((S − S0 + 28)/15)다. 주요 Major 스킬 두 개와 가장 높은 Minor 스킬 하나만 레벨에 반영된다. 스킬마다 6 게임 내 시간의 쿨다운이 있고, 휴식·배회·고속이동 시 상승이 판정된다 — [UESP, Daggerfall:Leveling and Skills](https://en.uesp.net/wiki/Daggerfall:Leveling_and_Skills) [팬위키·검색요약, 원문 403]
- **Morrowind/Oblivion(클래스 구조):** 클래스마다 Major 5, Minor 5, Misc 17 스킬이 있었다. Major 또는 Minor 스킬이 10회 오르면 레벨이 올랐고, Misc는 레벨에 들어가지 않았다 — [2차 블로그가 UESP를 인용, 검색요약](https://ranneko.blogspot.com/2012/08/streamlining-skyrim.html) [2차]
- **Efficient leveling(플레이어 공략):** UESP 공략 페이지는 레벨당 스킬 상승 10회를 세 개의 관련 속성에 나누어 각 속성 +5를 목표로 한다고 설명한다. Minor 스킬이 하나 이상 있어야 일정한 +5가 보장되고, Minor 스킬은 경험치가 더 많이 필요하므로, 캐릭터 시간의 절반보다 훨씬 많은 시간을 Minor 스킬 훈련에 써야 한다고 페이지는 설명한다. 또 게임을 하지 않고 스킬 연습만 하게 될 수 있다고 경고한다(paraphrase) — [UESP, Oblivion:Efficient Leveling](https://en.uesp.net/wiki/Oblivion:Efficient_Leveling) [팬위키·검색요약, 원문 403]
- **설계자 의도(Rolston, 2006):** "...I think leveling was, at first, perceived as a cure for the obvious balance flaws of Morrowind. But as we refined leveling gameplay during development, we appreciated how it made the game more fun in every way." 그리고 "It does feel a little artificial, and, to some extent, it robs the player of the joy of getting the crap kicked out him." — 인터뷰는 2006-05-23에 RPG Codex에 게재되었으며 원래 [H]Consumers 인터뷰다 — [RPG Codex, Ken Rolston 인터뷰](https://rpgcodex.net/article.php?id=4408) [1차·추출]
- **Oblivion의 스케일링에 대한 설계자의 자기 비판(Nesmith, 2025 보도):** "I think the world levelling with you was a mistake." 그는 Skyrim의 방식이 "a much, much better way to continue to provide the player challenge"라고 말했다. 이 발언은 2025년 VideoGamer 인터뷰에서 나왔다 — [VideoGamer](https://www.videogamer.com/news/elder-scrolls-iv-oblivion-levelling-system-mistake-admits-designer-haunts-remaster) [2차 재인용, 원 인터뷰 미확인]
- **Oblivion Remastered(2025):** 여러 보도에 따르면 월드 스케일링은 유지되었다. 한 미러 기사만 스케일링이 제거되었다고 했으나, 다수 보도와 어긋나므로 신뢰하지 않는다 — [VideoGamer](https://www.videogamer.com/news/elder-scrolls-iv-oblivion-levelling-system-mistake-admits-designer-haunts-remaster) [2차]

#### Skyrim (2011): 재설계
- **속성과 스킬 축소:** "In Oblivion you have your eight attributes and 21 skills." "Now you have 18 skills and three attributes." "What we found is that all those attributes actually did something else." "They're all a trickle down to something else." — 토드 하워드(Todd Howard). 원문은 IGN 인터뷰에서 나왔고 RPG Codex가 재인용했다. 재인용 기사는 2011-04-26 게시됨 — [RPG Codex, "Five Changes from Oblivion to Skyrim"](https://rpgcodex.net/article.php?id=7599) [2차 재인용(IGN)]
- **레벨 구조:** 모든 스킬 상승이 전체 레벨 게이지에 기여한다. 높은 레벨 스킬을 올리면 게이지가 더 크게 오른다. 자주 쓰는 스킬을 올리는 것이 가장 효율적인 성장 경로이며(paraphrase), 레벨업마다 perk를 고른다 — 같은 출처 [2차]
- **Major/Minor 구분 제거:** Pete Hines가 GameSpot 인터뷰에서 말한 것으로 보도되었다. 기사 요약에 따르면 Major/Minor 구분이 사라져 어떤 스킬을 쓰든 레벨업에 도움이 된다(paraphrase) — [Gameranx, 2011-10-19 보도](https://gameranx.com/?p=3377) [2차, GameSpot 원문 미확인]
- **Skyrim 적 스케일링:** 하워드가 출시 전에 적이 "a lot more like Fallout 3"가 될 것이라고 말했다는 2차 재인용이 있다 — [Capsule Computers 재인용](https://www.capsulecomputers.com.au/?p=103572) [검색요약]. Skyrim 스케일링 방식에 대한 하워드 본인의 상세 설명은 찾지 못했다.

#### Final Fantasy II (Square; 일본판/패미컴 계열)
- **경험치 없는 행동 성장:** 경험치 대신 특정 행동이 스탯을 키운다. 힘(attribute)은 "the strength of a specific attribute would be governed by the successful execution of a related action", 즉 관련 행동이 성공적으로 실행되어야 오른다. 마법력은 "a party member's magic power would only increase after they'd cast a sufficient number of spells"로 설명된다 — [Goombastomp, 2018-02-01](https://goombastomp.com/not-final-fantasy-ffiis-intriguing-flawed-progression-system/) [2차 분석]
- **착취:** 확인과 취소 버튼 토글로 물리 공격 30회에 해당하는 경험을 얻을 수 있다고 저자가 주장한다. 아군을 공격해 HP를 소진시킬 수 있으며, Osmose 주문으로 MP를 올릴 수 있다. 아군 대상 공격 옵션은 원래 수면·혼란 해제용이었다 — 같은 출처 [2차 분석]
- **커뮤니티 통념:** 자기 파티를 때려 레벨업하는 파밍. TV Tropes는 이를 "stat farming"으로 기록한다 — [TV Tropes](https://www.tvtropes.org/pmwiki/pmwiki.php/GameBreaker/FinalFantasy) [통념, 검색요약]. StrategyWiki는 이 착취 항목이 Famicom과 PlayStation 판에만 적용된다고 표기한다 — [StrategyWiki, Final Fantasy II/Gameplay](https://strategywiki.org/wiki/Final_Fantasy_II/Gameplay) [팬위키·검색요약]
- **설계자:** Sakaguchi는 첫 작품 후 지쳐서 디자인 권한을 Kawazu에게 넘겼다고 회고했다. Kawazu가 전투 시스템과 성장 메커니즘을 설계했다. 이 내용은 기자 서술이며 Kawazu 본인의 직접 인용은 없다 — [Den of Geek, 2023-08-15](https://www.denofgeek.com/games/final-fantasy-creators-explain-final-fantasy-2s-controversial-changes) [2차]
- **계보:** 같은 "사용해서 올리는" 방식이 SaGa 시리즈로 이어졌다 — 같은 출처 [2차]

#### SaGa 시리즈 (Square; Akitoshi Kawazu)
- **설계 의도(1UP 2012-10 인터뷰, Retronauts 2017-11-13 재게재):** "for _SaGa_, I wanted to incorporate that kind of nurture system" "You make them grow in a certain way and then they'll eventually go in a direction to become whatever you set them up to be." "If one character uses a lot of magic, then they'll naturally become a mage." "It's not something you decide at the beginning." — [Retronauts](https://retronauts.com/article/670/akitoshi-kawazu-on-the-reasoning-behind-sagas-insanity) [1차·추출, 재게재]
- **영감:** "When I design games, I analyze elements of board games and how they work." — 같은 출처 [1차·추출]
- **예상 밖 결과:** "I had no idea people would use it to essentially grind levels." "I never realized it would become a way to increase your hit points or whatever." — 같은 출처 [1차·추출]. 이 두 문장은 사용 기반 시스템이 그라인드를 낳는다는 가장 직접적인 설계자 자백으로 쓸 수 있다.

#### Dungeon Siege (Gas Powered Games, 2002)
- **규칙:** 스킬은 사용으로 오르고 스킬 포인트를 쓰지 않는다. 한 프리뷰는 "One of the things I was immediately in love with about Dungeon Siege is something that I have always felt made the most sense when building skills."라고 평했다 — [GameBanshee, Dungeon Siege 프리뷰](https://www.gamebanshee.com/kpaqc) [2차, 검색요약]
- **스킬 범주:** melee, ranged, nature magic, combat magic의 네 범주다 — 사전 공개 인터뷰 [검색요약, 원문 URL 미확인]. Dexterity는 원거리 무기 사용으로 오른다 — [Dungeon Siege Wiki](https://dungeonsiege.fandom.com/wiki/Character_Leveling_and_Spell_Guide) [팬위키]
- **개발자 발언(Chris Taylor, 2003):** 인터뷰에서 확인된 발언은 인터페이스와 튜토리얼에 대한 것이다. "No need for a manual or a steep learning curve, which I think is the key to a great game." 스킬 관련 발언은 찾지 못했다. 검색 요약에서는 "you can construct a character class by simply reusing specific skills"라는 문장이 확인되지만 원문 URL을 열지 못했다 — [RPG Codex, Gas Powered Games 인터뷰 (1044)](https://rpgcodex.net/article.php?id=1044) [1차·추출]
- **사후 분석:** Bartosz Kijanka(기술 책임자)의 Gamasutra 포스트모템(2002-12-18)이 있다. 원문은 열지 못했고, Codex가 요약한 글에는 스킬 설계 내용이 없었다 — [RPG Codex 요약](https://rpgcodex.net/article.php?id=611) [2차]
- **후속작:** Dungeon Siege II에서 스킬 트리가 추가되었다 — [RPG Codex, CVG 프리뷰 (2005)](https://rpgcodex.net/article.php?id=3357) [2차]. 이것이 원작 방식의 한계 때문인지는 확인되지 않았다.

#### Quest 64 (Imagineer, N64; 북미 1998-06-10)
- **레벨 없음:** "The game differs from most RPGs in that the experience system is not based upon a traditional 'level-up' model." 스탯은 행동으로 오른다. 피격이 많으면 방어력이 오른다("If the character gets hit a lot, for instance, defense will increase."). 정령을 찾으면 원소 하나를 업그레이드한다 — [Wikipedia, Quest 64](https://en.wikipedia.org/wiki/Quest_64) [2차 정리]
- **체감 문제:** 한 리뷰어는 민첩이 오르는 데 매우 오래 걸린다고 평가했다. 아날로그 스틱을 테이프로 고정하고 밤새 돌린 실험에서도 민첩은 +30에 그쳤다 — [retro-daze, Quest 64 리뷰](https://www.retro-daze.org/site/article/9829) [2차, 단일 리뷰어 경험]

#### Kenshi (Lo-Fi Games; Chris Hunt)
- **규칙:** 스킬은 0 근처에서 시작하여 사용으로 오른다(검색 발췌: "you work on them simply by doing") — [PC Gamer, Kenshi 리뷰](https://www.pcgamer.com/uk/kenshi-review/) [2차, 검색요약]. 달리기는 Athletics, 짐 운반은 Strength, 싸움은 전투 스킬을 올린다 — [Pindrop, Kenshi 입문 가이드](https://pindrop.gg/kenshi/beginners-guide) [팬위키]
- **패배 학습:** 진 싸움도 전투 스킬과 강인함을 올린다는 설명이 팬 가이드 요약에 있다. 가이드 출처 귀속은 불확실하다 — [gameplay.tips 가이드(귀속 불확실)](https://gameplay.tips/guides/7339-kenshi.html) [통념, 검색요약]
- **개발자 철학(2025-05-14 mein-mmo 기사, 독일어 원문 → 번역):** "Zu viele Spiele lassen ihre Spieler Erfolg haben." = "Too many games let their players succeed." "Und das ist für mich unfassbar langweilig." = "And that is incredibly boring to me." PC Gamer 헤드라인은 이를 "mind-numbingly boring"으로 옮겼다 — [mein-mmo](https://mein-mmo.de/en/developer-of-popular-rpg-on-steam-reveals-his-recipe-for-success-says-to-torment-the-players,1299282) [2차, 1차 발언 재인용]
- **주의:** 같은 기사에서 "difficulty" 인용은 Chris Hunt가 아니라 공동 작가이자 대표인 Natalie Mikkelson의 말이다. 헌트가 스킬 성장 곡선을 설명한 1차 자료는 찾지 못했다.

#### RuneScape (Jagex)
- **메커니즘:** 확률형이 아니라 "행동당 고정 경험치" 구조다. 시간당 경험치는 시간당 행동 수 × 행동당 경험치이며, 재료 비용을 같이 고려한다 — [OSRS Wiki, Experience rate](https://oldschool.runescape.wiki/w/Experience_rate) [팬위키]. 필요 경험치는 레벨마다 약 10%씩 늘어난다 — 같은 출처 [팬위키]
- **매크로·봇:** OSRS 위키는 매크로·봇·autoing을 실제 플레이어에게 지나치게 지루하다고 여겨지는 작업(예: 특정 스킬 훈련)을 자동화하는 소프트웨어로 정의한다 — [OSRS Wiki, Macroers](https://oldschool.runescape.wiki/w/Macroers) [팬위키]
- **Jagex 대응(위키 인용):** 2011년 ClusterFlutterer 도입. 위키는 Jagex 주장으로 전체 봇의 98% 이상을 막았다고 기록한다 — [RuneScape Wiki, Bots](https://runescape.wiki/w/Bots) [팬위키, Jagex 원문 미확인]
- **2024 논란:** 새 소유주 CVC Capital Partners 측 발언이 봇 계정을 수용하는 것으로 읽히자 플레이어가 반발했다. Jagex는 해당 발언이 전략을 정확히 반영하지 않는다고 했다. 직전 연도에 약 700만 계정을 제재했다고 헤드라인에 나왔다. 블로그 "Bots, Bans and Appeals: An Update"는 콘텐츠를 봇이 하기 어렵게 만드는 전략이 일반 플레이어에게 부정적 영향을 줄 수 있다고 주장했다(검색 요약 paraphrase) — [PC Gamer](https://www.pcgamer.com/old-school-runescape-players-revolt-after-new-big-money-owners-say-bots-are-fine-actually-devs-furiously-walk-it-back-and-say-they-banned-7-million-bots-last-year), [Gamepressure](https://www.gamepressure.com/newsroom/runescape-bots-part-of-the-game-devs-explain-cvcs-unfortunate-sta/z269c0) [2차·검색요약]

#### EVE Online (CCP)
- **실시간 훈련:** 스킬을 고르면 로그오프 중에도 실시간으로 진행된다 — [Engadget, EVE Evolved 가이드 (2008)](https://www.engadget.com/2008-05-05-eve-evolved-skill-system-demystified-part-1.html) [2차]
- **Ghost training(2008-10-13):** 비구독 계정이 훈련을 계속하던 것을 CCP가 막았다. CCP는 이것이 "in all effect, this was a bug"라고 설명했다. 구독자의 오프라인 훈련은 변경하지 않았다 — [CCP, "Why ghost training was disabled"](https://www.eveonline.com/article/why-ghost-training-was-disabled) [1차]
- **스킬 큐 24시간(2009):** 큐 항목은 24시간 안에 시작되어야 했다. Engadget 보도는 CCP가 긴 큐 때문에 플레이어가 게임을 덜 하게 될 것을 우려했다고 전한다 — [Engadget, 2009-02-04](https://www.engadget.com/2009-02-04-long-awaited-skill-queue-coming-to-eve-online.html) [2차]
- **24시간 제한 제거(2014-10-28, CCP Delegate Zero):** 이 글은 24시간 창을 "arbitrary time limit"이라고 부르며 이를 제거한다고 발표했다. 플레이어는 "busy and varied schedules throughout the year" 속에서 훈련을 관리한다는 점을 들었다. 글은 명시적인 설계 근거를 밝히지 않는다(paraphrase). 실시간 훈련 자체에 대한 언급도 없다 — [CCP, "Longer Queues Expected"](https://www.eveonline.com/news/view/longer-queues-expected-skill-training-above-and-beyond-24-hours) [1차·추출]. 큐 항목 50개 상한은 검색 요약에만 있다 [검색요약].
- **Gap:** "시간 기반 훈련이 사용 기반 시스템에 대한 반작용이었다"는 주장은 Koster 관련 2차 블로그 요약에만 나온다 — [검색요약] [통념]. CCP의 1차 설계 근거는 찾지 못했다.

#### Star Wars Galaxies (SOE; 2003 출시)
- **결과 기반 XP 실험:** 크래프터가 다른 플레이어가 자기 아이템을 쓸 때 XP를 얻는 방식이 있었다. Koster는 이것이 "bottomfeeding would once again ensue"를 우려해 제작 XP 방식으로 밀려났다고 쓴다 — [Koster, "Use-based systems"](https://raphkoster.com/?p=592) [1차·추출]
- **속도 조정 실패:** 출시 3일 전 advancement를 "ten times slower"로 만들었다. Koster는 베타 이후 이를 되돌렸고 "it was still too grindy"라고 평가했다 — 같은 출처 [1차·추출]
- **NGE(2005-11-15 Publish 25):** 직업(profession) 체계를 없애고 Jedi를 처음부터 고를 수 있게 했다. Engadget 보도는 "allows players to choose the coveted Jedi profession from the very beginning"과 "Many players feel that these changes radically alter the style of the game."을 전한다 — [Engadget, 2005-11-24](https://www.engadget.com/2005/11/24/star-wars-galaxies-new-game-enhancements-cause-player-backlash/) [2차 당시 보도]. 직업 수가 34에서 9로 줄었다는 기록은 팬·아카이브 자료에서 나왔다 — [MassivelyOP, Game Archaeologist](https://massivelyop.com/2015/04/25/the-game-archaeologist-what-star-wars-galaxies-life-was-like-before-the-nge-2/) [검색요약]
- **Jedi 힌트 장치(Koster, 2015-04-17):** Holocron 힌트 박스가 Jedi 해금 스킬을 알려주었다. 결과는 다음과 같다. "Players simply started at A and learned every skill. In order." "weak cryptography." "Satisfaction fell off a cliff." "one month after Holocron drops began, we started losing subs, instead of gaining them." 그리고 스킬 사용 설계가 "skills is good enough"라는 급한 결정에서 나왔다고 밝혔다 — [Koster, "A Jedi Saga"](https://gamedeveloper.com/design/a-jedi-saga) [1차·추출]
- **그룹 XP 변경(Koster, 2015-04-27):** 플레이어의 과도한 힘을 줄이려는 그룹 XP 변경이 있었다. Koster는 "This single event doubled the churn rate of the game"이라고 썼다. 또 "in that sense, SWG didn't fail. I failed it."라고 결론지었다 — [Koster, "Did Star Wars Galaxies Fail?"](https://www.raphkoster.com/?p=25829) [1차·추출]
- **그라인드 평판에 대한 Koster의 반론:** "it actually had the fastest advancement of any MMO at the time it came out." 같은 글에서 Koster는 시간 소모 요소가 MMO 진입을 막는 장벽이었다고 썼다 — 같은 출처 [1차·추출]

#### Mount & Blade (Warband)
- **무기 숙련:** 해당 무기를 전투에서 계속 쓰고 적중으로 진행한다. 숙련이 오르면 근접 피해, 원거리 정확도, 공격 속도가 좋아진다 — [Mount & Blade Wiki, Proficiencies](https://mountandblade.fandom.com/wiki/Proficiencies) [팬위키·검색요약, 원문 402]. 이 페이지는 시리즈 전반을 다루며 Warband 전용 확인이 아니다.
- **Weapon Master:** 해당 무기 숙련의 더 높은 상한을 찍을 수 있고 학습이 빨라진다는 설명은 Steam 포럼 글이다 — [통념, Steam 포럼 플레이어 글 (검색요약)]
- **Gap:** Warband에서 비무기 스킬이 사용 기반으로 오르는지 확인하지 못했다.

#### Kingdom Come: Deliverance (Warhorse Studios, 2018)
- **사용 기반 스킬(2016-07-18 mein-mmo, 독일어 원문 → 번역):** "Indem ihr Dinge häufig tut, wie beispielsweise Schleichen oder mit dem Schwert kämpfen, verbessert sich der Skill und ihr werdet besser." = "By doing things often, like sneaking or fighting with a sword, the skill improves and you get better." — [mein-mmo, 2016](https://mein-mmo.de/kingdom-come-deliverance-skill-ruestungssystem/) [2차]
- **드문 스킬과 교사:** "Dies bedeutet aber nicht, dass jemand, der beispielsweise so gut wie nie Alchemie ausübt, darin nicht besser werden kann." 대신 유료 교사가 있다. "Es ist möglich, Lehrer in der Welt aufzusuchen, die einem gegen Geld dabei helfen, die Fertigkeiten zu erhöhen." — 같은 출처 [2차]
- **스킬 트리(2017 RPS 프리뷰, GameBanshee 재게재):** 스킬은 "traits that change the way your character interacts with the world and the people in it"로 설명된다. 음주 내성 가지가 있으며, 메뉴가 너무 깊어서 "like vanishing down a rabbit hole"이라는 평가가 있다 — [GameBanshee, KCD 스킬 프리뷰](https://gamebanshee.com/k43w3) [2차]. 이 글은 사용 기반 성장과 교사에 대해서는 말하지 않는다.
- **교사 규칙 충돌:** 같은 교사에게 같은 레슨은 한 번만 가능하다는 설명과 높은 레벨에서도 가능하다는 설명이 팬 가이드에 함께 있다 — [검색요약, 팬 가이드] [통념]
- **Gap:** Warhorse 개발자의 스킬 설계 발언(1차)은 찾지 못했다.

#### Project Zomboid (The Indie Stone)
- **성장 구조:** 행동에 따라 Perk XP가 오른다. 스킬북과 교육 체계가 있다. 멀티플레이 admin 명령으로 /addxp를 쓸 수 있다 — [pzfans, Build 42.19 멀티 레벨업 가이드](https://pzfans.com/how-to-level-up-players-skill-level-in-project-zomboid-multiplayer/) [팬위키·검색요약]
- **악용 사례(커뮤니티):** 창문 유리 파편을 제거하고 맨발로 다니면 First Aid XP가 오른다는 "Foot XP" 트릭 — [pzfans](https://pzfans.com/first_aid_hacks_level_up_fast_without_becoming_zombie_chow/) [통념, 팬위키]. 서버 재입장 시 VHS 시청 상태가 리셋되어 반복 시청으로 Carpentry·Foraging·Aiming XP를 얻는다는 보도 — [Recapio 요약](https://recapio.com/digest/exploiting-the-zombie-apocalypse-by-the-spiffing-brit) [2차, 검색요약]
- **완충 장치:** Skill Recovery Journal 모드는 죽은 뒤 기존 XP를 기본 100%까지 복구한다. 모드 제작자가 만든 것이며 개발사 설계가 아니다 — [pzfans](https://pzfans.com/project_zomboid_how_to_keep_your_skills_after_death) [팬위키]
- **Gap:** The Indie Stone의 XP·Perk 설계 근거(1차)를 찾지 못했다.

#### Dwarf Fortress (Bay 12) — Adventure mode
- **가시성:** Adventure 모드에서는 정확한 경험치가 보이지만, Fortress 모드의 드워프 경험치는 보이지 않는다 — [DF Wiki, Novice](https://catsplode.com/index.php/Novice) [팬위키(미러)]
- **학습 효율:** 실제 전투가 훈련보다 군사 스킬 경험치를 더 많이 준다 — 같은 출처 [팬위키]
- **Rust(Fortress 모드 규칙, v0.34 위키):** 쓰지 않는 스킬은 약 4.5개월 뒤 "rusty"가 되고, 약 2년 3개월에 최대치에 이른다. 6년 뒤 실제 레벨이 떨어지기 시작하며, 최대 6 layer까지 쌓인다 — [DF Wiki, v0.34:Rusty](https://dwarffortresswiki.org/index.php/v0.34:Rusty) [팬위키·검색요약]. 모험자에게 같은 규칙이 적용되는지는 확인하지 못했다.
- **플레이 전략:** 위키 "Hybrid playstyle"은 최고 군사 스킬을 가진 파티를 만들어 훈련시킨 뒤 요새로 은퇴하는 방식을 설명한다 — [DF Wiki, Hybrid playstyle](https://dwarffortresswiki.org/index.php/Hybrid_playstyle) [팬위키·검색요약]
- **실패 학습 철학:** "losing means that next time, you'll remember how you lost!" — [DF Wiki, Important advice](https://dwarffortresswiki.org/index.php/Important_advice) [팬위키, 발췌]. PC Gamer 입문 가이드는 플레이어가 실패를 받아들일 준비가 되어 있어야 한다고 쓴다(검색 발췌) — [PC Gamer](https://pcgamer.com/into-the-deep-its-time-to-learn-how-to-play-dwarf-fortress/3) [2차, 검색요약]
- **Gap:** Tarn Adams나 Bay 12의 1차 발언을 확보하지 못했다. Adventure 모드에서 스킬 규칙이 어떻게 바뀌었는지도 확인하지 못했다.

### Inferences
- **확률형 보정의 함정(추론):** UO에서 "빈도에 맞춰 확률을 조정"하자 기준선이 사라졌다. 플레이어는 실효 확률을 역산해 최적화했다. 따라서 사용 기반 성장에서는 기준 성장률을 먼저 고정하고, 그 위에 시간 기반 최소치(GGS형)나 맥락 조건을 얹는 편이 안전하다는 해석이 가능하다.
- **소수 스킬만 레벨에 기여하는 규칙(추론):** Morrowind/Oblivion/Daggerfall은 "무엇을 올릴지"를 최적화 문제로 바꾸었다. efficient leveling 공략이 존재한다는 사실이 근거다.
- **Skyrim의 방향(추론):** 모든 스킬이 같은 방식으로 레벨에 기여하게 한 변경은 최적화 탐색 공간을 줄이는 효과와 맞아 보인다. 다만 개발자가 이 목적을 명시한 자료는 찾지 못했다.

### Gaps
- **Bethesda 1차 자료:** Major/Minor 제거의 이유를 Howard나 Hines가 직접 설명한 원문(GameSpot 등)을 열지 못했다. 현재 근거는 Gameranx 재인용과 IGN 인용을 재인용한 Codex뿐이다.
- **Oblivion/Morrowind 공략 원문:** UESP 페이지가 403으로 막혀 검색 요약에 의존했다. 수치는 원문 대조가 필요하다.
- **Dungeon Siege 포스트모템:** Gamasutra 원문의 스킬 관련 내용을 확인하지 못했다.
- **Warhorse, Lo-Fi Games, The Indie Stone, Bay 12, Jagex의 설계 근거:** 1차 발언을 찾지 못했다. 현재 근거는 팬 가이드와 2차 보도다.
- **RuneScape XP 설계 근거:** Jagex가 "행동당 고정 XP" 구조를 택한 이유를 설명한 1차 자료는 찾지 못했다.
- **SWG의 NGE 세부 수치:** 직업 34→9 및 "250 skill points" 등은 팬 자료에서 나왔다. 1차 패치 노트로 확인하지 못했다.

---

## 핵심 질문 2: 문서화된 일반 실패 모드는 무엇인가

### Takeaway
문서로 확인되는 실패 모드는 여섯 가지다. (1) 반복 행동의 최적화(그라인드), (2) 매크로·봇 유인, (3) 지배 전략 수렴, (4) 스케일링·밸런스 실패, (5) 계산해야 보이는 불투명한 공식, (6) 실패 비용이나 도전이 없는 반복이다. "정체성 상실"은 SWG 사례로 간접 확인될 뿐, 개발자가 직접 쓴 용어로는 찾지 못했다.

### Cited Findings

#### 1) 최적화가 재미를 없앤다 — Soren Johnson
- **핵심 문장:** "Given the opportunity, players will optimize the fun out of a game." — [Soren Johnson, "Water Finds a Crack," Designer Notes(칼럼 17)](https://www.designer-notes.com/game-developer-column-17-water-finds-a-crack/) [1차]. 원래 Game Developer 2011년 3월호 칼럼이며, 사이트에는 2011-06-12 게시됨.
- **문맥:** "Many players cannot help approaching a game as an optimization puzzle." 그리고 "a single dominant strategy will emerge that drowns out all others." 또 "Games lose their dynamic quality once a strategy emerges that dominates under all conditions." — 같은 출처 [1차·추출]
- **발견되는 허점:** "any hole a player can possibly find in the game's design will be inevitably abused over and over." 그러나 "Discovering and abusing a hole in a game's design can be a fun experience." — 같은 출처 [1차·추출]
- **대응 원칙:** "designers can go too far by trying to remove all exploits from a game." 그리고 "If possible, designers should provide the ability to turn an exploit on or off." — 같은 출처 [1차·추출]
- **출처 주의:** 위 칼럼이 이 문장의 원 출처로 확인되었다. 다른 블로그는 같은 취지를 다른 사람의 말로 돌리기도 하므로, 인용할 때는 칼럼 원문을 쓸 것.

#### 2) 매크로와 봇: 유인이 되는 구조
- **UO:** 확률이 낮은 성장이 자동화를 불렀다. 플레이어는 "one time in a thousand"를 쫓다 실효 확률을 1/10,000으로 만들었다 — [Koster, "Use-based systems"](https://raphkoster.com/?p=592) [1차·추출]
- **UO 가두기:** 강한 몬스터를 집에 가둬서 매크로로 사냥했다 — 같은 출처 [1차·추출]
- **RuneScape:** 봇은 실제 플레이어에게 지루하다고 여겨지는 특정 스킬 훈련 같은 작업을 노린다 — [OSRS Wiki, Macroers](https://oldschool.runescape.wiki/w/Macroers) [팬위키]
- **Zomboid:** 반복 시청 XP 악용 — [Recapio](https://recapio.com/digest/exploiting-the-zombie-apocalypse-by-the-spiffing-brit) [2차, 검색요약]
- **FF II:** 토글 기반 "경험 복사" — [Goombastomp](https://goombastomp.com/not-final-fantasy-ffiis-intriguing-flawed-progression-system/) [2차 분석]

#### 3) 지배 전략과 기준선 붕괴
- **Johnson:** "a single dominant strategy will emerge that drowns out all others" — [designer-notes](https://www.designer-notes.com/game-developer-column-17-water-finds-a-crack/) [1차·추출]
- **Oblivion의 efficient leveling:** 특정 스킬과 속성을 짜 맞추는 공략이 사실상 표준이 되었다 — [UESP](https://en.uesp.net/wiki/Oblivion:Efficient_Leveling) [팬위키·검색요약]
- **SWG Jedi:** 힌트 체계가 깨지자 플레이어는 모든 스킬을 순서대로 다 배워 Jedi에 도달했다 — [Koster, "A Jedi Saga"](https://gamedeveloper.com/design/a-jedi-saga) [1차·추출]
- **UO 시간 조정의 실패:** 빈도 기반 조정이 기준선을 없애 전체 성장을 늦추었다 — [Koster](https://raphkoster.com/?p=592) [1차·추출]

#### 4) 스케일링과 밸런스
- **Oblivion:** "I think the world levelling with you was a mistake." — [VideoGamer](https://www.videogamer.com/news/elder-scrolls-iv-oblivion-levelling-system-mistake-admits-designer-haunts-remaster) [2차 재인용]. 레벨업이 "pointless"하게 느껴지는 문제는 원 발언에서 확인되지 않았다. 설계자는 "dungeon went up in levels with me" 문제를 피하려 했다고 설명했다 — 같은 출처 [2차]
- **Rolston:** 레벨링은 Morrowind의 "obvious balance flaws"를 고치는 수단이었다 — [RPG Codex](https://rpgcodex.net/article.php?id=4408) [1차·추출]
- **SWG 그룹 XP:** "an egregious math error in the grouping XP bonus" 및 "extreme overpower of players" 문제를 고치려던 변경이 churn을 두 배로 만들었다 — [Koster, "Did SWG Fail?"](https://www.raphkoster.com/?p=25829) [1차·추출]

#### 5) 불투명한 진행 공식
- **Daggerfall:** 레벨 공식과 쿨다운 규칙은 공략 페이지에서 설명된다. 게임 내 설명이 충분했는지는 미확인이므로 "공식 해설이 필요했다"는 추론이다 — [UESP](https://en.uesp.net/wiki/Daggerfall:Leveling_and_Skills) [팬위키·검색요약]
- **Oblivion:** 레벨을 "효율적으로" 올리려면 공략이 필요했다. 공략 페이지는 게임을 하지 않고 연습만 하게 될 수 있다고 경고한다(paraphrase) — [UESP](https://en.uesp.net/wiki/Oblivion:Efficient_Leveling) [팬위키·검색요약]
- **FF II:** 확인/취소 토글이 행동으로 인정되는 것은 명시되지 않았고 플레이어가 발견했다 — [Goombastomp](https://goombastomp.com/not-final-fantasy-ffiis-intriguing-flawed-progression-system/) [2차 분석]

#### 6) 도전과 실패가 없는 반복(그라인드의 정의)
- **Koster:** "There's no challenge in jumping off a hill in Oblivion." 또 실패 비용이 없으면 플레이어는 bottomfeed한다(paraphrase) — [Koster, "Use-based systems"](https://raphkoster.com/?p=592) [1차·추출]
- **Schubert(GDC Online 2010 강연):** 그라인드는 인식의 문제이며, 그라인드 자체는 본질적으로 보상적이지 않다 — [Engadget, 2010-10-08](https://www.engadget.com/2010/10/08/star-wars-the-old-republic-tackles-the-grind/) [2차·검색요약]. 그는 "any time developers ask players to do something they don't enjoy in order to open up something that they will enjoy"로 정의했다 — 같은 출처 [2차·검색요약]
- **Yang & Cho(2022):** 그라인딩은 "a monotonous, boring, unconscious, obligatory and rote game experience"로 기술된다 — [Journal of Multimedia Information System, DOI 10.33851/JMIS.2022.9.2.127](https://koreascience.kr/article/JAKO202219441666855.do) [학술, 1차 논문]
- **Quest 64:** 민첩이 "takes forever"로 오른다는 리뷰 — [retro-daze](https://www.retro-daze.org/site/article/9829) [2차, 단일 리뷰어]

#### 7) 정체성 상실/모두가 같아짐 — 간접 근거만 있음
- **SWG:** 힌트가 깨지자 플레이어는 원하던 역할과 무관하게 모든 스킬을 배웠다. Koster는 많은 플레이어가 원치 않는 플레이 방식으로 밀려났고 이것이 큰 불만 요인이었다고 썼다(paraphrase) — [Koster, "A Jedi Saga"](https://gamedeveloper.com/design/a-jedi-saga) [1차·추출]
- **Skyrim:** 두 무기 스킬(Blade, Blunt)을 하나로 합쳤다는 보고가 있으나 근거는 Codex의 풍자 글이므로 사용하지 않는다. 다른 근거는 찾지 못했다.
- **Kawazu(반대 방향):** 사용에 따라 캐릭터가 "naturally become a mage" 하는 것이 설계 의도다 — [Retronauts](https://retronauts.com/article/670/akitoshi-kawazu-on-the-reasoning-behind-sagas-insanity) [1차·추출]. 즉 정체성 차별화가 설계 목표였음을 보여준다.
- **"jack-of-all-trades" 용어:** 개발자 문서에서 이 표현을 쓴 사례를 찾지 못했다 — [통념]

#### 8) 시간 장벽과 세션 설계
- **Koster:** "Time sinks had historically been a huge barrier to adoption of MMOs by audiences beyond the core." — [Koster, "Did SWG Fail?"](https://www.raphkoster.com/?p=25829) [1차·추출]
- **UO power hour:** 플레이어가 세션 첫 시간에 스킬을 몰아 올리는 경향 — [UO Team Comment, 2001](https://uo.stratics.com/content/interviews/evocare.shtml) [검색요약, 원문 403]
- **EVE 큐 제한:** 2009년 Engadget 보도는 CCP가 긴 큐 때문에 플레이어가 게임에서 멀어질까 우려했다고 전한다 — [Engadget, 2009](https://www.engadget.com/2009-02-04-long-awaited-skill-queue-coming-to-eve-online.html) [2차]

### Inferences
- 사용 기반 시스템의 착취 문제는 "행동 비용이 거의 0이고 결과가 결정적일 때" 가장 크다. UO 매크로, FF II 토글, Zomboid VHS 반복 사례가 같은 패턴이다. 이는 사례 3개에서 얻은 추론이다.
- Johnson의 "착취 제거는 역효과가 날 수 있다"와 "토글을 제공하라"는 권고는 착취를 막는 대신 설계자가 착취를 플레이어의 선택지로 취급하라는 뜻으로 읽힌다.
- 정체성 문제는 "스킬이 레벨을 결정하는 구조"에서 "모든 스킬이 같은 방식으로 기여하는 구조"로 가면서 심해질 가능성이 있다. 이 해석을 뒷받침하는 1차 자료는 없다. SWG의 "모든 스킬 배우기"가 가장 강한 사례다.

### Gaps
- "jack-of-all-trades"처럼 정체성 상실을 명시한 개발자 자료를 찾지 못했다.
- 불투명한 공식이 "문제"였다는 것은 공략 존재로 간접 확인할 뿐, 개발자가 이를 문제라고 인정한 자료는 찾지 못했다.
- Johnson 칼럼의 원문 전체를 열지 못했다. 인용문은 WebFetch 요약에서 나온 것이다.

---

## 핵심 질문 3: 성공한 설계는 무엇이며, 무엇이 작동했나

### Takeaway
살아남았거나 개발자가 긍정적으로 평가한 설계는 대체로 네 가지 공통 요소를 갖는다. (a) 총량 상한과 감쇠, (b) 난이도·맥락 조건, (c) 시간·쿨다운 게이팅, (d) 교사나 퀘스트 같은 외부 획득 통로다. 다만 이 설계들의 "성공"을 측정한 1차 자료는 거의 없다. 대부분 개발자 자평이거나 커뮤니티 평가다.

### Cited Findings

#### 설계 요소별 근거
- **총량 상한과 감쇠(UO):** 총 스킬 700 상한과 한 스킬이 오르면 다른 스킬이 내려가는 구조로 선택을 강제했다 — [Koster, "Use-based systems"](https://raphkoster.com/?p=592) [1차·추출]. 이것이 성공이었다는 평가는 Koster 글에 없다.
- **시간 상한과 타이머 체감(UO GGS):** 스킬 구간별로 타이머가 길어진다. 예를 들어 총 700 기준 50.0–54.9 구간은 2.3시간, 100.0–104.9 구간은 32시간이다 — [uo.com GGS](https://uo.com/?p=6342) [1차 공식 문서 재수록]
- **난이도·맥락 조건(UO GGS):** 난이도 기반 스킬은 현재 스킬 근처의 과제에서만 인정된다. Koster도 연습은 도전적이고 가르쳐 줄 때 의미가 있다고 paraphrase했다 — [uo.com GGS](https://uo.com/?p=6342), [Koster](https://raphkoster.com/?p=592) [1차·추출]
- **쿨다운과 판정 시점(Daggerfall):** 스킬당 6 게임 내 시간 쿨다운과 휴식·고속이동 판정 — [UESP](https://en.uesp.net/wiki/Daggerfall:Leveling_and_Skills) [팬위키·검색요약]
- **큐 제한(EVE, 2009–2014):** 24시간 창은 CCP가 "arbitrary"하다고 2014년에 직접 말하며 제거했다 — [CCP, 2014](https://www.eveonline.com/news/view/longer-queues-expected-skill-training-above-and-beyond-24-hours) [1차·추출]
- **교사와 유료 훈련(KCD, UO 가속 퀘스트):** KCD는 드문 스킬을 유료 교사로 올리게 했다 — [mein-mmo, 2016](https://mein-mmo.de/kingdom-come-deliverance-skill-ruestungssystem/) [2차]. UO는 신규 캐릭터용 Accelerated Gains Quests를 두었다 — [uo.com](https://uo.com/?p=6342) [1차 공식 문서 재수록]
- **실패에서 성장(Kenshi, DF, Tim Cain):** 진 싸움도 전투 스킬을 올린다는 가이드가 있다 — [gameplay.tips](https://gameplay.tips/guides/7339-kenshi.html) [통념]. DF는 "losing means that next time, you'll remember how you lost!"라고 표방한다 — [DF Wiki](https://dwarffortresswiki.org/index.php/Important_advice) [팬위키]. Tim Cain은 실패 누적으로 스킬 포인트가 열리는 구조와 실패 시에만 XP를 주는 방식을 제안했다고 3자 위키가 요약한다 — [Turbo Wiki, Tim Cain 요약](https://turbo-wiki.pages.dev/tim-cain/system-design/experience-level-progression) [2차, 원문 미확인]
- **결과 기반의 한계(SWG):** Koster는 결과 기반으로 옮기면 "XP" 쪽으로 되돌아가기 쉽다고 본다. 그가 빠르게 되돌린 속도 조정은 "still too grindy"였다 — [Koster, "Use-based systems"](https://raphkoster.com/?p=592) [1차·추출]
- **스킬 감쇠(DF rust, UO 감쇠):** 쓰지 않으면 녹이 슬어 특화가 유지된다. 평가는 원문에서 확인하지 못했다 — [DF Wiki, v0.34:Rusty](https://dwarffortresswiki.org/index.php/v0.34:Rusty) [팬위키·검색요약]
- **스킬 레벨 가중(Skyrim):** 높은 스킬을 올리면 더 크게 오르고, 자주 쓰는 스킬을 올리는 것이 가장 효율적인 성장 경로가 된다(paraphrase) — [RPG Codex, Five Changes](https://rpgcodex.net/article.php?id=7599) [2차 재인용(IGN)]. Nesmith는 Skyrim의 접근이 "much, much better"라고 말했다 — [VideoGamer](https://www.videogamer.com/news/elder-scrolls-iv-oblivion-levelling-system-mistake-admits-designer-haunts-remaster) [2차 재인용]

#### 설계자의 자기 평가
- **Koster:** 어떤 기준표든 플레이어가 악용을 찾으면 갱신이 필요하므로, 사용 빈도 지표를 추적할 것을 권했다(paraphrase) — [Koster, "Use-based systems"](https://raphkoster.com/?p=592) [1차·추출]
- **Kawazu:** 설계 의도 자체는 "사용에 따라 캐릭터가 된다"였지만 그라인드를 예상하지 못했다고 밝혔다 — [Retronauts](https://retronauts.com/article/670/akitoshi-kawazu-on-the-reasoning-behind-sagas-insanity) [1차·추출]
- **Johnson:** 모든 착취를 제거하려는 것은 지나칠 수 있으며, 가능하다면 착취를 켜고 끌 수 있게 하라고 권했다 — [designer-notes](https://www.designer-notes.com/game-developer-column-17-water-finds-a-crack/) [1차·추출]

### Inferences
- **UO GGS(추론):** "사용하면 오른다"는 규칙을 유지하면서 AFK 대량 사용의 이득을 줄이는 구조다. 성공 지표는 공개되지 않았다. 시간 기반 최소치와 맥락 조건이 결합된 형태가 확률 조정보다 덜 해로웠다고 해석할 수 있으나, 이는 추론이다.
- **실패 학습 설계(추론):** Kenshi, DF, Tim Cain의 방향은 "실패 = 낭비"를 "실패 = 재료"로 바꾼다. 그러나 "의도적으로 지는" 파밍이 새 착취가 될 수 있다는 자료는 찾지 못했다. 보고서에서는 검증이 필요한 가설로 다뤄야 한다.
- **인디 개발자를 위한 설계 원칙(추론, 위 근거에 기반):**
  1. 행동이 성장으로 이어지는 규칙을 플레이어가 이해할 수 있게 문서화하고, 수치를 숨기지 않는다(SaGa의 "naturally become a mage"는 이 방향을 보여준다).
  2. 확률 대신 "최소치 + 시간 게이트"를 쓰면 기준선을 유지하기 쉽다(UO GGS).
  3. 총량 상한을 두고 한 스킬이 오르면 다른 스킬이 내려가게 하면 정체성이 희석되기 어렵다(UO 700 상한).
  4. 난이도나 맥락 조건을 두면 "반복만으로 오르는" 착취를 줄인다(UO GGS 난이도 조건, Koster의 연습-도전 관점).
  5. 교사나 퀘스트 같은 외부 통로를 두면 드문 스킬을 살릴 수 있다(KCD, UO).
  6. 사용 빈도를 로그로 추적하고 수치를 조정한다(Koster 권고). 단, 표 기반 튜닝만으로는 부족하다(Runesabre 사례 언급; Koster).

### Gaps
- 사용 기반 설계가 "성공했다"는 측정 가능한 1차 근거가 없다. 플레이어 수나 유지율 같은 지표가 공개된 사례는 찾지 못했다.
- Tim Cain의 실패 기반 설계는 3자 위키 요약뿐이다. 원문 강연이나 글을 찾지 못했다.
- KCD의 교사 규칙은 가이드 사이에서 충돌한다. 게임 내 확인이 필요하다.

---

## 핵심 질문 4: 학술 또는 GDC 자료는 무엇이 있는가

### Takeaway
사용 기반 진행 자체를 실험한 동료 심사 연구는 찾지 못했다. 가장 가까운 자료는 (1) 경쟁 욕구(competence)를 다룬 자기결정이론(SDT) 연구, (2) MMORPG 동기 연구(Yee), (3) 그라인딩을 다룬 소규모 설문 연구(Yang & Cho 2022), (4) 착취(exploit)를 다룬 Consalvo, Meades, SAGE 2007 논문, (5) GDC Online 2010의 Schubert 강연이다.

### Cited Findings

#### 플레이어 동기
- **Ryan, Rigby & Przybylski (2006), "The motivational pull of video games: A self-determination theory approach", Motivation and Emotion 30(4):347–363:** 게임의 동기 효과는 자율성·유능감·관계성 욕구 충족과 관련된다. 연구자 요약은 게임이 자율성, 유능감, 관계성의 감정을 만들어낸다고 말한다(paraphrase) — [ACU Research Bank 초록](https://acuresearchbank.acu.edu.au/item/8q128/the-motivational-pull-of-video-games-a-self-determination-theory-approach), [University of Rochester 보도](https://www.rochester.edu/news/printable.php?id=2719) [학술, 초록·보도 기반]. 4개 연구로 구성되었다고 보고된다. 표본과 효과 크기는 확인하지 못했다.
- **Yee, "Motivations of Play in MMORPGs" (DiGRA 2005)과 "Motivations for Play in Online Games" (CyberPsychology & Behavior, 2006):** 약 3,000명의 MMORPG 플레이어 설문에서 10개 하위 요인이 Achievement, Social, Immersion 세 축으로 묶였다. 설문 모집 포털에 UO와 SWG 등이 포함되었다 — [DiGRA 2005](https://dl.digra.org/index.php/dl/article/view/239), [Nick Yee, The Daedalus Project](https://nickyee.com/facets/home.html) [학술, 검색요약]. "Achievement" 축에는 레벨을 가능한 한 빨리 올리는 것이 얼마나 중요한지 묻는 문항이 있다고 보고된다 — [검색요약]
- **Schubert(GDC Online 2010), "How Online Gaming Has Adopted the Grind":** 그라인드 인식의 문제이며, 디자이너가 명분이 있더라도 그라인드는 본질적으로 보상적이지 않다고 말했다. SWTOR는 고품질 콘텐츠를 많이 넣었다가 "grindy"하다는 평을 받고 콘텐츠를 줄이고 흩뿌리는 방향으로 바꿨다 — [GDC Vault 목록](https://gdcvault.com/play/1013826/How-Online-Gaming-Has-Adopted), [Engadget 2010 보도](https://www.engadget.com/2010/10/08/star-wars-the-old-republic-tackles-the-grind/) [1차 강연 목록 + 2차 보도] (직함은 GameSpot과 Engadget이 다르게 표기함)

#### 그라인딩 실증
- **Yang & Cho (2022), "Research on the Influence of Curiosity on MMORPG Grinding Player Experience", Journal of Multimedia Information System 9(2):127–136, DOI 10.33851/JMIS.2022.9.2.127:** 그라인딩 경험을 Autonomy, Competence, Relatedness, Positive affect로 나눠 측정했다. I-type 호기심은 네 차원 모두와 관련되었다. D-type 호기심은 Relatedness와 관련되지 않았다 — [KoreaScience](https://koreascience.kr/article/JAKO202219441666855.do) [학술 1차]
- **한계(논문에서 확인됨):** 300부 중 220부를 썼고, 중국 인터넷 카페와 QQ·WeChat 링크로 모집한 편의 표본이다. 표 9의 adjusted R²(0.354)가 R²(0.351)보다 크게 나와 오류로 보인다 — 같은 출처 [학술 1차]
- **Bojin (2013), SFU 박사 논문(Guild Wars 사례):** 검색 요약에서 언급된다. 원문 접근이 403으로 막혀 확인하지 못했다 — [검색요약, URL 미확인]

#### 착취와 글리치
- **Consalvo, *Cheating: Gaining Advantage in Videogames*, MIT Press:** 치팅 산업과 플레이어가 치팅을 정의하는 방식을 다룬다. FFXI 온라인 민족지 연구를 포함하며, "gaming capital" 개념을 제시한다. 출판 연도는 목록마다 달라 2007·2009·2019로 나온다 — [TAMU 도서관 기록](https://libcat.library.tamu.edu/Record/in00004601805) [학술, 목록 기반; 원문 미확인]
- **Meades (2013), "Why we Glitch: process, meaning and pleasure in the discovery, documentation, sharing and use of videogame exploits", Well Played 2(2):79–98:** 착취를 발견·기록·공유·사용하는 과정을 분석한다. 대항 플레이(counterplay)에는 "grief-play, greed-play, trolling, hacking, cheating, boosting" 같은 부정적 꼬리표가 붙는다고 지적한다 — [ETC Press](https://press.etc.cmu.edu/node/2907) [학술, 검색요약 기반]
- **SAGE, "Creative Uses of Software Errors: Glitches and Cheats" (first published 2007; 저널은 Social Science Computer Review로 추정):** 751개 글리치를 155개 인기 게임에서 모아 분석했다. 소프트웨어 공학의 "제거" 관행과 플레이어의 "착취" 관행을 대비하며, 글리치와 치팅이 긍정적 기능을 할 수 있다고 결론짓는다 — [SAGE](https://journals.sagepub.com/doi/10.1177/0894439306289510) [학술, 초록 기반]
- **Backus (2025) arXiv 2504.19010:** 버그(배후의 오류)와 글리치(시스템이 의도대로 돌아가는 중 생기는 오류)를 구분한다. 플레이 경험에 미치는 영향을 묻는 탐색 연구다 — [arXiv](https://arxiv.org/abs/2504.19010) [학술 프리프린트, 동료 심사 전]
- **Backus (2025) arXiv 2504.15408:** 의도적 버그와 비의도적 버그가 경험을 바꾸는지, 개발자 대응이 플레이어 평가를 바꾸는지 묻는다 — [arXiv](https://arxiv.org/abs/2504.15408v1) [학술 프리프린트]

#### GDC 자료
- **Schubert, GDC Online 2010 "How Online Gaming Has Adopted the Grind":** 위 내용 참조 — [GDC Vault](https://gdcvault.com/play/1013826/How-Online-Gaming-Has-Adopted) [1차 강연 목록]
- **사용 기반 진행을 직접 다룬 GDC 강연은 찾지 못했다.** Esports Summit "Skill Progression, Visual Attention..." 강연은 경쟁 게임의 실력 성장에 대한 것이라 직접 관련성은 낮다 — [GDC Vault](https://gdcvault.com/play/1026604/Esports-Summit-Skill-Progression-Visual) [검색요약]

### Inferences
- 사용 기반 진행이 "더 몰입적인가"는 이 자료들로 답할 수 없다. SDT의 competence 욕구가 이론적 틀로 가장 직접적이다. 다만 이것은 추론이다.
- 그라인딩의 정의와 측정(Yang & Cho, Schubert)은 "반복 행동 = 그라인드"를 독립 변수로 쓸 수 있게 한다. 그러나 사용 기반 설계에서 그라인드를 측정한 연구는 찾지 못했다.
- 착취 연구(SAGE 2007, Meades, Backus)는 착취를 "제거"보다 "관리"하는 쪽으로 가는 관점을 제공한다. 이는 Johnson의 토글 권고와 같은 방향이다.

### Gaps
- 사용 기반 진행 또는 learn-by-doing을 직접 실험한 동료 심사 연구는 찾지 못했다.
- Bojin(2013) 논문 원문에 접근하지 못했다.
- Consalvo 책의 정확한 출판 연도가 목록마다 다르다. 원서 판권 페이지를 확인해야 한다.
- 사용 기반 설계의 GDC 강연은 찾지 못했다. GDC Vault 검색을 직접 해야 할 수 있다.

---

**부록: 검증 필요 목록(보고서 작성 전 확인)**
- UO 2001 Team Comment(power hour, GGS 의도): 원문 접근 실패(403). 검색 요약에 의존함.
- UESP(Daggerfall, Oblivion 공략, Skyrim): 원문 접근 실패(403). 검색 요약에 의존함.
- Mount & Blade 위키 Proficiencies: 원문 접근 실패(402). 검색 요약에 의존함.
- DF 위키 Rust: 원문 접근 실패(429). 검색 요약에 의존함.
- Nesmith 인용: VideoGamer 기사를 요약 도구로 읽었다. 원 인터뷰를 찾지 못함.
- Skyrim major/minor 제거 발언: GameSpot 원문 미확인. Gameranx 재인용만 있음.
- SWG NGE 직업 수 34→9와 Publish 25 날짜: 팬·아카이브 출처. 공식 패치 노트로 확인하지 못함.
- 검색 발췌 기반 인용(원문 미열람, [검색요약] 표기): Dungeon Siege 프리뷰 인용, Kenshi PC Gamer 리뷰 인용, DF 가이드 "fail" 문장, OSRS 위키 문구, Sakaguchi/Kawazu 관련 Den of Geek 외 발췌, Schubert 정의 문장(Engadget). 인용 전 원문 확인 권장.
- 요약 도구 추출 인용([1차·추출]): UO Koster 글, Rolston 인터뷰, Koster SWG 글 3편, Johnson 칼럼, Kawazu 인터뷰, CCP 2014, Ken Rolston. 발췌된 문장이라 원문 대조가 필요.
- 일부 Oblivion/Skyrim 설명은 검색 요약의 "UESP 인용" 블로그에 기대고 있다. UESP 원문 확인이 필요하다.
