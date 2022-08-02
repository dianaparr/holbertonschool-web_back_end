import { createUser, uploadPhoto } from './utils';

function handleProfileSignup() {
  const promise1 = createUser();
  const promise2 = uploadPhoto();

  return Promise.all([promise1, promise2])
    .then((value) => {
      console.log(`${value[1].body} ${value[0].firstName} ${value[0].lastName}`);
    })
    .catch(() => console.log('Signup system offline'));
}

export default handleProfileSignup;
