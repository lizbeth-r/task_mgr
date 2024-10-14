
CREATE TABLE IF NOT EXISTS task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(64),
    summary VARCHAR(128),
    description TEXT,
    is_done BOOLEAN DEFAULT 0
);


INSERT INTO task (
    name,
    summary,
    description
) VALUES
(
    "Wash car",
    "Take the car to the car wash",
    "Make sure the car gets waxed"
),
(
    "Walk the dog",
    "Fido needs his exercise",
    "Two laps around the park should be enough"
),
(
    "But groceries",
    "Get everything on the list",
    "We need tomatoes, lettuce, milk and eggs"
);