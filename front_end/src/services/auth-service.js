
class AuthService {


    registerUser(data) {

        return fetch('http://localhost:5000/api/v1/users', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => {
            console.log('response in then block', response)
            return response.json();
        })
        .catch(error => {
            console.log('Error occurred registering user', error);
        })
    }

    authenticateUser(data) {

        return fetch('http://localhost:5000/api/v1/sessions', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
            .then(response => {
                return response.json();
            })
            .catch(error => {
                console.log('Error occurred when authenticating user', error);
            })
    }
}

export default new AuthService();