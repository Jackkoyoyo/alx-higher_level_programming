#!/usr/bin/node
const squar = process.argv[2];
if (isNaN(squar)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < squar; x++) {
    console.log('X'.repeat(squar));
  }
}
