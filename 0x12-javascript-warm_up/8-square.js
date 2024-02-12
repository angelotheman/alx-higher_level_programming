#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (isNaN(num)) {
  console.log('Missing Size');
}

for (let i = 0; i < num; i++) {
  console.log('X'.repeat(num));
}
