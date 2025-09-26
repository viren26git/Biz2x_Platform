const express =require('express')
const routeExample = require('./router-example')
const app = express()

app.use('/user',routeExample); //use routeExample.js to handle routes starting with '/'
app.use('/home',routeExample); //use routeExample.js to handle routes starting with '/home'
app.use('/landingpage',routeExample); //use routeExample.js to handle routes starting with '/landingpage'

app.listen(3000, () => console.log("running main.js on port 3000......."));
