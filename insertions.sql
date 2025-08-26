-- 1. STATES
INSERT INTO states (description) VALUES
('Activo'),
('Inactivo');


-- 2. PROFILES
INSERT INTO profiles (name, description, state_id) VALUES
('Administrador', 'Acceso total a la plataforma', 1),
('Organizador', 'Gestiona eventos y participantes', 1),
('Asistente', 'Solo visualiza información', 1);


-- 3. PERMISSIONS
INSERT INTO permissions (name, route, state_id) VALUES
('Gestionar eventos',     '["/eventos", "/crear-evento", "/editar-evento"]', 1),
('Gestionar usuarios',    '["/usuarios", "/crear-usuario", "/editar-usuario"]', 1),
('Gestionar perfiles',    '["/perfiles", "/crear-perfil", "/editar-perfil"]', 1);


-- 4. PROFILE_PERMISSION (asociaciones)
INSERT INTO profile_permission (perfil_id, permission_id) VALUES
(1, 1), (1, 2), (1, 3), (2, 1);

-- 5. USERS
-- Solo un par de usuarios de prueba
INSERT INTO users (name, email, password, profile_id, state_id) VALUES
('Admin User', 'admin@myevent.com', 'hashedpassword1', 1, 1),
('Event Organizer', 'organizer@myevent.com', 'hashedpassword2', 2, 1);

-- 6. EVENTS (máximo 10)
INSERT INTO events (event_name, initial_date, end_date, speaker_name, state_id) VALUES
('Evento 1', '2025-09-01 10:00:00', '2025-09-01 12:00:00', 'Juan Pérez', 1),
('Evento 2', '2025-09-02 14:00:00', '2025-09-02 17:00:00', 'Laura Gómez', 1),
('Evento 3', '2025-09-03 09:00:00', '2025-09-03 11:00:00', 'Carlos Ramírez', 1),
('Evento 4', '2025-09-04 15:00:00', '2025-09-04 17:00:00', 'Sofía Castro', 1),
('Evento 5', '2025-09-05 13:00:00', '2025-09-05 16:00:00', 'Pedro Martínez', 1),
('Evento 6', '2025-09-06 08:00:00', '2025-09-06 10:30:00', 'Ana Torres', 1),
('Evento 7', '2025-09-07 11:00:00', '2025-09-07 13:00:00', 'David Rojas', 1),
('Evento 8', '2025-09-08 14:00:00', '2025-09-08 16:00:00', 'Mónica Pérez', 1),
('Evento 9', '2025-09-09 10:00:00', '2025-09-09 12:00:00', 'Ricardo Gómez', 1),
('Evento 10', '2025-09-10 09:00:00', '2025-09-10 11:30:00', 'Lucía Díaz', 1);