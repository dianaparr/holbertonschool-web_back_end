import redis from "redis";

const cliRedis = redis.createClient();

const keySecret = [
  "Portland",
  "Seattle",
  "New York",
  "Bogota",
  "Cali",
  "Paris",
];
const valueSecret = [50, 80, 20, 20, 40, 2];

cliRedis.on("connect", () => {
  console.log("Redis client connected to the server");
});
cliRedis.on("error", (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

keySecret.forEach((key, idx) => {
  cliRedis.hset("HolbertonSchools", key, valueSecret[idx], redis.print);
});

cliRedis.hgetall("HolbertonSchools", (_err, res) => {
  console.log(res);
});
