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
    PersonalRut VARCHAR(100),
    JardinID INT,
    FOREIGN KEY (PersonalRut) REFERENCES Usuarios(Rut),
    FOREIGN KEY (JardinID) REFERENCES JARDIN(JardinID)
);

CREATE TABLE IF NOT EXISTS ALUMNO (
    EstudianteRut VARCHAR(100) PRIMARY KEY,
    CursoID INT,
    JardinID INT,
    Nombre TEXT,
    Apellido TEXT,
    FechaNacimiento DATE,
    FOREIGN KEY (CursoID) REFERENCES CURSO(CursoID),
    FOREIGN KEY (JardinID) REFERENCES JARDIN(JardinID)
);

CREATE TABLE IF NOT EXISTS JARDIN (
    JardinID INT PRIMARY KEY,
    Nombre VARCHAR(100),
    Direccion TEXT,
    Telefono TEXT
);

CREATE TABLE IF NOT EXISTS ASISTENCIA (
    AsistenciaID INT PRIMARY KEY,
    PersonaRut VARCHAR(100),
    Fecha DATE,
    Estado BOOLEAN,
    FOREIGN KEY (PersonaRut) REFERENCES Usuarios(Rut)
);

CREATE TABLE IF NOT EXISTS PRIVILEGIO (
    PrivilegioID INT PRIMARY KEY,
    Nombre INT,
    NivelPermiso INT
);