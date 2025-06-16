const express = require("express");
const app = express();
const path = require("path");

app.use(express.static(path.join(__dirname, "build")));

app.listen(6700, function (err){
console.log("server run on port 6700");
});
