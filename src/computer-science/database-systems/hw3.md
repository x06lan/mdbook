
# hw3 110590049

tags `db` `database`

[2023 database-systems HW3.pdf](../../assets/pdf/database_systemsHW3.pdf)

# 1
| table        | column        |                          |              |            |            |
| ------------ | ------------- | ------------------------ | ------------ | ---------- | ---------- |
| PREREQUISITE | CourseNumber  | PrerequisiteCourseNumber |              |            |            |
| GRADE_REPORT | StudentNumber | SectionNumber            | Grade        |            |            |
| STUDENT      | StudentNumber | Name                     | Class        | Major      |            |
| COURSE       | CourseNumber  | CourseName               | "CreditHour" | Department |            |
| SECTION      | SectionNumber | CourseNumber             | Semester     | Year       | Instructor |

## a
```sql
UPDATE "COURSE"
SET "CreditHour" = 2
WHERE "CourseName" = 'Object-Oriented Programming'
  AND "Department" = 'EECS';
```
## b
```sql
DELETE FROM "STUDENT"
WHERE Name = 'David'
  AND "StudentNumber" = '005';
```
## c
```sql
SELECT "COURSE"."CourseName" FROM "SECTION"
LEFT JOIN "COURSE" ON "COURSE"."CourseNumber" = "SECTION"."CourseNumber"
WHERE "Instructor" = 'John'
  AND "Year" = 2022;
```

## d
```sql
SELECT "S"."CourseNumber", "SE"."Semester", "SE"."Year", COUNT("GR"."StudentNumber") AS "NumberOfStudents"
FROM "SECTION" "SE"
JOIN "COURSE" "S" ON "SE"."CourseNumber" = "S"."CourseNumber"
LEFT JOIN "GRADE_REPORT" "GR" ON "SE"."SectionNumber" = "GR"."SectionNumber"
WHERE "SE"."Instructor" = 'Eric'
GROUP BY "S"."CourseNumber", "SE"."Semester", "SE"."Year";
```
## e

```sql
SELECT "P"."PrerequisiteCourseNumber", "PC"."CourseName"
FROM "PREREQUISITE" "P"
JOIN "COURSE" "C" ON "P"."CourseNumber" = "C"."CourseNumber"
JOIN "COURSE" "PC" ON "P"."PrerequisiteCourseNumber" = "PC"."CourseNumber"
WHERE "C"."CourseName" = 'Database Systems' AND "C"."Department" = 'EECS';
```

## f
```sql
SELECT "STUDENT"."Name", "COURSE"."CourseNumber", "COURSE"."CourseName", "COURSE"."CreditHour", "SECTION"."Semester", "SECTION"."Year", "GRADE_REPORT"."Grade"
FROM "STUDENT"
JOIN "GRADE_REPORT" ON "STUDENT"."StudentNumber" = "GRADE_REPORT"."StudentNumber"
JOIN "SECTION" ON "GRADE_REPORT"."SectionNumber" = "SECTION"."SectionNumber"
JOIN "COURSE" ON "SECTION"."CourseNumber" = "COURSE"."CourseNumber"
WHERE "STUDENT"."Class" = 3 AND "STUDENT"."Major" = 'EECS';
```
## g
```sql
SELECT DISTINCT "STUDENT"."Name"
FROM "STUDENT"
WHERE NOT EXISTS (
    SELECT *
    FROM "GRADE_REPORT"
    WHERE "STUDENT"."StudentNumber" = "GRADE_REPORT"."StudentNumber" AND "GRADE_REPORT"."Grade" < 80
);
```
## h
```sql
SELECT "STUDENT"."Name", "STUDENT"."Major"
FROM "STUDENT"
WHERE NOT EXISTS (
    SELECT *
    FROM "GRADE_REPORT"
    WHERE "STUDENT"."StudentNumber" = "GRADE_REPORT"."StudentNumber" AND "GRADE_REPORT"."Grade" < 60
);
```
## i
```sql
SELECT DISTINCT "STUDENT"."Name", "STUDENT"."Major"
FROM "STUDENT"
JOIN "GRADE_REPORT" ON "STUDENT"."StudentNumber" = "GRADE_REPORT"."StudentNumber"
WHERE "GRADE_REPORT"."Grade" < 60
ORDER BY "STUDENT"."StudentNumber";
```

## j
```sql
SELECT "STUDENT"."Name", AVG("GRADE_REPORT"."Grade") AS "AverageGrade"
FROM "STUDENT"
JOIN "GRADE_REPORT" ON "STUDENT"."StudentNumber" = "GRADE_REPORT"."StudentNumber"
JOIN "SECTION" ON "GRADE_REPORT"."SectionNumber" = "SECTION"."SectionNumber"
WHERE "SECTION"."Year" = 2023
GROUP BY "STUDENT"."Name"
HAVING AVG("GRADE_REPORT"."Grade") > 80.0;
```
## k
```sql
SELECT "STUDENT"."Major", COUNT(DISTINCT "STUDENT"."StudentNumber") AS "NumStudents"
FROM "STUDENT"
JOIN "GRADE_REPORT" ON "STUDENT"."StudentNumber" = "GRADE_REPORT"."StudentNumber"
GROUP BY "STUDENT"."Major"
HAVING AVG("GRADE_REPORT"."Grade") < 60.0;
```
## l
```sql
CREATE VIEW "StudentTranscript" AS
SELECT "STUDENT"."StudentNumber", "STUDENT"."Name", "COURSE"."CourseName", "SECTION"."Semester", "SECTION"."Year", "GRADE_REPORT"."Grade"
FROM "STUDENT"
JOIN "GRADE_REPORT" ON "STUDENT"."StudentNumber" = "GRADE_REPORT"."StudentNumber"
JOIN "SECTION" ON "GRADE_REPORT"."SectionNumber" = "SECTION"."SectionNumber"
JOIN "COURSE" ON "SECTION"."CourseNumber" = "COURSE"."CourseNumber";
```
# 2
## a
```sql
CREATE TABLE "STUDENT" (
    "StudentNumber" INT PRIMARY KEY,
    "Name" VARCHAR(255),
    "Class" INT,
    "Major" VARCHAR(255)
);

CREATE TABLE "COURSE" (
    "CourseNumber" INT PRIMARY KEY,
    "CourseName" VARCHAR(255),
    "CreditHour" INT,
    "Department" VARCHAR(255)
);

CREATE TABLE "SECTION" (
    "SectionNumber" INT PRIMARY KEY,
    "CourseNumber" INT REFERENCES "COURSE"("CourseNumber")ON DELETE CASCADE,
    "Semester" VARCHAR(255),
    "Year" INT,
    "Instructor" VARCHAR(255)
);

CREATE TABLE "GRADE_REPORT" (
    "StudentNumber" INT REFERENCES "STUDENT"("StudentNumber")ON DELETE CASCADE,
    "SectionNumber" INT REFERENCES "SECTION"("SectionNumber")ON DELETE CASCADE,
    "Grade" INT
);

CREATE TABLE "PREREQUISITE" (
    "CourseNumber" INT REFERENCES "COURSE"("CourseNumber")ON DELETE CASCADE,
    "PrerequisiteCourseNumber" INT REFERENCES "COURSE"("CourseNumber")ON DELETE CASCADE,
    PRIMARY KEY ("CourseNumber", "PrerequisiteCourseNumber")
);
```
<image src="https://imgur.com/alL1xya.png" width="80%">

## b
```sql
INSERT INTO "STUDENT" ("StudentNumber", "Name", "Class", "Major") VALUES
(1, 'Alice', 3, 'EECS'),
(2, 'Bob', 2, 'Mathematics'),
(3, 'Charlie', 1, 'Physics'),
(4, 'Eva', 3, 'Computer Science'),
(5, 'David', 2, 'EECS');

-- Sample data for COURSE table
INSERT INTO "COURSE" ("CourseNumber", "CourseName", "CreditHour", "Department") VALUES
(1, 'Introduction to Computer Science', 3, 'EECS'),
(2, 'Linear Algebra', 4, 'Mathematics'),
(3, 'Modern Physics', 3, 'Physics'),
(4, 'Object-Oriented Programming', 3, 'EECS'),
(5, 'Database Systems', 4, 'EECS');

-- Sample data for SECTION table
INSERT INTO "SECTION" ("SectionNumber", "CourseNumber", "Semester", "Year", "Instructor") VALUES
(1, 1, 'Fall', 2022, 'John'),
(2, 2, 'Spring', 2023, 'Alice'),
(3, 4, 'Fall', 2022, 'Eric'),
(4, 5, 'Spring', 2023, 'Bob');

-- Sample data for GRADE_REPORT table
INSERT INTO "GRADE_REPORT" ("StudentNumber", "SectionNumber", "Grade") VALUES
(1, 1, 90),
(2, 2, 85),
(3, 3, 59),
(4, 4, 92),
(5, 1, 88);

-- Sample data for PREREQUISITE table
INSERT INTO "PREREQUISITE" ("CourseNumber", "PrerequisiteCourseNumber") VALUES
(5, 4),
(5, 3),
(2, 1);
```
## c
### a
<image src="https://imgur.com/oLroM0e.png" width="80%">

### b
<image src="https://imgur.com/cDlqw1w.png" width="80%">

### c
<image src="https://imgur.com/13eFyXg.png" width="80%">

### d
<image src="https://imgur.com/e1W89dy.png" width="80%">

### e
<image src="https://imgur.com/CMWHT4e.png" width="80%">

### f
<image src="https://imgur.com/o1zk4Mk.png" width="80%">

### g
<image src="https://imgur.com/k5hxUFD.png" width="80%">

### h
<image src="https://imgur.com/GmCQxNG.png" width="80%">

### i
<image src="https://imgur.com/VstHEZb.png" width="80%">

### j
<image src="https://imgur.com/OoYws77.png" width="80%">

### k
<image src="https://imgur.com/ICsgG0r.png" width="80%">

### l
<image src="https://imgur.com/ESBunyw.png" width="80%">


## d
```sql
CREATE OR REPLACE FUNCTION get_student_average_grade(student_number INT)
RETURNS varchar AS $$
DECLARE
    avg_grade numeric;
    result_text varchar;
BEGIN
    SELECT AVG("GRADE_REPORT"."Grade") INTO avg_grade
    FROM "GRADE_REPORT"
    WHERE "GRADE_REPORT"."StudentNumber" = student_number;

    IF avg_grade >= 60 THEN
        result_text := 'PASS';
    ELSE
        result_text := 'FAIL';
    END IF;
    RETURN result_text;
END;
$$ LANGUAGE plpgsql;
```
<image src="https://imgur.com/9ejsbNW.png" width="80%">

