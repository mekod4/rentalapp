(function(){
	'use strict';

	angular
		.module('rentApp')
		.service('Login', ['$http', '$location', Login])

	function Login($http, $location){
        this.login = login;
        this.isLoggedIn = isLoggedIn;
        this.logout = logout;
        this.redirectIfNotLoggedIn = redirectIfNotLoggedIn;
        this.currentUser = currentUser;

        function login(credentials) {
            return $http.post('/auth/login/', credentials)
                .then(function (response) {
                    localStorage.currentUser = JSON.stringify(response.data);
                });        	
        }

        function currentUser() {
            var retrievedUser = localStorage['currentUser']
            var parsedUser = JSON.parse(retrievedUser)
            return parsedUser;
        }

        function isLoggedIn () {
            return !!localStorage.currentUser;
        }


        function logout () {
            delete localStorage.currentUser;
            $http.get('/auth_api/logout/').then(function(){
                    $location.url('/login');
                });
        }

        function redirectIfNotLoggedIn () {
            if (!isLoggedIn()) {
                $location.url('/login');
            }
        }
	}
})();