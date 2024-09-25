import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Connected to Redis');
});

client.on('error', (err) => {
  console.error('Redis Client Error', err);
});

(async () => {
  await client.connect();

  await client.hSet('HolbertonSchools', 'Portland', 50);
  await client.hSet('HolbertonSchools', 'Seattle', 80);
  await client.hSet('HolbertonSchools', 'New York', 20);
  await client.hSet('HolbertonSchools', 'Bogota', 20);
  await client.hSet('HolbertonSchools', 'Cali', 40);
  await client.hSet('HolbertonSchools', 'Paris', 2);

  const result = await client.hGetAll('HolbertonSchools');
  console.log('HolbertonSchools hash:', result);

  await client.quit();
})();
