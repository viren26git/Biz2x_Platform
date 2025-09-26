var express = require('express')
var app = express();

app.set('view engine','pug')
app.set('views', './views')

const products = ['Watch', 'Oven', 'Microwave', 'Phone', 'tablet', 'Laptop', 'pen drive']
const clothing = ['Jeans', 'Tshirts', 'Coats', 'Jackets', 'caps', 'mufler']

app.get('/index', (req,res)=>{
  res.render('index')
})

app.get('/product', (req,res)=>{
    res.render('sample', { 'title': 'Electronics', 'message': 'Buy Products', 'prod': products})
  })

app.get('/clothing', (req,res)=>{
    res.render('sample', { 'title': 'Clothing', 'message': 'Buy Clothing Products', 'prod': clothing})
  })

app.listen(8080, ()=>{
    console.log(' The server has started on port no 8080..')
})



==================

  Doctype
  html
     head
        title Exploring the Pug template
     body
        h1#myHeading This is a pug template
        p.firstParagraph I love this template!!!
