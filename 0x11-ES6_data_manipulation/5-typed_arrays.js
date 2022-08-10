export default function createInt8TypedArray(length, position, value) {
  const newArrInt8 = new Int8Array(length);
  newArrInt8[position] = value;
  return newArrInt8;
}
