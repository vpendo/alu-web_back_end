export default function getStudentsByLocation(arrOfStudentIds, city) {
  const arr = [];
  if (Array.isArray(arrOfStudentIds) && typeof city === 'string') {
    return arrOfStudentIds.filter((student) => student.location === city);
  }
  return arr;
}
