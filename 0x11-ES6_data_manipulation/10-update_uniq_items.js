export default function updateUniqueItems(item) {
  if (item instanceof Map) {
    for (const i of item) {
      if (i[1] === 1) {
        item.set(i[0], 100);
      }
    }
    return item;
  }
  throw Error('Cannot process');
}
