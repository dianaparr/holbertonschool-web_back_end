import redis from 'redis';

const cliRedis = redis.createClient();

cliRedis.on('connect', () => {
  console.log('Redis client connected to the server');
});
cliRedis.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

const suscriptionChannel = 'holberton school channel';

const publishMessage = (message, time) => {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    cliRedis.publish(suscriptionChannel, message);
  }, time);
};

publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
