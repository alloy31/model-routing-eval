# 싼 반복과 숨은 규칙이 행동 성장 게임을 무너뜨렸다

행동이 곧 성장이 되고 AI가 이야기와 기술을 그 자리에서 만들어 주는 게임은 **테이블탑 RPG부터 2026년 생성형 AI 시제품까지** 여러 갈래에서 되풀이 시도됐다. 노트가 다룬 다섯 갈래를 모두 보면 **흥행과 지속에 성공한 사례는 손에 꼽고**, 그 성공도 대부분 개발사 발표나 소규모 평점에 기댄다. 실패의 뿌리는 세 가지로 모인다. 행동 횟수에 보상을 붙이면 가장 싸고 지루한 반복이 이기고, 성장 규칙이 풀리면 게임의 성격이 바뀌며, 말은 하지만 결과로 이어지지 않는 공백이 생긴다. 여기에 저작과 추론 비용, 응답 지연, "기술은 돌아가는데 재미는 없다"는 검증 실패가 겹쳤다. 살아남은 쪽은 범위를 좁히고, 한도와 대가를 두고, 플레이어의 과거를 되돌려 주고, 결과는 코드가 정했다. LIMEN 설계 3판은 깨달음을 중심에 두고, 익숙함을 따로 쌓고, 서기가 기록을 읽은 뒤 장을 쓰는 구조라서 앞선 실패의 상당수를 이미 피한다. 다만 무엇이든 말해 보는 열린 입력, 조건 목록을 채우는 실마리 규칙, 근거 없이 나오는 서기의 깨달음은 같은 함정으로 이어질 수 있으므로, 닫힌 어휘와 '결과가 달라졌을 때만 세기', '근거 기록 남기기'를 먼저 정해야 한다.

*표기: 원문을 직접 연 근거는 그대로 적었다. 검색 요약이나 2차 자료로만 본 내용은 **(요약 확인)**, 팬 위키의 작중 설정은 **(팬 위키)**로 표시했다. 판매량 같은 수치는 대부분 개발사 발표나 서드파티 추정이라서, 흥행 실패를 숫자로 입증하지는 못한다.*

## 같은 약속을 다섯 갈래가 다른 장치로 붙들었다

다섯 갈래의 약속은 한 문장으로 줄어든다. 플레이어가 한 행동이 곧 능력이 되고 이야기가 된다는 것이다. 설계자들은 이 약속을 저마다 다른 장치로 옮겼고, 장치마다 실패한 자리가 달랐다.

### 사용 기반 성장: 횟수를 세면 싼 행동이 이긴다

Ultima Online(1997)은 기술을 쓸 때마다 확률로 오르는 방식을 택했다. Raph Koster의 정의로는 "쓸 때마다 오를 기회가 있는" 시스템이었다([Koster, Use-based systems](https://www.raphkoster.com/?p=592), 원문 확인). 기술마다 쓰는 빈도가 달라서 빈도 표를 따로 두었지만, 플레이어는 **8×8 타일 단위로 난수가 바뀐다**는 점을 알아내 매크로를 돌렸다. Koster는 그때를 두고 "we were rolling dice to see when people were going to advance"라고 썼다. Morrowind에서는 벽에 몇 시간 부딪히기만 해도 Athletics가 올랐다([Johnson, Water Finds a Crack](https://www.designer-notes.com/?p=369), 원문 확인). Oblivion은 Major 기술을 올려 레벨을 맞추는 '효율 레벨링'을 낳았고, 설계자 Bruce Nesmith는 세계를 플레이어에 맞춰 강하게 만든 것을 "a mistake"라고 인정했다([VideoGamer](https://www.videogamer.com/news/elder-scrolls-iv-oblivion-levelling-system-mistake-admits-designer-haunts-remaster), 원문 확인). FF2에서는 아군을 때려 깨우는 행동이 성장 경로가 됐고, 설계자 Kawazu는 "I had no idea people would use it to essentially grind levels"라고 답했다([Retronauts](https://retronauts.com/article/670/akitoshi-kawazu-on-the-reasoning-behind-sagas-insanity), 원문 확인). SWG의 제다이는 조건을 숨긴 행동 목록이었다. 힌트 아이템 홀로크론이 풀리자 플레이어는 A부터 전부 배웠고, Koster는 작동 방식을 아무도 모를 때 잘 돌던 시스템이었다고 평했다([A Jedi Saga](https://www.gamedeveloper.com/design/a-jedi-saga), 원문 확인). 살아남은 쪽은 한도를 걸었다. Bannerlord는 포커스를 한 번 넣으면 되돌릴 수 없게 했고(요약 확인), Kenshi는 약한 상대에게서 XP를 거의 주지 않는다(요약 확인). 공통점은 보상이 '행동의 횟수'에 붙었다는 것이다. 횟수는 가장 싼 행동으로 채워진다.

### 창발 서사: 세계는 깊었지만 플레이어는 그 깊이를 못 봤다

Façade는 대화형 드라마를 '비트'와 대사 묶음으로 짰다. **20분짜리 경험에 저작만 약 3인년**이 들었고, 제작자들은 전역 주체성이 결국 비트 27개에 묶여 처음 바랐던 것보다 훨씬 낮았다고 적었다([Mateas & Stern, Writing Façade](https://electronicbookreview.com/essay/writing-facade-a-case-study-in-procedural-authorship/), 원문 확인). Versu는 드라마 매니저 없이 캐릭터가 욕구 점수로 스스로 행동을 고르는 구조였는데, 욕구가 300개를 넘자 가중치를 맞추는 일이 "difficult and unrewarding problem"이 됐다([Evans & Short, 2014](https://www.cs.uky.edu/~sgware/reading/papers/evans2014versu.pdf), 원문 확인). Linden Lab은 2014년 이 프로젝트를 정리했다([Short](https://emshort.blog/2014/02/20/post-linden), 원문 확인). Storybricks는 EverQuest Next의 AI를 맡았다가 2015년 문을 닫았고, 창업자는 자기들이 게임 업계에는 기술 회사 같고 기술 업계에는 게임 회사 같았다고 말했다([TechCrunch](https://techcrunch.com/2015/03/08/game-over/), 원문 확인). Daybreak는 2016년 이 게임을 접으며 "it wasn't fun"이라고 했다([EQ2Wire](https://eq2wire.com/?p=23305), 원문 확인). 반면 Nemesis는 죽음이라는 한 종류의 순간만 붙잡고 나머지 연결은 플레이어가 채우게 했다. 모든 경우를 채우려 했다면 "so explosively complex that you couldn't make it"이 됐을 것이라고 개발자는 말했다([GamesBeat](https://gamesbeat.com/shadow-of-mordors-nemesis-system-draws-from-burnout-football-and-an-architecture-book/), 원문 확인). Left 4 Dead는 생존자의 감정 강도라는 숫자 하나로 위협의 양만 조절했다([Booth, Valve](https://cdn.fastly.steamstatic.com/apps/valve/2009/ai_systems_of_l4d_mike_booth.pdf), 원문 확인). 시뮬레이션 쪽 교훈은 Tynan Sylvester가 정리했다. 그는 게임의 흥미로운 것들이 실리콘 속에 갇혀 사람의 이해에 닿지 않는다고 썼다([The Simulation Dream](https://tynansylvester.com/2013/06/the-simulation-dream/), 원문 확인).

### 생성형 AI 게임: 화제는 컸고 지속 수익은 드물었다

AI Dungeon은 2019년 GPT-2 실험에서 출발했고, 정점에는 OpenAI와 AWS에 **월 20만 달러 가까이** 쓴 것으로 추정된다([CNBC](https://www.cnbc.com/2023/03/13/chatgpt-and-generative-ai-are-booming-but-at-a-very-expensive-price), 원문 확인, 추정치). 플레이 시간이 곧 비용이었다. 후속작 Voyage는 5년을 들여 **LLM이 서술하는 이야기 밑에 스탯, 판정, 지속 상태를 쌓는 방식**으로 2026년에 나왔다([TechCrunch](https://techcrunch.com/2026/04/21/voyage-is-an-ai-rpg-platform-for-creating-custom-gaming-worlds-with-ai-generated-npc-interactions/), 원문 확인). Death by AI는 출시 3일 만에 일일 이용자 70만을 찍었지만, 매 라운드를 새로 생성해서 캐싱도 못 했고 CEO는 "After three days we were freaking out"이라고 말했다([Inworld 블로그](https://inworld.ai/blog/how-inworld-helped-the-ai-game-death-by-ai-with-20-million-players-reach-profitability), 벤더 글). 판매에서는 격차가 컸다. Suck Up!은 영상 조회가 수억 회였지만 Steam 판매는 서드파티 추정으로 수천 장 수준이다(요약 확인). Vaudeville은 대형 스트리머 방송 뒤에도 약 7,500장에 그쳤다([Game Developer 보도자료](https://www.gamedeveloper.com/press-release/vaudeville-a-pre-mortem), 원문 확인). Covert Protocol은 "Every object is potentially a topic"이라는 말처럼 대화 범위가 끝이 없어서, 기존 게임보다 플레이테스트가 더 들었다([Aftermath](https://aftermath.site/ai-npcs-nvidia-unity-ubisoft-convai-inworld.md), 원문 확인). 가장 오래 간 Infinite Craft는 입력을 **두 원소와 결과 한 쌍**으로 극단적으로 줄이고, 생성 결과를 저장해 모든 플레이어에게 같은 답을 줬다. 하루 3억 개가 넘는 레시피가 생겼지만 제작자는 재정 회복이 불가능할 것이라고 썼다([Wikipedia](https://en.wikipedia.org/wiki/Infinite_Craft)). 화제를 만드는 힘과 돈을 버는 힘이 따로 움직였다는 뜻이다.

### 능력 제작과 수련: 조합은 살아남았고 깨달음은 숫자로 남았다

Breath of the Wild의 설계팀은 불, 물, 얼음 같은 원소와 나무, 바위 같은 고체 사이의 규칙을 **세 줄로 고정**하고, 그 위에 퍼즐을 곱해 세웠다([Thumbsticks](https://www.thumbsticks.com/gdc-17-breath-of-the-wild-science-lies), 원문 확인). 소수의 규칙이 많은 상황에 곱해지는 구조가 조합형 능력 게임의 기본 틀이 됐다. Mystralia의 Borealys는 주문을 노드 흐름으로 짜게 했다가 "way too complex"라는 이유로 버렸고, 행동 룬으로 줄이자 "dumbed down to a customization system"이 됐다. 네 번째 설계에서 **템플릿과 트리거(주문이 다른 주문을 부르는 구조)**에 이르렀고, 행동 룬은 20개에서 11개로 줄었다([Mondou, Game Developer](https://gamedeveloper.com/design/creative-process-of-a-procedural-spell-crafting-system), 원문 확인). 수련 게임 쪽은 더 단순했다. 조사한 중국어권 수선·무협 게임에서 깨달음(悟性)은 대부분 **학습 속도와 성공률을 바꾸는 숫자**였고, 돌파는 재료와 확률 격자로 처리됐다. 太吾绘卷은 칸마다 성공률이 90%여도 25칸을 모두 통과할 확률이 7%라는 커뮤니티 계산이 있다(요약 확인). 플레이어 행동이 직접 깨달음을 여는 사례는 SaGa의 전투 중 '인스피레이션'과 Where Winds Meet의 기술 훔치기 정도였고, 후자도 장소와 대상이 미리 정해진 스크립트 이벤트였다([AllThings.How](https://allthings.how/where-winds-meet-skill-theft-how-to-steal-skills-and-unlock-martial-arts/), 원문 확인). LLM으로 능력을 만든 2025~2026년 연구는 한결같이 **유효성은 올라가는데 재미는 재지 않았다**. Latent Space는 LLM이 전용 형식의 데이터만 쓰게 하고 실패하면 무해한 "fizzle"로 돌렸다([Drake & Dong](https://arxiv.org/html/2510.16952v1), 원문 확인). Neural Spore Genesis는 같은 입력에 대한 다양성이 규칙 기반 생성기는 0, LLM은 0.43 남짓이었지만, 형태와 행동의 일치는 LLM이 0.42~0.55로 규칙 기반의 1.0보다 낮았다([Xu & Verbrugge](https://www.pcgworkshop.com/archive/xu2026infinite.pdf), 원문 확인). GAVEL은 진화시킨 185개 변형 가운데 130개가 플레이 가능했지만, 저자들은 생성한 규칙이 실제 플레이에서 **쓰이지 않는** 실패가 흔하다고 적었다([Todd et al.](https://arxiv.org/html/2407.09388v1), 원문 확인).

### 가상현실 소설: 욕망은 같았고 구현은 장면만 옮겼다

소설은 이 판타지를 훨씬 자주 상상했다. 달빛조각사는 튜토리얼 4주 동안 허수아비만 치며 힘과 민첩을 올리고, 조건을 채우면 열리는 히든 직업에 이른다(**팬 위키**). SAO는 Cardinal이라는 AI가 세계를 운영하고, Unique Skill을 **반응 속도 1위 한 명**에게 준다(**팬 위키**). Bofuri는 "한 시간 동안 무피해로 공격 받기" 같은 맥락 조건을 쓰고, 운영진은 악용 뒤 특정 스킬을 하루 10회로 제한한다(**팬 위키**). Infinite Dendrogram은 주인의 행동 패턴을 관찰해 알을 부화시키고, Shangri-La Frontier는 NPC가 자질을 인정해야 열리는 시나리오를 둔다(**팬 위키**). 같은 욕망을 장치로 줄인 것이다.

현실에서 옮긴 시도는 대개 장면만 옮겼다. 달빛조각사 모바일은 사전 예약 320만 명을 모았지만(요약 확인), 출시 11일 뒤 구글플레이 평점이 5점 만점에 1.8점이었다([시사저널e](https://www.sisajournal-e.com/news/articleView.html?idxno=207392), 원문 확인). SAO 게임들은 MMO처럼 보이는 싱글 RPG에 머물렀고, Fractured Daydream은 출시 주말 동접 12,290명이 한 달 뒤 하루 약 2,000명으로 떨어졌다([Final Weapon](https://finalweapon.net/2024/11/01/sword-art-online-fractured-daydream-review-a-fractured-love-letter), 원문 확인). '살아 있는 세계'를 내건 서구 MMO는 더 크게 무너졌다. Chronicles of Elyria는 위키백과 기준 2026년 10월 스튜디오 폐쇄가 발표됐다([Wikipedia](https://en.wikipedia.org/wiki/Chronicles_of_Elyria)). 2026년 7월에는 송재경이 AI의 도움으로 혼자 MMO를 만들었다고 밝혔는데, 그 안의 경비병 NPC는 토큰 비용을 묻자 "I am a guard, the token cost is none of my business"라고 답했다([Inven Global](https://www.invenglobal.com/articles/24233/song-jae-kyung-and-ai-in-gaming), 원문 확인). 학술 쪽은 이 욕망을 노력이 가장 중심적인 동력이 되는 '공정한 사회'에 대한 판타지로 읽는다([이융희, 2021](https://www.jkfr.co.kr/xml/28650/28650.pdf), 원문 확인).

## 실패가 되풀이된 다섯 자리

갈래는 달라도 실패가 놓인 자리는 다섯 곳으로 모인다. 아래는 설계자 발언이나 사후 보고로 확인된 사례를 중심으로 본 것이다.

첫째, 행동 횟수에 보상이 붙으면 가장 싼 행동이 이긴다. Johnson은 플레이어가 자기 시간을 안전과 맞바꾸며, 반복 숙련 시스템은 그 틈을 그대로 파고든다고 썼다. Koster는 Oblivion에 언덕에서 뛰어내리는 것만큼 도전이 없는 행동이 있어서 그라인드가 고개를 든다고 봤다([Koster, Use-based systems](https://www.raphkoster.com/?p=592), 원문 확인). 여기서 두 번째 결과가 나온다. 모두가 가장 싼 경로에 모여 같은 빌드가 된다. UO의 tank-mage가 그랬고, FF2 설계자 Kawazu도 육성 끝에 캐릭터들이 서로 복제품이 되는 문제를 의식했다([Retronauts](https://retronauts.com/article/670/akitoshi-kawazu-on-the-reasoning-behind-sagas-insanity), 원문 확인).

둘째, 규칙이 풀리면 게임이 다른 게임이 된다. UO의 8×8 매크로가 그랬고, Koster는 플레이어가 세계의 모든 공식과 알고리즘을 실험으로 풀어낸다는 법칙을 남겼다([Koster, Laws](https://www.raphkoster.com/games/laws-of-online-world-design/the-laws-of-online-world-design/), 원문 확인). SWG 제다이의 숨은 조건과 Bofuri의 Devour 제한도 같은 구조다. 숨은 규칙은 설계자 자신에게도 흐릿했다는 점이 중요하다. 뒤에서 보겠지만, LIMEN의 서기가 깨달음을 고르는 방식도 같은 종류의 흐릿함을 가진다.

셋째, 말은 하는데 결과가 따라오지 않는다. Smallville의 에이전트는 지식을 윤색하는 환각을 보였고 지나치게 협조적이었으며, 25명을 이틀치 돌리는 데 수천 달러의 토큰이 들었다([ar5iv, Park et al.](https://ar5iv.labs.arxiv.org/html/2304.03442), 원문 확인). Convai 데모에서 보안 로봇 NPC는 따라가겠다고 답하고 제자리에 서 있었다([Aftermath](https://aftermath.site/ai-npcs-nvidia-unity-ubisoft-convai-inworld.md), 원문 확인). 장식용 생성물은 플레이어가 눈치채는 순간 무시된다는 것이 Emily Short의 2016년 정리다([Short](https://emshort.blog/2016/09/21/bowls-of-oatmeal-and-text-generation/), 원문 확인). 같은 모양의 결과가 이름만 바꿔 나오는 '오트밀 문제'도 여기에 속한다.

넷째, 비용이 플레이 시간과 선택지 수에 비례해 늘어난다. Riedl & Bulitko는 분기형 서사의 저작량이 선택 지점 수에 따라 지수적으로 늘 수 있다고 정리했고([Riedl & Bulitko](https://cs.uky.edu/~sgware/reading/papers/riedl2013interactive.pdf), 원문 확인), Watch Dogs: Legion은 대사 한 줄마다 20개 변형을 만들어 녹음해야 했다([Ubisoft News](https://news.ubisoft.com/en-us/article/7b1jdUkg7ctAgg2NqW4tsy/how-watch-dogs-legion-told-a-story-without-a-main-character), 원문 확인). 응답 지연도 문제다. Mantella 문서는 0.5초 미만을 목표로 권하지만, 저사양 로컬 환경에서 45초가 걸렸다는 이용자 보고도 있다(이용자 보고, 요약 확인).

다섯째, 기술이 돌아가는 것과 재미있는 것을 가르지 못했다. Togelius는 LLM이 전형적인 게임은 한 번의 프롬프트로 만들어도 "the LLM can't play it"이라서 좋은 게임을 만들지 못한다고 말했다([IEEE Spectrum](https://spectrum.ieee.org/ai-video-games-llms-togelius), 원문 확인). Watch Dogs: Legion 개발진은 생성 캐릭터에 과거가 없으니 금붕어처럼 지금만 산다고 보아야 한다고 말했다(["we have to assume the characters are goldfish, because they only live in the moment"](https://news.ubisoft.com/en-us/article/7b1jdUkg7ctAgg2NqW4tsy/how-watch-dogs-legion-told-a-story-without-a-main-character), 원문 확인). 약속이 구현보다 컸던 경우도 많다. Fable은 출시 전에 말한 나무 성장과 자녀 기능이 빠진 것을 사과했고([Kotaku](https://kotaku.com/the-man-who-promised-too-much-1537352493), 원문 확인), Spore 개발진은 "다섯 개의 게임을 한꺼번에" 만들다가 뒤늦게 플레이 가능해졌다([Johnson, Spore](https://www.designer-notes.com/?p=654), 원문 확인). 이 다섯 자리의 공통점은 기술이 모자라서가 아니라 **무엇을 세고, 무엇을 보여 주고, 무엇을 약속하는지**를 잘못 정했다는 데 있다.

## 드물게 살아남은 쪽이 좁힌 것

살아남은 사례는 대부분 시스템이 맡는 일을 줄였다. Nemesis는 한 종류의 순간만, L4D는 숫자 하나만 다뤘다. Wildermyth는 "어떤 사건에 누구를 배역할지"만 절차로 맡기고 사건 자체는 작가가 쓴 연극으로 두었다. 개발자는 무작위 장애물은 쉽게 던질 수 있어도 그것에 넓은 의미를 주기는 어렵다고 말했다([Turn Based Lovers](https://turnbasedlovers.com/10-turns-interview/with-wildermyth-developer), 원문 확인). Caves of Qud는 생성기를 핵심 진행에서 떨어진 '부차 시스템'으로 두어 실패가 본 게임을 망치지 않게 했다([Grinblat & Bucklew](https://pcgworkshop.com/archive/grinblat2017subverting.pdf), 원문 확인).

둘째, 총량을 두고 대가를 걸었다. UO의 총합 700점 상한은 한 기술을 포기해야 다른 기술을 배우는 구조였다(Koster, 원문 확인). Sekiro는 적의 자세가 시간이 지나면 회복되게 해서 치고 빠지기와 거북이 전략을 함께 막았다([Xbox Wire](https://news.xbox.com/en-us/?p=112348), 원문 확인). 대가는 생존 쪽에도 있었다. 太吾绘卷은 안전 횟수를 넘기면 내상이 쌓인다. 대가가 있으니 실패가 드라마가 된다.

셋째, 플레이어가 한 일을 나중에 되돌려 준다. Nemesis의 살아남은 적은 '되돌아오는 악당'으로 다시 나타나서 플레이어에게 감정을 남긴다. 노트의 추론에 따르면 이 감정은 기억의 양보다 **알아볼 수 있는 구체적인 콜백 하나**에서 나온다. Watch Dogs: Legion이 약했던 이유가 과거 없는 캐릭터였다는 점과 정확히 맞물린다.

넷째, 결과는 코드가 정했다. Voyage는 판정과 상태를 규칙 시스템에 두었고, Latent Space와 Neural Spore는 LLM이 닫힌 형식 안에서만 고르게 했다. Bitpart는 LLM으로 상호작용을 설계 시점에 대량으로 만든 뒤 사람이 골라 '레고 블록'으로 쓰는 방식을 택했다([MIT Technology Review](https://www.technologyreview.com/2024/06/20/1093428/generative-ai-reinventing-video-games-immersive-npcs/), 원문 확인). 조사한 사례들은 LLM을 설계자 대신 판정자로 세우지 않았다.

이 절의 '성공' 판정은 개발자 발언과 평론의 반복 인용에 기댄다. 판매량, 유지율, 수상을 1차 자료로 확보한 사례는 드물다. Nemesis가 플레이어의 기억에 실제로 어떤 효과를 냈는지 측정한 연구는 찾지 못했다. Kenshi와 Skyrim이 호평받는 이유를 개발자 발언으로 직접 확인하지도 못했다. EverQuest Next 취소가 AI 때문이었는지 내부 증언도 없다. 생성 능력의 밸런스를 실험으로 잰 논문도 찾지 못했다. 반대로 '행동 → 깨달음 문장 → 규칙'의 고리를 가진 상용 게임은 이번 조사 범위에서 찾지 못했다. 찾지 못한 것이지 없다는 증거는 아니다.

## LIMEN 설계가 이미 피하는 실패

설계 3판은 앞선 실패를 의식하고 짠 흔적이 뚜렷하다. 먼저 싼 반복을 막는 구조다. [설계 3판 4.1절](limen/docs/design-v3.md)은 "같은 일을 백 번 하면 손에 익을 뿐"이라고 하고, 새 실마리는 **다른 조건**에서 나온다고 정했다. [4.5절](limen/docs/design-v3.md)은 익숙함을 따로 두어 되풀이가 헛되지 않게 하면서도 "새로운 것은 열리지 않는다"고 선을 그었다. Morrowind의 벽 달리기가 깨달음으로 바뀌지 않는다는 뜻이다. [4.4절](limen/docs/design-v3.md)의 "숫자를 앞세우지 않는다"도 UO에서 확률 굴림을 쫓던 구조를 피하려는 장치로 읽힌다.

둘째, 설계는 세계를 세지 않고 기록한다. [0단계](limen/docs/design-v3.md)의 사건 기록은 놀이 시간, 장소, 비, 밤, 몸 상태, 도구, 대상을 함께 남긴다. 세계 사전은 없는 이름이 나오면 가까운 이름을 돌려준다. 기억이 LLM의 문맥이 아니라 저장된 데이터에 있으므로, 모델이 사건을 잊거나 윤색하는 문제를 덜 겪는다. [8절](limen/docs/design-v3.md)의 세계 사전("여기 있는 것만 말한다")과 [13절](limen/docs/design-v3.md)의 목표("서기가 없는 것을 지어내지 않는다")는 Smallville식 윤색과 '금붕어 캐릭터'를 피하려는 장치다.

셋째, 서기는 사후에 장을 쓴다. 서기는 플레이 도중 상황을 바꾸지 않고 기록을 읽은 뒤 장을 쓴다. Ryan의 박사논문을 Emily Short가 요약한 글에 따르면, 외부 관리자가 시뮬레이션을 조정하면 사건은 실제로 일어난 것이 아니게 되고 실제로 일어난 것처럼 느껴지지도 않게 된다([Short, Ryan 요약](https://emshort.blog/2019/05/23/curating-simulated-storyworlds-james-ryan-2/), 원문 확인). 이 설계는 Façade와 Versu처럼 실시간으로 극적 흐름을 맞추느라 드는 저작과 조율 비용을 피한다. 다만 선별이 부실하면 밋밋한 산문이 나온다는 큐레이션의 고통은 그대로 남는다.

넷째, 능력은 문법을 쓰고 효과는 엔진이 낸다. [5절](limen/docs/design-v3.md)의 기본기 목록, "열린 기본기만 쓸 수 있다", "효과의 크기는 쓴 힘에서 나온다"는 Mystralia가 템플릿과 트리거로 찾은 중간 지점과 같고, Latent Space와 Neural Spore의 "의미는 LLM, 실행은 닫힌 형식" 구조와도 같다. 익숙함이 모자라면 "흔들린 채로 나간다"는 실패를 글이 아니라 화면에서 보여 주는 점도 Kenshi와 Sekiro가 쓴 대가 장치를 떠올리게 한다.

다섯째, 세계 이치를 작게 깔았다. [2절](limen/docs/design-v3.md)은 2판이 물리 계산 중심이라 "모래 놀이터가 되고 이야기가 묻힐 위험"이 있었다고 스스로 짚었고, [9절](limen/docs/design-v3.md)은 열·물기·바람·빛 네 가지만 주변에 깐다. Noita 개발진이 시뮬레이션이 재미있는 플레이를 가로막을 수 있다고 말한 것, RimWorld가 필요한 최소 표현만 쓴 것과 맞는 방향이다. [6절](limen/docs/design-v3.md)의 "몸 안 보기"도 내부 상태를 게이지가 아니라 살필 대상으로 만든다. 노트의 추론으로는 자각을 높이는 쪽에 가깝다.

여섯째, 단계마다 통과 기준이 있다. [11절](limen/docs/design-v3.md)의 자동 시험, 화면 시험, 직접 해 보기는 재미없는 게임이 개발 끝에야 드러나는 실패를 막는 장치다. 응답 지연 3~12초는 물음을 미리 지어 두었다가 쉬는 순간에 건네는 방식으로 흡수했다([8절](limen/docs/design-v3.md)). 설계 시점에 후보를 많이 만들고 사람이 고르는 Orkin의 방식과 방향이 같다.

일곱째, 말투를 신경 썼다. [14절](limen/docs/design-v3.md)은 번역투와 한자어 겹침을 걷어 내겠다고 했다. Crawford는 동격을 쌓는 기계적인 문장을 사람들이 금방 알아본다고 썼다([Crawford](https://erasmatazz.com/library/interactive-storytelling/negative-lessons-from-story.html), 원문 확인). 글투는 작은 부분 같지만, 서기 글에서 'AI 냄새'가 나면 세계 전체의 믿음이 깨진다.

## 같은 함정이 남은 자리와 먼저 정할 것

아래 표의 아홉 자리는 설계에 이미 있는 장치가 선행 실패를 되풀이할 수 있는 곳이다.

| 설계 부분 | 같은 함정의 근거 | 바꾸거나 정할 것 |
|---|---|---|
| 7절 "무엇이든 해 보기"(말이나 글로 행동 선언) | Storytron, Judas, Covert Protocol | 기본기와 대상 사전 안에서 고르게 하고, 화면에 "이렇게 알아들었다"를 먼저 보여 준다 |
| 4.1절 실마리(조건 축 8개) | UO 매크로, Bofuri의 횟수 제한 | 결과가 기대와 달랐을 때만 칸을 채운다. 같은 조건 반복은 익숙함으로만 쌓는다 |
| 4.4절 서기가 "그냥 주기" | UO의 주사위, Smallville의 과잉 협조 | 깨달음마다 근거 기록을 붙이고, 장마다 상한을 두며, '없음'도 정상 결과로 둔다 |
| 4.3절 문장이 곧 규칙 | GAVEL의 쓰이지 않는 규칙 | 문장은 엔진 효과 목록의 항목과 짝을 짓고, 짝이 없으면 꾸밈으로만 쓴다 |
| 4.5절 익숙함 | Morrowind 벽 달리기 | 상한과 체감 감소를 정하고, 익숙함은 눈금으로 보여 준다. 숫자 금지는 깨달음에만 적용한다 |
| 6절 기운이 실리는 자리 | Skyrim의 만능화(커뮤니티 통념), UO의 tank-mage | 기운 총량을 정하고, 한 자리에 실린 만큼 다른 자리에서 빠지게 한다 |
| 8절 장(章) 쓰기 | Qud가 부차 시스템이어야 했던 조건 | 장 속 이름, 장소, 횟수를 기록과 자동 대조하고, 어긋나면 그 장을 다시 쓴다 |
| 5절 기술 이름과 설명 | GAVEL, ScriptDoctor, 오트밀 문제 | 설명은 효과 조합에서 템플릿으로 만들고, 서기는 이름과 말투만 맡는다. 같은 효과의 중복은 거른다 |
| 11절과 단계 0~7 | Spore의 "다섯 개 게임", Fable의 약속 | 1단계와 2단계를 한 길로 끝까지 완성하는 것을 첫 목표로 하고, 컷라인 밖 항목을 적어 둔다 |

가장 큰 위험은 열린 입력이다. 설계는 "무엇이든 해 보기"를 핵심 조작으로 두었는데, Crawford가 동사의 그물은 대부분의 사람에게 너무 엉켜 있다고 쓴 바로 그 지점이다([Crawford, Negative Lessons](https://erasmatazz.com/library/interactive-storytelling/negative-lessons-from-story.html), 원문 확인). Judas를 만든 Ken Levine도 플레이어가 할 수 있는 모든 일을 생각하고 캐릭터별 반응을 따로 써야 해서 엄청난 작업이라고 말했다(2차 보도, 요약 확인). 열린 입력을 유지하려면 서기가 기본기와 대상 사전 안에서 가장 가까운 것을 고르고, 그 해석을 화면에 먼저 보여 준 뒤 실행하는 편이 낫다. 목록에 없는 말은 실패가 아니라 "아직 모르는 말"이라는 힌트로 처리한다. Latent Space가 쓴 무해한 fizzle과 같은 방식이다.

실마리 규칙은 설계의 본질이라 고치기 어렵다. 그래도 '같은 주제에서 조건을 바꿔 봤다'는 사실만으로 칸을 채우면, 플레이어는 조건 축을 하나씩 돌려 보는 체크리스트로 바꿔 버린다. Johnson이 말한 좋은 결정, 곧 어떤 상황에서는 맞고 다른 상황에서는 틀린 결정이 되려면 칸은 **결과가 기대와 달랐을 때만** 채워야 한다. 목록에는 해 본 것만 적고, 아직 안 해 본 조건은 암시하지 않는다.

서기의 '그냥 주는 깨달음'은 가장 조심해야 한다. 기록 몇 건을 근거로 삼았는지 남기지 않으면, 플레이어에게는 주사위와 다를 게 없다. 설계는 4.4절에서 "무엇을 언제 깨닫는지는 서기의 눈에 맡긴다"고 적었는데, 엔진이 지키는 것이 효과의 크기뿐이라면 이 부분이 UO의 주사위 굴림과 같아진다. 근거 번호를 붙이고, 장마다 상한을 두고, 같은 기록을 여러 번 넣어 보는 재생 시험으로 '서기가 늘 예스라고 하는지'를 재야 한다. 깨달음 책에 근거를 적는다는 설계는 그대로 살리되, 그냥 준 깨달음에도 적용한다.

익숙함과 기운의 자리도 정해야 한다. 익숙함에 상한이 없으면 Morrowind의 벽 달리기가 '안전한 성장'으로 남는다. 상한을 두고 체감이 줄어드는 곡선을 정하면 된다. 또 익숙함은 보이게, 깨달음은 숨기는 두 층으로 나누면 달빛조각사가 쓴 구조와 같아진다. 스탯은 예측 가능하고 히든은 예측 불가능하다. 기운은 총량을 정하고 팔, 다리, 눈, 배에 실린 만큼 다른 데서 빠지게 해야 한다. 한 깨달음이 기본기, 몸, 기술을 한꺼번에 열면 모든 플레이어가 같은 자리에 모이는 것을 막기 어렵다.

세계 이치와 장의 연결도 약하다. Sylvester가 말한 대로 게임의 값은 플레이어 머릿속에 그려지는 모델에 있다. 성공이나 실패마다 엔진이 "빗속이라 불이 약해졌다"처럼 한 줄 이유를 찍게 하면, LLM이 틀리더라도 원인이 흐려지지 않는다. 장에 나오는 이름과 횟수도 기록과 자동으로 맞춰 보고, 어긋나면 다시 쓴다. Qud의 방식이 통한 조건은 이야기가 부차 시스템이었기 때문이다. LIMEN에서는 장이 곧 진행이라서 그 조건을 그대로 빌릴 수 없다.

범위와 공급이 실제 성패를 가를 것이다. 8단계, 4길, 말로 하는 조작, 겉모습, 부적, '세계가 알아본다'를 한꺼번에 가면 Spore가 되풀이된다. 1단계와 2단계를 한 길로 끝까지 완성하는 것을 첫 목표로 두고, 나머지는 통과 뒤에 여는 편이 낫다. 음성도 "말로도 된다"로 두고 모든 동작에 키보드와 클릭 대체를 남긴다. 한국어 음성 인식의 실제 정확도는 노트에서 확인하지 못했다. 'Whispers from the Star'의 리뷰가 음성 인식을 약점으로 꼽았다는 요약이 있을 뿐이다(요약 확인). "이 컴퓨터의 Claude만 쓴다"는 개발 단계에서는 맞는 결정이지만, 공개 전에는 플레이어가 자기 키를 넣는 방식, 로컬 소형 모델, 규칙 서기만 쓰는 방식 가운데 무엇인지 정해야 한다. 어느 쪽이든 서기 없이도 1단계를 끝까지 깰 수 있어야 한다. 비용은 플레이 시간에 비례하므로, AI Dungeon과 Death by AI가 겪은 것처럼 호출 상한을 미리 적어 둔다.

마지막으로 재미를 재는 사람이 한 명이라는 문제다. Baba Is You의 개발자는 혼자 설계하면 난이도에 눈이 멀기 쉽다고 말했고 베타 테스터로 보정했다([Red Bull](https://www.redbull.com/ng-en/baba-is-you-interview), 요약 확인). 2단계 전에 외부 테스터 두세 명을 붙이고, 통과 기준을 미리 적어 두는 것이 좋다. 예를 들면 "물음을 받은 뒤 다르게 해 보겠다는 말이 절반을 넘는가" 같은 기준이다. 홍보 문구도 '가상현실처럼'은 실제로 구현된 것으로 좁히는 편이 안전하다. 노트에서 본 SAO류 게임은 "내 캐릭터가 세계에 산다"는 약속에 비해 주인공의 주체성이 빈약하다는 비평을 계속 들었다(요약 확인).

## 결론: 서기는 기록을 읽는 자리에 둬야 한다

노트를 모두 읽고 나면 LLM이 제 몫을 할 자리가 분명해진다. 이 갈래들에서 LLM이 잘한 일은 짧고 닫힌 판정, 저장된 기록을 읽고 말로 옮기는 일, 설계 시점에 후보를 많이 만드는 일이었다. 규칙을 세우고 판정을 맡기면 반복해서 실패했다. LIMEN 설계는 이 구분을 대체로 따른다. 서기는 기록을 읽고 장을 쓰고 물음을 건네고, 효과와 판정은 엔진이 맡는다. 다만 가장 큰 질문은 설계 문서가 아니라 플레이어의 경험에 있다. 노트에서 찾은 어떤 프로젝트도 '같은 일을 다른 조건에서 해 보는 것'이 깨달음 문장으로 이어지고, 그것이 재미있는 탐구로 느껴지는지를 재지 않았다. 이 질문은 기술 시연으로는 답이 나오지 않는다.

그러므로 다음 한 걸음은 작고 시험 가능해야 한다. 한 길, 세 가지 조건, 닫힌 어휘, 결과가 달라졌을 때만 세는 실마리 규칙을 먼저 넣고, 테스터가 규칙을 스스로 추리했는지와 다음 조건을 스스로 고르려 했는지를 기록한다. 이 노트가 확인하지 못한 것은 판매와 유지율, 생성 능력의 밸런스, 한국어 음성 인식, 그리고 깨달음 고리가 실제로 재미있는지다. 네 가지 모두 LIMEN에서 가장 큰 불확실성이고, 기술을 더 쌓기 전에 먼저 답해야 할 질문이다.
