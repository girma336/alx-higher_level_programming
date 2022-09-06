#!/usr/bin/node
exports.esrever = function (list) {
  const lists = [];
  for (let i = list.length - 1; i >= 0; i--) {
    lists.push(list[i]);
  }
  return lists;
};
