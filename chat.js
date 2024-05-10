"use strict";

var connection = new signalR.HubConnectionBuilder().withUrl("/chathub").build();
document.getElementById("sendbutton").disabled = true;

connection.on("ReceiveMessage", function (user, message) {
    var li = document.createElement("li");
    document.getElementById("messagesList").appendChild(li);
    li.textContent = `${user} says ${message}`;
});

connection.start().then(function () {
    document.getElementById("sendbutton").disabled = false;
}).catch(function (err) {
    return console.error(err.toString());
});

document.getElementById("sendbutton").addEventListener("click", function (event) {
    var user = document.getElementById("userinput").value;
    var message = document.getElementById("messageinput").value;
    connection.invoke("SendMessage", user, message).catch(function (err) {
        return console.error(err.toString());
    });
    event.preventDefault();
});