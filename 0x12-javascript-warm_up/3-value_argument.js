#!/usr/bin/node
const [,, ...arg] = process.argv;
if (!arg[0]) {
  console.log('No argument');
} else {
  console.log(arg[0]);
}
