CREATE TABLE IF NOT EXISTS Usuarios(
    Nombre VARCHAR(100) not null, 
    Rut VARCHAR(100), 
    Correo VARCHAR(100), 
    Contrasena VARCHAR(100), 
    Telefono VARCHAR(100), 
    Rol VARCHAR(100), 
    Jardin VARCHAR(100), 
    primary key(Rut)
    foreign key (Rol) REFERENCES PRIVILEGIO(PrivilegioID)
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
    PrivilegioID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nombre TEXT,
    NivelPermiso INTEGER
);

INSERT OR IGNORE INTO Usuarios (Nombre, Rut, Correo, Contrasena, Telefono, Rol, Jardin)
VALUES 
('Benjamin', '205740171', 'benjamin.tello@mail.udp.cl', 'benjamin1234', '12345678', '1', 'aweonao'),
('Rodrigo', '19160024k', 'rodrigo.ordenes@mail.udp.cl', 'rodrigo1234', '98765432', '2', 'jeje'),
('Abel', '202458351', 'abel.baulloza@mail.udp.cl', 'abel1234', '11112222', '3', 'jaja');