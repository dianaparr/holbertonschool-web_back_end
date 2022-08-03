// promiseStatus AND promiseValue
// Info: https://ourcodeworld.com/articles/read/317/how-to-check-if-a-javascript-promise-has-been-fulfilled-rejected-or-resolved#:~:text=Fulfilled%20is%20a%20state%20of,promise%20has%20been%20completed%20successfully.
import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

async function handleProfileSignup(firstName, lastName, fileName) {
  const signUser = await signUpUser(firstName, lastName);
  let upPhoto;
  try {
    upPhoto = await uploadPhoto(fileName);
  } catch (error) {
    upPhoto = error.toString();
  }

  return [
    { value: signUser, status: 'fulfilled' },
    { value: upPhoto, status: 'reject' },
  ];
}

export default handleProfileSignup;
