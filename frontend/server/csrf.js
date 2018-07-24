const csurf = require('csurf')
const app = require('express')()

app.use(csurf({ cookie: false }))

// we'll just check the csrf token from the cookie (same usage as Django)
// easier to use with Axios
app.use((req, res, next) => {
  res.cookie('csrf-token',  req.csrfToken())
  next()
})

module.exports = app
