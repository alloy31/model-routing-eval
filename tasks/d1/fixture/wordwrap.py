def wrap(text, width):
    """text 를 공백으로 나눈 단어들을, 각 줄의 길이가 width 를 넘지 않게 채워 줄 리스트로 돌려준다.

    - 한 줄 안의 단어 사이는 공백 한 칸이다. 입력의 연속 공백은 한 칸으로 본다.
    - 한 단어가 width 보다 길면 자르지 않고 그 단어만으로 한 줄을 쓴다.
    - 줄 길이가 정확히 width 인 것은 허용한다.
    - 빈 문자열이면 빈 리스트다.
    """
    lines, cur = [], ""
    for word in text.split():
        if not cur:
            cur = word
        elif len(cur) + 1 + len(word) < width:
            cur += " " + word
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines
