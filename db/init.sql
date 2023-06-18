CREATE TABLE IF NOT EXISTS CURSO (
    CursoID INT PRIMARY KEY,
    JardinID INT,
    PersonalID INT,
    FOREIGN KEY (JardinID) REFERENCES JARDIN(JardinID),
    FOREIGN KEY (PersonalID) REFERENCES PERSONAL(PersonalID)
);

CREATE TABLE IF NOT EXISTS ALUMNO (
    EstudianteID INT PRIMARY KEY,
    CursoID INT,
    JardinID INT,
    Nombre TEXT,
    Apellido TEXT,
    Rut TEXT,
    FechaNacimiento DATE,
    FOREIGN KEY (CursoID) REFERENCES CURSO(CursoID),
    FOREIGN KEY (JardinID) REFERENCES JARDIN(JardinID)
);

CREATE TABLE IF NOT EXISTS PERSONAL (
    PersonalID INT PRIMARY KEY,
    JardinID INT,
    Nombre TEXT,
    Apellido TEXT,
    Rut TEXT,
    Cargo TEXT,
    FechaNacimiento DATE,
    FOREIGN KEY (JardinID) REFERENCES JARDIN(JardinID)
);

CREATE TABLE IF NOT EXISTS JARDIN (
    JardinID INT PRIMARY KEY,
    Nombre TEXT,
    Direccion TEXT,
    Telefono TEXT
);

CREATE TABLE IF NOT EXISTS ASISTENCIA (
    AsistenciaID INT PRIMARY KEY,
    PersonaID INT,
    Fecha DATE,
    Estado BOOLEAN,
    FOREIGN KEY (PersonaID) REFERENCES PERSONAL(PersonalID),
    FOREIGN KEY (PersonaID) REFERENCES ALUMNO(EstudianteID)
);

CREATE TABLE IF NOT EXISTS PRIVILEGIO (
    PrivilegioID INT PRIMARY KEY,
    Nombre INT,
    NivelPermiso INT
);

CREATE TABLE IF NOT EXISTS Usuarios (
    Nombre VARCHAR(100) not null, 
    Rut VARCHAR(100), 
    Correo VARCHAR(100), 
    Contrasena VARCHAR(100), 
    Telefono VARCHAR(100), 
    Rol VARCHAR(100), 
    Jardin VARCHAR(100), 
    primary key(Rut)
);