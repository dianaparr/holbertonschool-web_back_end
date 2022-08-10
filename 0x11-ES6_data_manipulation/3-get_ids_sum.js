export default function getStudentIdsSum(arr) {
  const initialValue = 0;
  return arr.reduce((prevValue, currValue) => prevValue + currValue.id, initialValue);
}
