#!/usr/bin/node
const name = typeof process.argv[2] === 'undefined' ? 'undefined': process.argv[2];
const newName = typeof process.argv[3] === 'undefined' ? 'undefined' : process.argv[3];
console.log(name + ' is ' + newName);
