const kue = require('kue'),
  queue = kue.createQueue();

var jobCreator = queue
  .create('push_notification_code', {
    phoneNumber: '33331568889',
    message: 'This is a notification message.',
  })
  .save((err) => {
    if (!err) console.log(`Notification job created: ${jobCreator.id}`);
  })
  .on('complete', () => console.log('Notification job completed'))
  .on('failed', () => console.log('Notification job failed'));