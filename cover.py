from caligned import Hand

lines = """Arnab De
3rd Year, CSE""".split('\n')
# lines = [i.ljust(75) for i in lines]
biases = [.75 for i in lines]
styles = [5 for i in lines]
stroke_colors = ['black' for i in lines]
stroke_widths = [2 for i in lines]

hand = Hand()
hand.write(
    filename='img/cver.svg',
    lines=lines,
    biases=biases,
    styles=styles,
    stroke_colors=stroke_colors,
    stroke_widths=stroke_widths
)
