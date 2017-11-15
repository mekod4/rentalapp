(function(){
	'use strict';

	angular
		.module('rentApp')
		.controller('registrationController', 
			['$scope', '$location', '$http', RegisterController])

	function RegisterController($scope, $location, $http) {
        $scope.register = function () {
            $http.post('/auth/registration/', $scope.user)
                .then(function () {
                        $location.url('/login');
                    },
                    function () {
                        $scope.registration_error = "All Fields are neccesary";
                    })
        }

	}
})();