def createH1(text):
    return f'# {text}\n'

def addBreak():
    return '\n<br>\n'

def createTableInMD(summaryTxt, tableCols, references):
    markdown = f'\n<details><summary>{summaryTxt}</summary>'

    markdown += '\n|'
    for column in tableCols:
        markdown += f' {column} |' 

    markdown += '\n|'
    for column in tableCols:
        markdown += f' -- |'

    for row in references:
        markdown += '\n|'
        for column in row:
            markdown += f' {column} |'

    markdown += '\n</details>\n\n'

    return markdown

def createBulletPoint(text):
    return f'- {text}\n'