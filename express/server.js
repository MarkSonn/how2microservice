/*
 * An express microservice that GETs a JSON object from another API,
 * then deletes the field with key 'Mark',
 * then serves the modified object at /reconciliation
 * USAGE: `npm i; npm start`
*/

// Setup express
const express = require('express')
const app = express()
const port = 3000

// Other import(s)
const fetch = require('node-fetch')
const request = require('request')

// Most basic route for reference
app.get('/', (req, res) => res.send('Hello Express'))

// GETs a JSON object from another API, deletes the 'Mark' field and serves the modified JSON object
app.get('/reconciliation', async (req, res, next) => {
  try {
    const raw_batch = await fetch('http://localhost:5000/batch')
    const json_batch = await raw_batch.json()

    delete json_batch['Mark']
    var clientOptions = {
      'uri': 'http://localhost:5000/receive',
      'body': JSON.stringify(json_batch),
      'method': 'POST',
      'headers': {
        'content-Type': 'application/json'
      }
    }
    request(clientOptions);
    res.send('Completed')
    //res.send(json_batch)
  } catch(error) {
    console.log(`Error in GET /reconciliation: ${error}`)
  }
})


// Serve application
app.listen(port, () => console.log(`Example app listening on port ${port}!`))
