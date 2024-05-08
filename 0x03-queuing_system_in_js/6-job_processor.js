import kue from 'kue';
import redis from 'redis';

// Connect to Redis
const client = redis.createClient();

// Create a queue with Kue using the connected Redis client
const queue = kue.createQueue({ redis: client });

// Define the function to send notification
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Queue process to listen for new jobs on push_notification_code
queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);
  done();
});
