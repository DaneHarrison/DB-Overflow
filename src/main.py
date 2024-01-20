from dotenv import load_dotenv
import os

from database.db import DB
from database.queries import getTables, getTableColumns, getTableReferences
from mdDocsGenerator import createH2, createBreak, createTable, createBulletPoint, createSelfReference


DOCS_SAVE_LOC = '../output/dbDocs.md'
COL_SUMMARY_TABLE_TXT = 'Table Columns'
COL_TABLE_COLS = ['Columns', 'Data Type']
REF_SUMMARY_TABLE_TXT = 'Table References'
REF_TABLE_COLS = [
    'Table with Foreign key',
    'Column with Foreign key',
    'Referenced Table',
    'Referenced Column'
]

load_dotenv("../.env")
PG_USER = os.getenv("POSTGRES_USER")
PG_PW = os.getenv("POSTGRES_PW")
PG_DB = os.getenv("POSTGRES_DB")
PG_ADDR = os.getenv("POSTGRES_ADDR")
PG_PORT = int(os.getenv("POSTGRES_PORT"))
if not PG_DB or not PG_ADDR or not PG_PORT or not PG_USER or not PG_PW:
    raise ValueError("[ERROR] Environment variables not detected")


db = DB(PG_DB, PG_ADDR, PG_PORT, PG_USER, PG_PW)
conn = db.connect()

tables = getTables(db)
file = open(DOCS_SAVE_LOC, "w")
for table in tables:
    table = table[0]

    references = getTableReferences(db, table)
    references = createSelfReference(references, [2])
    columns = getTableColumns(db, table)

    file.write(createH2(table))
    file.write(createBulletPoint('Schema: public')) 
    file.write(createBulletPoint(f'Number of Columns: {len(columns)}')) 

    if columns:
        file.write(createTable(COL_SUMMARY_TABLE_TXT, COL_TABLE_COLS, columns))
    if references:
        file.write(createTable(REF_SUMMARY_TABLE_TXT, REF_TABLE_COLS, references))

    file.write(createBreak())


file.close()
db.cleanup()