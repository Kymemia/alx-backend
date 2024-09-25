import kue from 'kue';

export default function createPushNotificationsJobs(jobs, queue) {
	if (!Array.isArray(jobs)) {
		throw new Error('Jobs is not an array');
	}

	jobs.forEach((jobData) => {
		const job = queue.create('push_notification_code_3', jobData)
		 job.save((err) => {
			  if (!err) {
				  console.log(`Notification job created: ${job.id}`);
			  } else {
				  console.log(`Error creating job: ${err}`);
			  }
		  });

		job.on('complete', () => {
			console.log(`Notification job ${job.id} completed`);
		});

		job.on('failed', (error) => {
			console.log(`Notification job ${job.id} failed: ${error}`);
		});

		job.on('progress', (progress) => {
			console.log(`Notification job ${job.id} ${progress}% complete`);
		});
	});
}
