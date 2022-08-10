export default function cleanSet(set, startString) {
  const str2 = [];
  if (set instanceof Set === false) return '';
  if (startString || typeof startString === 'string') {
    [...set].forEach((x) => {
      if (x && x.startsWith(startString)) {
        str2.push(x.substring(startString.length));
      }
    });
  }
  return str2.join('-');
}
