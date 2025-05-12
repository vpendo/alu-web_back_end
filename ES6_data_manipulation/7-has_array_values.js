export default function hasValuesFromArray(set, array) {
  return array.every((e) => set.has(e));
}
