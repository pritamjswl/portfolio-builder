CREATE TABLE users (
    id INTEGER NOT NULL PRIMARY KEY,
    fname TEXT NOT NULL,
    lname TEXT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL, -- Hashed
    joined_on DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_active DATETIME,
    -- Basic details
    profile_photo TEXT,
    cover_photo TEXT,
    profession TEXT,
    status TEXT, -- E.g, Available to work
    bio TEXT,
    institution TEXT,
    address TEXT,
    public_email TEXT,
    phone TEXT,
    website TEXT,
    -- Action buttons
    primary_btn TEXT NOT NULL DEFAULT 'contact', -- contact (for contact form), email, or call
    secondary_btn TEXT NOT NULL DEFAULT 'more', -- more (default), visit_url (website url), download_cv, download_resume
    -- Added things
    cv TEXT,
    resume TEXT,
    about TEXT
);

CREATE TABLE social_media (
    id INTEGER NOT NULL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    site TEXT NOT NULL,
    link TEXT NOT NULL,
    UNIQUE(user_id, site),
    FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE experiences (
    id INTEGER NOT NULL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    duration TEXT NOT NULL,
    description TEXT NOT NULL,
    UNIQUE(user_id, title),
    FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE educations (
    id INTEGER NOT NULL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    qualification TEXT NOT NULL,
    year INTEGER NOT NULL,
    institution TEXT NOT NULL,
    UNIQUE(user_id, qualification),
    FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE skills (
    id INTEGER NOT NULL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    skill TEXT NOT NULL,
    type TEXT NOT NULL, -- technical or soft skill
    UNIQUE(user_id, skill),
    FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE achievements (
    id INTEGER NOT NULL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    achievement TEXT NOT NULL,
    type TEXT NOT NULL, -- award, honor, certificate
    year INTEGER NOT NULL,
    UNIQUE(user_id, achievement),
    FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE testimonials (
    id INTEGER NOT NULL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    photo TEXT,
    name TEXT NOT NULL,
    profession TEXT NOT NULL,
    description TEXT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE portfolio (
    id INTEGER NOT NULL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    photo TEXT NOT NULL,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    link TEXT,
    FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE notifications (
    id INTEGER NOT NULL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    message TEXT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE contact_form (
    id INTEGER NOT NULL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    fname TEXT NOT NULL,
    lname TEXT,
    email TEXT NOT NULL,
    message TEXT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE feedback (
    id INTEGER NOT NULL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    message TEXT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
);
