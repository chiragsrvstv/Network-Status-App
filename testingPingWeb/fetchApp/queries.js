var Pool = require('pg').Pool
var pool = new Pool({
  user: 'chiragsrivastava',
  host: 'localhost',
  database: 'hostinfo',
  password:'1234',
  port: '5432'
});

var srcFile = require('./index.js');


// display all from details
var getDetails = (req, res) => {
  pool.query('select * from details order by status', (error, results) =>{
    if(error){
      throw error
    }
    res.status(200).json(results.rows)
  })
}

// display or search from id


const getById = (request, response) => {
  const id = parseInt(request.params.id)
  //ip.toString(new Buffer([id]))
  pool.query('SELECT * FROM details WHERE ip_address = $1', [id], (error, results) => {
    if (error) {
      throw error
    }
    response.status(200).json(results.rows)
  })
}


const createDetails = (request, response) => {
  console.log(request.body);
  const {ip_address, name} = request.body
  pool.query('INSERT INTO details (ip_address, name) VALUES ($1, $2)', [ip_address, name], (error, results) => {
    if (error) {
      throw error
      response.write("Something's not right -_-");
      response.end()
    }
    //response.status(201).send(`User added data`)
    response.redirect('/')
  })
}

const updateUser = (request, response) => {
  const id = parseInt(request.params.id)
  const { name, email } = request.body

  pool.query(
    'UPDATE users SET name = $1, email = $2 WHERE id = $3',
    [name, email, id],
    (error, results) => {
      if (error) {
        throw error
      }
      response.status(200).send(`User modified with ID: ${id}`)
    }
  )
}

/*const deleteUser = (request, response) => {
  const ipToDelete = parseInt(request.params.ipToDelete)

  pool.query('DELETE FROM details WHERE ip_address = $1', [ipToDelete], (error, results) => {
    if (error) {
      throw error
    }
    response.status(200).send(`User deleted with ID`)
  })
}*/

const deleteData = (request, response) => {
  console.log(request.body);
  const {ip_address, name, ipToDelete} = request.body
  pool.query('delete from details where ip_address = $1', [ipToDelete], (error, results) => {
    if (error) {
      throw error
      response.write("Something's not right -_-");
      response.end()
    }
    //response.status(201).send(`User added data`)
    response.redirect('/')
  })
}


module.exports = {
  getDetails,
  getById,
  createDetails,
  updateUser,
  deleteData
}
