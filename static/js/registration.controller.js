(function(){
	'use strict';

	angular
		.module('rentApp')
		.controller('registrationController', 
			['$scope', '$location', '$http', 'Login', RegisterController])

	function RegisterController($scope, $location, $http, Login) {
        $scope.register = function () {
            $http.post('/auth/registration/', $scope.user)
                .then(function () {
                        $location.url('/login');
                    },
                    function () {
                        $scope.registration_error = "All Fields are neccesary";
                    })
        }
        $scope.logout = function(){
            delete localStorage.currentUser;
            $http.get('/auth/logout/')
                .then(function(){
                    $location.url('/login')
                });
        }

	}
})();