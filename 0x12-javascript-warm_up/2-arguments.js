#!/usr/bin/node
const process = require('process');
const args = process.argv;
if (args.length === 2) {
	console.log('No argument');
} else {
	console.log('Argument found');
}
