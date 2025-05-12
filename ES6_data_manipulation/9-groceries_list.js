// Adds a number of items with their qtys to a Map object
export default function groceriesList() {
  const atlas = new Map();
  const items = [
    ['Apples', 10],
    ['Tomatoes', 10],
    ['Pasta', 1],
    ['Rice', 1],
    ['Banana', 5],
  ];
  items.map((keyValue) => atlas.set(keyValue[0], keyValue[1]));
  return atlas;
}
