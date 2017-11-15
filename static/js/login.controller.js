(function(){
	'use strict';

	angular
		.module('rentApp')
		.controller('loginController', 
			['$scope', '$location', 'Login', LoginController])

	function LoginController($scope, $location, Login) {
        $scope.login = function () {
            Login.login($scope.user)
                .then(function () {
                        $location.url('/store');
                    },
                    function () {
                        $scope.login_error = "Invalid username/password combination";
                    })
        }

		if (Login.isLoggedIn()) {
			$location.url('/');
		}
	}
})();