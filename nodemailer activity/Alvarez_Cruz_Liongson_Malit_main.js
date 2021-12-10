const express = require('express');
const bodyParser = require('body-parser');

const app = express();

app.use(bodyParser.json());

app.use('/api', require('./routes/Alvarez_Cruz_Liongson_Malit_api'));

app.listen(process.env.port || 4000, function(){
    console.log("Listening for requests");
});