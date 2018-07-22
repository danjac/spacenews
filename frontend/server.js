const { Nuxt, Builder } = require('nuxt')
const bodyParser = require('body-parser')
const session = require('express-session')
const csurf = require('csurf')
const proxy = require('http-proxy-middleware')
const axios = require('axios')
const app = require('express')()
const RedisStore = require('connect-redis')(session);

const API_URI = process.env.API_URI || 'http://django:8000'

let config = require('./nuxt.config')
config.isDev = process.env.NODE_ENV !== 'production'

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
    secure: !config.isDev, // require HTTPS in production
  }
}))

app.use(bodyParser.json())

app.use(csurf({ cookie: false }))

// we'll just check the csrf token from the cookie (same usage as Django)
// easier to use with Axios
app.use((req, res, next) => {
  res.cookie('csrf-token',  req.csrfToken())
  next()
})

app.use('/api', proxy({
  target: API_URI,
  changeOrigin: true,
  auth: false,
  logLevel: 'debug',
  onProxyReq(proxyReq, req, res) {
    if (req.session.authToken) {
      proxyReq.setHeader('Authorization', 'Token ' + req.session.authToken)
    }
    // workaround for bodyParser incompat
    // https://stackoverflow.com/questions/25207333/socket-hang-up-error-with-nodejs/25651651#25651651
    if (req.body) {
      let bodyData = JSON.stringify(req.body)
      // in case if content-type is application/x-www-form-urlencoded -> we need to change to application/json
      proxyReq.setHeader('Content-Type','application/json')
      proxyReq.setHeader('Content-Length', Buffer.byteLength(bodyData))
      // stream the content
      proxyReq.write(bodyData)
    }
  },
  async onProxyRes(proxyRes, req, res) {
    // if the API returns a 401, the token can be considered invalid. Delete the token.
    if (proxyRes.statusCode === 401) {
      delete req.session.authToken
      await req.session.save()
    }
  }
}))

app.post('/auth/login/', async (req, res) => {
  try {
    const result = await axios.post(API_URI + '/api/auth/token/create/', req.body)
    req.session.authToken = result.data.auth_token
    await req.session.save()
    return res.json({"OK": true})
  } catch (e) {
    console.log(e)
    return res.status(401).json({ error: 'Bad credentials' })
  }
})

app.post('/auth/logout/', async (req, res) => {
  delete req.session.authToken
  await req.session.save()
  axios.post(API_URI + '/api/auth/token/destroy/')
  return res.status(200).json({ ok: true })
})

// instantiate Nuxt
// make sure we load all modules, plugins etc
const nuxt = new Nuxt(config)

if (config.isDev) {
  new Builder(nuxt).build()
}
app.use(nuxt.render)
app.listen(3000)
console.log('Server listening on port 3000')
