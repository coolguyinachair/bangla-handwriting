from laligned import Hand

lines = """
These four C's highlight the interconnectedness and integration of various
technologies to enable effective communication, collaboration, and
information management.


















""".split('\n')
# lines = [i.ljust(75) for i in lines]
biases = [.75 for i in lines]
styles = [10 for i in lines]
stroke_colors = ['black' for i in lines]
stroke_widths = [2 for i in lines]

hand = Hand()
hand.write(
    filename='img/test.svg',
    lines=lines,
    biases=biases,
    styles=styles,
    stroke_colors=stroke_colors,
    stroke_widths=stroke_widths
)
