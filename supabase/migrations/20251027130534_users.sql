create table if not exists users (
  id text primary key,
  name text not null,
  surname text not null,
  email text unique not null,
  password text not null,
  refresh_token text unique,
  created_at timestamptz default now()
);