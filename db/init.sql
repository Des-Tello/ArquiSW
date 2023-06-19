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
    CursoID INT PRIMARY KEY,
    JardinID INT,
    PersonalID INT,
    FOREIGN KEY (JardinID) REFERENCES JARDIN(JardinID),
    FOREIGN KEY (PersonalID) REFERENCES PERSONAL(PersonalID)
);

CREATE TABLE IF NOT EXISTS ALUMNO (
    Rut TEXT PRIMARY KEY,
    Nombre TEXT,
    Apellido TEXT,
    FechaNacimiento DATE,
    JardinID INT,
    CursoID INT,
    FOREIGN KEY (CursoID) REFERENCES CURSO(CursoID),
    FOREIGN KEY (JardinID) REFERENCES JARDIN(JardinID)
);

CREATE TABLE IF NOT EXISTS PERSONAL (
    Rut TEXT PRIMARY KEY,
    JardinID INT,
    Nombre TEXT,
    Apellido TEXT,
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
    AsistenciaID INT AUTO_INCREMENT PRIMARY KEY,
    PersonaRut INT,
    Fecha DATE,
    Estado BOOLEAN,
    FOREIGN KEY (PersonaRut) REFERENCES PERSONAL(Rut),
    FOREIGN KEY (PersonaRut) REFERENCES ALUMNO(Rut)
);

CREATE TABLE IF NOT EXISTS PRIVILEGIO (
    PrivilegioID INT PRIMARY KEY,
    Nombre INT,
    NivelPermiso INT
);

