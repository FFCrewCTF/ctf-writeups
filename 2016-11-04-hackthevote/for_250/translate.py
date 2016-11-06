import untangle

s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
font = untangle.parse('lexicographic.646ab52fa361f7d2b3649ccca31a26771ac7f30dad486e1880434210b9d83ae6.ttx')

font_map = {
    '0400': 'a',
    '0401': 'e',
    '0402': 'f',
    '0403': 'g',
    '0404': 'h',
    '0405': 'i',
    '0406': 'l',
    '0407': 'n',
    '0408': 'r',
    '0409': 's',
    '040A': 't',
    '040B': 'u',
    '040C': '{',
    '040D': '}',
}

lig_map = {}

for lig in font.ttFont.GSUB.LookupList.Lookup.LigatureSubst.children:
    key = lig['glyph'][0]
    val = lig.Ligature['glyph'][3:]
    lig_map[key] = val

for c in s:
    print(font_map[lig_map[c]], end='')
print()
