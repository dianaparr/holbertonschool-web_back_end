import redis from 'redis';

const cliRedis = redis.createClient();

cliRedis.on('connect', () => {
  console.log('Redis client connected to the server');
});
cliRedis.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

const setNewSchool = (schoolName, value) => {
    cliRedis.set(schoolName, value, redis.print);
};

const displaySchoolValue = (schoolName) => {
    cliRedis.get(schoolName, (_err, res) => {
    console.log(res);
  });
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
