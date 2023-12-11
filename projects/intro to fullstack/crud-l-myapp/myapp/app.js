const cors = require('cors')
const sqlite3 = require('sqlite3').verbose()
const express = require('express')
const pars = require('body-parser')
const app = express()

const db = new sqlite3.Database('./db.sqlite')

app.use(cors())
app.use(pars.json())
app.use(
  pars.urlencoded({
    extended: true,
  })
)

const PORT = 4000

app.delete('/:id', (req, res) => {
  const rowId = req.params.id;
  const sql = `DELETE FROM r_table WHERE id = ?`;
  console.log(rowId);
  db.run(sql, [rowId]);
  res.send();
})


app.post('/', (req, res) => {
  const {first_name, last_name, phon_number, email, role} = req.body;
  const query = 'INSERT INTO r_table (first_name, last_name, phon_number, email, role) VALUES (?, ?, ? ,? ,?)'
  db.run(query, [first_name, last_name, phon_number, email, role]);
  res.send({first_name, last_name, phon_number, email, role});
})

app.get('/', (req, res) => {
  db.all('SELECT * FROM r_table', (err, rows) => {
  if(err){
      res.status(500).send({err: err.message});
  }
  console.log(rows);
  res.send();
  });
})

app.listen(PORT, () => {
  console.log(`Example app listening on port ${PORT}`)
})