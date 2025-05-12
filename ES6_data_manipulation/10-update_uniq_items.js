export default function updateUniqueItems(someMap) {
  try {
    return [...someMap.entries()]
      .filter((keyValArr) => keyValArr[1] === 1)
      .map((keyValArr) => someMap.set(keyValArr[0], 100));
  } catch (e) {
    throw Error('Cannot process');
  }
}
