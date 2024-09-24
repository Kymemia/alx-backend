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

function setNewSchool (schoolName, value) {
  console.log(`Setting value for ${schoolName}`);
  client.set(schoolName, value, (error, reply) => {
    if (error) {
      console.error('Error setting value:', error.message);
    } else {
      console.log(`Set operation reply: ${reply}`);
    }
  });
}

function displaySchoolValue (schoolName) {
  console.log(`Getting value for ${schoolName}`);
  client.get(schoolName, (error, reply) => {
    if (error) {
      console.error('Error retrieving school value:', error.message);
    } else if (reply === null) {
      console.log(`No value found for ${schoolName}`);
    } else {
      console.log(`Value for ${schoolName}: ${reply}`);
    }
  });
}

async function run () {
  await connectRedis();

  displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco');
}

run();
