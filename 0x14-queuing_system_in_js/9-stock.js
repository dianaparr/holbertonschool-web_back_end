const express = require('express');
const redis = require('redis');
const { promisify } = require('util');

const app = express();
const redisClient = redis.createClient();
const redisSet = promisify(redisClient.set).bind(redisClient);
const redisGet = promisify(redisClient.get).bind(redisClient);

const ltProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 },
];

const getItemById = (id) => ltProducts.find((item) => item.id === id);
const reserveStockById = (item, stock) => redisSet(`item.${item}`, stock);
const getCurrentReservedStockById = async (item) =>
  await redisGet(`item.${item}`);

redisClient.on('ready', () =>
  console.log('Redis client connected to the server')
);
redisClient.on('error', (error) =>
  console.log(`Redis client not connected to the server: ${error}`)
);
app.listen(1245, () => console.log('Express server is now running'));

app.get('/list_products', (_req, res) => {
  res.status(200).send(JSON.stringify(ltProducts));
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemID = parseInt(req.params.itemId);
  const item = getItemById(itemID);

  if (!item)
    res.status(404).send(JSON.stringify({ status: 'Product not found' }));
  else {
    let currentStock = await getCurrentReservedStockById(itemID);

    if (!currentStock)
      reserveStockById(itemID, getItemById(itemID).initialAvailableQuantity);

    currentStock = parseInt(await getCurrentReservedStockById(itemID));

    res
      .status(200)
      .send(JSON.stringify({ ...item, currentQuantity: currentStock }));
  }
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemID = parseInt(req.params.itemId);
  const item = getItemById(itemID);

  if (!item)
    res.status(404).send(JSON.stringify({ status: 'Product not found' }));
  else {
    let currentStock = await getCurrentReservedStockById(itemID);
    if (currentStock < 1)
      res
        .status(418)
        .send(
          JSON.stringify({
            status: 'Not enough stock available',
            itemId: itemID,
          })
        );
    else {
      res
        .status(200)
        .send(
          JSON.stringify({ status: 'Reservation confirmed', itemId: itemID })
        );
      reserveStockById(itemID, currentStock - 1);
    }
  }
});

export default app;
