import redis from "redis";

const cliRedis = redis.createClient();

cliRedis.on("connect", () => {
  console.log("Redis client connected to the server");
});
cliRedis.on("error", (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

const suscriptionChannel = "holberton school channel";

cliRedis.subscribe(suscriptionChannel);
cliRedis.on("message", (channel, message) => {
  console.log(message);
  if (message === "KILL_SERVER") {
    cliRedis.unsubscribe(suscriptionChannel);
    cliRedis.quit();
  }
});
