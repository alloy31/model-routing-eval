"""웹 조사 노트의 자동 지표: 지시문이 요구한 항목의 포함 여부, 출처 수·종류, 인용 표본 추출."""
import json, pathlib, random, re, sys

REQUIRED = {  # 지시문 'Cover at least' 목록과 지목된 출처 (실행 전에 고정)
    "Ultima Online": ["ultima online", "울티마 온라인"], "Daggerfall": ["daggerfall"], "Morrowind": ["morrowind"],
    "Oblivion": ["oblivion"], "Skyrim": ["skyrim"], "Final Fantasy II": ["final fantasy ii", "ff2", "ffii", "파이널 판타지 ii", "파이널 판타지 2"],
    "Dungeon Siege": ["dungeon siege"], "Quest 64": ["quest 64"], "SaGa": ["saga"], "Kenshi": ["kenshi"], "RuneScape": ["runescape"],
    "EVE Online": ["eve online"], "Star Wars Galaxies": ["star wars galaxies"], "NGE": ["nge", "new game enhancements"],
    "Mount & Blade": ["mount & blade", "mount and blade"], "Kingdom Come": ["kingdom come"], "Project Zomboid": ["project zomboid"],
    "Dwarf Fortress": ["dwarf fortress"], "Soren Johnson": ["soren johnson"], "Raph Koster": ["raph koster", "koster"],
    "Todd Howard": ["todd howard"], "Bruce Nesmith": ["bruce nesmith", "nesmith"], "GDC": ["gdc"], "power hour": ["power hour"],
    "macro": ["macro", "매크로"], "efficient leveling": ["efficient level", "효율 레벨", "효율적 레벨", "효율적인 레벨"],
}
PRIMARY = ("raphkoster.com", "designer-notes.com", "gdcvault.com", "gamedeveloper.com", "gamasutra.com", "bethesda.net", "lofigames.com",
           "eveonline.com", "runescape.com", "projectzomboid.com", "bay12games.com", "taleworlds.com", "warhorsestudios", "youtube.com", "youtu.be",
           "pcgamer.com", "ign.com", "eurogamer.net", "rockpapershotgun.com", "polygon.com", "kotaku.com", "gamesindustry.biz", "theverge.com", "wired.com", "mit.edu", "acm.org", "arxiv.org", "digra.org")
WIKI = ("wikipedia.org", "fandom.com", "uesp.net", "wiki")


def metrics(text):
    low = text.lower()
    cov = {k: any(a in low for a in al) for k, al in REQUIRED.items()}
    urls = re.findall(r"https?://[^\s)\]>\"']+", text)
    uniq = sorted(set(u.rstrip(".,;") for u in urls))
    dom = lambda u: u.split("/")[2].lower()
    doms = sorted({dom(u) for u in uniq})
    cited = [l for l in text.splitlines() if l.strip().startswith(("-", "*")) and "http" in l]
    return dict(chars=len(text), coverage=sum(cov.values()), coverage_total=len(cov), missing=[k for k, v in cov.items() if not v],
                urls=len(uniq), domains=len(doms), primary_share=round(sum(any(p in dom(u) for p in PRIMARY) for u in uniq) / max(1, len(uniq)), 2),
                wiki_share=round(sum(any(w in dom(u) for w in WIKI) for u in uniq) / max(1, len(uniq)), 2),
                cited_findings=len(cited), gaps_sections=len(re.findall(r"(?m)^#+\s*Gaps", text)), quotes=text.count("“") + text.count('"') // 2)


def sample_citations(text, k, seed):
    """'- 주장 — [출처](URL)' 꼴의 줄에서 (주장, URL) 표본을 뽑는다."""
    items = []
    for l in text.splitlines():
        if not l.strip().startswith(("-", "*")):
            continue
        m = re.findall(r"\[([^\]]*)\]\((https?://[^)\s]+)\)", l)
        if not m:
            continue
        claim = re.sub(r"\[([^\]]*)\]\((https?://[^)\s]+)\)", r"[\1]", l).strip("-* ").strip()
        if len(claim) > 60:
            items.append(dict(claim=claim[:700], url=m[0][1]))
    random.Random(seed).shuffle(items)
    return items[:k], len(items)


if __name__ == "__main__":
    for p in sys.argv[1:]:
        t = pathlib.Path(p).read_text()
        print(pathlib.Path(p).name, json.dumps(metrics(t), ensure_ascii=False))
        s, n = sample_citations(t, 2, 1)
        print("  인용 줄", n, "| 예:", s[0]["claim"][:140], "→", s[0]["url"][:70])
