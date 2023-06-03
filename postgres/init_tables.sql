CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(30) UNIQUE NOT NULL,
    password VARCHAR(30) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
    phone_number INT NOT NULL,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    birth_date DATE NOT NULL,
    address VARCHAR(150) NOT NULL,
    cpf VARCHAR(11) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS hotels (
    hotel_id SERIAL PRIMARY KEY,
    hotel_name VARCHAR(50) NOT NULL,
    address VARCHAR(150) NOT NULL,
    cep VARCHAR(8) NOT NULL,
    phone_number INT NOT NULL,
    description VARCHAR(500) NOT NULL
);

CREATE TABLE IF NOT EXISTS rooms (
    room_id SERIAL PRIMARY KEY,
    hotel_id INT NOT NULL,
    type VARCHAR(50) NOT NULL,
    price NUMERIC NOT NULL,
    description VARCHAR(500) NOT NULL,
    max_customers INT NOT NULL,
    total_rooms INT NOT NULL,
    FOREIGN KEY (hotel_id) REFERENCES hotels(hotel_id)
);

CREATE TABLE IF NOT EXISTS bookings (
    booking_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    room_id INT NOT NULL,
    check_in DATE NOT NULL,
    check_out DATE NOT NULL,
    total_price NUMERIC NOT NULL,
    total_nights INT NOT NULL,
    total_customers INT NOT NULL,
    status VARCHAR(50) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (room_id) REFERENCES rooms(room_id)
);

INSERT INTO users (id, username, password, email, phone_number, first_name, last_name, birth_date, address, cpf) VALUES 
    (1, "lukasallegretti", "password_lukas", "lukas@gmail.com", 11999999999, "Lukas", "Allegretti", "1999-01-01", "Rua dos Bobos, 0", "12345678910"),
    (2, "gabriel", "password_gabriel", "gabriel@gmail.com", 11999999999, "Gabriel", "Allegretti", "1999-01-01", "Rua dos Bobos, 0", "12345678910"),
    (3, "joao", "password_joao", "joao@gmail.com", 11999999999, "Joao", "Allegretti", "1999-01-01", "Rua dos Bobos, 0", "12345678910"),
    (4, "maria", "password_maria", "maria@gmail.com", 11999999999, "Maria", "Allegretti", "1999-01-01", "Rua dos Bobos, 0", "12345678910");

INSERT INTO hotels (hotel_id, hotel_name, address, cep, phone_number, description) VALUES 
    (1, "Hilton", "Av. das Cores, 1500", "12345678", 11999999999, "Hotel 5 estrelas"),
    (2, "Ibis", "Av. das Cores, 1500", "12345678", 11999999999, "Hotel 3 estrelas"),
    (3, "Motel", "Av. das Cores, 1500", "12345678", 11999999999, "Hotel 1 estrela"),
    (4, "Hotel", "Av. das Cores, 1500", "12345678", 11999999999, "Hotel 2 estrelas");

INSERT INTO rooms (room_id, hotel_id, type, price, description, max_customers, total_rooms) VALUES 
    (1, 2, "Deluxe", 100.00, "Quarto de luxo", 4, 10),
    (2, 2, "Standard", 50.00, "Quarto simples", 2, 10),
    (3, 2, "Luxury", 150.00, "Quarto de luxo", 2, 10),
    (4, 1, "Deluxe", 100.00, "Quarto de luxo", 2, 10),
    (5, 1, "Standard", 50.00, "Quarto simples", 3, 10),
    (6, 1, "Luxury", 150.00, "Quarto de luxo", 2, 10),
    (7, 3, "Deluxe", 100.00, "Quarto de luxo", 2, 10),
    (8, 3, "Standard", 50.00, "Quarto simples", 2, 10),
    (9, 3, "Luxury", 150.00, "Quarto de luxo", 3, 10),
    (10, 4, "Deluxe", 100.00, "Quarto de luxo", 2, 10),
    (11, 4, "Standard", 50.00, "Quarto simples", 2, 10),
    (12, 4, "Luxury", 150.00, "Quarto de luxo", 5, 10);

INSERT INTO bookings (user_id, room_id, check_in, check_out, total_price, total_nights, total_customers, status) VALUES 
    (1, 1, "2023-11-01", "2023-11-02", 100.00, 1, 2, "PENDING"),
    (2, 2, "2023-10-01", "2023-10-05", 200.00, 4, 2, "PENDING"),
    (3, 3, "2023-07-01", "2023-07-10", 1350.00, 9, 2, "PENDING"),
    (4, 4, "2023-08-01", "2023-08-03", 200.00, 2, 2, "CANCELLED");