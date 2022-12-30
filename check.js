function inventoryList() {
  // write your code here
  return {
    items: [],
    add: function (name) {
      let check = this.items.find((item) => item === name);
      if (check === undefined) {
        this.items.push(name);
      }
    },
    remove: function (name) {
      this.items = this.items.filter((item) => item !== name);
    },
  };
}

let x = inventoryList();
x.add("Hello");
x.add("World");
x.remove("Hello");
