import axios from "axios";
const API_URL = "https://www.glsteamedition.com";
// import authHeader from './auth-header';

export class APIService {
  constructor() {}

  async getContacts() {
    const url = `${API_URL}/v0/media/GET/video/Bend%20the%20Curve/`;
    const response = await axios.get(url);
    // axios
    // .get('https://api.coindesk.com/v1/bpi/currentprice.json')
    // .then(response => (this.info = response.data.bpi))
    // .catch(error => console.log(error))
    // console.log(response.data);
    return response.data;
  }
  async createToken(asd) {
    let post =asd
    let response = await axios.post(`${API_URL}/create_token_with_code/`, post)
    // console.log(asd.name);
    // console.log(response.data); 
      if (response.data.access) {
        console.log(response.data.access);
        localStorage.setItem('user_code', JSON.stringify(response.data));
      }
      return response.data
    
  }

  // async getValueToken() {
  //   return await axios.get(`${API_URL}/create_token_with_code/`, post);
  // }

  // logout() {
  //   localStorage.removeItem('user');
  // }

}




//   postContacts(data) {
//     // POST request using fetch with error handling
//     const requestOptions = {
//       method: 'POST',
//       headers: { 'Content-Type': 'application/json' },
//       body: JSON.stringify(data)
//     };
//     fetch('https://jsonplaceholder.typicode.com/invalid-url', requestOptions)
//       .then(async response => {
//         const data = await response.json();
  
//         // check for error response
//         if (!response.ok) {
//           // get error message from body or default to response status
//           const error = (data && data.message) || response.status;
//           return Promise.reject(error);
//         }
  
//         this.postId = data.id;
//       })
//       .catch(error => {
//         this.errorMessage = error;
//         console.error('There was an error!', error);
//       });
//   }


// return axios.get(API_URL + 'user', { headers: authHeader() });