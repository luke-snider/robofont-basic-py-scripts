### corrects the order of base glyph and component  - thanks to Frederik Berlaen

g = CurrentGlyph()

components = g.components

baseGlyphs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i, component in enumerate(components):
    if component.baseGlyph in baseGlyphs:
        components.remove(component)
        components.insert(0, component)
        break
        
g.clearComponents()

for component in components:
    g.appendComponent(component.baseGlyph, component.offset, component.scale)
