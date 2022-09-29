const assert = require('assert');
const Rooster = require('../index');

describe('Rooster', () => {
  describe('.announceDawn', () => {
    it('returns a rooster call', () => {
      // setup
        const expected = 'cock-a-doodle-doo!';

      // exercise
      const result = Rooster.announceDawn();

      //verify
      assert.equal(result, expected);
    });
  });
  describe('.timeAtDawn', () => {
    it('returns its argument as a string', () => {
      // setup
      const expected = '3';

      // exercise
      const result = Rooster.timeAtDawn(3);

      // verify
      assert.strictEqual(result, expected);
    });

    it('throws an error if passed a number less than 0', () => {  
      const negNum = -1;
      
      assert.throws(
        () => {
          Rooster.timeAtDawn(negNum);
        },
        RangeError
      );

    });

    it('throws an error if passed a number  greater than 23', () => {
      const greaterNum = 25;
      assert.throws(() => {
        Rooster.timeAtDawn(greaterNum);
      }, RangeError);
    })
  });
});
