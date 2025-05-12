export default function getStudentIdsSum(arrOfStudentObjs) {
  if (Array.isArray(arrOfStudentObjs)) {
    return arrOfStudentObjs.reduce((acc, currObj) => acc + currObj.id, 0);
  }
  return 0;
}
