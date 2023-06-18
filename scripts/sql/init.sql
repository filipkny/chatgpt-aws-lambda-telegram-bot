CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS users(
    uuid UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    telegram_id BIGINT,
    is_bot BOOLEAN,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    username VARCHAR(255),
    language_code VARCHAR(255)
);
