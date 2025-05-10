// Express app (user_service/index.js)
app.post('/users', (req, res) => {
  res.send({ id: 1, username: req.body.username });
});

