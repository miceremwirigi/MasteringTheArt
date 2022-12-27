console.log('Shop');

const costRate = 0.3;
console.log(costRate);

let shop = {
    name: 'Buymart',
    owner: 'Dan',
    location: 'Kahawa',
    buyFrom: true,
    items: ['Floor','Rice'],
}
let selection = 'buyFrom';
//shop.name = 'Sellmart';
shop['name'] = 'Sellmart';
shop[ selection ] = false;

console.log(shop);
console.log(shop.items.length)

function greetOwner(shop){
    console.log('Hello ' + shop.owner);
}

greetOwner(shop);