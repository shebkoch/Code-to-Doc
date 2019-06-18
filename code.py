from sys import argv
from pathlib import Path
from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_COLOR_INDEX
from docx.shared import Pt, RGBColor

if __name__ == '__main__':

    def styles(document):
        styles = document.styles
        new_heading_style = styles.add_style('filename', WD_STYLE_TYPE.PARAGRAPH)
        new_heading_style.base_style = styles['Heading 1']
        font = new_heading_style.font
        font.name = 'Times New Roman'
        font.size = Pt(14)
        font.color.rgb = RGBColor(0, 0, 0)

        normalStyle = document.styles['Normal']
        normalFont = normalStyle.font
        normalFont.name = 'Courier New'
        normalFont.size = Pt(10)

    document = Document()
    styles(document)

    for filename in Path(argv[1]).glob('**/*.'+argv[2]):
        fr = open(str(filename), 'r')
        document.add_paragraph(filename.name, style='filename')
        document.add_paragraph(fr.read())

    document.save(argv[3])



    # fr = open(argv[1], 'r')
    # str = fr.read()
    # hash = hashlib.sha1(str.encode()).hexdigest()
    # fw = open(argv[2], 'w')
    # print(hash)
    # fw.write(hash)
