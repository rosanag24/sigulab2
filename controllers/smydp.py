#-----------------------------------------------------------------------------
# Controladores provisionales utilizados solo para probar las vistas del modulo de SMyDP
#
# - Samuel Arleo <saar1312@gmail.com>
#-----------------------------------------------------------------------------


@auth.requires_login(otherwise=URL('modulos', 'login'))
def index():
    return locals()


@auth.requires_login(otherwise=URL('modulos', 'login'))
def sustancias():
    return locals()

# Muestra el inventario de acuerdo al cargo del usuario y la dependencia que tiene
# a cargo
@auth.requires_login(otherwise=URL('modulos', 'login'))
def inventarios():
    
    # Inicializando listas de espacios fisicos y dependencias
    espacios = []
    dependencias = []
    dep_nombre = ""
    es_espacio = False

    if auth.has_membership("TÉCNICO"):
        # Si el tecnico ha seleccionado un espacio fisico
        if request.vars.dependencia:
            # Se muestra solo el inventario de ese espacio y no se muestran mas
            # dependencias pues ya se alcanzo el nivel mas bajo de la jerarquia 
            # de dependencias
            pass
        # Si el tecnico no ha seleccionado un espacio sino que acaba de entrar
        # a la opcion de inventarios
        else:
            # Se muestran los espacios fisicos que tiene el tecnico a cargo
            pass
    # Si el usuario no es tecnico, para la base de datos es indiferente su ROL
    # pues la jerarquia de dependencias esta almacenada en la misma tabla
    # con una lista de adyacencias
    else:
        # Si el usuario ha seleccionado una dependencia o un espacio fisico
        if request.vars.dependencia:
            if request.vars.es_espacio == "True":
                # Se muestra el inventario del espacio
                espacio_id = request.vars.dependencia
                dep_nombre = db.espacios_fisicos(db.espacios_fisicos.id == espacio_id).nombre

            else:
                # Se muestran las dependencias que componen a esta dependencia padre
                # y se lista el inventario agregado
                dep_id = request.vars.dependencia
                dep_nombre = db.dependencias(db.dependencias.id == dep_id).nombre
                dependencias = list(db(db.dependencias.unidad_de_adscripcion == dep_id).select(
                                                                          db.dependencias.ALL))
                # Si la lista de dependencias es vacia, entonces la dependencia no 
                # tiene otras dependencias por debajo (podria tener espacios fisicos
                # o estar vacia)
                if len(dependencias) == 0:
                    # Buscando espacios fisicos que apunten a la dependencia escogida
                    espacios = list(db(db.espacios_fisicos.dependencia == dep_id).select(
                                                                db.espacios_fisicos.ALL))
                    es_espacio = True

        else:

            # Obteniendo la entrada en t_Personal del usuario conectado
            user_id = auth.user.id
            user = db.t_Personal(db.t_Personal.id == user_id)

            # Dependencia a la que pertenece el usuario o que tiene a cargo
            dep_id = user.f_dependencia
            dep_nombre = db.dependencias(db.dependencias.id == dep_id).nombre

            # Se muestran las dependencias que componen a la dependencia que
            # tiene a cargo el usuario y el inventario agregado de esta
            dependencias = list(db(db.dependencias.unidad_de_adscripcion == dep_id).select(
                                                                      db.dependencias.ALL))

        return dict(dep_nombre=dep_nombre, 
                    dependencias=dependencias, 
                    espacios=espacios, 
                    es_espacio=es_espacio)


@auth.requires_login(otherwise=URL('modulos', 'login'))
def desechos():
    return locals()

#-------------------------------------- Catalogo ---------------------------------------

@auth.requires_login(otherwise=URL('modulos', 'login'))
def catalogo():

    if(auth.has_membership('Gestor de SMyDP') or  auth.has_membership('WEBMASTER')):
        table = SQLFORM.smartgrid(  db.t_Sustancia, 
                                    onupdate=auth.archive,
                                    links_in_grid=False,
                                    csv=False,
                                    user_signature=True,
                                    paginate=10)

    else:
        table = SQLFORM.smartgrid(  db.t_Sustancia, 
                                    editable=False,
                                    deletable=False,
                                    csv=False,
                                    links_in_grid=False,
                                    create=False,
                                    paginate=10,
                                    showid=False)
    return locals()

