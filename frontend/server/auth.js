const axios = require('axios')
const app = require('express')()

const API_URI = process.env.API_URI

app.post('/login/', async (req, res) => {
  try {
    const result = await axios.post(API_URI + '/auth/token/create/', req.body)
    req.session.authToken = result.data.auth_token
    await req.session.save()
    return res.json({"OK": true})
  } catch (e) {
    console.log(e)
    return res.status(401).json({ error: 'Bad credentials' })
  }
})

app.post('/logout/', async (req, res) => {
  delete req.session.authToken
  await req.session.save()
  axios.post(API_URI + '/auth/token/destroy/')
  return res.status(200).json({ ok: true })
})

module.exports = {
  path: '/auth',
  handler: app
}
