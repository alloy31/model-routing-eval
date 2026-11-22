# 사용 기반(learn-by-doing) 캐릭터 성장: 설계, 실패 모드, 대응, 결론

> **표기 규칙**
> - **[문서]**: 원문 또는 원문에 가까운 1차 출처를 직접 확인한 항목
> - **[2차]**: 검색 스니펫 또는 WebFetch 요약에 의존한 항목. WebFetch 결과는 요약 모델을 거친 발췌이므로, 따옴표 안 문장도 원문 대조 전에는 verbatim으로 인용하지 말 것
> - **[커뮤니티]**: 팬 위키, 가이드, 포럼 등 문서화되지 않은 통념
>
> **조사 범위**: 도구 호출 14회 안에서 수행했다. 요청된 게임 중 Ultima Online, Elder Scrolls(Oblivion/Skyrim), Final Fantasy II, EVE Online, Star Wars Galaxies, Kingdom Come: Deliverance는 일부 확인했다. Dungeon Siege, Quest 64, SaGa 시리즈, Kenshi, RuneScape, Project Zomboid, Mount & Blade, Dwarf Fortress adventure mode는 이번 패스에서 조사하지 않았다(각 절의 Gaps 참고). Daggerfall과 Morrowind도 미조사다.

---

## 핵심 질문 1. 시스템은 구체적으로 어떻게 작동했고, 무엇이 잘못됐나

### Takeaway
"쓴 만큼 는다"는 규칙은 직관적이지만, 세 가지 문제가 반복해서 나타났다. (1) 행동마다 사용 빈도가 달라 성장 속도가 극단적으로 불균등해졌다. (2) 반복 가능하고 위험이 없는 행동이 최적 경로가 되어 매크로, AFK, 의미 없는 반복을 유도했다. (3) 이를 막으려고 추가한 보정(보장 성장, 속도 제한, 레벨 기반 전환)이 다시 새로운 최적화 경로를 만들었다. 가장 상세히 문서화된 사례는 UO이고, Bethesda 시리즈에서는 "효율적 레벨링"이라는 형태로 반복됐다.

### Cited Findings

#### Ultima Online (UO)
- **기본 규칙**: 스킬을 성공적으로 쓸 때마다 해당 스킬이 오를 가능성이 있다. 관련 UO 공식 페이지는 [Guaranteed Gain System | Rate Over Time System | Other Aids to Gaining](https://uo.com/?p=6342)이며, 검색 요약으로만 확인했다. **[2차]**
- **사용 빈도 불균형**: Raph Koster는 "swords were swung quickly"(검을 빨리 휘두른다)와 "Talking to the dead was done rarely"(죽은 자와 대화하는 일은 드물다)를 대비하며, 이 때문에 성장 시점이 "a random draw"(주사위 굴림)가 됐다고 설명했다. 출처는 [Koster, "Use-based systems"](https://raphkoster.com/?p=592)이며, WebFetch 요약 기준으로 게시일은 2006년 7월 18일이다. **[2차]**
- **보정의 실패**: 빈도에 따라 성공 확률을 조정하자 성장이 너무 느려졌고, 플레이어들은 "chasing after the one time in a thousand that they would go up"(천 번에 한 번 오르는 기회를 쫓는) 매크로를 돌렸다. Koster는 이를 "feedback loop broke"(피드백 루프가 깨짐)로 진단했다. **[2차]**
- **보정의 연쇄**: 빈도 기반 방식은 Runesabre가 수작업 테이블로 교체했고, 이후 "guaranteed gain"과 "power hour"가 추가됐다(Koster 글 요약). **[2차]**
- **행동 악용 사례(Koster 글 요약)**: 실패 후 8타일을 움직이면 성공률이 오른다는 것을 실험으로 알아낸 플레이어가 있었고, 수정 후에는 강한 몬스터를 집 안에 가둬 두고 매크로로 사냥했다. Koster는 이를 "players will decode systems through experimentation"(플레이어는 실험을 통해 시스템을 해독한다)의 예로 든다. **[2차]**
- **맥락 무관 성장**: 스킬은 다른 사람이 쓰는 것을 지켜보는 것만으로도 오를 수 있었고, 사소한 행동을 막는 난이도 등급이 없었다(Koster 글 요약). **[2차]**
- **감쇠와 상한**: 쓰지 않은 스킬은 감쇠했고 총합 상한은 700이었다(Koster 글 요약). **[2차]**
- **보장 성장(GGS)**: 일정 기간 성장이 없으면 최소 성장을 보장하는 보정이다. 검색 요약에 따르면 2001년 팀 코멘트가 이를 제안하면서 "power hour" 방식의 문제, 즉 하드코어 플레이어가 극단적으로 쉽게 이득을 보는 환경을 지적했다. 원문인 [UO team comment, "Skills and Stat Gain", 2001-09-20](https://uo.stratics.com/content/interviews/prophet.shtml)은 HTTP 403으로 열지 못했다. **[2차, 원문 미확인]**
- **속도 제한**: Siege Perilous와 Mugen은 70 이상 스킬에 시간당 증가율 제한을 적용했고, 검색 요약에 따르면 70.0–79.9 구간은 5분마다 0.1을 얻는다. 출처는 팬 문서와 UO 팀 문서이며 Koster 글이 아니다. **[커뮤니티/팬 문서, 2차]**

#### The Elder Scrolls: Oblivion
- **레벨업 구조**: 메이저 스킬을 10번 올린 뒤 침대나 bedroll에서 수면하면 레벨업이 발생한다. 속성 보너스는 10번째 메이저 상승 시점에 확정되며, 마이너 스킬 상승도 속성 보너스 계산에 포함된다. 출처는 [UESP, Oblivion:Level](https://en.uesp.net/wiki/Oblivion:Level)이다. 검색 스니펫 기준이며 전문은 열지 않았다. **[문서(위키), 2차 확인]**
- **효율적 레벨링**: 속성 보너스 표는 관련 스킬 상승 횟수에 따라 1–4회 +2, 5–7회 +3, 8–9회 +4, 10회 이상 +5이다. 가이드는 필요 이상으로 훈련하지 말고 레벨업 직전에 저장하라고 권한다. 출처는 [UESP, Oblivion:Efficient Leveling](https://content1.uesp.net/wiki/Oblivion:Efficient_Leveling)이다. **[문서(위키), 2차 확인]**
- **"레벨링 문제"의 두 층위**: Nesmith는 "I think the world levelling with you was a mistake"라고 말했다. 맥락은 세계 레벨링, 즉 "the dungeon went up in levels with me"(던전이 나와 함께 레벨이 올라갔다)다. 이는 스킬 기반 레벨업이 아니라 적 스케일링에 관한 발언이다. 출처는 [VideoGamer, Oblivion levelling "mistake"](https://www.videogamer.com/news/elder-scrolls-iv-oblivion-levelling-system-mistake-admits-designer-haunts-remaster)이며 날짜는 없다. **[2차]**
- **점프 악용**: Koster 글 요약에 따르면 Oblivion에서 회피 관련 스킬을 올리려고 언덕에서 계속 뛰는 행동이 있었고, Koster는 "no challenge in jumping off a hill in Oblivion"이라고 지적했다. 검색 스니펫은 이를 일반론으로 적었으나, WebFetch 요약은 Oblivion으로 특정했다. **[2차]**
- **Skyrim의 방향 전환**: Nesmith는 속성 시스템을 개발 초기부터 제거했다고 말했다. 그의 발언으로 보도된 헤드라인은 "we got rid of attributes in skyrim and you know who complained almost nobody"(Skyrim에서 속성을 없앴는데 불만을 제기한 사람은 거의 없었다)이다. 출처는 [PC Gamer 보도](https://www.pcgamer.com/games/the-elder-scrolls/bethesda-veteran-says-less-rpg-complexity-in-the-elder-scrolls-series-is-good-actually-we-got-rid-of-attributes-in-skyrim-and-you-know-who-complained-almost-nobody)다. **[2차, 헤드라인 포함]**
- **메이저/마이너 제거**: 사전 보도는 "어떤 스킬에 집중하든 레벨업에 도움이 된다"는 점이 강조됐다고 전한다. 개발자 원문 인용은 찾지 못했다. **[2차, 개발자 직접 인용 미확인]**
- **개별 스킬 정리(Nesmith 2011 Q&A 요약)**: Acrobatics는 쓸모가 낮았고, Mysticism은 혼란스러웠으며, Hand to Hand는 제거됐다. 무기군 차이는 퍽 선택으로 옮겨졌다. **[2차]**
- **TES VI 관련(MinMaxx 인터뷰 요약)**: Nesmith는 TES VI가 Skyrim 진행 시스템 대부분을 유지할 것이라고 말했다고 전해진다. 출처는 [80.lv 보도](https://80.lv/articles/bethesda-doesn-t-plan-to-bring-back-cut-rpg-stats-in-the-elder-scrolls-6)다. **[2차]**

#### Final Fantasy II
- **스탯 성장 방식**: 스탯은 사용으로 오른다. 회피율은 물리 공격을 받을 때 오른다. 출처는 [RPGSite](https://www.rpgsite.net/feature/11516-final-fantasy-ii-how-to-level-up-and-an-explanation-on-the-leveling-system)이다. **[2차]**
- **아군 공격 악용**: [TV Tropes(GameBreaker)](https://www.tvtropes.org/pmwiki/pmwiki.php/GameBreaker/FinalFantasy)는 아군을 공격하거나 초반 적을 상대로 전투를 끌어 스탯을 키우는 악용을 기술한다. [StrategyWiki](https://strategywiki.org/wiki/Final_Fantasy_II/Gameplay)에는 "Abusing the leveling system (Famicom/PSX only)" 섹션이 있으나 본문은 확인하지 못했다. **[커뮤니티/위키 존재 확인, 세부 미확인]**
- **구현 악용 두 가지**: [Goombastomp](https://goombastomp.com/not-final-fantasy-ffiis-intriguing-flawed-progression-system/)는 첫 세 명의 명령 취소와 타겟팅 악용을 설명하며, 두 방법 모두 그라인드를 완전히 해결하지 못하고 게임을 지나치게 쉽게 만들 수 있다고 본다. **[2차]**
- **효과 크기 논쟁**: [Substack 에세이](https://faea.substack.com/p/final-fantasy-ii-and-moving-backwards)는 "아군 공격으로 레벨업"이라는 평판이 과장됐다고 주장한다. 낮은 품질의 PSP 가이드는 이를 "myth"라고 부른다(신뢰도 낮음). **[2차, 논쟁 상태]**
- **후속작의 대응**: Pixel Remaster는 스탯 성장 속도를 최대 4배까지 올리는 옵션을 제공한다. 출처는 [Push Square 리뷰](https://www.pushsquare.com/reviews/ps4/final-fantasy-ii-pixel-remaster)다. 이것이 개발진의 악용 대응인지 여부는 확인하지 못했다. **[2차]**

#### EVE Online
- **시간 기반 훈련**: EVE의 스킬은 경험치가 아니라 실시간으로 훈련된다. 로그오프 중에도 진행된다. 출처는 [Engadget, 2009](https://www.engadget.com/2009-02-04-long-awaited-skill-queue-coming-to-eve-online.html)이다. **[2차]**
- **도입 배경**: Engadget은 CCP가 긴 스킬 큐를 걸어 두고 AFK 상태로 있는 플레이어가 늘어날 것을 우려했고, 타협안으로 큐에 24시간 제한을 두었다고 전한다. **[2차]**
- **제한 해제**: CCP는 공식 뉴스 [Longer Queues Expected: Skill Training Above and Beyond 24 Hours](https://www.eveonline.com/news/view/longer-queues-expected-skill-training-above-and-beyond-24-hours)에서 24시간 이상 큐를 예고했다. 제목으로만 확인했고 본문은 열지 못했다. 2014년 CCP 블로그가 이 제한을 해제했다고 검색 요약에 나오지만 원문은 확인하지 못했다. **[문서(제목), 2차]**
- **플레이어 이론**: 훈련 시간은 지수적으로 늘고 혜택은 선형적으로 늘기 때문에 숙련이 비효율적이라는 주장이 포럼에 있다. 긴 훈련 시간이 저렴한 스파이 캐릭터를 억제한다는 주장과, 과금과 연결짓는 주장도 있다. 모두 공식 근거가 없다. 이 주장들은 여러 공식 포럼 스레드에 흩어져 있으며, 예로 [Skill Training - Just a set of artificial delay timers?](https://forums.eveonline.com/t/skill-training-just-a-set-of-artificial-delay-timers/22679)와 [Wasted training time](https://forums.eveonline.com/t/wasted-training-time/475982?page=2)을 들 수 있다. 검색 스니펫으로만 확인했고, 주장별로 어느 글에서 나왔는지는 분리하지 못했다. **[커뮤니티]**

#### Star Wars Galaxies (SWG)
- **NGE 이전 구조**: 레벨이 없었다. 250 포인트 스킬 풀에서 스킬 박스를 골랐고, 각 박스는 포인트, 특정 종류의 XP, 선행 박스나 직업을 요구했다. 출처는 [2007년 블로그](https://flatfingers-theory.blogspot.com/2007/09/lessons-of-star-wars-galaxies.html)다. **[2차]**
- **교육 기능**: 같은 블로그는 다른 플레이어에게 스킬을 배우는 "teaching" 기능이 초기에 잘린 기능 중 하나라고 적었다. **[2차]**
- **결과 기반 성장**: Koster는 SWG 제작 XP를 다른 플레이어가 아이템을 사용할 때 지급하는 "results-based" 방식으로 설명했다. 출처는 [Koster, "Use-based systems"](https://raphkoster.com/?p=592) 요약이다. **[2차]**
- **NGE 이후**: 스킬 시스템은 9개의 "iconic professions"로 대체됐다([SWG Wiki, Professions (pre-NGE)](https://swg.fandom.com/wiki/Professions_(pre-NGE)) 관련 위키). Engadget은 스킬 빌딩에서 레벨과 명확한 클래스 중심으로 옮겨갔다고 정리한다([Engadget SWG history](https://www.engadget.com/2008/06/26/a-star-wars-galaxies-history-lesson-from-launch-to-the-nge-5/)). GamesRadar는 WoW식 클래스를 튜토리얼 미션에서 고르게 했다고 전한다([GamesRadar](https://gamesradar.com/time-extend-star-wars-galaxies)). **[2차, 커뮤니티 위키 포함]**
- **출처 충돌**: NGE 이전 직업 수는 34개와 32개로 출처마다 다르다. 9개라는 수치의 출처는 Wikipedia 스니펫으로, URL 표기가 이상해 신뢰도가 낮다. **[출처 충돌]**
- **직업 축소**: Creature Handler와 Bio-Engineer가 제거됐다는 내용이 [MassivelyOP의 GDC 2021 정리](https://massivelyop.com/2021/07/23/gdc-2021-star-wars-galaxies-was-a-complex-game-of-corporate-greed-and-fan-love/)에 있다. **[2차]**

#### Kingdom Come: Deliverance (KCD / KCD2)
- **KCD 원작**: 전통적 XP가 없고 스킬은 사용으로 오른다. 예로 무기 사용은 해당 무기 숙련을, 약초 채집은 약초학을 올린다. 퀘스트 완료로는 XP를 주지 않는다. 출처는 [GamePressure 가이드](https://www.gamepressure.com/kingdom-come-deliverance/character-progression/z7a9f7)와 [GamerGuides 가이드](https://www.gamerguides.com/kingdom-come-deliverance/character-development/what-to-do-first/essential-skills)다. **[커뮤니티 가이드, 개발사 원문 아님]**
- **KCD2**: 스킬 XP는 능동적 사용에서만 쌓이고, 그 XP가 퍼크 포인트가 된다. 각 퍼크는 스킬 레벨 요구치가 있어 해당 스킬을 숙달해야 모든 퍼크를 열 수 있다. 출처는 [GamerGuides KCD2](https://gamerguides.com/kingdom-come-deliverance-ii/guide/getting-started/gameplay/earning-and-spending-perk-points)다. **[2차]**
- **개발사 근거 미확인**: XP 없는 설계를 Warhorse Studios가 어떤 이유로 택했는지 설명하는 인터뷰는 찾지 못했다. **[Gap]**

### Inferences
- **실패 연쇄 패턴**: UO의 기록은 "빈도 기반 성장 → 매크로 → 수작업 보정 → 보장 성장과 속도 제한 → 새로운 최적화" 순으로 진행됐다. 보정이 새 최적화 경로를 만드는 패턴이 반복된 것으로 보인다. 사례가 UO 중심이라 일반화에는 한계가 있다.
- **두 종류의 "레벨링 문제"를 구분해야 한다**: Oblivion의 악명 높은 문제는 (a) 스킬 기반 레벨업을 악용하는 효율적 레벨링과 (b) 적 스케일링(Nesmith 발언) 두 가지가 섞여 있다. 보고서에서 둘을 혼동하면 안 된다.
- **규칙이 공개되면 최적화 메타가 빨리 형성된다**: Oblivion의 속성 보너스 타이밍 규칙과 효율 표는 위키에 정리되어 있고, 그 자체가 최적화 압력의 증거다. UO의 8타일 실험도 같은 현상이다. 이는 두 사례에 기반한 추론이며 정량 검증은 없다.
- **EVE의 실시간 훈련은 행동 대신 시간을 보상하는 설계**로 읽을 수 있다. 이는 매크로와 AFK가 시간 기반 보상에서도 발생한다는 점과 함께 고려해야 한다. 추론이다.

### Gaps
- Morrowind, Daggerfall의 스킬 상승 규칙과 악용 사례를 조사하지 않았다.
- UO 팀 코멘트(2001-09-20) 원문이 403으로 열리지 않았다. GGS와 power hour의 정확한 공식과 정의를 확인하지 못했다.
- Koster 글은 약 186,740자 중 앞 100,000자만 요약됐다. 후반부의 결론을 확인하지 못했다.
- Bethesda가 메이저/마이너 구분을 없앤 이유에 대한 개발자 직접 인용을 찾지 못했다. Todd Howard, Bruce Nesmith의 원문 인터뷰가 필요하다.
- FFII 아군 공격 악용의 구체적 메커니즘과 개발진의 설계 의도를 확인하지 못했다.
- EVE의 CCP 2014 블로그 원문을 확인하지 못했다.
- SWG NGE 전환의 개발사 설명(이유)을 확인하지 못했다.
- Dungeon Siege, Quest 64, SaGa 시리즈, Kenshi, RuneScape, Project Zomboid, Mount & Blade, Dwarf Fortress adventure mode를 조사하지 않았다.

---

## 핵심 질문 2. 일반적 실패 모드와 원전 정식화는 무엇인가

### Takeaway
가장 자주 인용되는 정식화 "Given the opportunity, players will optimize the fun out of a game"은 Soren Johnson의 Game Developer 칼럼 "Water Finds a Crack"(2011)에서 나왔다. Koster의 2006년 글은 use-based 시스템의 빈도 불균형, 매크로, 점프 악용을 구체적으로 기록했다. 실패 모드 중 그라인드, 매크로/AFK, 최적화로 인한 재미 상실은 원전과 사례로 뒷받침된다. "캐릭터 정체성 상실"과 "해독 불가능한 진행"은 원전 정식화를 찾지 못했다.

### Cited Findings

#### 원전: Soren Johnson
- "Given the opportunity, players will optimize the fun out of a game." — Soren Johnson, "GD Column 17: Water Finds a Crack" (Game Developer 2011년 3월호로 명시; 웹 게재 2011-06-12). 출처는 [Designer Notes](https://www.designer-notes.com/?p=369)이다. **[문서, WebFetch 발췌]**
- 문맥: 칼럼은 "Many players cannot help approaching a game as an optimization puzzle."(많은 플레이어는 게임을 최적화 퍼즐로 접근하지 않을 수 없다) 뒤에 이 문장을 배치한다. 이어서 "Games, however, are so complex that it is difficult to anticipate exactly how players will optimize a game until after release"(게임은 너무 복잡해서 출시 후 플레이어가 어떻게 최적화할지 미리 예측하기 어렵다)라고 적고, "Often, designers don't even understand their own games until they finally see them in the wild."(디자이너는 게임이 실제로 풀리는 모습을 보기 전까지 자기 게임을 이해하지 못하는 경우가 많다)로 끝난다. **[문서, WebFetch 발췌]**
- 단일 지배 전략(dominant strategy)이 다른 플레이 방식을 밀어낸다고 경고한다. 과잉 교정, 즉 모든 익스플로잇을 제거하려는 시도도 경계한다. 판단 기준은 익스플로잇이 다른 플레이 스타일을 밀어내는지, 아니면 재미있는 대안을 주는지다. 검색 요약 기준이며 전문은 확인하지 못했다. **[2차]**
- Civ 3 사례: 세이브 파일에 랜덤 시드를 보존해 리로드해도 같은 전투 결과가 나오게 했다. 플레이어가 나쁜 전투 결과를 되돌리는 것을 막았다. 불만이 커지자 시드 보존은 게임 시작 시 고르는 옵션이 되었고, 기본값은 꺼짐이다. **[문서, WebFetch 발췌]**

#### 원전: Raph Koster (2006)
- 출처는 [Koster, "Use-based systems"](https://raphkoster.com/?p=592)이다. WebFetch 요약 기준 게시일은 2006년 7월 18일이다(페이지 헤더에는 2015년 6월 15일 업데이트 표시). **[2차]**
- "every skill was used at a different rate"를 첫 번째 주요 문제로 든다. 균일한 성장 확률에서는 자주 쓰는 전투 스킬이 훨씬 빨리 최대치에 도달한다. **[2차]**
- 빈도를 추적해 확률을 조정하자 성장이 지나치게 느려졌고, 매크로로 이어졌다. Koster는 "feedback loop broke"라고 썼다. **[2차]**
- 결론(요약 발췌): "practice itself isn't the problem"(연습 자체가 문제가 아니다)이며, 진짜 문제는 "practice without challenge or learning is boring"(도전과 배움이 없는 연습은 지루하다)이다. 또 "skills are enablers, and not as the point"(스킬은 수단이지 목적이 아니다)라고 말한다. **[2차]**
- 대안으로 "results-based" 성장을 제안하며, SWG의 제작 XP를 예로 든다. **[2차]**

#### 원전 그 외
- Oblivion 효율 표와 "필요 이상 훈련하지 말 것" 가이드는 최적화 행동이 위키 수준에서 정리되었음을 보여준다. [UESP](https://content1.uesp.net/wiki/Oblivion:Efficient_Leveling) **[문서(위키), 2차 확인]**
- EVE 실시간 훈련은 AFK 큐 우려에 대한 대응으로 설명된다. [Engadget](https://www.engadget.com/2009-02-04-long-awaited-skill-queue-coming-to-eve-online.html) **[2차]**
- Nesmith는 Skyrim 설계 방향을 설명하며 "less complexity"를 지지했다고 보도된다. [PC Gamer](https://www.pcgamer.com/games/the-elder-scrolls/bethesda-veteran-says-less-rpg-complexity-in-the-elder-scrolls-series-is-good-actually-we-got-rid-of-attributes-in-skyrim-and-you-know-who-complained-almost-nobody) **[2차, 헤드라인]**

#### 실패 모드 정리

| 실패 모드 | 사례 | 근거 등급 |
|---|---|---|
| 반복 그라인드(degenerate grinding) | UO 8타일 실험, 몬스터 가두기 매크로, Oblivion 점프, FFII 아군 공격 | Koster 글 [2차], UESP [2차], TV Tropes [커뮤니티] |
| 매크로/봇/AFK | UO 매크로(Koster [2차]), EVE AFK 큐 우려 [2차] | 2차 |
| 최적화로 재미 제거 | Soren Johnson 원문 [문서], Oblivion 효율 표 [2차] | 원문 있음 |
| 빈도 불균형 | UO 스킬 사용 빈도 차이(Koster) | 2차 |
| 맥락 없는 성장 | UO에서 다른 사람이 쓰는 것을 지켜보는 것으로도 성장, 난이도 등급 부재 | 2차 |
| 해독 불가능한 진행 | Oblivion의 속성 보너스 타이밍 규칙(10번째 상승 시 확정, 훈련 후 다음 레벨에 반영) | 위키 [문서], 해독 난이도는 추론 |
| 정체성 상실("모두가 같아짐") | 원전 정식화 미발견 | **[커뮤니티/Gap]** |
| 밸런스 | FFII Pixel Remaster의 성장 속도 최대 4배 옵션([Push Square](https://www.pushsquare.com/reviews/ps4/final-fantasy-ii-pixel-remaster)); 다만 밸런스 대응이라는 직접 근거는 없음. SWG는 밸런스 문제가 Combat Upgrade로 일부 다뤄졌다고 [Empire in Flames](https://www.empireinflames.com/?m=201504)가 전함 | 2차 |

### Inferences
- Koster의 진단은 use-based 실패를 "빈도"의 문제가 아니라 "행동의 의미"의 문제로 바꾼다. 행동마다 의미 있는 결과나 도전이 연결되지 않으면, 반복은 지루함으로 끝나거나 매크로로 대체된다. 인디 설계에서는 이 점이 가장 직접적인 시사점이다.
- Soren Johnson의 "optimize the fun out of" 명제는 익스플로잇 탐지보다 설계 단계에서의 "지배 전략" 점검이 중요하다는 뜻으로 읽힌다. 칼럼 자체가 이를 권고한다.
- 원전 정식화가 없는 "정체성 상실" 문제는 보고서에서 "커뮤니티 통념"으로 표기하는 것이 맞다. Skyrim의 메이저/마이너 제거는 "구분을 없애 선택의 의미를 줄였다"는 해석과 "선택을 퍽으로 옮겼다"는 설계자 설명이 함께 있어, 이 주장을 뒷받침하는 근거로도, 반박하는 근거로도 쓸 수 있다.

### Gaps
- "loss of character identity"와 "everyone becomes the same jack-of-all-trades"의 원전 정식화를 찾지 못했다.
- "unreadable progression"을 개발자가 문제로 지적한 원문을 찾지 못했다. 현재 근거는 위키 구조에 대한 추론이다.
- Koster 글 후반부(100,000자 이후)를 확인하지 못했다.
- Soren Johnson 칼럼의 전문과 익스플로잇 판단 기준의 세부는 검색 요약에만 의존한다.

---

## 핵심 질문 3. 성공 사례와 작동 요인은 무엇인가

### Takeaway
이번 조사에서 확인된 장치는 다섯 가지다. (1) 빈도 기반 확률을 고정 테이블이나 결과 기반 보상으로 옮긴 것, (2) 시간당 증가율 제한과 총합 상한, (3) 활동이 없을 때 최소 성장을 보장하는 GGS, (4) 퍼크를 스킬 숙달에 묶는 KCD2, (5) 행동 대신 시간을 보상하는 EVE의 실시간 훈련. 다만 이 중 어느 것이 플레이어 유지나 만족에 효과가 있었는지를 보여주는 정량 자료는 찾지 못했다. 대부분 설계자 주장이나 커뮤니티 평가다. 질문에 언급된 "rested/first-time 보너스"와 "learn from failure" 규칙은 이번 조사에서 확인하지 못했다.

### Cited Findings
- **UO 보장 성장(GGS)**: 성장이 없는 기간이 지속되면 최소 성장을 준다. 팀 코멘트 원문은 확인하지 못했고, 검색 요약은 이를 power hour 방식의 문제에 대한 대응으로 설명한다. [uo.com](https://uo.com/?p=6342) [2차, 원문 미확인]
- **UO 속도 제한**: 70 이상 스킬에 시간당 증가율 제한을 둔다(예: 70.0–79.9 구간에서 5분마다 0.1). 팬 문서 기준이다. [커뮤니티/팬 문서]
- **UO 총합 상한과 감쇠**: 총합 상한 700, 미사용 스킬 감쇠(Koster 글 요약). [2차]
- **SWG 결과 기반 성장**: 제작 XP를 다른 플레이어가 아이템을 사용할 때 지급하는 방식(Koster 요약). [2차]
- **SWG 교육 기능**: 다른 플레이어에게 배우는 기능이 있었으나 초기에 잘렸다. 이것은 성공 사례가 아니라 축소 사례다. [2차]
- **KCD2 퍼크 게이팅**: 퍼크가 스킬 레벨을 요구해 숙달을 강제한다. 원작은 능동적 사용에서만 XP를 얻는다. [2차 가이드]
- **EVE 실시간 훈련**: 시간 기반이며, 24시간 큐 제한은 나중에 해제됐다. 해제의 근거인 2014년 블로그 원문은 확인하지 못했다. [2차]
- **Skyrim의 방향**: 속성과 메이저/마이너 구분을 제거했고, Nesmith는 불만이 거의 없었다고 주장했다. 이는 설계자의 자기 평가이며 독립적 검증이 없다. [2차, 헤드라인]
- **Civ 3 시드 옵션화**: 리로드를 통한 결과 되돌리기를 막는 장치(시드 보존)가 플레이어 반발을 불러, 게임 시작 시 고르는 옵션(기본값 꺼짐)으로 바뀌었다. 익스플로잇 차단이 과하면 반발을 부른다는 사례로 읽을 수 있다. [문서]

### Inferences
- 확인된 성공 사례는 대부분 "행동 횟수"가 아니라 "행동의 결과, 난이도, 맥락"과 보상을 연결한다(KCD2의 능동적 사용, SWG의 결과 기반 성장, UO가 난이도 등급을 두지 않은 것의 문제점). 이는 Koster의 진단과 맞는다.
- 상한과 감쇠는 최적 빌드 문제를 다시 만든다. 따라서 상한은 단독으로 해법이 되기 어렵고, 다른 장치와 결합해야 한다. 추론이다.
- 현재 자료로는 어떤 장치가 "성공"했다고 객관적으로 말할 수 없다. 보고서에서는 "설계자 주장" 또는 "커뮤니티 평가"로 표기해야 한다.

### Gaps
- "rested/first-time 보너스"의 원문과 게임 사례를 찾지 못했다.
- "learn from failure" 규칙을 확인하지 못했다.
- 교사(teacher) 요구는 SWG 외에 확인하지 못했다.
- 플레이어 유지율, 만족도 등 정량적 성과 자료가 없다.

---

## 핵심 질문 4. 학술 또는 GDC 자료는 무엇이 있나

### Takeaway
이번 패스에서 확인한 학술 자료는 Mia Consalvo의 *Cheating: Gaining Advantage in Videogames*(MIT Press) 한 권이다. 이 책은 부정행위와 익스플로잇의 정의가 플레이어와 개발자 사이에서 협상된다고 본다. 사용 기반 성장, 그라인드 동기, GDC 강연에 대한 직접적 자료는 찾지 못했다.

### Cited Findings
- Mia Consalvo, *Cheating: Gaining Advantage in Videogames*, MIT Press, 240쪽, ISBN 9780262513289. 출판사 설명에 따르면 플레이 방식 선택과 플레이 제약 상황, 온라인 부정행위, 공략서와 하드웨어(Game Genie 등) 시장을 다룬다. 방법은 공략서와 하드웨어 분석, 플레이어 인터뷰, MMO 탐구다. 핵심 주장은 무엇이 공정한지를 플레이어와 개발자가 계속 협상한다는 것이다. "gaming capital" 개념을 도입한다. 출처는 [MIT Press Bookstore](https://mitpressbookstore.mit.edu/book/9780262513289)다. **[문서(출판사), 본문 미열람]**
- 출판 연도와 저자 소속은 판매처마다 다르다(2007, 2009, 2019 등). 2009년 페이퍼백이 현 판본으로 보이나 MIT Press 사이트에서 확인이 필요하다. **[출처 충돌]**
- 한 블로그 리뷰는 학문적 수준이 낮다고 평가했다. 자료 분석이 피상적이라는 지적이다. 출처는 [The Geek Anthropologist](https://thegeekanthropologist.com/2013/08/19/review-1-cheating-gaining-advantage-in-videogames/)다. **[커뮤니티 평가]**
- Soren Johnson의 칼럼은 학술 논문이 아니라 실무자 칼럼이다. 1차 출처이기는 하지만 학술적 근거로는 약하다. [Designer Notes](https://www.designer-notes.com/?p=369)

### Inferences
- Consalvo의 "부정행위의 정의는 협상된다"는 관점은 익스플로잇을 자동으로 나쁜 것으로 보지 않게 한다. 인디 개발자가 특정 반복 행동을 "버그"로 막을지 "창발적 플레이"로 둘지 판단하는 기준으로 쓸 수 있다. 추론이다.

### Gaps
- Nick Yee의 MMORPG 동기 연구(grinding 및 성취 동기)를 검색하지 않았다.
- Koster의 *A Theory of Fun*을 직접 확인하지 않았다. Soren Johnson 칼럼 에피그래프에서만 언급되는 것을 확인했다.
- GDC Vault 강연(use-based progression, degenerate gameplay 등)을 검색하지 않았다. 관련 강연 원문을 찾지 못했다.
- 사용 기반 성장을 직접 다룬 동료 심사 논문을 찾지 못했다.
- Consalvo의 책 본문은 열람하지 못했다. 내용은 출판사 설명에 기반한다.
