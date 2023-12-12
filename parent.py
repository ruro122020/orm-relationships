from __init__ import conn, cursor


class Parent:

    all: {}

    def __init__(self, name):
        self.id = None
        self.name = name
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise TypeError('name must be of string type')
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS parents (
            id INTEGER PRIMARY KEY,
            name TEXT)
        """

        cursor.execute(sql)
        conn.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS parents
        """

        cursor.execute(sql)
        conn.commit()

    
    def save(self):
        sql = """
            INSERT INTO parents (name)
            VALUES (?)
        """

        cursor.execute(sql, (self.name,))
        conn.commit()

        self.id = cursor.lastrowid
        #type(self).all[self.id] = self

    @classmethod
    def create(cls, name):
        parent = cls(name)
        parent.save()
        return parent
    
    def update(self):
        sql = """
            UPDATE parents
            SET name = ?
            WHERE id = ?
        """
        cursor.execute(sql, (self.name, self.id))
        conn.commit()