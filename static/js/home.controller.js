(function(){
	'use strict';

	angular
		.module('rentApp')
		.controller('homeController', 
			['$scope', '$location', '$http', 'Login', HomeController])

	function HomeController($scope, $location, $http, Login) {
        $scope.logout = function(){
            delete localStorage.currentUser;
            $http.get('/auth/logout/')
                .then(function(){
                    $location.url('/login')
                });
        }
        
        $scope.homeLogged = function(){
            if (Login.isLoggedIn()) {
                return true;
                console.log('true')
            } else {
                return false;
                console.log('false')
            }
        }

		if (Login.isLoggedIn()) {
			$location.url('/');
		}
	}
})();