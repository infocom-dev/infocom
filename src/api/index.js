
import axios from "axios";
import router from "../router/router";
import store from "../store/store.js";

const options = {
  baseURL: 'http://localhost',
  headers: {
    "Content-Type": "application/json",
  },
  xsrfCookieName: "csrftoken",
  xsrfHeaderName: "X-CSRFTOKEN",
  withCredentials: true,
  timeout: 5000
};

const handleError = (error, noRedirect) => {
  if (
    error.response &&
    error.response.config &&
    error.response.status === 401
  ) {
    return plainApi
      .post("api/token/refresh/")
      .then(() => api.request(error.response.config))
      .catch(error => {
        store.commit("auth/REMOVE_ACTIVE_USER");
        if (!noRedirect) {
          router.push({ name: "login" });
        }
        return Promise.reject(error);
      });
  } else {
    return Promise.reject(error);
  }
};

const plainApi = axios.create(options);
const api = axios.create(options);
const apiNoRedirect = axios.create(options);

api.interceptors.response.use(
  response => response,
  error => handleError(error)
);

apiNoRedirect.interceptors.response.use(
  response => response,
  error => handleError(error, true)
);

export { api, apiNoRedirect, plainApi };