import sqlalchemy as sq


def getTables(db, schema='public'):
    query = sq.text(f'''
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = '{schema}'
        AND table_type = 'BASE TABLE';
    ''')

    results = db.execute(query)
    results = results.fetchall()

    return results

def getTableColumns(db, tableName):
    query = sq.text(f'''
        SELECT column_name
        FROM information_schema.columns
        WHERE table_name = '{tableName}';
    ''')

    results = db.execute(query)
    results = results.fetchall()

    return results

def getTableReferences(db, tableName):
    query = sq.text(f'''
        SELECT
            con.table_name AS table_with_foreign_key,
            kcu.column_name AS column_with_foreign_key,
            ccu.table_name AS referenced_table_name,
            ccu.column_name AS referenced_column_name
        
        FROM information_schema.constraint_column_usage AS kcu
        
        JOIN information_schema.referential_constraints AS rc ON kcu.constraint_name = rc.constraint_name
        JOIN information_schema.table_constraints AS con ON kcu.constraint_name = con.constraint_name
        JOIN information_schema.constraint_column_usage AS ccu ON rc.unique_constraint_name = ccu.constraint_name
        
        WHERE con.constraint_type = 'FOREIGN KEY' AND con.table_name = '{tableName}';
    ''')

    results = db.execute(query)
    results = results.fetchall()

    return results