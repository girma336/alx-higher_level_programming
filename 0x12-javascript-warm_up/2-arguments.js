#!/usr/bin/node
const process = require('process');
const args = process.argv;
if (args.length > 2) {
	console.log('Argument found');
} else {
	console.log('No argument');
}
