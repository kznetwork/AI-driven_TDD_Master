import { appConfig } from "./config.js";
import { add, subtract, multiply, divide } from "./utils/math.js";

console.log(`${appConfig.name} v${appConfig.version}`);
console.log("10 + 5 =", add(10, 5));
console.log("10 - 5 =", subtract(10, 5));
console.log("10 × 5 =", multiply(10, 5));
console.log("10 ÷ 5 =", divide(10, 5));
