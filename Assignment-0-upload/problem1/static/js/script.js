const addBtn = document.querySelector("#add");
const subtractBtn = document.querySelector("#subtract");
const input1 = document.querySelector("#num1");
const input2 = document.querySelector("#num2");

let num1 = 0, num2 = 0;

input1.addEventListener("change", function () {
    num1 = parseFloat(input1.value);
});

input2.addEventListener("change", function () {
    num2 = parseFloat(input2.value);
});

addBtn.addEventListener("click", function () {
    const result = num1 + num2;
    document.querySelector("#res").innerHTML = `Result : ${result}`;
    document.querySelector("#res").classList.add("result");
});

subtractBtn.addEventListener("click", function () {
    const result = num1 - num2;
    document.querySelector("#res").innerHTML = `Result : ${result}`;
    document.querySelector("#res").classList.add("result");
});