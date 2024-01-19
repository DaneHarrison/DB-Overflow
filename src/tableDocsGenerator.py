def createH1(text):
    return f'# {text}\n'

def createTableInMD(tableCols, references):
    markdown = '\n<details><summary>Table References</summary>'

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
