export default function updateStudentGradeByCity(arr, city, newGrades) {
  if (Array.isArray(arr)) {
    return arr
      .filter((c) => c.location === city)
      .map((e) => {
        let arrStudent;
        newGrades.forEach((newGrade) => {
          if (newGrade.studentId === e.id) {
            arrStudent = { ...e, grade: newGrade.grade };
          }
        });
        if (!arrStudent) {
          return { ...e, grade: 'N/A' };
        }
        return arrStudent;
      });
  }
  return [];
}
