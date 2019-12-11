class Instrumento(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        sql = """
            SELECT  instrumento.id, instrumento.nombre, instrumento.codigo, instrumento.tipo_id, tipo_instrumento.id AS tipo_id, tipo_instrumento.nombre AS tipo
            FROM instrumento
            INNER JOIN tipo_instrumento ON instrumento.tipo_id = tipo_instrumento.id
        """
        cursor.execute(sql)
        return cursor.fetchall()
    
    @classmethod
    def total_paginas(cls,paginacion):
        cursor = cls.db.cursor()
        sql = """
            SELECT *
            FROM instrumento
        """
        cursor.execute(sql)
        result = cursor.fetchall()
        count = 0
        for i in result:
            count += 1
            i = i
        paginas = count / paginacion 
        if not (count % paginacion == 0):
            paginas += 1
        return paginas

    @classmethod
    def allPaginated(cls,pagination,page):
        cursor = cls.db.cursor()
        sql = """
            SELECT  instrumento.id, instrumento.nombre, instrumento.codigo, instrumento.tipo_id, tipo_instrumento.id AS tipo_id, tipo_instrumento.nombre AS tipo
            FROM instrumento
            INNER JOIN tipo_instrumento ON instrumento.tipo_id = tipo_instrumento.id
            LIMIT {limit} offset {offset}
        """
        cursor.execute(sql.format(limit = pagination, offset = (pagination * int(page - 1)) ))
        return cursor.fetchall()

    @classmethod
    def searchByName(cls,name):
        cursor = cls.db.cursor()
        sql = """
            SELECT  instrumento.id, instrumento.nombre, instrumento.codigo, instrumento.tipo_id, tipo_instrumento.id AS tipo_id, tipo_instrumento.nombre AS tipo
            FROM instrumento
            INNER JOIN tipo_instrumento ON instrumento.tipo_id = tipo_instrumento.id
            WHERE instrumento.nombre LIKE '%{name}%'
        """
        cursor.execute(sql.format(name = name))
        return cursor.fetchall()

    @classmethod
    def getLastPage(cls,pagination,page):
        cursor = cls.db.cursor()
        sql = """
            SELECT * FROM instrumento
            COUNT
        """
        if ((cursor.execute(sql) / pagination) <= page):
            return 1
        else:
            return 0

    @classmethod
    def getInstrumento(cls, id_data):
        sql = """
            SELECT  instrumento.id, instrumento.nombre, instrumento.codigo, instrumento.tipo_id, instrumento.img, tipo_instrumento.id AS tipo_id, tipo_instrumento.nombre AS tipo FROM instrumento INNER JOIN tipo_instrumento ON instrumento.tipo_id = tipo_instrumento.id 
            WHERE instrumento.id=%s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (id_data))
        return cursor.fetchone()

    @classmethod
    def store(cls, data):
        sql = """
            INSERT INTO instrumento (nombre, tipo_id, codigo, img)
            VALUES (%s, %s, %s, %s)
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, list(data.values()))
        cls.db.commit()
        return True

    @classmethod
    def delete(cls, id_data):
        cursor = cls.db.cursor()
        cursor.execute("DELETE FROM instrumento WHERE id=%s", (id_data,))
        cls.db.commit()
        return True

    @classmethod
    def update(cls, request):
        id_data = request['id']
        apellido = request['apellido']
        nombre = request['nombre']
        fecha_nac = request['fecha_nac']
        cursor = cls.db.cursor()
        cursor.execute("""
               UPDATE estudiante
               SET apellido=%s, nombre=%s, fecha_nac=%s, localidad_id=%s, nivel_id=%s, domicilio=%s, genero_id=%s, escuela_id=%s, tipo_doc_id=%s, numero=%s, tel=%s, barrio_id=%s, responsable_id=%s
               WHERE id=%s
            """, (apellido, nombre, fecha_nac, localidad_id, nivel_id, domicilio, genero_id, escuela_id, tipo_doc_id, numero, tel, barrio_id, responsable_id, id_data))
        cls.db.commit()
        return True
        