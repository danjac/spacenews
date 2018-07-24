const session = require('express-session')
const RedisStore = require('connect-redis')(session);
const app = require('express')()

app.use(session({
  store: new RedisStore({
    host: 'redis',
    port: 6379
  }),
  secret: 'super-secret-key', // TBD: grab from env
  resave: false,
  saveUninitialized: false,
  cookie: {
    maxAge: 1000 * 60 * 60 * 24,
    secure: false, // require HTTPS in production
  }
}))

module.exports = app
