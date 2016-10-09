// 	Most Secure Crypto Algo
// npm install crypto-js
var CryptoJS = require("crypto-js");

var user = "\x68\x34\x78\x30\x72";
var k = CryptoJS.SHA256("\x93\x39\x02\x49\x83\x02\x82\xf3\x23\xf8\xd3\x13\x37");
var iv = CryptoJS.enc.Hex.parse(k.toString().substring(32,64));
var key = CryptoJS.enc.Hex.parse(k.toString().substring(0,32));

//CryptoJS.AES.encrypt(p, CryptoJS.enc.Hex.parse(k.toString().substring(0,32)), 
//	{ iv: CryptoJS.enc.Hex.parse(k.toString().substring(32,64)) }) == "ob1xQz5ms9hRkPTx+ZHbVg==";

console.log("Your username: "+user.toString());
console.log("k: "+k);
console.log("iv: "+iv);
console.log("key: "+key);

var ciphertext = "ob1xQz5ms9hRkPTx+ZHbVg==";
console.log("The ciphertext: "+ciphertext);

var plain = CryptoJS.AES.decrypt(ciphertext, key, { iv: iv });

console.log("Password in hex: "+plain);
// http://string-functions.com/hex-string.aspx
console.log("Password in plain: "+hex2str(plain));


function hex2str(text) {
	return unescape(('' + text).replace(/(..)/g, '%$1'))
}