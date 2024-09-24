import { createClient } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('error', (error) => {
  console.error('Redis client not connected to the server');
});

async function connectRedis () {
  try {
    await client.connect();
    console.log('Redis client connected to the server');
  } catch (error) {
    console.error('Failed to connect to Redis:', error.message);
  }
}

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

async function setNewSchool (schoolName, value) {
  console.log(`Setting value for ${schoolName} to ${value}`);
  try {
    const reply = await setAsync(schoolName, value);
    console.log(`Set operation reply: ${reply}`);
  } catch (error) {
    console.error(`Error setting value:, ${error.message}`);
  }
}

async function displaySchoolValue (schoolName) {
  console.log(`Getting value for ${schoolName}`);
  try {
    await Promise.race([
      getAsync(schoolName),
      new Promise((_resolve, reject) => setTimeout(() => reject(new Error('Timeout')), 5000))
    ]);
    const reply = await getAsync(schoolName);
    if (reply === null) {
      console.log(`No value found for ${schoolName}`);
    } else {
      console.log(`Value for ${schoolName}: ${reply}`);
    }
  } catch (error) {
    if (error.message === 'Timeout') {
      console.error(`Timeout happened for ${schoolName}`);
    } else {
      console.error('Error retrieving school value:', error.message);
    }
  }
}

async function run () {
  await connectRedis();
  await displaySchoolValue('Holberton');
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}

run();
