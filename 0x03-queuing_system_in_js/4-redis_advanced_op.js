import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// Log a message on successful connection
client.on('connect', () => {
  console.log('Connected to Redis');
});

// Handle errors
client.on('error', (err) => {
  console.error('Redis Client Error', err);
});

(async () => {
  // Connect to the Redis server
  await client.connect();

  // Store hash values using hSet
  await client.hSet('HolbertonSchools', 'Portland', 50);
  await client.hSet('HolbertonSchools', 'Seattle', 80);
  await client.hSet('HolbertonSchools', 'New York', 20);
  await client.hSet('HolbertonSchools', 'Bogota', 20);
  await client.hSet('HolbertonSchools', 'Cali', 40);
  await client.hSet('HolbertonSchools', 'Paris', 2);

  // Retrieve the stored hash using hGetAll
  const result = await client.hGetAll('HolbertonSchools');
  console.log('HolbertonSchools hash:', result);

  // Close the Redis connection
  await client.quit();
})();
