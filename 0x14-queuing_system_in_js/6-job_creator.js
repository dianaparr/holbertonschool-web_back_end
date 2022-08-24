const kue = require('kue'),
  queue = kue.createQueue();

const jobCreator = queue
  .create('push_notification_code', {
    phoneNumber: '4153518780',
    message: 'This is the code to verify your account',
  })
  .save((err) => {
    if (!err) console.log(`Notification job created: ${jobCreator.id}`);
  })
  .on('complete', () => console.log('Notification job completed'))
  .on('failed', () => console.log('Notification job failed'));
