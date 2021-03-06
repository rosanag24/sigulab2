#------------------------------------------------Modulo de Personal-----------------------------------------------------------------------------------------------------------------------------------------------------------

#t_Personal: Tabla de publicaciones.
db.define_table(
    #Nombre de la entidad
    't_Publicacion', 
    #Atributos;
    Field('f_anio',          'integer', requires=IS_INT_IN_RANGE(minimum=1900,maximum=2100, error_message='Introduzca un año válido'), notnull=True, label=T('Año de Publicación')),
    Field('f_arbitrada',          'boolean', requires=IS_NOT_EMPTY(), notnull=True, label=T('Arbitrada')),
    Field('f_titulo',          'string', requires=IS_NOT_EMPTY(), notnull=True, label=T('Título')),
    Field('f_autores',          'string', requires=IS_NOT_EMPTY(), notnull=True, label=T('Autores')),
    Field('f_referencia',          'string', requires=IS_NOT_EMPTY(), notnull=True, label=T('Referencia')),
    #Referencia
    Field('f_publicacion_Personal',         'reference t_Personal', requires=IS_IN_DB(db, db.t_Personal.id, '%(f_Personal)s', zero=None), label=T('Autor')),
    )

db.t_Publicacion._plural = 'Publicaciones'
db.t_Publicacion._singular = 'Publicacion'

#t_Personal: Tabla de eventos.
db.define_table(
    #Nombre de la entidad
    't_Evento', 
    #Atributos;
    Field('f_anio',          'integer', requires=IS_INT_IN_RANGE(minimum=1900,maximum=2100, error_message='Introduzca un año válido'), notnull=True, label=T('Año')),
    Field('f_lugar',          'string', requires=IS_NOT_EMPTY(), notnull=True, label=T('Lugar')),
    Field('f_titulo',          'string', requires=IS_NOT_EMPTY(), notnull=True, label=T('Título')),
    Field('f_coactores',          'string', requires=IS_NOT_EMPTY(), notnull=True, label=T('Coactores')),
    Field('f_nombre',          'string', requires=IS_NOT_EMPTY(), notnull=True, label=T('Nombre')),
    #Referencia (Revisar si el label es asistio o organizo)
    Field('f_evento_Personal',         'reference t_Personal', requires=IS_IN_DB(db, db.t_Personal.id, '%(f_Personal)s', zero=None), label=T('Asistió')),
    )

db.t_Evento._plural = 'Eventos'
db.t_Evento._singular = 'Evento'


#t_Personal: Tabla de Reconocimientos.
db.define_table(
    #Nombre de la entidad
    't_Reconocimiento', 
    #Atributos;
    Field('f_anio',          'integer', requires=IS_INT_IN_RANGE(minimum=1900,maximum=2100, error_message='Introduzca un año válido'), notnull=True, label=T('Año')),
    Field('f_referencia',          'string', requires=IS_NOT_EMPTY(), notnull=True, label=T('Referencia')),
    Field('f_otorgado_por',          'string', requires=IS_NOT_EMPTY(), notnull=True, label=T('Otorgado por')),
    #Referencia (Revisar si el label es asistio o organizo)
    Field('f_Reconocimiento_Personal',         'reference t_Personal', requires=IS_IN_DB(db, db.t_Personal.id, '%(f_Personal)s', zero=None), label=T('Obtuvo')),
    )

db.t_Reconocimiento._plural = 'Reconocimientos'
db.t_Reconocimiento._singular = 'Reconocimiento'

#t_Personal: Tabla de Historial de trabajo.
db.define_table(
    #Nombre de la entidad
    't_Historial_trabajo', 
    #Atributos;
    Field('f_periodo',          'string', requires=IS_NOT_EMPTY(), notnull=True, label=T('Periodo')),
    Field('f_organizacion',          'string', requires=IS_NOT_EMPTY(), notnull=True, label=T('Organización')),
    Field('f_cargo',          'string', requires=IS_NOT_EMPTY(), notnull=True, label=T('Cargo')),
    #Referencia (Revisar si el label es asistio o organizo)
    Field('f_Historial_trabajo_Personal',         'reference t_Personal', requires=IS_IN_DB(db, db.t_Personal.id, '%(f_Personal)s', zero=None), label=T('Posee')),
    )

db.t_Historial_trabajo._plural = 'Historial de trabajo'
db.t_Historial_trabajo._singular = 'Historial de trabajo'


#t_Personal: Tabla de Comisiones.
db.define_table(
    #Nombre de la entidad
    't_Comision', 
    #Atributos;
    Field('f_fecha',          'string', requires=IS_DATE(format=T('%d/%m/%Y'), error_message='Debe tener el siguiente formato: dd/mm/yyyy'), notnull=True, label=T('Fecha')),
    Field('f_rol',          'string', requires=IS_NOT_EMPTY(), notnull=True, label=T('Rol')),
    Field('f_nombre',          'string', requires=IS_NOT_EMPTY(), notnull=True, label=T('Nombre')),
    #Referencia (Revisar si el label es asistio o organizo)
    Field('f_Comision_Personal',         'reference t_Personal', requires=IS_IN_DB(db, db.t_Personal.id, '%(f_Personal)s', zero=None), label=T('Participó')),
    )

db.t_Comision._plural = 'Comisiones'
db.t_Comision._singular = 'Comision'

#t_Personal: Tabla de Actividades.
db.define_table(
    #Nombre de la entidad
    't_Actividad', 
    #Atributos;
    Field('f_periodo',          'string', requires=IS_NOT_EMPTY(), notnull=True, label=T('Periodo')),
    Field('f_cargo',          'string', requires=IS_NOT_EMPTY(), notnull=True, label=T('Cargo')),
    Field('f_institucion',          'string', requires=IS_NOT_EMPTY(), notnull=True, label=T('Institución')),
    #Referencia (Revisar si el label es asistio o organizo)
    Field('f_Actividad_Personal',         'reference t_Personal', requires=IS_IN_DB(db, db.t_Personal.id, '%(f_Personal)s', zero=None), label=T('Dirigió')),
    )

db.t_Actividad._plural = 'Actividades'
db.t_Actividad._singular = 'Actividad'

#t_Personal: Tabla de Materias.
db.define_table(
    #Nombre de la entidad
    't_Materia', 
    #Atributos;
    Field('f_area',          'string', requires=IS_NOT_EMPTY(), notnull=True, label=T('Area')),
    Field('f_codigo',          'string', requires=IS_NOT_EMPTY(), notnull=True, label=T('Código')),
    Field('f_nombre',          'string', requires=IS_NOT_EMPTY(), notnull=True, label=T('Nombre')),
    Field('f_periodo',          'string', requires=IS_NOT_EMPTY(), notnull=True, label=T('Periodo')),
    #Referencia (Revisar si el label es asistio o organizo)
    Field('f_Materia_Personal',         'reference t_Personal', requires=IS_IN_DB(db, db.t_Personal.id, '%(f_Personal)s', zero=None), label=T('Dirigió')),
    )

db.t_Materia._plural = 'Materias'
db.t_Materia._singular = 'Materia'

#t_Personal: Tabla de Tesis.
db.define_table(
    #Nombre de la entidad
    't_Tesis', 
    #Atributos;
    Field('f_anio',          'integer', requires=IS_INT_IN_RANGE(minimum=1900,maximum=2100, error_message='Introduzca un año válido'), notnull=True, label=T('Año')),
    Field('f_nivel',          'string', requires=IS_NOT_EMPTY(), notnull=True, label=T('Nivel')),
    Field('f_trabajo',          'string', requires=IS_NOT_EMPTY(), notnull=True, label=T('Trabajo')),
    #Referencia (Revisar si el label es asistio o organizo)
    Field('f_Tesis_Personal',         'reference t_Personal', requires=IS_IN_DB(db, db.t_Personal.id, '%(f_Personal)s', zero=None), label=T('Publicó')),
    )

db.t_Tesis._plural = 'Tesis'
db.t_Tesis._singular = 'Tesis'

#t_Personal: Tabla de Cursos.
db.define_table(
    #Nombre de la entidad
    't_Curso', 
    #Atributos;
    Field('f_anio',          'integer', requires=IS_INT_IN_RANGE(minimum=1900,maximum=2100, error_message='Introduzca un año válido'), notnull=True, label=T('Año')),
    Field('f_horas',          'integer', requires=IS_NOT_EMPTY(), notnull=True, label=T('Horas')),
    Field('f_titulo',          'string', requires=IS_NOT_EMPTY(), notnull=True, label=T('Título')),
    Field('f_dictado_por',          'string', requires=IS_NOT_EMPTY(), notnull=True, label=T('Dictado por')),
    #Referencia (Revisar si el label es asistio o organizo)
    Field('f_Curso_Personal',         'reference t_Personal', requires=IS_IN_DB(db, db.t_Personal.id, '%(f_Personal)s', zero=None), label=T('Asistió')),
    )

db.t_Curso._plural = 'Curso'
db.t_Curso._singular = 'Curso'

#t_Personal: Tabla de Trabajos.
db.define_table(
    #Nombre de la entidad
    't_Trabajo', 
    #Atributos;
    Field('f_anio',          'integer', requires=IS_INT_IN_RANGE(minimum=1900,maximum=2100, error_message='Introduzca un año válido'), notnull=True, label=T('Año')),
    Field('f_nivel',          'string', requires=IS_NOT_EMPTY(), notnull=True, label=T('Nivel')),
    Field('f_estudiantes',          'string', requires=IS_NOT_EMPTY(), notnull=True, label=T('Estudiantes')),
    Field('f_intistitucion',          'string', requires=IS_NOT_EMPTY(), notnull=True, label=T('Intistitución')),
    Field('f_nombre',          'string', requires=IS_NOT_EMPTY(), notnull=True, label=T('Nombre')),
    #Referencia (Revisar si el label es asistio o organizo)
    Field('f_Trabajo_Personal',         'reference t_Personal', requires=IS_IN_DB(db, db.t_Personal.id, '%(f_Personal)s', zero=None), label=T('Fue Parte')),
    )

db.t_Trabajo._plural = 'Trabajos'
db.t_Trabajo._singular = 'Trabajo'

#t_Personal: Tabla de Extensiones.
db.define_table(
    #Nombre de la entidad
    't_Extension', 
    #Atributos;
    Field('f_naturaleza_actividad',          'string', requires=IS_NOT_EMPTY(), notnull=True, label=T('Naturaleza de la actividad')),
    Field('f_periodo',          'string', requires=IS_NOT_EMPTY(), notnull=True, label=T('Periodo')),
    Field('f_intistitucion',          'string', requires=IS_NOT_EMPTY(), notnull=True, label=T('Intistitución')),
    Field('f_nombre',          'string', requires=IS_NOT_EMPTY(), notnull=True, label=T('Nombre')),
    #Referencia (Revisar si el label es asistio o organizo)
    Field('f_Extension_Personal',         'reference t_Personal', requires=IS_IN_DB(db, db.t_Personal.id, '%(f_Personal)s', zero=None), label=T('Realizó')),
    )

db.t_Extension._plural = 'Extensiones'
db.t_Extension._singular = 'Extension'