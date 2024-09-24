import { createClient } from 'redis';
const client = createClient();

client.on('error', (error) => {
  console.error('Redis client not connected to the server:', error.message);
});

async function connectRedis () {
  try {
    await client.connect();
    console.log('Redis client connected to the server');
  } catch (error) {
    console.error('Failed to connect to Redis:', error.message);
  }
}

connectRedis();
