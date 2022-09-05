#!/usr/bin/node
const count = process.argv.length;
if (count === 2) {
	console.log('No argument');
} else {
	console.log('Argument found');
}
