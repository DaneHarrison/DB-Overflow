from dotenv import load_dotenv
import os

from database.db import DB
from database.queries import getTables, getTableReferences
from tableDocsGenerator import createH1, addBreak, createTableInMD

COL_SUMMARY_TABLE_TXT = 'Table Columns'
COL_TABLE_COLS = ['Columns']
REF_SUMMARY_TABLE_TXT = 'Table References'
REF_TABLE_COLS = [
    'Table with Foreign key',
    'Column with Foreign key',
    'Referenced table',
    'Referenced column'
]


load_dotenv("../deployment/.env")
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
file = open("../output/referencingTables.md", "w")
for table in tables:
    references = getTableReferences(db, table)
    columns = getTableColumns(db, table)
    
    #addReference(references, [2])# add link to third entry per reference

    file.write(createH1(table))
    file.write(createBulletPoint('Schema: public')) 
    file.write(createBulletPoint(f'Number of Columns: {len(columns)}')) 

    if columns:
        file.write(createTableInMD(COL_SUMMARY_TABLE_TXT, COL_TABLE_COLS, columns))
    if references:
        file.write(createTableInMD(REF_SUMMARY_TABLE_TXT, TABLE_COLS, references))

    file.write(addBreak())

file.close()
db.cleanup()