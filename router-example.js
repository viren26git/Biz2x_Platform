const express = require('express')
const router= express.Router()

router.route('/:username/:id')   // we have tow paramters here = username + id
    .get((req,res)=>{
        console.log(req.params.id);   //we can access the URL dunamic paramters inside using the 'params'
        console.log(req.params.username); 
        res.send(' welcome to page, ' + req.params.username + ' your id is ' + req.params.id)
})
    .post((req,res)=>{
        console.log(req.params.username);
        res.send('Welcome to this page again using the post request ')
})


module.exports = router;
