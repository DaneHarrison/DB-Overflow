import sqlalchemy as sq


def getTables(db, schema='public'):
    query = sq.text(f'''
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = '{schema}'
        AND table_type = 'BASE TABLE'
        ORDER BY table_name;
    ''')

    results = db.execute(query)
    results = results.fetchall()

    return results

def getTableColumns(db, tableName):
    query = sq.text(f'''
        SELECT column_name, data_type
        FROM information_schema.columns
        WHERE table_name = '{tableName}'
        ORDER BY column_name;
    ''')

    results = db.execute(query)
    results = results.fetchall()

    return results

def getTableReferences(db, tableName):
    query = sq.text(f'''
        SELECT 
            conrelid::regclass AS table_name,
            a.attname AS column_name,
            confrelid::regclass AS foreign_table_name,
            af.attname AS foreign_column_name
        
        FROM pg_constraint AS c
        JOIN pg_attribute AS a 
            ON a.attnum = ANY(c.conkey) AND a.attrelid = c.conrelid
        JOIN pg_attribute AS af 
            ON af.attnum = ANY(c.confkey) AND af.attrelid = c.confrelid

        WHERE confrelid IS NOT NULL and conrelid::regclass::text = '{tableName}'
        ORDER BY a.attname;
    ''')

    results = db.execute(query)
    results = results.fetchall()

    return results