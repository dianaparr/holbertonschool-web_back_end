const createPushNotificationsJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) throw new Error('Jobs is not an array');

  for (const aJob of jobs) {
    let job = queue
      .create('push_notification_code_3', aJob)
      .save((err) => {
        if (!err) console.log(`Notification job created: ${job.id}`);
      })
      .on('complete', () => console.log(`Notification job ${job.id} completed`))
      .on('failed', (err) =>
        console.log(`Notification job ${job.id} failed: ${err}`)
      )
      .on('progress', (percentage) =>
        console.log(`Notification job ${job.id} ${percentage}% complete`)
      );
  }
};

export default createPushNotificationsJobs;
