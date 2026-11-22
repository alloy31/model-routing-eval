# 사용 기반("learn by doing") 캐릭터 성장 시스템: 설계, 실패 유형, 대응, 교훈

> 작성 기준일: 2026-11-15. 표기 규칙: **[1차]** = 개발자 본인 발언/공식 패치노트, **[2차]** = 언론·리뷰, **[커뮤니티]** = 위키·포럼·가이드(사실이 아니라 커뮤니티 통념일 수 있음). 일부 내용은 WebFetch 요약 도구를 거친 것이라, 원문 인용으로 표시한 문장도 보고서에 넣기 전에 원문 대조를 권장함(특히 Koster 블로그 글).
> 주의: UESP(en.uesp.net)는 이번 조사에서 403으로 직접 열람이 막혀 Oblivion 수치는 검색 스니펫 기반임.

---

## Q1. 게임별 시스템 작동 방식과 무엇이 잘못되었나

### Takeaway
거의 모든 사례에서 같은 패턴이 반복된다. "행동 횟수 → 성장"을 보상하면 플레이어는 가장 싸고 반복 가능한 행동을 찾아내 자동화하거나(UO·RuneScape·Morrowind), 의도와 반대되는 행동(아군 공격·일부러 KO당하기)을 하게 된다(FFII·Kenshi). 개발사는 (a) 난이도/성공 조건, (b) 시간 기반 보장·상한, (c) 총량 상한과 감쇠, (d) 정체성을 유지하는 별도 축(종족·퍼크·포커스)으로 대응했고, Bethesda는 "사용 기반 스킬 + 전역 레벨 + 월드 스케일링" 결합을 실수로 인정하고 Skyrim에서 구조를 바꿨다.

### Cited Findings

#### Ultima Online (1997~) — 사용 기반 스킬의 원형
- [1차] Raph Koster 블로그 글 "Use-based systems"(2006-07-18 게시, 2015-06-15 수정). 요약 내용: 모든 플레이어가 처음부터 모든 스킬에 접근 가능했고, 사용할 때마다 성장 확률이 있었음. 초기에는 **남이 스킬을 쓰는 것을 지켜보기만 해도** 성장할 수 있었고, 난이도 개념이 없어 "내 수준보다 쉬운 과제"를 구별할 방법이 없었음 — [Raph Koster, Use-based systems](https://raphkoster.com/?p=592)
- [1차] 같은 글: 총 **700 스킬 포인트** 상한. 포인트를 얻으면 다른 스킬에서 자동으로 1포인트가 빠지고, 사용하지 않는 스킬은 감쇠(decay) — [Koster](https://raphkoster.com/?p=592)
- [1차] 첫 번째 큰 문제는 **스킬마다 사용 빈도가 다르다**는 것: 검은 끊임없이 휘두르지만 "죽은 자와의 대화"는 드물게 씀. 같은 확률이면 검술이 훨씬 빨리 마스터됨. 해결책으로 모든 스킬의 사용 빈도를 동적으로 추적해 성장 확률을 조정했으나, 성장이 계속 느려지자 플레이어는 희귀한 성장을 위해 **매크로**로 대응. Koster: "the thing players had an infinite amount of was time"(요약 도구 경유 인용) — 피드백 루프가 붕괴 — [Koster](https://raphkoster.com/?p=592)
- [1차] 연습용 허수아비(practice dummy)는 새로운 것을 가르쳐주지 않는 "도전 없는 연습"이었고, 플레이어는 강한 몬스터를 자기 집에 가둬두고 매크로를 돌렸음. 매크로를 "overnight" 장시간 돌렸다는 언급 — [Koster](https://raphkoster.com/?p=592)
- [1차] 결과 예측 가능성을 위해 난수 시드를 맵 구역 자원 정보("chunk egg") ID로 설정하는 안을 냈으나, **8타일 이동하면 결과가 바뀐다**는 점을 플레이어가 매크로로 악용 — [Koster](https://raphkoster.com/?p=592)
- [1차] Koster 본인 표현: 매크로 문제는 골드 파머 때문이 아니라 사용 기반 메커니즘 자체 때문에 "we waged a silent war against macroing from very early on" — [Koster(검색 스니펫)](https://raphkoster.com/?p=592)
- [1차] 이후 Runesabre가 동적 테이블을 수작업 고정 테이블로 교체. Koster는 어떤 테이블이든 익스플로잇이 발견될 때마다 갱신해야 하므로 사용 통계는 계속 유지해야 한다고 주장. "Guaranteed gain"과 "power hour"는 자신이 떠난 뒤 추가되어 그 논리는 모른다고 명시 — [Koster](https://raphkoster.com/?p=592)
- [1차·공식] **Power Hour**(Publish 13, 2001-08): 하루 중 캐릭터를 처음 플레이하는 1시간 동안 보너스 스킬 성장 기회. 원래 샤드 현지 시간 기준이라 많은 플레이어에게 불편한 시각에 리셋되었고, 캐릭터별 플레이 시간 기준으로 변경 — [UO Publish 13 (2001-08-19)](https://uo.com/wiki/ultima-online-wiki/technical/previous-publishes/2001-2/2001-publish-13-19th-august/)
- [1차] 2001-09-20 개발팀 코멘트: GGS가 정상 플레이 중 보장된 성장 기회를 제공함으로써 "power hour"의 필요성을 없앨 것이라고 설명 — [Stratics, Team Comment – Skills and Stat Gain (2001-09-20)](https://uo.stratics.com/content/interviews/prophet.shtml), [동일 제목 다른 페이지](https://uo.stratics.com/content/interviews/evocare.shtml)
- [1차·공식] **Guaranteed Gain System**(Publish 16 part 2, 2002-07-23): "if you use a skill and fail, GGS will not come into play"(성공했을 때만 작동). 타이머는 서버 시계 기준이라 로그인하지 않아도 갱신됨. 총 스킬 포인트가 높을수록 타이머가 길어짐. 타이머 만료 시까지 사용 기반 성장이 없으면 "a mandatory point (as in 0.0 to 0.1)" 지급. 난이도 기반 스킬은 "현재 스킬 레벨 근처"의 과제에 성공할 때 보장. 스탯은 30분당 최대 1, 하루 최대 6. 예시: 총 350포인트 캐릭터의 0.0–4.9 구간은 +0.1당 1분, 총 700포인트의 80.0–84.9 구간은 +0.1당 **15시간** — [UO Publish 16 part 2](https://uo.com/wiki/ultima-online-wiki/technical/previous-publishes/2002-2/2002-publish-16-part-2-23rd-july/)
- [2차] 이후 Grandmaster(100)이 상한이었으나 많은 스킬이 특수 스크롤로 Legendary(120)까지 확장됨; 총량 제한 때문에 전문화가 핵심 — [GameBanshee UO Retrospective](https://gamebanshee.com/k4xp)
- [1차] "tank-mage"라는 용어는 UO에서 유래(탱킹과 딜을 동시에 하는 빌드) — Soren Johnson이 지배 전략의 예로 언급 — [Soren Johnson, Water Finds a Crack](https://www.designer-notes.com/game-developer-column-17-water-finds-a-crack/)

#### The Elder Scrolls (Morrowind / Oblivion / Skyrim)
- [1차] Morrowind의 스킬 시스템은 "rewards players for repeating any activity" — 벽에 대고 달리면 Athletics, 반복 점프하면 Acrobatics가 올랐고 많은 플레이어가 이 작은 보상을 위해 몇 시간을 썼음(Soren Johnson의 사례) — [Soren Johnson, Water Finds a Crack (Game Developer 2011년 3월호, 블로그 2011-06-12)](https://www.designer-notes.com/game-developer-column-17-water-finds-a-crack/)
- [커뮤니티] Oblivion: 주요(major) 스킬 상승 합계 **10회**마다 레벨업, 레벨업 시 속성 보너스는 최대 **+5**. 보너스는 해당 속성이 관장하는 스킬(major+minor) 상승 횟수로 결정되며 다음 레벨로 이월되지 않음("attribute bonuses not used at one level are lost"). "Efficient leveling" = 매 레벨 3개 속성에 +5를 받는 것 — [UESP: Oblivion:Efficient Leveling](https://content1.uesp.net/wiki/Oblivion:Efficient_Leveling), [UESP: Oblivion:Leveling](https://en.uesp.net/wiki/Oblivion:Leveling) (둘 다 검색 스니펫 기준, 직접 열람 403)
- [커뮤니티] UESP 조언: 표준 클래스는 선택 속성의 스킬 대부분이 major라 그 속성에 +5를 받기 어려움 → 커스텀 클래스가 효율 레벨링에 유리; 한 속성의 3개 스킬을 모두 major로 고르지 말 것 — [UESP Efficient Leveling](https://content1.uesp.net/wiki/Oblivion:Efficient_Leveling)
- [커뮤니티] Nexus 가이드: Endurance 비관련 major 스킬이 하나라도 오르면 Endurance +5가 불가능해 효율 레벨링이 "virtually impossible"; 효율 레벨링을 위해 덜 중요한 스킬을 major로 골라야 해서 캐릭터가 초반에 약해짐 — [Nexus Mods Oblivion 가이드 (mods/13879 또는 19622 중 하나 — 검색 요약상 어느 쪽인지 불명확)](https://www.nexusmods.com/oblivion/mods/19622)
- [커뮤니티] 적이 플레이어 레벨에 맞춰 스케일링되므로 +5를 놓치면 고레벨에서 "out leveled" 된다는 주장 vs. "1000시간 넘게 5회 플레이하며 효율 레벨링을 쓴 적 없다"는 반론 공존 — 커뮤니티 내에서도 문제의 심각도는 논쟁적 — [Reddit r/oblivion 스레드(미러)](https://cal1.lr.ggtyler.dev/r/oblivion/comments/vgt9zb/how_to_abuse_magic_for_fun_and_profit_or_how_i/id7z3su/?context=3)
- [1차] Bruce Nesmith(전 Bethesda 수석 디자이너, Oblivion 레벨링에 깊이 관여): "I think the world levelling with you was a mistake", "that's proven out by the fact it did not happen the same way in Skyrim", Skyrim에서 "a much, much better way to continue to provide the player challenge"를 찾았다고 발언. 월드가 함께 레벨업하면 레벨업의 의미가 사라진다는 취지 — [VideoGamer 인터뷰 (2025-04 갱신)](https://www.videogamer.com/news/elder-scrolls-iv-oblivion-levelling-system-mistake-admits-designer-haunts-remaster), [GamesRadar 보도](https://www.gamesradar.com/games/the-elder-scrolls/as-oblivion-remastered-introduces-new-fans-to-bethesdas-iconic-2006-rpg-ex-elder-scrolls-dev-admits-the-level-scaling-system-was-a-mistake-eventually-fixed-in-skyrim)
- [1차, 언론 경유] Todd Howard(Game Informer 팟캐스트, 2011-02-03, PSU 2011-02-07 보도): "What we found in Oblivion – you start the game, you pick your race and you play for a while." / "they'd play for like, three hours and then 'oh I picked the wrong skills, I'm going to start over'" / "You just play, and your skills go up as you play and the higher your skill, the more it affects your leveling." — 클래스 선택 프롬프트가 플레이를 끊고, 스킬을 이해하기 전에 고른 선택을 후회하게 만든다는 이유로 제거 — [PlayStation Universe](https://www.psu.com/news/bethesda-explains-elder-scrolls-v-classes-axe/)
- [2차] Skyrim 변경 요약: major/minor 구분 제거("anything you focus on will still help you level up" — Pete Hines의 GameSpot 인터뷰로 보도됨), 개별 무기 스킬 대신 한손/양손/궁술 같은 전투 스타일 + 퍼크로 전문화, Oblivion 8속성·21스킬 → Skyrim 3속성·18스킬 — [검색 요약; 관련 기사 예: RPG Codex "Five Changes from Oblivion to Skyrim"](https://rpgcodex.net/article.php?id=7599) (원 GameSpot 기사 URL은 미확인)
- [1차] Nesmith: Skyrim은 연습 기반 — 특정 스킬을 많이 쓸수록 좋아지고 이것이 레벨업으로 이어짐; Elder Scrolls 6도 "absolutely" 같은 시스템을 쓸 것 — [GamesRadar](https://www.gamesradar.com/games/the-elder-scrolls/as-oblivion-remastered-introduces-new-fans-to-bethesdas-iconic-2006-rpg-ex-elder-scrolls-dev-admits-the-level-scaling-system-was-a-mistake-eventually-fixed-in-skyrim), [Insider Gaming](https://insider-gaming.com/the-elder-scrolls-6-will-feature-same-leveling-as-skyrim-former-designer-says)

#### Final Fantasy II (1988) / SaGa 시리즈 — Akitoshi Kawazu
- [1차] Kawazu 인터뷰(Jeremy Parish, 1UP.com 2012-10, Retronauts 2017-11-13 재게재): 스탯은 생성 시 고정되지 않고 플레이로 성장. "The character-building process goes through the entire game." 마법을 많이 쓰면 자연스럽게 마법사가 됨. "You don't choose what you are in the beginning." 이야기 중심 속편이라 특정 캐릭터가 설정상의 역할을 맡아야 했음("we wanted a more story-driven game for the second Final Fantasy") — [Retronauts](https://retronauts.com/article/670/akitoshi-kawazu-on-the-reasoning-behind-sagas-insanity)
- [1차] 아군 공격 그라인딩을 예상했냐는 질문에: "No, I had no idea." — 잠든 아군을 때려 깨우는 것이 논리적이라 아군 공격을 넣었을 뿐 — [Retronauts](https://retronauts.com/article/670/akitoshi-kawazu-on-the-reasoning-behind-sagas-insanity)
- [1차] **SaGa에서의 대응**: 모두가 같은 행동을 하면 모두 비슷해진다는 문제를 인식하고 종족(인간·몬스터·에스퍼)을 도입. "I needed to differentiate the characters so that they wouldn't all be clones of each other at the end." 에스퍼는 고유 능력을, 몬스터는 고기를 먹어 변화 — [Retronauts](https://retronauts.com/article/670/akitoshi-kawazu-on-the-reasoning-behind-sagas-insanity)
- [2차] Kawazu는 이후 원작과 다르게 만들려다 팀이 너무 멀리 갔다고 느꼈다고 함 — [Wikipedia: Final Fantasy II](https://en.wikipedia.org/wiki/Final_Fantasy_II)
- [2차] Pixel Remaster 기준으로도 HP는 전투 중 HP를 잃을 때 증가 — [vorxu 가이드](https://vorxu.pages.dev/final-fantasy-2-pixel-remaster/leveling) (신뢰도 낮음)
- [커뮤니티/평론] 반론: 아군 자해 그라인딩에 대한 대중적 인식은 개념적으로도, 흔히 말하는 효율적 그라인딩 방법으로서도 "obviously silly"하다는 평론 — 즉 "FFII = 아군 때리기 게임"이라는 이미지 자체가 과장일 수 있음 — [FAEA Substack](https://faea.substack.com/p/final-fantasy-ii-and-moving-backwards)

#### Star Wars Galaxies (2003) / NGE (2005)
- [1차] Koster의 SWG 회고: 사용 기반이 아닌 직업(profession) 목록과 스킬 포인트 예산으로 자유롭게 조합; 상한에 도달하면 "you could simply surrender any skill, and go learn another one"; 기본 스킬·경제 인프라는 "fundamentally about equality"(역할 간 동등한 지위) — [Koster, Designing a Living Society in SWG, part one](https://www.raphkoster.com/?p=25717), [part two](https://www.raphkoster.com/?p=25743)
- [1차] "Use-based systems" 글의 SWG 부분: 제작 XP를 **다른 플레이어가 내 제작품을 사용할 때** 주는 "results-based" 설계로 가치를 검증하려 했으나 아이템 제작 자체에 XP를 주는 방식으로 밀려남; 모든 XP를 이 방식으로 해야 "bottomfeeding"을 막을 수 있었을 것. 베타 사용 데이터로 성장률 조정·도전 난이도 등급 추가. 후반에 성장을 10배 느리게 만든 변경을 테스트 후 되돌림 — [Koster](https://raphkoster.com/?p=592)
- [2차] NGE: 스킬 시스템을 WoW식 클래스(튜토리얼 중 선택)로 교체, Creature Handler·Bio-Engineer 직업 삭제 — [Massively OP, Game Archaeologist: SWG NGE](https://massivelyop.com/2015/08/22/the-game-archaeologist-star-wars-galaxies-nge/)
- [1차, 출처 페이지 미특정] Koster: NGE가 이탈률(churn)을 2배로 만들었고, 되돌린 뒤에도 이전보다 50% 높게 유지; 관련자 모두 "more Star Warsy"하게 만들려는 선의였다; 파괴의 씨앗은 출시 몇 달 후 이미 뿌려졌다 — 검색 요약에서 확인, 원문 URL 특정 못함. 후보: [Paizo 스레드 "Did Star Wars Galaxies Fail? ~ Raph Koster"](https://paizo.com/threads/rzs2s7w7), [Koster part two](https://www.raphkoster.com/?p=25743)

#### EVE Online — 시간 기반 훈련
- [2차] EVE는 연습으로 능력이 성장하는 방식을 허용하지 않음; 스킬은 실시간으로, 로그오프 중에도 훈련 — [Engadget, EVE Evolved: skill system demystified part 1 (2008-05-05)](https://www.engadget.com/2008-05-05-eve-evolved-skill-system-demystified-part-1.html)
- [커뮤니티] "playing more does not accelerate it, and not playing does not stop it" — [EVE University Wiki: Skill training](https://wiki.eveuniversity.org/Skill_training)
- [2차] 스킬 큐는 처음에 없었고 2009년 도입 예정 보도; 이후 24시간 제한도 확장 — [Engadget 2009-02-04](https://www.engadget.com/2009-02-04-long-awaited-skill-queue-coming-to-eve-online.html), [CCP: Skill Training Above and Beyond 24 Hours](https://www.eveonline.com/article/longer-queues-expected-skill-training-above-and-beyond-24-hours)
- [커뮤니티 비판] 게임이 "you'd be better off waiting for better skills than actually playing"을 끊임없이 상기시킨다는 비판(Tobold, 2010) — [Tobold's Blog](https://tobolds.blogspot.com/2010/04/trying-to-understand-eve-skill-system.html?m=1)
- [커뮤니티] 효과는 선형, 훈련 시간은 지수적 증가; 신규 유저가 훈련 시간을 "낭비"할까 걱정하는 문제 — [EVE 포럼 스레드](https://forums.eveonline.com/t/a-new-player-suggesting-some-refinements/444889)

#### RuneScape — 행동당 XP(사실상 사용 기반) + 봇 전쟁
- [커뮤니티] 매크로는 "overly tedious" 작업, 특히 스킬 훈련에 주로 쓰임 — [OSRS Wiki: Macroing](https://oldschool.runescape.wiki/w/Macroing)
- [커뮤니티] 연표: 2002-05 RuneBot 사용자 약 2,000명 스탯 초기화(최초 대규모 밴); 2007-12 매크로 대응 업데이트(랜덤 이벤트 색상 변경으로 컬러봇 무력화 — 일부 봇은 객체 스캔으로 적응); 2009-06-11 무관용 정책; 2010-12-15 XP 롤백 처벌 추가; 2011-02-01 국민투표 결과로 봇 감소에 기여했던 업데이트 다수 철회; 2011-10-25 Project ClusterFlutterer(Jagex 주장 봇 최소 98% 차단); "Bot Nuke" 업데이트가 인젝션 봇 교란에 가장 성공적 — [OSRS Wiki: Macroing](https://oldschool.runescape.wiki/w/Macroing), [RuneScape Wiki: Macroing](https://runescape.wiki/w/Macroing)
- [커뮤니티] 현대 봇은 랜덤 이벤트 해결, 이동, 채팅 응답, 위험 회피까지 수행 — [RuneScape Wiki: Bots](https://runescape.wiki/w/Bots)

#### Dungeon Siege (2002)
- [2차] 근접·원거리·전투 마법·자연 마법 능력이 사용 빈도에 따라 향상; 그러나 Diablo II 같은 스킬 트리의 깊이와 재플레이성이 없고 스킬 간 밸런스가 맞지 않는다는 평가 — [GameSpot Dungeon Siege 리뷰](https://gamespot.com/reviews/dungeon-siege-review/1900-2860893/)
- [1차, 출시 전] Chris Taylor는 "skill-based class system"으로 설명; 숙련자는 전문화, 초보자는 다양화·일반화하는 경향이 있을 것이라 예상 — [GameSpot Dungeon Siege Q&A](https://www.gamespot.com/articles/dungeon-siege-qanda/1100-2625619/)
- [1차] Dungeon Siege II: 스킬을 섞어 하이브리드 클래스를 만드는 "skill-based class system" — [Kikizo, Chris Taylor 인터뷰](https://games.kikizo.com/features/dungeonsiege2_christaylor_interview.asp)

#### Kenshi
- [커뮤니티] Toughness는 피해 저항·상처 악화·KO 기준점을 결정; KO당하되 죽지 않을 때마다 Toughness가 오름 — [Kenshi Wiki: Toughness](https://kenshi.fandom.com/wiki/Toughness), [GameSkinny 가이드](https://www.gameskinny.com/?p=61286)
- [커뮤니티] 대표적 훈련법: 한 캐릭터를 도적 캠프에 보내 KO당한 뒤 "playing dead" 상태에서 붕대를 감으며 회복 → 반복("playing-dead wakeup exploit"). 이 익스플로잇 없이는 Toughness를 올리기 매우 어렵다는 증언과, 익스플로잇 없이 반복 구타로 50대에 도달했다는 증언 공존 — [GOG 포럼 훈련 가이드 (2020-08-22)](https://gog.com/forum/kenshi/my_kenshi_training_guide_from_zero_to_hero_part_1), [Steam 토론](https://steamcommunity.com/app/233860/discussions/0/2790493983185432552)
- [1차, 성장 시스템과 직접 관련은 없음] Chris Hunt: "A writer's job is to torment their protagonist", "Too many games let the player succeed" — 실패·고난 자체를 콘텐츠로 보는 철학(KO로 성장하는 설계와 일관) — [PC Gamer](https://www.pcgamer.com/games/survival-crafting/too-many-games-let-their-players-succeed-says-developer-of-notoriously-tough-survival-rpg-kenshi-and-thats-mind-numbingly-boring-to-me)

#### Project Zomboid
- [커뮤니티] 스킬북: 각 시리즈 5권이 레벨 1–2, 3–4, 5–6, 7–8, 9–10 구간을 담당; 책을 읽으면 **해당 레벨 구간 안에 있을 때만** 그 스킬 XP 배율 적용, 다 읽을수록 배율 상승 — [pindrop.gg: Project Zomboid Skills (Build 42)](https://pindrop.gg/project-zomboid/skills)
- [커뮤니티] Build 42.19 기준 일반 스킬 최대 배율 약 1×→16×; Aiming·Reloading·Long Blade는 낮은 트랙. 책을 읽기 전에 레벨이 구간을 넘으면 배율을 놓친다는 보고 — [pzfans: Books & Magazines](https://pzfans.com/item-books/)

#### Mount & Blade II: Bannerlord
- [커뮤니티] 스킬은 사용으로 XP를 얻지만 "Learning Limit"이 학습을 제한(소프트캡, 이후 매우 느려짐; 한계에서 학습 배율이 0이 된다는 주장도 있어 하드/소프트 여부가 커뮤니티 내 불일치). 한계는 기본값 + 스킬별 포커스 포인트 + 속성 포인트로 결정 — [Mount & Blade Wiki: Skills (Bannerlord)](https://mountandblade.fandom.com/wiki/Skills_(Bannerlord)), [Steam 토론](https://steamcommunity.com/app/261550/discussions/0/4233889679071523971)
- [커뮤니티, 수치 미검증] 포커스 1점당 학습률 ×1.25, 학습 한계 +30 레벨 — [GamerGuides](https://gamerguides.com/mount-and-blade-ii-bannerlord/guide/introduction/character-development/skills)

#### Kingdom Come: Deliverance
- [2차] 잠입·자물쇠 따기·승마·연금술 등 스킬이 훈련/사용으로 향상("Übung macht den Meister"); 스킬에 따라 퀘스트 해결 방식이 달라짐(예: 도적으로 위장해 캠프 잠입) — [Mein-MMO](https://mein-mmo.de/en/kingdom-come-deliverance-skill-ruestungssystem,97873)

#### Dwarf Fortress
- [커뮤니티] 스킬은 사용 시 경험치 획득; 오래 미사용 시 "rusty" → "very rusty". 기본값으로 약 4.5개월 후 녹 발생, 2년 3개월에 녹 최대, 6년 후 실제 스킬 레벨 감소. 경험치를 얻으면 녹이 제거(대부분 제작 작업이 30XP라 녹 6레벨 제거에 3회) — [DF Wiki: Rust](https://www.dwarffortresswiki.org/index.php/Rust)
- [커뮤니티] 위키는 cheat(게임 변경)와 exploit(버그·설계 누락 이용)을 구분하며, 싱글플레이어 게임이므로 어디까지 허용할지는 사용자가 결정한다는 입장 — [DF Wiki: Exploit](https://dwarffortresswiki.org/index.php/Exploit)
- [커뮤니티] 은퇴해 요새에 합류한 모험가도 스킬·속성 녹의 대상 — [DF Wiki: Powerplay Guide](https://dwarffortresswiki.org/index.php/Powerplay_Guide)

### Inferences
- UO GGS의 타이머 구조(총 700 기준 80점대 +0.1에 15시간, 로그인 불필요, 서버 시계)는 사실상 **"사용 기반 위에 시간 기반 보장층"**을 얹은 것이다. EVE의 완전 시간 기반 훈련과 같은 방향으로 수렴하고 있으며, 매크로의 한계 이득을 줄이는 대가로 성장을 벽시계 시간에 묶는다.
- Oblivion 문제의 핵심은 "사용 기반" 그 자체보다 **(사용 기반 스킬) × (클래스 선택 시 고정된 major 스킬) × (속성 배율 산식) × (월드 레벨 스케일링)**의 결합이었다. 자연스럽게 플레이하면 손해를 보고, 의도적으로 "쓰지 않기"나 특정 스킬만 쓰는 관리를 해야 최적화된다. Skyrim은 사용 기반 스킬 성장은 유지하고 클래스 선택·major/minor·속성 배율을 없앴다.
- FFII→SaGa의 진화(종족 도입)는 "모두 같은 행동을 하면 모두 같아진다"는 동질화 문제에 대한 가장 명시적인 1차 증언이다. 사용 기반 시스템만으로는 정체성이 보장되지 않으며, 행동과 무관한 **고정 차별화 축**이 필요했다는 결론으로 읽힌다.
- Kenshi와 FFII는 "실패/피해로 성장"하는 규칙이 "일부러 실패하기"라는 역방향 최적화를 만든다는 것을 보여준다. 다만 Kenshi는 이를 생존 게임의 고난 철학과 맞물려 어느 정도 받아들여지는 것으로 보인다(커뮤니티 증언 기준).

### Gaps
- **Quest 64**: 피격으로 HP/방어가 오르고 이동으로 민첩이 오른다는 통념이 있으나, 신뢰할 만한 출처를 찾지 못함(RPGClassics 페이지는 내용 추출 실패: https://tartarus.rpgclassics.com/quest64/stats.shtml).
- **Daggerfall/Morrowind 레벨링 세부 산식**(major/minor 10회 → 레벨, 속성 배율 등)은 UESP 403으로 직접 확인 못함. Morrowind는 Soren Johnson의 벽 달리기/점프 사례만 1차 확인.
- **Skyrim 자체의 익스플로잇**(예: 철 단검 대량 제작으로 Smithing, 반복 시전 등)은 널리 알려진 커뮤니티 통념이지만 이번 조사에서 출처 미확보.
- Todd Howard의 "a character is best defined by what he's actually doing" 류 발언과 Pete Hines의 GameSpot major/minor 발언은 검색 요약에서만 확인, 원문 URL 미특정.
- **Kenshi 개발자(Chris Hunt)가 스킬 시스템을 직접 설명한 발언**은 찾지 못함. KO 훈련 익스플로잇의 현재 패치 상태도 미확인.
- **Kingdom Come: Deliverance**의 트레이너 유료 훈련·독서 학습·피로 등 세부 및 Warhorse의 그라인딩 관련 1차 발언은 미확보(GameStar 인터뷰가 단서로 언급되나 미열람).
- **Mount & Blade(Warband)**: 원작이 XP+포인트 분배였는지 등은 미확인. Bannerlord 학습 한계 공식은 커뮤니티 간 불일치.
- **Dwarf Fortress 모험 모드**의 구체적 훈련 익스플로잇(예: 반복 공격·자해 훈련 등)은 출처 미확보.
- **SaGa 후속작**(Romancing SaGa의 "번뜩임/閃き" 기술 습득, SaGa Frontier 등)의 사용 기반 변형은 이번 조사 범위에서 다루지 못함.
- **EVE의 시간 기반 훈련이 "사용 기반의 문제에 대한 반작용"이었다는 CCP 공식 근거**는 찾지 못함. 이는 커뮤니티 해석일 가능성이 있음.
- UO Power Hour가 공식적으로 언제 폐지되었는지 미확인.
- Koster 블로그 글의 나머지 약 86,000자(댓글 등)는 읽지 못함.

---

## Q2. 문서화된 일반적 실패 유형과 유명 문구의 원전

### Takeaway
"Given the opportunity, players will optimize the fun out of a game."의 원전은 Soren Johnson의 Game Developer 칼럼 "Water Finds a Crack"(2011년 3월호)이며, 이 칼럼은 Morrowind의 반복 행동 보상을 직접 예시로 든다. Koster는 사용 기반 시스템의 핵심 장애를 "심리적인 것"(플레이어는 이점을 추구하고 재미없는 활동을 건너뛴다)으로 규정했다. 실패 유형은 (1) 퇴화 행동 그라인딩, (2) 매크로/봇 유인, (3) 자연스러운 플레이가 손해가 되는 역설, (4) 동질화, (5) 조기 선택 후회/불투명성, (6) 스킬 간 사용 빈도 불균형으로 정리된다.

### Cited Findings
- **원전 확인** — "Given the opportunity, players will optimize the fun out of a game." 많은 플레이어가 게임을 최소 위험·최대 보상의 최적화 퍼즐로 접근하며, 디자이너는 출시 후 플레이어가 전략을 공유하기 전까지 자기 게임을 이해하지 못하는 경우가 많다는 맥락. Game Developer 2011년 3월호 게재, Designer Notes 2011-06-12 게시 — [Soren Johnson, GD Column 17: Water Finds a Crack](https://www.designer-notes.com/game-developer-column-17-water-finds-a-crack/)
- 같은 칼럼: Civilization 팀은 이 현상을 "water finds a crack"이라고 불렀음(설계의 어떤 틈이든 반복적으로 악용됨) — [Designer Notes 2011-06 아카이브](https://www.designer-notes.com/2011/06/)
- 같은 칼럼: 주된 위험은 하나의 지배 전략이 다른 선택을 무의미하게 만드는 것 — 지배 전략은 "takes away choice from a game"; 플레이어는 이를 과도한 "micro-management"로 경험 — [Soren Johnson](https://www.designer-notes.com/game-developer-column-17-water-finds-a-crack/)
- 같은 칼럼의 예시: Civ3 "lumberjacking", UO 유래 "tank-mage", Civ "infinite city sleaze", 오버플로 낭비를 피하려는 세율·시민 미시관리, Morrowind 반복 행동, Super Mario Bros. 무한 1UP(의도적이고 재미있는 사례), Civ3 랜덤 시드 저장(리로드 익스플로잇 제거에 일부 팬 반발) — [Soren Johnson](https://www.designer-notes.com/game-developer-column-17-water-finds-a-crack/)
- Koster: 연습 자체가 문제가 아니라 **도전도 없고 새로 배우는 것도 없는** 연습이 지루한 것; 가장 큰 장벽은 심리적 — 플레이어는 이점을 추구하고 재미없는 활동은 건너뛰므로 시스템이 이를 감안해야 함; 스킬과 레벨은 "enablers"이지 목적이 아님 — [Koster, Use-based systems](https://raphkoster.com/?p=592)
- Koster의 "법칙" 인용: "players will decode every formula, statistic, and algorithm in your world via experimentation" — [Koster](https://raphkoster.com/?p=592)
- Koster의 2003 Austin Game Conference "Theory of Fun" 키노트: 성장을 추구하는 플레이어는 항상 자신이 하는 일을 최적화하려 한다는 취지 — [Theory of Fun 키노트 PDF](https://www.raphkoster.com/gaming/atof/theoryoffun.pdf) (검색 요약 기준)
- **사용 빈도 불균형**: 스킬마다 자연 사용 빈도가 달라(검 vs 강령술) 균등 확률이면 성장 속도가 극단적으로 달라짐 — [Koster](https://raphkoster.com/?p=592)
- **조기 선택 후회/불투명성**: 플레이어가 3시간 플레이 후 "I picked the wrong skills"라며 재시작 — [Todd Howard via PSU](https://www.psu.com/news/bethesda-explains-elder-scrolls-v-classes-axe/)
- **월드 스케일링과의 결합**: 월드가 함께 레벨업하면 레벨업이 무의미해짐 — "a mistake" — [Bruce Nesmith via VideoGamer](https://www.videogamer.com/news/elder-scrolls-iv-oblivion-levelling-system-mistake-admits-designer-haunts-remaster)
- **동질화("clones")**: 모든 캐릭터가 같은 행동을 하면 결국 클론이 됨 — [Kawazu via Retronauts](https://retronauts.com/article/670/akitoshi-kawazu-on-the-reasoning-behind-sagas-insanity)
- **밸런스 불량**: Dungeon Siege 사용 기반 스킬은 "not well balanced", 스킬 트리 대비 깊이·재플레이성 부족 — [GameSpot](https://gamespot.com/reviews/dungeon-siege-review/1900-2860893/)
- **매크로 유인**: RuneScape에서 매크로는 지루한 스킬 훈련에 주로 사용 — [OSRS Wiki](https://oldschool.runescape.wiki/w/Macroing); UO에서는 골드 파밍이 아니라 사용 기반 메커니즘 자체가 원인 — [Koster](https://raphkoster.com/?p=592)
- **시간 기반의 역효과**: 플레이보다 대기가 낫다는 메시지 — [Tobold](https://tobolds.blogspot.com/2010/04/trying-to-understand-eve-skill-system.html?m=1)

### Inferences
- Johnson의 문구는 사용 기반 시스템에 특히 날카롭게 적용된다. 사용 기반 시스템은 "행동 → 보상"의 연결이 가장 투명하고 짧아서, Koster의 "모든 공식은 해독된다" 법칙과 결합하면 출시 직후 최적 반복 행동이 확정된다.
- "infinite time" 문제(Koster)는 사용 기반 성장의 근본적 비대칭이다. 디자이너가 조절하는 것은 행동당 확률이지만, 플레이어가 조절하는 것은 행동 횟수(자동화 가능)이다. 확률을 낮출수록 자동화의 가치가 오르는 역설이 생긴다.
- 실패 유형은 서로 연결되어 있다. 동질화를 막으려 총량 상한을 두면 "무엇을 버릴지"의 관리 부담이 생기고(UO 감쇠), 매크로를 막으려 시간 보장을 두면 성장이 행동과 분리된다(GGS·EVE).

### Gaps
- Johnson 칼럼 외에 "optimize the fun out" 문구의 더 이른 사용 사례가 있는지는 확인하지 못함.
- Koster의 MUD-Dev 메일링 리스트(1998–1999) 사용 기반 성장 비판 원문은 스니펫이 단편적이라 인용 불가(단서: https://mud-dev.zer7.com/1998/5/6112, https://mud-dev.zer7.com/1999/7/10792).
- "가독성 없는 성장(unreadable progression)"을 직접 다룬 디자이너 1차 발언은 Howard의 "wrong skills" 발언 외에 찾지 못함.

---

## Q3. 성공으로 평가되는 설계와 그 요인

### Takeaway
"순수한" 사용 기반을 그대로 성공시킨 사례는 드물다. 성공 사례로 거론되는 시스템은 모두 사용 기반 성장에 제약층을 더했다: 성공/난이도 조건(UO GGS), 시간 기반 최소 보장과 일일 상한(GGS·Power Hour), 총량 상한과 감쇠·포기(UO·SWG·DF), 맥락 한정 배율(Project Zomboid 책), 학습 한계와 포커스 투자(Bannerlord), 사용과 무관한 정체성 축(SaGa 종족, Skyrim 퍼크). 디자이너들의 결론은 "성장을 재미의 원천으로 삼지 말라"(Koster)와 "익스플로잇은 맥락에 따라 판단하고 가능하면 플레이어에게 통제권을 줘라"(Johnson)이다.

### Cited Findings
- **성공 조건 + 난이도 근접성**: GGS는 실패 시 작동하지 않으며, 난이도 기반 스킬은 "현재 스킬 레벨 근처" 과제에 성공할 때 보장 — [UO Publish 16](https://uo.com/wiki/ultima-online-wiki/technical/previous-publishes/2002-2/2002-publish-16-part-2-23rd-july/); Koster도 초기 UO에 난이도 등급이 없어 쉬운 과제를 구별하지 못한 점을 문제로 지적, SWG에서는 도전에 난이도 등급 추가 — [Koster](https://raphkoster.com/?p=592)
- **시간 기반 보장/상한(rested·first-time 보너스 계열)**: Power Hour(하루 첫 1시간 보너스, 캐릭터 플레이 시간 기준으로 수정) — [UO Publish 13](https://uo.com/wiki/ultima-online-wiki/technical/previous-publishes/2001-2/2001-publish-13-19th-august/); GGS 스탯 30분당 1·하루 6 상한 — [UO Publish 16](https://uo.com/wiki/ultima-online-wiki/technical/previous-publishes/2002-2/2002-publish-16-part-2-23rd-july/)
- **결과 기반(results-based) 로직**: 단순 사용이 아니라 구체적 결과로 성장(XP의 기반); SWG에서는 다른 플레이어가 제작품을 쓸 때 XP 부여 구상 — [Koster](https://raphkoster.com/?p=592)
- **인증/트레이너 방식**: Privateer Online은 점진적 스킬 상승 대신 훈련·도전·회비를 거치는 인증(certification) 방식을 제안 — [Koster](https://raphkoster.com/?p=592)
- **총량 상한·감쇠·포기**: UO 700포인트 + 미사용 감쇠 — [Koster](https://raphkoster.com/?p=592); SWG 상한 시 스킬 포기 후 재학습 — [Koster SWG part one](https://www.raphkoster.com/?p=25717); DF 녹(rust)은 수개월~수년 단위로 천천히 진행되고 사용으로 회복 — [DF Wiki: Rust](https://www.dwarffortresswiki.org/index.php/Rust)
- **맥락 한정 배율(교재/교사형)**: PZ 스킬북 배율은 해당 레벨 구간 안에서만 적용 — [pindrop.gg](https://pindrop.gg/project-zomboid/skills)
- **사용 + 투자 하이브리드**: Bannerlord는 사용으로 XP를 얻되 포커스·속성 투자가 학습 한계·학습률을 정함 — [Mount & Blade Wiki](https://mountandblade.fandom.com/wiki/Skills_(Bannerlord))
- **고정 정체성 축**: SaGa 종족 도입으로 클론화 방지 — [Kawazu via Retronauts](https://retronauts.com/article/670/akitoshi-kawazu-on-the-reasoning-behind-sagas-insanity); Skyrim은 전투 스타일 스킬 + 퍼크로 전문화 — [검색 요약/RPG Codex](https://rpgcodex.net/article.php?id=7599)
- **클래스 선택 제거 + 월드 스케일링 완화**: Howard는 Skyrim 스킬 시스템을 스스로 균형을 잡는 더 우아한 설계로 설명 — [PSU](https://www.psu.com/news/bethesda-explains-elder-scrolls-v-classes-axe/); Nesmith는 Skyrim 방식이 "much, much better"라고 평가하고 ES6도 유지할 것이라 발언 — [GamesRadar](https://www.gamesradar.com/games/the-elder-scrolls/as-oblivion-remastered-introduces-new-fans-to-bethesdas-iconic-2006-rpg-ex-elder-scrolls-dev-admits-the-level-scaling-system-was-a-mistake-eventually-fixed-in-skyrim)
- **익스플로잇을 다루는 원칙(Johnson)**: 익스플로잇이 게임을 망치는지, 아니면 재미있는 지름길인지 먼저 판단; Civ4는 도시별 유지비로 ICS를 막고 오버플로를 다음 생산에 이월; "If possible, designers should provide the ability to turn an exploit on or off."; "Ultimately, the designer can't go wrong putting the player in control of his or her own experience." — [Soren Johnson](https://www.designer-notes.com/game-developer-column-17-water-finds-a-crack/)
- **사용 통계의 지속 관리**: 어떤 성장 테이블이든 익스플로잇 발견에 맞춰 계속 갱신해야 하므로 사용 지표를 유지해야 함; SWG는 베타 사용 데이터로 성장률 조정 — [Koster](https://raphkoster.com/?p=592)
- **실패/고난을 콘텐츠로 수용**: Kenshi는 KO당하며 Toughness가 오르는 구조 — [Kenshi Wiki](https://kenshi.fandom.com/wiki/Toughness); 개발자 철학 "Too many games let the player succeed" — [PC Gamer](https://www.pcgamer.com/games/survival-crafting/too-many-games-let-their-players-succeed-says-developer-of-notoriously-tough-survival-rpg-kenshi-and-thats-mind-numbingly-boring-to-me)
- **완전 시간 기반의 대안(EVE)**: 플레이 여부와 무관하게 성장 → 매크로 유인 제거, 대신 "기다리는 게 낫다"는 비판 — [EVE Uni Wiki](https://wiki.eveuniversity.org/Skill_training), [Tobold](https://tobolds.blogspot.com/2010/04/trying-to-understand-eve-skill-system.html?m=1)

### Inferences
- "you become what you do"를 목표로 하는 인디 개발자에게 적용 가능한 설계 체크리스트(조사 결과 종합, 추론):
  1. **도전 조건**: 현재 숙련도에 비해 충분히 어려운 과제의 성공(또는 의미 있는 실패)만 성장으로 인정한다(UO GGS, Koster의 난이도 등급).
  2. **행동 수가 아니라 결과/맥락을 보상**한다(Koster의 results-based, SWG 타인 사용 검증). 같은 대상·장소·패턴의 반복에는 수확 체감을 둔다(UO 동적 테이블의 교훈: 체감만으로는 매크로를 부르므로 시간 기반 상한과 함께 써야 함).
  3. **시간 상한/보장층**(일일 상한, 첫 플레이 보너스, 최소 보장)으로 무한 반복과 자동화의 한계 이득을 낮춘다(Power Hour, GGS).
  4. **정체성 고정 축**: 행동과 무관한 출신·종족·성향(SaGa), 또는 상호배타적 퍼크·포커스(Skyrim, Bannerlord)와 총량 상한(UO)으로 "만능 캐릭터" 수렴을 막는다.
  5. **전역 레벨 및 월드 스케일링과 결합하지 않는다.** 사용 기반 스킬이 월드 난이도를 끌어올리면 "자연스러운 플레이 = 손해"가 된다(Oblivion, Nesmith의 반성).
  6. **조기 확정 선택을 피한다.** 플레이어가 시스템을 이해하기 전에 내린 선택이 사용 기반 성장 효율을 좌우하면 재시작 유인이 생긴다(Howard).
  7. 싱글플레이라면 Johnson의 권고대로 익스플로잇 허용 여부를 **플레이어가 선택**할 수 있게 하는 것을 고려한다(DF 위키도 싱글플레이 익스플로잇은 사용자 재량이라는 입장).
- 성공 사례의 공통점은 사용 기반을 **유일한 성장 원천이 아니라 여러 입력 중 하나**로 격하했다는 점이다(Skyrim: 퍼크 선택, Bannerlord: 포커스, PZ: 책, SaGa: 종족).

### Gaps
- Skyrim이 출시 후 사용 기반 익스플로잇 문제로 패치·조정을 했는지에 대한 Bethesda 1차 자료는 찾지 못함.
- WoW식 "rested XP"를 사용 기반 시스템에 적용해 효과를 측정한 공개 자료는 찾지 못함(UO Power Hour가 가장 가까운 사례).
- 각 대응책의 정량적 효과(예: GGS 도입 후 매크로 감소율)는 공개 자료 미확보. RuneScape ClusterFlutterer의 "98%"는 Jagex 주장을 커뮤니티 위키가 전한 수치임.
- KCD의 "learn from failure"(예: 자물쇠 따기 실패 시 XP) 등 실패 보상 규칙의 공식 설명은 미확보.

---

## Q4. 학술·GDC 자료

### Takeaway
사용 기반 성장 자체를 다룬 학술 논문이나 GDC 강연은 이번 조사에서 찾지 못했다. 관련성이 있는 것은 그라인딩을 "일과 놀이의 수렴"으로 본 게임 연구 문헌, 그라인딩 경험과 호기심에 관한 2022년 논문, 그리고 개발자 저작(Koster의 Theory of Fun, Johnson의 칼럼) 정도다. 실질적 지식은 대부분 개발자 블로그와 패치노트에 있다.

### Cited Findings
- Simon Fraser University 학위논문(Guild Wars 그라인딩): MMOG의 그라인드는 게임 연구자들에 의해 "an inscrutable, paradoxical convergence of work and play"로 묘사되어 왔으며(Dibbell 2006, Yee 2006 인용), 플레이어 공동체에게 그라인딩이 무엇을 의미하는지 매핑하려는 연구 — [SFU Summit](https://summit.sfu.ca/item/13445), [CORE PDF](https://core.ac.uk/download/56377584.pdf)
- Yang & Cho (2022), *Journal of Multimedia Information System* 9(2), 127–136: 그라인딩 경험을 자율성·유능감·관계성·긍정 정서로 나누고 설문으로 호기심의 역할을 검증, 그라인딩 메커니즘 설계 변경을 제안 — [DOI 10.33851/jmis.2022.9.2.127](https://doi.org/10.33851/jmis.2022.9.2.127) (저널 페이지 직접 미열람, 초록 재게재 페이지 기반: [universityxp](https://www.universityxp.com/research/2023/6/19/research-on-the-influence-of-curiosity-on-mmorpg-grinding-player-experience))
- Guild Wars는 최대 레벨 20이라는 매우 낮은 상한으로 그라인딩을 줄이려 함 — [Wikipedia: Grinding (video games)](https://www.wikipedia.org/wiki/Level_grind)
- 개발자 측 이론 자료: Koster "Theory of Fun"(2003 Austin Game Conference 키노트) — [PDF](https://www.raphkoster.com/gaming/atof/theoryoffun.pdf); Johnson "Water Finds a Crack"(Game Developer 2011-03) — [Designer Notes](https://www.designer-notes.com/game-developer-column-17-water-finds-a-crack/)
- GDC 2021 SWG 관련 세션 보도(기업 압력과 팬 사랑의 복합 게임으로 회고) — [Massively OP 2021-07-23](https://massivelyop.com/2021/07/23/gdc-2021-star-wars-galaxies-was-a-complex-game-of-corporate-greed-and-fan-love/) (세부 내용 미열람; 스킬 시스템 언급 여부 미확인)

### Inferences
- 학술 연구는 "그라인딩/반복 행동의 동기"와 "플레이어 동기 모델"(Yee 등)은 다루지만, "사용 기반 vs XP 기반 vs 시간 기반" 같은 성장 구조를 비교한 실증 연구는 공백으로 보인다. 보고서에서는 이 부분을 개발자 1차 증언에 의존해야 한다.
- 자기결정이론(자율성·유능감) 틀(Yang & Cho)은 "you become what you do" 설계의 매력(자율성)과 위험(자동화·반복이 유능감 신호를 오염시킴)을 설명하는 이론적 연결고리로 쓸 수 있다(추론).

### Gaps
- 사용 기반 성장 또는 봇/매크로를 직접 다룬 DiGRA·CHI PLAY·Game Studies 논문은 이번 검색에서 확인하지 못함(후속 검색어 제안: "botting MMORPG DiGRA", "skill-based progression player behavior", "learning by doing game mechanics").
- GDC Vault에서 사용 기반 성장을 주제로 한 강연(예: Skyrim 시스템 디자인, UO 회고)의 존재 여부와 내용은 확인하지 못함.
- Nick Yee의 플레이어 동기 요인 분석 원문은 검색 결과에서 출처가 불분명한 사본만 확인되어 인용하지 않음.
