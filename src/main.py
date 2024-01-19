from dotenv import load_dotenv
import os

from database.db import DB
from database.queries import getTables, getTableReferences
from tableDocsGenerator import createH1, createTableInMD


TABLE_COLS = [
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
    refereces = getTableReferences(db, table)
    
    file.write(createH1(table))
    file.write(createTableInMD(TABLE_COLS, refereces))

file.close()
db.cleanup()