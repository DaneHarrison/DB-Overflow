import sys
def createH2(text):
    return f'# {text}\n'

def createBreak():
    return '\n\n<br>\n\n'

def createTable(summaryTxt, tableCols, references):
    markdown = f'\n\n<details><summary>{summaryTxt}</summary>\n'

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

def createReferenceLinks(data, listPosi=None):
    results = []

    if not listPosi:
        results = f'[{data}](#{data.replace(" ", "-")})'
    else:
        for i in range(len(data)):
            innerList = []
            for j in range(len(data[i])):
                if j in listPosi:
                    innerList.append(f'[{data[i][j]}](#{data[i][j].replace(" ", "-")})')
                else:
                    innerList.append(data[i][j])

            results.append(innerList)

    return results