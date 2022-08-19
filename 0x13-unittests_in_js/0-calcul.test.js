const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
  it('sum of integers', () => {
    assert.strictEqual(calculateNumber(14, 7), 21);
    assert.strictEqual(calculateNumber(-5, -10), -15);
    assert.strictEqual(calculateNumber(100, -36), 64);
  });

  it('with floats you most round up', () => {
    assert.strictEqual(calculateNumber(1.7, 3.7), 6);
    assert.strictEqual(calculateNumber(2, 7.9), 10);
    assert.strictEqual(calculateNumber(3.5, 3), 7);
  });

  it('must be a number returns it rounded', () => {
    assert.strictEqual(calculateNumber(9.8), 10);
    assert.strictEqual(calculateNumber(7), 7);
    assert.strictEqual(isNaN(calculateNumber()), true);
  });

  it('negative numbers', () => {
    assert.strictEqual(calculateNumber(-1, 1), 0);
    assert.strictEqual(calculateNumber(-1, -1), -2);
  });
});
