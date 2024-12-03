ALTER TABLE classlesson
ADD CONSTRAINT fk_classlesson_class
FOREIGN KEY(classid) REFERENCES class(id)

ALTER TABLE classlesson
ADD CONSTRAINT fk_classlesson_lesson
FOREIGN KEY(lessonid) REFERENCES lesson(id)

ALTER TABLE classlesson
ADD CONSTRAINT fk_classlesson_teacher
FOREIGN KEY(teacherid) REFERENCES teacher(id)
