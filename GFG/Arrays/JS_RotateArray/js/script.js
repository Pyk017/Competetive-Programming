import { stringToArray, arrayToString } from "./utility.js";
import { rotate, rotateReverse } from "./rotate.js";

//? CONSTANTS DOM ELEMENTS
const arrayElement = document.querySelector("[data-array]");
const paramElement = document.querySelector("[data-parameters]");
const answerElement = document.querySelector("[data-answer]");
const submitBtnElement = document.getElementById("submitButton");
const resetBtnElement = document.getElementById("resetButton");
const textareaElement = document.getElementById("floatingTextarea2");
const radioElements = document.getElementsByClassName("form-check-input");

let result = 0;
let selectedElement;
let arr;
let arrParam;

//? Change Event Listener on Array Input Element for enabling buttons
arrayElement.addEventListener("change", () => {
  submitBtnElement.disabled = false;
  resetBtnElement.disabled = false;
});

//? Change Event Listener on Parameters Input Element for enabling buttons
paramElement.addEventListener("change", () => {
  resetBtnElement.disabled = false;
  submitBtnElement.disabled = false;
});

//? Click Event Listener on RESET Button for resetting everything.
resetBtnElement.addEventListener("click", resetAll);

//? Reset all DOM elements
function resetAll() {
  answerElement.style.display = "none";
  arrayElement.value = "";
  paramElement.value = "";
  arrayElement.classList.remove("focusedInputError");
  paramElement.classList.remove("focusedInputError");
  resetBtnElement.disabled = true;
  submitBtnElement.disabled = true;
}

//? Click Event Listener on SUBMIT Button for Calculation.
submitBtnElement.addEventListener("click", () => {
  //! Error: If Array is entered but Parameters aren't.
  if (paramElement.value == "") {
    alert("Please give some parameter of rotation.");
    paramElement.classList.add("focusedInputError");
    return;
  }

  arr = stringToArray(arrayElement.value);
  arrParam = stringToArray(paramElement.value);

  //! Error: Only numbers are allowed in Array Inputs.
  if (arr.some((val) => !Number.isFinite(val))) {
    alert("Only Numbers must be entered in Array!");
    arrayElement.value = "";
    arrayElement.classList.add("focusedInputError");
    return;
  }

  //! Error: Only numbers are allowed in Parameters Inputs.
  if (arrParam.some((val) => !Number.isFinite(val))) {
    alert("Only Numbers must be entered in Parameters!");
    paramElement.value = "";
    paramElement.classList.add("focusedInputError");
    return;
  }

  //! Error: Length of parameters must be less than length of Array.
  if (arrParam[0] > arr.length) {
    alert("The Parameter is larger than the length of the array");
    paramElement.value = "";
    paramElement.classList.add("focusedInputError");
    return;
  }

  //! Error: Only one parameter is allowed to rotate the array.
  if (arrParam.length > 1) {
    alert("Multiple paramters detected! Only one parameter is allowed");
    paramElement.value = "";
    paramElement.classList.add("focusedInputError");
    return;
  }

  //? TO get the radio element which is selected by the user.
  selectedElement = Array.from(radioElements).reduce((acc, val) =>
    val.checked ? val : acc
  );

  if (selectedElement.dataset.algo == "brute-force") {
    result = rotate(arr, arrParam[0]);
  } else {
    result = rotateReverse(arr, arrParam[0]);
  }

  answerElement.style.display = "flex";
  textareaElement.value = arrayToString(result);
});
