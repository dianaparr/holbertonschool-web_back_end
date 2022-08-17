const fs = require('fs');

function countStudents(path) {
  if (!fs.existsSync(path)) {
    throw Error('Cannot load the database');
  }

  try {
    const obj = {};
    const ltStudents = fs.readFileSync(path, { encoding: 'utf8' }).split('\n');

    for (let i = 1; i < ltStudents.length; i += 1) {
      const row = ltStudents[i].split(',');
      if (obj[row[3]]) {
        obj[row[3]].counter += 1;
        obj[row[3]].students.push(` ${row[0]}`);
      } else {
        obj[row[3]] = { counter: 1, students: [`${row[0]}`] };
      }
    }

    console.log(`Number of students: ${ltStudents.length - 1}`);

    for (const item in ltStudents) {
      if (Object.prototype.hasOwnProperty.call(ltStudents, item)) {
        console.log(
          `Number of students in ${item}: ${ltStudents[item].counter}. List: ${ltStudents[item].students}`
        );
      }
    }
  } catch (err) {
    throw new Error(err);
  }
}

module.exports = countStudents();
