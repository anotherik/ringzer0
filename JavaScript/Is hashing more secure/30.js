// npm install sha1
var sha1 = require('sha1');

// https://hashkiller.co.uk/sha1-decrypter.aspx
// b89356ff6151527e89c4f3e3d30c8e6586c63962 SHA1 : adminz

var p = "adminz"
if(sha1(p) == "b89356ff6151527e89c4f3e3d30c8e6586c63962") {
    console.log("You got it!");
} else {
	console.log("Wrong password!");
}
