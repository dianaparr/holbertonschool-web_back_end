export const weakMap = new WeakMap();
let timesCalled = 1;

export function queryAPI(endpoint) {
  weakMap.set(endpoint, timesCalled);
  timesCalled += 1;
  const search = weakMap.get(endpoint);
  if (search >= 5) {
    throw new Error('Endpoint load is high');
  }
}
