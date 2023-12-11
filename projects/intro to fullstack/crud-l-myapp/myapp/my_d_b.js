const sqlite3 = require('sqlite3').verbose()
const filepath = './db.sqlite'
// var data = [
//   { first_name: "Anom", last_name: 'xxx', phon_number: 3, email:'gh' ,role: ''},
//   { first_name: "Megha", last_name: 'xxx', phon_number: 33, email:'' ,role: ''},
//   { first_name: "Subham", last_name: 'xxx', phon_number: 333 ,email:'',role:'19'}
// ]

function createDbConnection() {
    const db = new sqlite3.Database(filepath, (error) => {
      if (error) {
        return console.error(error.message);
      }
      createTable(db)
    
    });
    console.log("Connection with SQLite has been established");
    return db;
  }

  function createTable(db) {
    db.run(`
    CREATE TABLE r_table
    (
      ID INTEGER PRIMARY KEY AUTOINCREMENT,
      first_name VARCHAR(50) NOT NULL, 
      last_name VARCHAR(50) NOT NULL,
      phon_number INTEGER NOT NULL,
      email VARCHAR(50) NOT NULL,
      role VARCHAR(50) NOT NULL
    );
  `);
  
  }

  // function insertRow() {
  //   const [first_name, last_name, phon_number, email, role] = process.argv.slice(2);
  //   db.run(
  //       `INSERT INTO r_table(first_name, last_name, phon_number, email, role) VALUES (?, ?, ?, ?, ?)`,
  //       [first_name, last_name, phon_number, email, role],
  //       function (error) {
  //           if (error) {
  //             console.error(error.message);
  //           }
  //           console.log(`Inserted a row with the ID: ${this.lastID}`);
  //         }
  //   );
  // }

  module.exports = createDbConnection();

