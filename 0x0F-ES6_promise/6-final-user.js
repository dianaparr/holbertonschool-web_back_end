import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
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
