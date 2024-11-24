INSERT INTO gym_2.users (first_name, last_name, email, registration_data) VALUES
('Anna', 'Johnson', 'anna.johnson@example.com', '2024-01-05'),
('Michael', 'Brown', 'michael.brown@example.com', '2024-01-12'),
('Emma', 'Davis', 'emma.davis@example.com', '2024-02-08'),
('Oliver', 'Martinez', 'oliver.martinez@example.com', '2024-03-20'),
('Sophia', 'Garcia', 'sophia.garcia@example.com', '2024-04-15'),
('Isabella', 'Robinson', 'isabella.robinson@example.com', '2024-05-10'),
('Liam', 'Harris', 'liam.harris@example.com', '2024-06-18'),
('Mia', 'Clark', 'mia.clark@example.com', '2024-07-22'),
('Noah', 'Rodriguez', 'noah.rodriguez@example.com', '2024-08-30'),
('Charlotte', 'Lewis', 'charlotte.lewis@example.com', '2024-09-12'),
('Ethan', 'Parker', 'ethan.parker@example.com', '2024-10-01'),
('Grace', 'Hill', 'grace.hill@example.com', '2024-10-15');

INSERT INTO gym_2.trainers (first_name, last_name, email) VALUES
('Mike', 'Brown', 'mike.brown@example.com'),
('Sarah', 'Davis', 'sarah.davis@example.com'),
('Emily', 'Johnson', 'emily.johnson@example.com'),
('David', 'Smith', 'david.smith@example.com'),
('Sophia', 'Williams', 'sophia.williams@example.com'),
('James', 'Miller', 'james.miller@example.com'),
('Olivia', 'Wilson', 'olivia.wilson@example.com'),
('Daniel', 'Moore', 'daniel.moore@example.com'),
('Ava', 'Taylor', 'ava.taylor@example.com'),
('Lucas', 'Green', 'lucas.green@example.com'),
('Mason', 'Baker', 'mason.baker@example.com');

INSERT INTO gym_2.program_days (day) VALUES
('Monday'),
('Tuesday'),
('Wednesday'),
('Thursday');

INSERT INTO gym_2.programs (name, description, program_day_id) VALUES
('Fitness Program', 'A detailed fitness program', 1),
('Yoga Program', 'Relaxing yoga exercises', 2),
('Strength Training', 'Advanced weightlifting program', 3),
('HIIT Program', 'High-intensity interval training', 4);

INSERT INTO gym_2.program_assignment (user_id, program_id, trainer_id, start_date, end_date)
VALUES
(1, 1, 1, '2024-11-01', '2024-11-30'),
(2, 2, 2, '2024-11-05', '2024-11-25'),
(3, 3, 3, '2024-11-10', '2024-12-10'),
(4, 4, 4, '2024-11-15', '2024-12-15');

INSERT INTO gym_2.exercise (name, description) VALUES
('Squats', 'Lower body exercise that targets.'),
('Push Ups', 'Upper body exercise that strengthens.'),
('Deadlift', 'Compound exercise that works.'),
('Bench Press', 'Chest exercise targeting.'),
('Lunges', 'Lower body exercise focusing.'),
('Pull-Ups', 'Upper body exercise for back and biceps.'),
('Bicep Curls', 'Exercise targeting the biceps muscles.'),
('Leg Press', 'Lower body exercise for leg muscles.'),
('Shoulder Press', 'Exercise targeting shoulder muscles.'),
('Plank', 'Core stability exercise.'),
('Mountain Climbers', 'Cardio and strength exercise.'),
('Jumping Jacks', 'Full-body cardio exercise.');

INSERT INTO gym_2.programs_has_exercise (program_id, exercise_id, program_exercise_id, duration, repetition, criteria)
VALUES
(1, 1, 1, 30, 10, 'High Intensity'),
(2, 2, 2, 15, 20, 'Medium Intensity'),
(3, 3, 3, 40, 8, 'Low Intensity'),
(4, 4, 4, 20, 12, 'High Intensity'),
(1, 5, 5, 25, 15, 'Medium Intensity');

INSERT INTO gym_2.exercise_session (assignment_id, exercise_id, session_date)
VALUES
(1, 3, '2024-11-05'),
(2, 2, '2024-11-07'),
(3, 3, '2024-11-09'),
(4, 4, '2024-11-11'),
(1, 2, '2024-11-12'),
(2, 3, '2024-11-13');

INSERT INTO gym_2.exercise_criteria (exercise_id, criteria_type, criteria_value) VALUES
(1, 'Sets', 3),
(2, 'Reps', 10),
(3, 'Duration (minutes)', 15),
(4, 'Sets', 4),
(5, 'Reps', 12),
(6, 'Distance (meters)', 100);

INSERT IGNORE INTO gym_2.trainers_has_users (trainer_id, user_id, start_date, end_date) VALUES
(1, 1, '2023-01-10', '2023-03-10'),
(2, 2, '2023-02-15', '2023-04-15'),
(3, 3, '2023-03-01', '2023-05-01'),
(4, 4, '2023-04-10', '2023-06-10'),
(5, 5, '2023-05-20', '2023-07-20'),
(6, 6, '2023-06-01', '2023-08-01'),
(7, 7, '2023-07-15', '2023-09-15');

INSERT INTO gym_2.user_feedback (user_id, trainer_id, feedback_text, rating, created_at) VALUES
(1, 2, 'Great trainer, very helpful!', 5, '2024-01-05 10:30:00'),
(2, 3, 'Very knowledgeable, highly recommend!', 4, '2024-01-12 11:00:00'),
(3, 4, 'Good experience, but could be better.', 3, '2024-02-08 09:15:00'),
(4, 5, 'Fantastic! Helped me improve my workouts a lot.', 5, '2024-03-20 14:20:00'),
(5, 6, 'The trainer was okay, but I expected more guidance.', 3, '2024-04-15 16:45:00'),
(6, 7, 'Excellent, made me feel confident with my exercises.', 5, '2024-05-10 13:30:00'),
(7, 8, 'Not much progress, need more one-on-one sessions.', 2, '2024-06-18 08:00:00'),
(8, 9, 'Trainer was great at explaining everything in detail!', 4, '2024-07-22 17:10:00'),
(9, 10, 'Very helpful, could improve communication skills.', 3, '2024-08-30 12:00:00'),
(10, 11, 'Fantastic energy, kept me motivated throughout the session!', 5, '2024-09-12 11:30:00'),
(11, 12, 'Could be better in terms of technique explanations.', 3, '2024-10-01 10:15:00'),
(12, 13, 'Good session, but needs more individualized attention.', 4, '2024-10-15 15:20:00');



