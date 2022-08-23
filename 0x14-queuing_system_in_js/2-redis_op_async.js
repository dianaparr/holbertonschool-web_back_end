import redis from "redis";
import { promisify } from "util";

const cliRedis = redis.createClient();
const get = promisify(cliRedis.get).bind(cliRedis);

cliRedis.on("connect", () => {
  console.log("Redis client connected to the server");
});
cliRedis.on("error", (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

const setNewSchool = (schoolName, value) => {
  cliRedis.set(schoolName, value, redis.print);
};

const displaySchoolValue = async (schoolName) => {
  try {
    console.log(await get(schoolName));
  } catch (err) {
    console.log(err);
  }
};

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
