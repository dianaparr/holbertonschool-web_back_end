// promiseStatus AND promiseValue

import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

async function handleProfileSignup(firstName, lastName, fileName) {
  const sign = await signUpUser(firstName, lastName);
  let photo;
  try {
    photo = await uploadPhoto(fileName);
  } catch (error) {
    photo = error.toString();
  }

  return [
    { value: sign, status: 'fulfilled' },
    { value: photo, status: 'reject' },
  ];
}

export default handleProfileSignup;
