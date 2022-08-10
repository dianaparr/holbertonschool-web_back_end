export default function createInt8TypedArray(length, position, value) {
  const newBuffInt8 = new ArrayBuffer(length);
  const newView = new DataView(newBuffInt8, 0);
  if (position > length - 1) {
    throw Error('Position outside range')
  }
  newView.setInt8(position, value);
  return newView;
}
