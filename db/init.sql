CREATE TABLE IF NOT EXISTS Usuarios(
    Nombre VARCHAR(100) not null, 
    Rut VARCHAR(100), 
    Correo VARCHAR(100), 
    Contrasena VARCHAR(100), 
    Telefono VARCHAR(100), 
    Rol VARCHAR(100), 
    Jardin VARCHAR(100), 
    primary key(Rut)
);

CREATE TABLE IF NOT EXISTS CURSO (
    CursoID INTEGER PRIMARY KEY,
    NombreJardin INTEGER,
    PersonalID INTEGER,
    FOREIGN KEY (NombreJardin) REFERENCES JARDIN(NombreJardin),
    FOREIGN KEY (PersonalID) REFERENCES PERSONAL(PersonalID)
);

CREATE TABLE IF NOT EXISTS ALUMNO (
    Rut TEXT PRIMARY KEY,
    Nombre TEXT,
    Apellido TEXT,
    FechaNacimiento DATE,
    NombreJardin TEXT,
    CursoID INTEGER,
    FOREIGN KEY (CursoID) REFERENCES CURSO(CursoID),
    FOREIGN KEY (NombreJardin) REFERENCES JARDIN(NombreJardin)
);

CREATE TABLE IF NOT EXISTS PERSONAL (
    Rut TEXT PRIMARY KEY,
    NombreJardin INTEGER,
    Nombre TEXT,
    Apellido TEXT,
    Cargo TEXT,
    FechaNacimiento DATE,
    FOREIGN KEY (NombreJardin) REFERENCES JARDIN(NombreJardin)
);

CREATE TABLE IF NOT EXISTS JARDIN (
    NombreJardin TEXT PRIMARY KEY,
    Direccion TEXT,
    Telefono TEXT
);

CREATE TABLE IF NOT EXISTS ASISTENCIA (
    AsistenciaID INTEGER PRIMARY KEY AUTOINCREMENT,
    PersonaRut INTEGER,
    Fecha DATE,
    Estado BOOLEAN,
    FOREIGN KEY (PersonaRut) REFERENCES PERSONAL(Rut),
    FOREIGN KEY (PersonaRut) REFERENCES ALUMNO(Rut)
);

CREATE TABLE IF NOT EXISTS PRIVILEGIO (
    PrivilegioID INTEGER PRIMARY KEY,
    Nombre INTEGER,
    NivelPermiso INTEGER
);

