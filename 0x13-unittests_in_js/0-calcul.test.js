const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
  it('sum of integers', () => {
    assert.strictEqual(calculateNumber(14, 7), 21);
    assert.strictEqual(calculateNumber(-5, -10), -15);
    assert.strictEqual(calculateNumber(100, -36), 64);
  });

  it('with floats, you most round up', () => {
    assert.strictEqual(calculateNumber(1.7, 3.7), 6);
    assert.strictEqual(calculateNumber(2, 7.9), 10);
    assert.strictEqual(calculateNumber(3.5, 3), 7);
    assert.strictEqual(calculateNumber(2, 0.6), 3);
    assert.strictEqual(calculateNumber(0.4, 3.5), 4);
  });

  it('must be a number, returns it rounded', () => {
    assert.strictEqual(isNaN(calculateNumber(9.8)), true);
    assert.strictEqual(isNaN(calculateNumber(7)), true);
    assert.strictEqual(isNaN(calculateNumber()), true);
  });

  it('negative numbers', () => {
    assert.strictEqual(calculateNumber(-1, 1), 0);
    assert.strictEqual(calculateNumber(-1, -1), -2);
  });

  it('should throw typeerror if either param cannot be coerced to a number', () => {
    assert.throws(() => calculateNumber('betty'), {
      name: 'TypeError',
      message: 'Parameters must be numbers'
    });
    assert.throws(() => calculateNumber(2.4, 'cat'), {
      name: 'TypeError',
      message: 'Parameters must be numbers'
    });
  });
});
