
import session from './session';

export default {
  login(email, password) {
    console.log(email)
    return session.post("/auth/login/", { email, password});
  },
  logout() {
    return session.post('/auth/logout/', {});
  },
  createAccount( password1, password2, email,phone) {
    
    return session.post('/registration/', {  password1, password2, email,phone });
  },
};