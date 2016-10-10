// Look's like weak JavaScript auth script :)
var u = "admin"
// the password is going to be
var p = String.fromCharCode(74,97,118,97,83,99,114,105,112,116,73,115,83,101,99,117,114,101);
console.log("Password: " + p)

if(u == "admin" && p == String.fromCharCode(74,97,118,97,83,99,114,105,112,116,73,115,83,101,99,117,114,101)) {
    console.log("You got it!");
} else {
	console.log("Wrong password!");
}
