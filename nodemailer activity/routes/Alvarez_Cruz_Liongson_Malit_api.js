const express = require('express');
var nodemailer = require("nodemailer");
const router = express.Router();


// get name 
router.get('/name', function(req, res){
    res.send({name: "Lexter Malit"});
});

// get age
router.get('/age', function(req, res){
    res.send({age: 23});
});

// get age
router.get('/gender', function(req, res){
    res.send({gender: "Male"});
});

// get address
router.get('/address', function(req, res){
    res.send({address: "Concepcion Lubao, Pampanga"});
});

// get section
router.get('/section', function(req, res){
    res.send({section: "CS - 401"});
});

// transporter. this will handle the credentials of the email sender.
var transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
        user: "week4activity@gmail.com",
        pass: "week4act"
    }
})

// POST REQUEST FOR SENDING EMAIL TO THE RECEIVER
router.post('/sendmail', function(req, res){
    console.log("Email : ", req.body.email_address);
    console.log("Message : ", req.body.message);

    res.send({
       email_address: req.body.email_address,
       message: req.body.message
    });

    // THIS IS THE MESSAGE. value of "to" and "text" will vary on what you posted on res.send
    var message = {
        from: "week4activity@gmail.com",
        to: req.body.email_address,
        subject: "Prelim Exam",
        text: req.body.message
    };

    // CONFIRMATION. this will either throw an error that says "error sending the email" if there is something wrong with the nodemailer code.
    // else it will say "email successfully sent to : (email)" means that sending of email succeeded.
    transporter.sendMail(message, function(err,data){
        if (err){
            console.log("Error sending the email" + err);
        }
        else{
            console.log("Email successfully sent to " + message.to);
        }
    });

});

module.exports = router;