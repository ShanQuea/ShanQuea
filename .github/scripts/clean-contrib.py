import io, re, sys

def drop_group(s, marker):
    start = s.find(marker)
    if start < 0:
        return s
    depth, i = 0, start
    for m in re.finditer(r'<g[\s>]|</g>', s[start:]):
        depth += 1 if m.group(0) != '</g>' else -1
        if depth == 0:
            i = start + m.end()
            break
    return s[:start] + s[i:]

for path in sys.argv[1:]:
    s = io.open(path, encoding='utf-8').read()
    for marker in ['<g transform="translate(980, ', '<g transform="translate(40, 520)', '<g transform="translate(608, ', '<g transform="translate(736, ']:
        s = drop_group(s, marker)
    s = re.sub(r'<text [^>]*x="(?:650|772)" y="830"[^>]*>.*?</text>', '', s)
    io.open(path, 'w', encoding='utf-8', newline='\n').write(s)
